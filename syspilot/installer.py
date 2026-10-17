# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = [
#   "PyYAML==6.0.3",
#   "Sphinx==8.2.3",
#   "sphinx-needs==8.5.0",
# ]
# ///

"""Deterministic, harness-independent syspilot installation engine."""

from __future__ import annotations

import argparse
import base64
import ctypes
import hashlib
import hmac
import io
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
import uuid
import zipfile
from collections.abc import Callable, Mapping
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any

if os.name == "nt":
    from ctypes import wintypes

try:
    import yaml
except ImportError:
    yaml = None


PRODUCT_ROOTS = (
    "syspilot/agents/",
    "syspilot/prompts/",
    "syspilot/skills/",
    "syspilot/templates/",
)
INSTALLER_RUNTIME_SOURCE = "syspilot/installer.py"
HARNESS_ROOTS = {
    "vscode": ".github",
    "claude": ".claude",
    "opencode": ".opencode",
    "qoder": ".qoder",
}
PRODUCTION_HARNESSES = ("vscode", "claude", "opencode", "qoder")
# Valid --harness CLI selector values, not a maturity claim: vscode/claude/opencode
# are production-parity; qoder is experimental, installable-only (staging only).
ORCHESTRATION_SKILL = "syspilot.orchestration-subagent"
QODER_ARCHIVE = ".syspilot/qoder/syspilot-qoder-plugin.zip"
QODER_PACKAGE_ID = "syspilot-qoder"
QODER_ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
DOC_INDEX = b"""Welcome to Project Documentation
=================================

This is the documentation base for this project.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
"""
DOC_CONF = b'project = "Project Documentation"\nextensions = ["sphinx_needs"]\n'
CHECKPOINT_ROOT = Path(tempfile.gettempdir()) / "syspilot-checkpoints"
CHECKPOINT_TTL_SECONDS = 15 * 60
CHECKPOINT_STALE_SECONDS = 24 * 60 * 60
CHECKPOINT_CLEANUP_LIMIT = 128


class DependencyError(RuntimeError):
    """A required runtime dependency is unavailable."""


@dataclass(frozen=True)
class SourceSnapshot:
    """All selected product bytes resolved from one immutable revision."""

    files: Mapping[str, bytes]
    revision: str
    branch: str

    @classmethod
    def from_directory(
        cls, root: Path, *, revision: str, branch: str
    ) -> "SourceSnapshot":
        files: dict[str, bytes] = {}
        for product_root in PRODUCT_ROOTS:
            directory = root / product_root.rstrip("/")
            if not directory.exists():
                continue
            for path in sorted(directory.rglob("*")):
                if path.is_file():
                    files[path.relative_to(root).as_posix()] = path.read_bytes()
        runtime = root / INSTALLER_RUNTIME_SOURCE
        if runtime.is_file():
            files[INSTALLER_RUNTIME_SOURCE] = runtime.read_bytes()
        return cls(files=files, revision=revision, branch=branch)


@dataclass
class DirectorySummary:
    installed: int = 0
    updated: int = 0
    removed: int = 0


@dataclass
class InstallResult:
    success: bool
    branch: str
    revision: str
    summary: dict[str, DirectorySummary] = field(default_factory=dict)
    error: str | None = None
    commit: str | None = None
    status: str | None = None
    package_digest: str | None = None


@dataclass(frozen=True)
class Checkpoint:
    identifier: str
    target_root: Path
    files: Mapping[str, bytes]
    directories: frozenset[str]
    git_index: bytes | None
    git_head: str | None
    git_ref: str | None
    mutable_paths: frozenset[str] = frozenset()
    git_index_path: str | None = None
    display_paths: Mapping[str, str] = field(default_factory=dict)
    path_fingerprints: Mapping[str, PathIdentity] = field(default_factory=dict)
    nonce: str = ""
    binding: str = ""
    target_identity: PathIdentity = field(default_factory=lambda: PathIdentity("missing"))
    created_at: float = 0.0
    expires_at: float = 0.0
    leased: bool = False
    plan_digest: str | None = None


@dataclass(frozen=True)
class PathIdentity:
    kind: str
    digest: str | None = None
    device: int | None = None
    file_id: int | None = None


@dataclass(frozen=True)
class InstallPlan:
    target_root: Path
    target_identity: PathIdentity
    harness: str
    writes: Mapping[str, bytes]
    deletes: tuple[str, ...]
    expected: Mapping[str, PathIdentity]
    mutable_paths: tuple[str, ...]


def _plan_digest(plan: InstallPlan) -> str:
    payload = {
        "harness": plan.harness,
        "writes": {
            _canonical_checkpoint_relative(relative): hashlib.sha256(content).hexdigest()
            for relative, content in sorted(plan.writes.items())
        },
        "deletes": sorted(
            _canonical_checkpoint_relative(relative) for relative in plan.deletes
        ),
        "mutable_paths": sorted(
            _canonical_checkpoint_relative(relative) for relative in plan.mutable_paths
        ),
    }
    encoded = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()


def _checkpoint_path(identifier: str) -> Path:
    try:
        parsed = uuid.UUID(identifier)
    except (ValueError, AttributeError) as error:
        raise ValueError("invalid checkpoint identifier") from error
    if parsed.version != 4 or str(parsed) != identifier:
        raise ValueError("invalid checkpoint identifier")
    return CHECKPOINT_ROOT / f"{identifier}.json"


def _checkpoint_key_path(identifier: str) -> Path:
    _checkpoint_path(identifier)
    return CHECKPOINT_ROOT / f"{identifier}.key"


def _checkpoint_lease_path(identifier: str) -> Path:
    _checkpoint_path(identifier)
    return CHECKPOINT_ROOT / f"{identifier}.lease"


def _checkpoint_now() -> float:
    return time.time()


def _secure_checkpoint_root() -> None:
    CHECKPOINT_ROOT.mkdir(mode=0o700, parents=True, exist_ok=True)
    try:
        CHECKPOINT_ROOT.chmod(0o700)
    except OSError:
        pass


def _retire_checkpoint(identifier: str) -> None:
    try:
        checkpoint_path = _checkpoint_path(identifier)
    except ValueError:
        return
    for path in (
        checkpoint_path,
        _checkpoint_key_path(identifier),
        _checkpoint_lease_path(identifier),
    ):
        path.unlink(missing_ok=True)
    try:
        CHECKPOINT_ROOT.rmdir()
    except OSError:
        pass


def _cleanup_stale_checkpoints(now: float) -> None:
    if not CHECKPOINT_ROOT.is_dir():
        return
    identifiers: set[str] = set()
    for path in list(CHECKPOINT_ROOT.iterdir())[:CHECKPOINT_CLEANUP_LIMIT]:
        identifier = path.name.split(".", 1)[0]
        try:
            _checkpoint_path(identifier)
        except ValueError:
            continue
        try:
            stale = now - path.stat().st_mtime > CHECKPOINT_STALE_SECONDS
            if path.suffix == ".json":
                payload = json.loads(path.read_text(encoding="utf-8"))
                stale = stale or float(payload.get("expires_at", 0)) < now
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            stale = True
        if stale:
            identifiers.add(identifier)
    for identifier in identifiers:
        _retire_checkpoint(identifier)


def _validated_relative(value: str) -> str:
    relative = PurePosixPath(value)
    windows = PureWindowsPath(value)
    if (
        relative.is_absolute()
        or windows.is_absolute()
        or bool(windows.drive)
        or not relative.parts
        or any(part in {"", ".", ".."} for part in relative.parts)
        or "\\" in value
    ):
        raise ValueError("checkpoint contains an invalid target path")
    return relative.as_posix()


def _canonical_checkpoint_relative(value: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError("checkpoint contains an invalid target path")
    windows = PureWindowsPath(value)
    normalized = value.replace("\\", "/")
    if PurePosixPath(normalized).is_absolute() or windows.is_absolute() or windows.drive:
        raise ValueError("checkpoint contains an invalid target path")
    parts: list[str] = []
    for part in normalized.split("/"):
        if part in {"", "."}:
            continue
        if part == "..":
            if not parts:
                raise ValueError("checkpoint contains an invalid target path")
            parts.pop()
        else:
            parts.append(part)
    if not parts:
        raise ValueError("checkpoint contains an invalid target path")
    relative = "/".join(parts)
    return os.path.normcase(relative.replace("/", os.sep)).replace("\\", "/")


def _canonical_checkpoint_paths(values: object) -> frozenset[str]:
    if not isinstance(values, list):
        raise ValueError("checkpoint mutable paths are invalid")
    canonical: set[str] = set()
    for value in values:
        relative = _canonical_checkpoint_relative(value)
        if relative in canonical:
            raise ValueError("checkpoint contains a duplicate normalized mutable path")
        canonical.add(relative)
    return frozenset(canonical)


def _validated_source_path(value: str) -> PurePosixPath:
    try:
        normalized = _validated_relative(value)
    except ValueError as error:
        raise ValueError(f"invalid source path: {value}") from error
    relative = PurePosixPath(normalized)
    approved = any(
        relative.parts[: len(PurePosixPath(root).parts)]
        == PurePosixPath(root).parts
        for root in PRODUCT_ROOTS
    )
    if not approved:
        raise ValueError(f"invalid source path: {value}")
    return relative


def _is_link_like(path: Path, metadata: os.stat_result) -> bool:
    if stat.S_ISLNK(metadata.st_mode):
        return True
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    if reparse_flag and getattr(metadata, "st_file_attributes", 0) & reparse_flag:
        return True
    is_junction = getattr(path, "is_junction", None)
    return bool(is_junction and is_junction())


def _lstat(path: Path) -> os.stat_result | None:
    try:
        return path.lstat()
    except FileNotFoundError:
        return None


def _filesystem_identity(path: Path, metadata: os.stat_result) -> tuple[int, int]:
    if os.name != "nt":
        return metadata.st_dev, metadata.st_ino

    class FileInformation(ctypes.Structure):
        _fields_ = [
            ("attributes", wintypes.DWORD),
            ("creation_time", wintypes.FILETIME),
            ("last_access_time", wintypes.FILETIME),
            ("last_write_time", wintypes.FILETIME),
            ("volume_serial", wintypes.DWORD),
            ("file_size_high", wintypes.DWORD),
            ("file_size_low", wintypes.DWORD),
            ("number_of_links", wintypes.DWORD),
            ("file_index_high", wintypes.DWORD),
            ("file_index_low", wintypes.DWORD),
        ]

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
    ]
    create_file.restype = wintypes.HANDLE
    handle = create_file(
        str(path),
        0,
        0x00000001 | 0x00000002 | 0x00000004,
        None,
        3,
        0x00200000 | 0x02000000,
        None,
    )
    if handle == wintypes.HANDLE(-1).value:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        information = FileInformation()
        if not kernel32.GetFileInformationByHandle(
            handle, ctypes.byref(information)
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        if information.attributes & 0x00000400:
            raise ValueError(f"link-like reparse path rejected: {path}")
        file_id = (information.file_index_high << 32) | information.file_index_low
        return information.volume_serial, file_id
    finally:
        kernel32.CloseHandle(handle)


def _path_identity(path: Path) -> PathIdentity:
    metadata = _lstat(path)
    if metadata is None:
        return PathIdentity("missing")
    if _is_link_like(path, metadata):
        return PathIdentity("link")
    device, file_id = _filesystem_identity(path, metadata)
    if stat.S_ISREG(metadata.st_mode):
        return PathIdentity(
            "file", hashlib.sha256(path.read_bytes()).hexdigest(), device, file_id
        )
    if stat.S_ISDIR(metadata.st_mode):
        return PathIdentity("directory", device=device, file_id=file_id)
    return PathIdentity("other")


def _validate_target_path(target_root: Path, relative_value: str) -> Path:
    try:
        relative = PurePosixPath(_validated_relative(relative_value))
    except ValueError as error:
        raise ValueError(f"invalid target path: {relative_value}") from error
    path = target_root.joinpath(*relative.parts)
    try:
        path.relative_to(target_root)
    except ValueError as error:
        raise ValueError(f"target path escapes root: {relative_value}") from error
    current = target_root
    for part in relative.parts:
        current /= part
        metadata = _lstat(current)
        if metadata is None:
            continue
        if _is_link_like(current, metadata):
            raise ValueError(f"link-like symlink, junction, or reparse path rejected: {relative_value}")
        if current != path and not stat.S_ISDIR(metadata.st_mode):
            raise ValueError(f"non-directory target ancestry: {relative_value}")
        if current != target_root and os.path.ismount(current):
            raise ValueError(f"link-like mount path rejected: {relative_value}")
    return path


def _git_output_path(target_root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else target_root / path


def _discover_git_state(
    target_root: Path,
) -> tuple[Path | None, Path | None, str | None, str | None]:
    git_dir_result = subprocess.run(
        ["git", "rev-parse", "--git-dir"],
        cwd=target_root,
        capture_output=True,
        text=True,
    )
    if git_dir_result.returncode != 0:
        return None, None, None, None
    git_dir = _git_output_path(target_root, git_dir_result.stdout.strip()).absolute()
    index_result = subprocess.run(
        ["git", "rev-parse", "--git-path", "index"],
        cwd=target_root,
        check=True,
        capture_output=True,
        text=True,
    )
    index_path = _git_output_path(target_root, index_result.stdout.strip()).absolute()
    ref_result = subprocess.run(
        ["git", "rev-parse", "--symbolic-full-name", "HEAD"],
        cwd=target_root,
        capture_output=True,
        text=True,
    )
    ref_value = ref_result.stdout.strip() if ref_result.returncode == 0 else ""
    git_ref = ref_value if ref_value.startswith("refs/") else None
    if git_ref is None:
        symbolic_result = subprocess.run(
            ["git", "symbolic-ref", "-q", "HEAD"],
            cwd=target_root,
            capture_output=True,
            text=True,
        )
        if symbolic_result.returncode == 0:
            git_ref = symbolic_result.stdout.strip()
    head_result = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"],
        cwd=target_root,
        capture_output=True,
        text=True,
    )
    git_head = head_result.stdout.strip() if head_result.returncode == 0 else None
    return git_dir, index_path, git_head, git_ref


def _encode_bytes(content: bytes) -> str:
    return base64.b64encode(content).decode("ascii")


def _decode_bytes(content: str) -> bytes:
    return base64.b64decode(content.encode("ascii"), validate=True)


def _checkpoint_binding(checkpoint: Checkpoint, secret: bytes) -> str:
    payload = {
        "identifier": checkpoint.identifier,
        "nonce": checkpoint.nonce,
        "target_root": str(checkpoint.target_root),
        "mutable_paths": sorted(checkpoint.mutable_paths),
        "display_paths": dict(sorted(checkpoint.display_paths.items())),
        "path_fingerprints": {
            key: asdict(value)
            for key, value in sorted(checkpoint.path_fingerprints.items())
        },
        "git_head": checkpoint.git_head,
        "git_ref": checkpoint.git_ref,
        "git_index_path": checkpoint.git_index_path,
        "git_index": (
            _encode_bytes(checkpoint.git_index)
            if checkpoint.git_index is not None
            else None
        ),
        "target_identity": asdict(checkpoint.target_identity),
        "created_at": checkpoint.created_at,
        "expires_at": checkpoint.expires_at,
        "plan_digest": checkpoint.plan_digest,
    }
    encoded = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    return hmac.new(secret, encoded, hashlib.sha256).hexdigest()


def _store_checkpoint(checkpoint: Checkpoint, secret: bytes) -> None:
    _secure_checkpoint_root()
    destination = _checkpoint_path(checkpoint.identifier)
    key_destination = _checkpoint_key_path(checkpoint.identifier)
    payload = {
        "identifier": checkpoint.identifier,
        "target_root": str(checkpoint.target_root.resolve()),
        "files": {
            relative: _encode_bytes(content)
            for relative, content in checkpoint.files.items()
        },
        "directories": sorted(checkpoint.directories),
        "git_index": (
            _encode_bytes(checkpoint.git_index)
            if checkpoint.git_index is not None
            else None
        ),
        "git_head": checkpoint.git_head,
        "git_ref": checkpoint.git_ref,
        "mutable_paths": sorted(checkpoint.mutable_paths),
        "git_index_path": checkpoint.git_index_path,
        "display_paths": dict(checkpoint.display_paths),
        "path_fingerprints": {
            key: asdict(value) for key, value in checkpoint.path_fingerprints.items()
        },
        "nonce": checkpoint.nonce,
        "binding": checkpoint.binding,
        "target_identity": asdict(checkpoint.target_identity),
        "created_at": checkpoint.created_at,
        "expires_at": checkpoint.expires_at,
        "plan_digest": checkpoint.plan_digest,
    }
    key_descriptor = os.open(
        key_destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600
    )
    try:
        with os.fdopen(key_descriptor, "wb") as key_stream:
            key_stream.write(secret)
            key_stream.flush()
            os.fsync(key_stream.fileno())
    except BaseException:
        key_destination.unlink(missing_ok=True)
        raise
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{checkpoint.identifier}-", dir=CHECKPOINT_ROOT
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(payload, stream, separators=(",", ":"), sort_keys=True)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_name, destination)
    except BaseException:
        Path(temporary_name).unlink(missing_ok=True)
        key_destination.unlink(missing_ok=True)
        raise


def _load_checkpoint_artifact(
    target_root: Path, identifier: str, path: Path, *, leased: bool
) -> Checkpoint:
    """Load a persisted checkpoint only for its owning target root."""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload["identifier"] != identifier:
            raise ValueError("checkpoint identifier does not match its artifact")
        owner = Path(payload["target_root"]).resolve(strict=True)
        resolved_target = target_root.resolve(strict=True)
        if not os.path.samefile(owner, resolved_target):
            raise ValueError("checkpoint does not belong to the target root")
        files = {
            _canonical_checkpoint_relative(relative): _decode_bytes(content)
            for relative, content in payload["files"].items()
        }
        directories = frozenset(
            _canonical_checkpoint_relative(relative)
            for relative in payload["directories"]
        )
        encoded_index = payload["git_index"]
        git_index = _decode_bytes(encoded_index) if encoded_index is not None else None
        git_head = payload["git_head"]
        git_ref = payload["git_ref"]
        mutable_paths = _canonical_checkpoint_paths(
            payload.get("mutable_paths", [*files.keys(), *directories])
        )
        if not set(files).union(directories).issubset(mutable_paths):
            raise ValueError("checkpoint snapshot exceeds its mutable paths")
        git_index_path = payload.get("git_index_path")
        display_paths = {
            _canonical_checkpoint_relative(key): value
            for key, value in payload["display_paths"].items()
        }
        if any(
            not isinstance(value, str)
            or _canonical_checkpoint_relative(value) != key
            for key, value in display_paths.items()
        ):
            raise ValueError("checkpoint display paths are invalid")
        path_fingerprints = {
            _canonical_checkpoint_relative(key): PathIdentity(**value)
            for key, value in payload["path_fingerprints"].items()
        }
        nonce = payload["nonce"]
        binding = payload["binding"]
        target_identity = PathIdentity(**payload["target_identity"])
        created_at = float(payload["created_at"])
        expires_at = float(payload["expires_at"])
        plan_digest = payload.get("plan_digest")
        if plan_digest is not None and not re.fullmatch(r"[0-9a-f]{64}", plan_digest):
            raise ValueError("checkpoint plan digest is invalid")
        if git_head is not None and not isinstance(git_head, str):
            raise ValueError("checkpoint Git HEAD is invalid")
        if git_ref is not None and not isinstance(git_ref, str):
            raise ValueError("checkpoint Git ref is invalid")
        if git_index_path is not None and not isinstance(git_index_path, str):
            raise ValueError("checkpoint Git index path is invalid")
        # use resolved_target, not target_root: create_checkpoint() discovers Git
        # state from the resolved root, so a /var-vs-/private/var-style symlink
        # prefix mismatch (e.g. macOS) would otherwise make discovery disagree
        _, discovered_index, _, _ = _discover_git_state(resolved_target)
        if git_index_path is not None and (
            discovered_index is None
            or discovered_index != Path(git_index_path).absolute()
        ):
            raise ValueError("checkpoint Git index path does not match Git discovery")
    except FileNotFoundError as error:
        raise ValueError("checkpoint does not exist") from error
    except (KeyError, TypeError, json.JSONDecodeError, ValueError) as error:
        if isinstance(error, ValueError) and str(error).startswith("checkpoint "):
            raise
        raise ValueError("checkpoint artifact is invalid") from error
    checkpoint = Checkpoint(
        identifier,
        resolved_target,
        files,
        directories,
        git_index,
        git_head,
        git_ref,
        mutable_paths,
        git_index_path,
        display_paths,
        path_fingerprints,
        nonce,
        binding,
        target_identity,
        created_at,
        expires_at,
        leased,
        plan_digest,
    )
    if set(display_paths) != set(mutable_paths) or set(path_fingerprints) != set(
        mutable_paths
    ):
        raise ValueError("checkpoint fingerprint coverage is invalid")
    try:
        parsed_nonce = uuid.UUID(nonce)
    except (ValueError, AttributeError) as error:
        raise ValueError("checkpoint nonce is invalid") from error
    if parsed_nonce.version != 4 or str(parsed_nonce) != nonce:
        raise ValueError("checkpoint nonce is invalid")
    try:
        secret = _checkpoint_key_path(identifier).read_bytes()
    except FileNotFoundError as error:
        raise ValueError("checkpoint authentication secret is missing") from error
    if len(secret) != 32 or not hmac.compare_digest(
        binding, _checkpoint_binding(checkpoint, secret)
    ):
        raise ValueError("checkpoint authentication is invalid")
    if checkpoint.expires_at <= _checkpoint_now():
        raise ValueError("checkpoint token is expired")
    if _path_identity(resolved_target) != checkpoint.target_identity:
        raise ValueError("checkpoint target identity changed")
    return checkpoint


def load_checkpoint(target_root: Path, identifier: str) -> Checkpoint:
    """Load and authenticate an unleased checkpoint without consuming it."""
    if _checkpoint_lease_path(identifier).exists():
        raise ValueError("checkpoint is already leased or consumed")
    return _load_checkpoint_artifact(
        target_root, identifier, _checkpoint_path(identifier), leased=False
    )


def _claim_checkpoint(identifier: str) -> None:
    """Atomically claim one checkpoint identifier without inspecting its state."""
    _secure_checkpoint_root()
    lease_path = _checkpoint_lease_path(identifier)
    try:
        descriptor = os.open(lease_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as error:
        raise ValueError("checkpoint is already leased or consumed") from error
    os.close(descriptor)


def _load_claimed_checkpoint(target_root: Path, identifier: str) -> Checkpoint:
    """Authenticate and consume checkpoint state after its lease is owned."""
    checkpoint = _load_checkpoint_artifact(
        target_root, identifier, _checkpoint_path(identifier), leased=True
    )
    _checkpoint_path(identifier).unlink()
    return checkpoint


def _lease_checkpoint(target_root: Path, identifier: str) -> Checkpoint:
    """Atomically claim and load one checkpoint for exactly one attempt."""
    _claim_checkpoint(identifier)
    try:
        return _load_claimed_checkpoint(target_root, identifier)
    except BaseException:
        _retire_checkpoint(identifier)
        raise


def _validate_supplied_checkpoint(plan: InstallPlan, checkpoint: Checkpoint) -> None:
    planned_paths = _canonical_checkpoint_paths(list(plan.mutable_paths))
    if checkpoint.mutable_paths != planned_paths:
        raise ValueError("checkpoint mutable paths do not match the frozen plan")
    if checkpoint.plan_digest != _plan_digest(plan):
        raise ValueError("checkpoint plan does not match the frozen plan")
    for key in sorted(checkpoint.mutable_paths):
        path = _validate_target_path(plan.target_root, checkpoint.display_paths[key])
        if _path_identity(path) != checkpoint.path_fingerprints[key]:
            raise ValueError(f"checkpoint is stale: {checkpoint.display_paths[key]}")
    _, git_index_path, git_head, git_ref = _discover_git_state(plan.target_root)
    current_index = (
        git_index_path.read_bytes()
        if git_index_path is not None and git_index_path.is_file()
        else None
    )
    if (
        git_head != checkpoint.git_head
        or git_ref != checkpoint.git_ref
        or current_index != checkpoint.git_index
        or (
            checkpoint.git_index_path is not None
            and git_index_path != Path(checkpoint.git_index_path).absolute()
        )
    ):
        raise ValueError("checkpoint is stale: Git state changed")


def delete_checkpoint(target_root: Path, identifier: str) -> None:
    """Delete a persisted checkpoint after validating target ownership."""
    load_checkpoint(target_root, identifier)
    _retire_checkpoint(identifier)


def parse_frontmatter(content: bytes) -> tuple[dict[str, Any], bytes]:
    """Parse the first YAML frontmatter block and return its exact body bytes."""
    if yaml is None:
        raise DependencyError("PyYAML is required; install it before retrying")
    if content.startswith(b"\xef\xbb\xbf"):
        raise ValueError("UTF-8 BOM is not permitted")
    if not content.startswith((b"---\n", b"---\r\n")):
        raise ValueError("missing opening YAML frontmatter delimiter")

    first_line_end = content.find(b"\n") + 1
    cursor = first_line_end
    while cursor < len(content):
        line_end = content.find(b"\n", cursor)
        if line_end == -1:
            line = content[cursor:]
            next_cursor = len(content)
        else:
            line = content[cursor:line_end]
            next_cursor = line_end + 1
        if line.rstrip(b"\r") == b"---":
            parsed = yaml.safe_load(content[first_line_end:cursor].decode("utf-8")) or {}
            if not isinstance(parsed, dict):
                raise ValueError("YAML frontmatter must be a mapping")
            return parsed, content[next_cursor:]
        cursor = next_cursor
    raise ValueError("missing closing YAML frontmatter delimiter")


def _render_frontmatter(metadata: dict[str, Any], body: bytes) -> bytes:
    if yaml is None:
        raise DependencyError("PyYAML is required; install it before retrying")
    yaml_bytes = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).encode("utf-8")
    return b"---\n" + yaml_bytes + b"---\n" + body


def _claude_agent_name(source_path: str) -> str:
    relative = _validated_source_path(source_path)
    if relative.parts[:2] != ("syspilot", "agents"):
        raise ValueError(f"Claude Code agent source path is invalid: {source_path}")
    filename = relative.name
    if not filename.startswith("syspilot.") or not filename.endswith(".agent.md"):
        raise ValueError(f"Claude Code agent source filename is invalid: {source_path}")
    source_id = filename.removesuffix(".agent.md")
    if re.fullmatch(r"syspilot\.[a-z]+", source_id) is None:
        raise ValueError(f"Claude Code agent source ID is invalid: {source_id}")
    return source_id.replace(".", "-")


def _adapt_claude_workflow_bindings(body: bytes, allowlist: list[str]) -> bytes:
    workflow_marker = b"## Workflow"
    marker_count = body.count(workflow_marker)
    if marker_count == 0:
        return body
    if marker_count != 1:
        raise ValueError("agent has a duplicate Workflow boundary")
    start = body.index(workflow_marker)
    next_heading = body.find(b"\n## ", start + len(workflow_marker))
    end = len(body) if next_heading == -1 else next_heading
    workflow = body[start:end]
    lines = workflow.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if not any(verb in line for verb in (b"SEND", b"RECEIVE", b"RESPOND")):
            continue
        for source_id in allowlist:
            lines[index] = lines[index].replace(
                source_id.encode("utf-8"), source_id.replace(".", "-").encode("utf-8")
            )
    return body[:start] + b"".join(lines) + body[end:]


def adapt_agent(
    content: bytes,
    harness: str,
    source_path: str | None = None,
    agent_identities: Mapping[str, str] | None = None,
) -> bytes:
    """Adapt agent metadata and harness-specific structural bindings."""
    metadata, body = parse_frontmatter(content)
    if harness == "vscode":
        return content
    description = metadata.get("description")
    if not isinstance(description, str) or not description:
        raise ValueError("agent description is required")
    allowlist = metadata.get("agents") or []
    if not isinstance(allowlist, list) or not all(
        isinstance(agent, str) for agent in allowlist
    ):
        raise ValueError("agent allowlist must be a list of names")
    native_allowlist = [
        agent_identities.get(agent, agent) if agent_identities else agent
        for agent in allowlist
    ]
    if harness == "opencode":
        adapted: dict[str, Any] = {"description": description}
        if native_allowlist:
            adapted["mode"] = "primary"
            adapted["permission"] = {
                "task": {
                    "*": "deny",
                    **{agent: "allow" for agent in native_allowlist},
                }
            }
        elif metadata.get("user-invocable") is True:
            adapted["mode"] = "primary"
        else:
            adapted["mode"] = "subagent"
        return _render_frontmatter(adapted, body)
    if harness == "claude":
        if source_path is None:
            raise ValueError("Claude agent source path is required")
        adapted = {
            "name": _claude_agent_name(source_path),
            "description": description,
            "user-invocable": False,
        }
        if native_allowlist:
            if metadata.get("user-invocable") is True:
                native_targets = ", ".join(
                    agent.replace(".", "-") for agent in native_allowlist
                )
                adapted["tools"] = [f"Agent({native_targets})"]
            else:
                adapted["tools"] = ["Agent"]
            body = _adapt_claude_workflow_bindings(body, native_allowlist)
        return _render_frontmatter(adapted, body)
    if harness == "qoder":
        return _render_frontmatter({"description": description}, body)
    raise ValueError(f"unsupported harness: {harness}")


def adapt_skill(content: bytes, harness: str) -> bytes:
    """Retain portable Skill metadata and preserve instruction bytes."""
    if harness == "vscode":
        return content
    metadata, body = parse_frontmatter(content)
    portable = {
        key: metadata[key]
        for key in ("name", "description", "license", "compatibility", "metadata")
        if key in metadata
    }
    if not isinstance(portable.get("description"), str):
        raise ValueError("skill description is required")
    if metadata.get("name") == ORCHESTRATION_SKILL and harness in (
        "claude",
        "opencode",
    ):
        body = _adapt_orchestration_binding(body, harness)
    return _render_frontmatter(portable, body)


def _adapt_orchestration_binding(body: bytes, harness: str) -> bytes:
    start_marker = b"## Verb Mappings"
    end_marker = b"## RECEIVE: Obtaining Your Assignment"
    if body.count(start_marker) != 1 or body.count(end_marker) != 1:
        raise ValueError("orchestration Skill has a missing or duplicate binding boundary")
    start = body.index(start_marker)
    end = body.index(end_marker)
    if end <= start:
        raise ValueError("orchestration Skill binding boundary is malformed")
    if harness not in ("claude", "opencode"):
        return body
    if harness == "claude":
        binding = (
            b"## Verb Mappings\n\n"
            b"Claude Code binds the shared synchronous vocabulary to its built-in Agent tool.\n\n"
            b"| Verb | Syntax | Native Binding |\n"
            b"|------|--------|----------------|\n"
            b"| `SEND` | `SEND <work> to <agent>` | Invoke the built-in Agent tool for the exact allowed `syspilot-<agent>` with `<work>` and wait for its result. |\n"
            b"| `RECEIVE` | `RECEIVE` | Use the task that started the current agent. |\n"
            b"| `RESPOND` | `RESPOND` | Return normal output as the Agent result. |\n\n"
        )
    else:
        binding = (
            b"## Verb Mappings\n\n"
            b"OpenCode binds the shared synchronous vocabulary to its native Task tool.\n\n"
            b"| Verb | Syntax | Native Binding |\n"
            b"|------|--------|----------------|\n"
            b"| `SEND` | `SEND <work> to <agent>` | Invoke native Task for the exact allowed `syspilot.<agent>` with `<work>` and wait for its result. |\n"
            b"| `RECEIVE` | `RECEIVE` | Use the task that started the current agent. |\n"
            b"| `RESPOND` | `RESPOND` | Return normal terminal output as the Task result. |\n\n"
        )
    return body[:start] + binding + body[end:]


def adapt_prompt(content: bytes, fallback_description: str) -> bytes:
    """Create an OpenCode command routing the full request to the source agent."""
    metadata, _ = parse_frontmatter(content)
    agent = metadata.get("agent")
    if not isinstance(agent, str) or not agent:
        raise ValueError("prompt agent is required")
    description = metadata.get("description", fallback_description)
    if not isinstance(description, str) or not description:
        raise ValueError("prompt description or agent fallback is required")
    return _render_frontmatter(
        {"description": description, "agent": agent}, b"$ARGUMENTS\n"
    )


def enumerate_product(source: SourceSnapshot) -> dict[str, bytes]:
    """Return only the four approved product source roots."""
    inventory: dict[str, bytes] = {}
    for path, content in sorted(source.files.items()):
        if not path.startswith(PRODUCT_ROOTS):
            continue
        if path.startswith("syspilot/agents/") and not path.endswith(".agent.md"):
            continue
        if path.startswith("syspilot/prompts/") and not path.endswith(".prompt.md"):
            continue
        inventory[path] = content
    return inventory


def _github_slug(repository: str) -> str:
    if "://" in repository or repository.startswith("git@"):
        parsed = urllib.parse.urlparse(repository)
        if (
            parsed.scheme != "https"
            or parsed.hostname != "github.com"
            or parsed.netloc != "github.com"
            or parsed.params
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("GitHub repository must be owner/name or a GitHub URL")
        value = parsed.path.removeprefix("/").removesuffix(".git").removesuffix("/")
    else:
        value = repository.removesuffix(".git")
    parts = value.split("/")
    if (
        len(parts) != 2
        or any(part in {"", ".", ".."} for part in parts)
        or any(re.fullmatch(r"[A-Za-z0-9_.-]+", part) is None for part in parts)
    ):
        raise ValueError("GitHub repository must be owner/name or a GitHub URL")
    return value


def _validated_branch(branch: str) -> str:
    if (
        not isinstance(branch, str)
        or not branch
        or branch.strip() != branch
        or any(ord(character) < 32 or ord(character) == 127 for character in branch)
    ):
        raise ValueError("GitHub branch must be a non-empty branch or revision")
    return branch


def _request_json(url: str) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "syspilot-installer",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(
        url,
        headers=headers,
    )
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def _validate_source_inventory(paths: list[str]) -> list[str]:
    if len(paths) != len(set(paths)):
        raise ValueError("source inventory contains duplicate paths")
    if INSTALLER_RUNTIME_SOURCE not in paths:
        raise ValueError("source inventory is missing syspilot/installer.py")
    for product_root in PRODUCT_ROOTS:
        if not any(path.startswith(product_root) for path in paths):
            raise ValueError(f"source inventory is missing product root: {product_root}")
    for path in paths:
        if path != INSTALLER_RUNTIME_SOURCE:
            _validated_source_path(path)
    return sorted(paths)


def acquire_source(repository: str, branch: str = "main") -> SourceSnapshot:
    """Resolve one branch and fetch product inventory and bytes at its revision."""
    slug = _github_slug(repository)
    branch = _validated_branch(branch)
    encoded_branch = urllib.parse.quote(branch, safe="")
    commit = _request_json(f"https://api.github.com/repos/{slug}/commits/{encoded_branch}")
    revision = commit["sha"]
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", revision):
        raise ValueError("GitHub commit response contains an invalid revision")
    tree = _request_json(
        f"https://api.github.com/repos/{slug}/git/trees/{revision}?recursive=1"
    )
    if not isinstance(tree, dict) or tree.get("truncated") is True:
        raise ValueError("GitHub source inventory is truncated")
    paths = _validate_source_inventory([
        item["path"]
        for item in tree["tree"]
        if item.get("type") == "blob"
        and (
            item["path"].startswith(PRODUCT_ROOTS)
            or item["path"] == INSTALLER_RUNTIME_SOURCE
        )
    ])
    files: dict[str, bytes] = {}
    for path in paths:
        url = f"https://raw.githubusercontent.com/{slug}/{revision}/{path}"
        with urllib.request.urlopen(url) as response:
            files[path] = response.read()
    return SourceSnapshot(files=files, revision=revision, branch=branch)


def _atomic_write(
    path: Path,
    content: bytes,
    *,
    target_root: Path | None = None,
    relative: str | None = None,
    mutation_hook: Callable[[str, Path], None] | None = None,
    preflight_phase: str = "before_temp_create",
    expected_paths: Mapping[str, PathIdentity] | None = None,
    target_identity: PathIdentity | None = None,
) -> str | None:
    if os.name != "nt" and target_root is not None and relative is not None:
        if expected_paths is None or target_identity is None:
            raise RuntimeError("POSIX descriptor mutation requires frozen identities")
        return _atomic_write_posix(
            path,
            content,
            target_root=target_root,
            relative=relative,
            mutation_hook=mutation_hook,
            preflight_phase=preflight_phase,
            expected_paths=expected_paths,
            target_identity=target_identity,
        )
    if target_root is not None and relative is not None:
        _validate_target_path(target_root, relative)
    if content.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"source contains a UTF-8 BOM: {path}")
    if path.exists():
        if path.read_bytes() == content:
            return None
        action = "updated"
    else:
        action = "installed"
    path.parent.mkdir(parents=True, exist_ok=True)
    parent_identity = _path_identity(path.parent)
    if mutation_hook is not None:
        mutation_hook(preflight_phase, path)
    if target_root is not None and relative is not None:
        _validate_target_path(target_root, relative)
        if _path_identity(path.parent) != parent_identity:
            raise RuntimeError(f"target parent identity changed: {relative}")
    descriptor, temporary_name = tempfile.mkstemp(prefix=".syspilot-write-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        if mutation_hook is not None:
            mutation_hook("before_replace", path)
        if target_root is not None and relative is not None:
            _validate_target_path(target_root, relative)
            if _path_identity(path.parent) != parent_identity:
                raise RuntimeError(f"target parent identity changed: {relative}")
        os.replace(temporary_name, path)
    except BaseException:
        Path(temporary_name).unlink(missing_ok=True)
        raise
    return action


def _posix_directory_flags() -> int:
    if not hasattr(os, "O_DIRECTORY") or not hasattr(os, "O_NOFOLLOW"):
        raise RuntimeError("POSIX descriptor no-follow operations are unavailable")
    # os.rename, not os.replace, is the dir_fd-capable primitive on macOS; both are
    # atomic-overwrite on POSIX (they only differ on Windows, excluded by the caller).
    required = (os.open, os.stat, os.mkdir, os.unlink, os.rmdir, os.rename)
    if any(operation not in os.supports_dir_fd for operation in required):
        raise RuntimeError("POSIX descriptor-relative operations are unavailable")
    return os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW


def _directory_identity(metadata: os.stat_result) -> PathIdentity:
    if not stat.S_ISDIR(metadata.st_mode):
        return PathIdentity("other")
    return PathIdentity("directory", device=metadata.st_dev, file_id=metadata.st_ino)


def _posix_identity_at(parent_fd: int, name: str) -> PathIdentity:
    try:
        metadata = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return PathIdentity("missing")
    if stat.S_ISLNK(metadata.st_mode):
        return PathIdentity("link")
    if stat.S_ISDIR(metadata.st_mode):
        return _directory_identity(metadata)
    if not stat.S_ISREG(metadata.st_mode):
        return PathIdentity("other")
    descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
    try:
        opened = os.fstat(descriptor)
        digest = hashlib.sha256()
        while chunk := os.read(descriptor, 1024 * 1024):
            digest.update(chunk)
        if (opened.st_dev, opened.st_ino) != (metadata.st_dev, metadata.st_ino):
            raise RuntimeError(f"target identity changed while opening: {name}")
        return PathIdentity(
            "file", digest.hexdigest(), opened.st_dev, opened.st_ino
        )
    finally:
        os.close(descriptor)


def _open_posix_parent(
    target_root: Path,
    relative: str,
    expected_paths: Mapping[str, PathIdentity],
    target_identity: PathIdentity,
) -> tuple[int, str]:
    parts = PurePosixPath(_validated_relative(relative)).parts
    flags = _posix_directory_flags()
    descriptor = os.open(target_root, flags)
    try:
        if _directory_identity(os.fstat(descriptor)) != target_identity:
            raise RuntimeError("target root identity changed")
        prefix: list[str] = []
        for part in parts[:-1]:
            prefix.append(part)
            child = os.open(part, flags, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
            key = _canonical_checkpoint_relative("/".join(prefix))
            expected = expected_paths.get(key)
            if expected is not None and _directory_identity(os.fstat(descriptor)) != expected:
                raise RuntimeError(
                    f"target ancestry identity changed: {'/'.join(prefix)}"
                )
        return descriptor, parts[-1]
    except BaseException:
        os.close(descriptor)
        raise


def _assert_open_parent_current(
    target_root: Path, relative: str, parent_fd: int
) -> None:
    parent = target_root.joinpath(*PurePosixPath(relative).parts[:-1])
    if _path_identity(parent) != _directory_identity(os.fstat(parent_fd)):
        raise RuntimeError(f"target parent identity changed: {relative}")


def _atomic_write_posix(
    path: Path,
    content: bytes,
    *,
    target_root: Path,
    relative: str,
    mutation_hook: Callable[[str, Path], None] | None,
    preflight_phase: str,
    expected_paths: Mapping[str, PathIdentity],
    target_identity: PathIdentity,
) -> str | None:
    if content.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"source contains a UTF-8 BOM: {path}")
    parent_fd, name = _open_posix_parent(
        target_root, relative, expected_paths, target_identity
    )
    temporary_name = f".syspilot-write-{uuid.uuid4()}"
    try:
        current = _posix_identity_at(parent_fd, name)
        expected = expected_paths[_canonical_checkpoint_relative(relative)]
        if current != expected:
            raise RuntimeError(f"concurrent target change detected: {relative}")
        if current.kind == "file":
            descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
            try:
                existing = b""
                while chunk := os.read(descriptor, 1024 * 1024):
                    existing += chunk
            finally:
                os.close(descriptor)
            if existing == content:
                return None
            action = "updated"
        else:
            action = "installed"
        if mutation_hook is not None:
            mutation_hook(preflight_phase, path)
        _assert_open_parent_current(target_root, relative, parent_fd)
        if mutation_hook is not None:
            mutation_hook(f"after_{preflight_phase}_validation", path)
        descriptor = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            if mutation_hook is not None:
                mutation_hook("before_replace", path)
            _assert_open_parent_current(target_root, relative, parent_fd)
            if mutation_hook is not None:
                mutation_hook("after_before_replace_validation", path)
            # os.rename (not os.replace) is the dir_fd-capable primitive on macOS;
            # POSIX rename() already atomically replaces an existing destination.
            os.rename(
                temporary_name,
                name,
                src_dir_fd=parent_fd,
                dst_dir_fd=parent_fd,
            )
        except BaseException:
            try:
                os.unlink(temporary_name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
            raise
        return action
    finally:
        os.close(parent_fd)


def _safe_mkdir(
    target_root: Path,
    relative: str,
    expected_paths: Mapping[str, PathIdentity],
    target_identity: PathIdentity,
    mutation_hook: Callable[[str, Path], None] | None,
    *,
    phase: str = "before_mkdir",
) -> None:
    path = target_root.joinpath(*PurePosixPath(relative).parts)
    if os.name == "nt":
        path.mkdir()
        return
    parent_fd, name = _open_posix_parent(
        target_root, relative, expected_paths, target_identity
    )
    try:
        if _posix_identity_at(parent_fd, name).kind != "missing":
            raise RuntimeError(f"concurrent target change detected: {relative}")
        if mutation_hook is not None:
            mutation_hook(phase, path)
        _assert_open_parent_current(target_root, relative, parent_fd)
        if mutation_hook is not None:
            mutation_hook(f"after_{phase}_validation", path)
        os.mkdir(name, dir_fd=parent_fd)
    finally:
        os.close(parent_fd)


def _safe_delete(
    target_root: Path,
    relative: str,
    expected: PathIdentity,
    mutation_hook: Callable[[str, Path], None] | None,
    *,
    phase: str = "before_delete",
    expected_paths: Mapping[str, PathIdentity] | None = None,
    target_identity: PathIdentity | None = None,
) -> None:
    if os.name != "nt":
        if expected_paths is None or target_identity is None:
            raise RuntimeError("POSIX descriptor mutation requires frozen identities")
        path = target_root.joinpath(*PurePosixPath(relative).parts)
        parent_fd, name = _open_posix_parent(
            target_root, relative, expected_paths, target_identity
        )
        try:
            if mutation_hook is not None:
                mutation_hook(phase, path)
            _assert_open_parent_current(target_root, relative, parent_fd)
            if _posix_identity_at(parent_fd, name) != expected:
                raise RuntimeError(f"concurrent target change detected: {relative}")
            if mutation_hook is not None:
                mutation_hook(f"after_{phase}_validation", path)
            if expected.kind == "file":
                os.unlink(name, dir_fd=parent_fd)
            elif expected.kind == "directory":
                os.rmdir(name, dir_fd=parent_fd)
        finally:
            os.close(parent_fd)
        return
    path = _validate_target_path(target_root, relative)
    parent_identity = _path_identity(path.parent)
    if mutation_hook is not None:
        mutation_hook(phase, path)
    path = _validate_target_path(target_root, relative)
    if _path_identity(path.parent) != parent_identity:
        raise RuntimeError(f"target parent identity changed: {relative}")
    _assert_identity(path, expected, relative)
    if expected.kind == "file":
        path.unlink()
    elif expected.kind == "directory":
        path.rmdir()


def _target_key(target_root: Path, path: Path) -> str:
    return path.parent.relative_to(target_root).as_posix()


def _inject_failure(requested_phase: str | None, current_phase: str) -> None:
    if requested_phase == current_phase:
        raise RuntimeError(f"injected failure at {current_phase}")


def _agent_description(inventory: Mapping[str, bytes], agent_name: str) -> str:
    source_name = f"syspilot/agents/{agent_name}.agent.md"
    if source_name not in inventory:
        raise ValueError(f"prompt agent source is missing: {source_name}")
    metadata, _ = parse_frontmatter(inventory[source_name])
    description = metadata.get("description")
    if not isinstance(description, str) or not description:
        raise ValueError(f"agent description is missing: {source_name}")
    return description


def _selected_inventory(source: SourceSnapshot) -> dict[str, bytes]:
    inventory = enumerate_product(source)
    skill_groups: dict[str, str] = {}
    selected_directory: str | None = None
    for path, content in inventory.items():
        relative = PurePosixPath(path)
        if not path.startswith("syspilot/skills/") or relative.name != "SKILL.md":
            continue
        metadata, _ = parse_frontmatter(content)
        skill_directory = relative.parts[2]
        group = metadata.get("group")
        if isinstance(group, str):
            skill_groups[skill_directory] = group
        if metadata.get("name") == ORCHESTRATION_SKILL:
            selected_directory = skill_directory
    if selected_directory is None:
        raise ValueError(
            f"selected orchestration Skill is missing: {ORCHESTRATION_SKILL}"
        )
    selected_group = skill_groups.get(selected_directory)
    selected: dict[str, bytes] = {}
    for path, content in inventory.items():
        if not path.startswith("syspilot/skills/"):
            selected[path] = content
            continue
        skill_name = PurePosixPath(path).parts[2]
        if (
            selected_group is not None
            and skill_groups.get(skill_name) == selected_group
            and skill_name != selected_directory
        ):
            continue
        selected[path] = content
    selected_skill = f"syspilot/skills/{selected_directory}/SKILL.md"
    if selected_skill not in selected:
        raise ValueError(
            f"selected orchestration Skill is missing: {ORCHESTRATION_SKILL}"
        )
    return selected


def _qoder_zip_info(member: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(member, date_time=QODER_ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = (stat.S_IFREG | 0o644) << 16
    return info


def _validate_qoder_archive(
    archive: bytes,
    payloads: Mapping[str, bytes],
    manifest: Mapping[str, Any],
) -> None:
    with zipfile.ZipFile(io.BytesIO(archive)) as package:
        members = package.namelist()
        if members != sorted(members) or len(members) != len(set(members)):
            raise ValueError("Qoder package member inventory is not normalized")
        if set(members) != {"plugin.json", *payloads}:
            raise ValueError("Qoder package member inventory is invalid")
        for info in package.infolist():
            path = PurePosixPath(info.filename)
            if (
                path.is_absolute()
                or not path.parts
                or any(part in {"", ".", ".."} for part in path.parts)
                or info.date_time != QODER_ZIP_TIMESTAMP
                or info.create_system != 3
                or info.external_attr != (stat.S_IFREG | 0o644) << 16
                or info.compress_type != zipfile.ZIP_DEFLATED
                or info.extra
                or info.comment
            ):
                raise ValueError(f"Qoder package member metadata is invalid: {info.filename}")
        parsed_manifest = json.loads(package.read("plugin.json"))
        if parsed_manifest != manifest:
            raise ValueError("Qoder package manifest is invalid")
        for member, content in payloads.items():
            if package.read(member) != content:
                raise ValueError(f"Qoder package member content is invalid: {member}")


def _build_qoder_archive(
    inventory: Mapping[str, bytes], source_revision: str
) -> bytes:
    payloads: dict[str, bytes] = {}
    for source_path, content in inventory.items():
        relative = _validated_source_path(source_path)
        source_kind = relative.parts[1]
        source_tail = PurePosixPath(*relative.parts[2:])
        if source_kind == "agents":
            member = (PurePosixPath("agents") / source_tail).as_posix()
            payloads[member] = adapt_agent(content, "qoder", source_path)
        elif source_kind == "skills" and source_tail.name == "SKILL.md":
            member = (PurePosixPath("skills") / source_tail).as_posix()
            payloads[member] = adapt_skill(content, "qoder")

    member_digests = {
        member: hashlib.sha256(content).hexdigest()
        for member, content in sorted(payloads.items())
    }
    manifest = {
        "id": QODER_PACKAGE_ID,
        "source_revision": source_revision,
        "members": member_digests,
    }
    manifest_bytes = (
        json.dumps(manifest, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    )
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as package:
        for member, content in sorted(
            {"plugin.json": manifest_bytes, **payloads}.items()
        ):
            package.writestr(
                _qoder_zip_info(member),
                content,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
    archive = buffer.getvalue()
    _validate_qoder_archive(archive, payloads, manifest)
    return archive


def _build_targets(
    inventory: Mapping[str, bytes],
    target_root: Path,
    harness: str,
    source_revision: str,
) -> dict[str, bytes]:
    if harness not in HARNESS_ROOTS:
        raise ValueError(f"unsupported initiating harness: {harness}")
    if harness == "qoder":
        return {QODER_ARCHIVE: _build_qoder_archive(inventory, source_revision)}
    agent_identities: dict[str, str] = {}
    for source_path, content in inventory.items():
        relative = _validated_source_path(source_path)
        if relative.parts[1] != "agents":
            continue
        metadata, _ = parse_frontmatter(content)
        name = metadata.get("name")
        identity = metadata.get("agent")
        if isinstance(name, str) and isinstance(identity, str):
            agent_identities[name] = identity

    targets: dict[str, bytes] = {}
    for source_path, content in inventory.items():
        relative = _validated_source_path(source_path)
        source_kind = relative.parts[1]
        source_tail = PurePosixPath(*relative.parts[2:])
        harness_root = PurePosixPath(HARNESS_ROOTS[harness])
        if source_kind == "templates":
            destination = PurePosixPath(".syspilot/templates") / source_tail
            targets[_validated_relative(destination.as_posix())] = content
        elif source_kind == "skills" and source_tail.name != "SKILL.md":
            destination = PurePosixPath(".syspilot/skills") / source_tail
            targets[_validated_relative(destination.as_posix())] = content
        elif harness == "vscode":
            destination = harness_root / source_kind / source_tail
            targets[_validated_relative(destination.as_posix())] = content
        elif source_kind == "agents":
            filename = source_tail.name.removesuffix(".agent.md") + ".md"
            destination = harness_root / "agents" / source_tail.parent / filename
            targets[_validated_relative(destination.as_posix())] = adapt_agent(
                content, harness, source_path, agent_identities
            )
        elif source_kind == "skills":
            destination = harness_root / "skills" / source_tail
            targets[_validated_relative(destination.as_posix())] = adapt_skill(content, harness)
        elif source_kind == "prompts" and harness == "opencode":
            filename = source_tail.name.removesuffix(".prompt.md") + ".md"
            prompt_meta, _ = parse_frontmatter(content)
            agent = prompt_meta.get("agent")
            if not isinstance(agent, str):
                raise ValueError(f"prompt agent is missing: {source_path}")
            destination = harness_root / "commands" / source_tail.parent / filename
            targets[_validated_relative(destination.as_posix())] = adapt_prompt(
                content, _agent_description(inventory, agent)
            )
    return targets


def _eligible_orphan(name: str) -> bool:
    return name.startswith("syspilot.") and not name.endswith(".tailoring.md")


def _walk_owned_tree(target_root: Path, relative: str) -> list[str]:
    path = _validate_target_path(target_root, relative)
    identity = _path_identity(path)
    if identity.kind != "directory":
        return [relative]
    entries: list[str] = []
    for child in path.iterdir():
        child_relative = child.relative_to(target_root).as_posix()
        _validate_target_path(target_root, child_relative)
        entries.extend(_walk_owned_tree(target_root, child_relative))
    entries.append(relative)
    return entries


def _orphan_plan(
    target_root: Path, targets: Mapping[str, bytes]
) -> tuple[str, ...]:
    expected_by_directory: dict[str, set[str]] = {}
    for relative_value in targets:
        relative = PurePosixPath(relative_value)
        if "skills" in relative.parts:
            skill_index = relative.parts.index("skills")
            if len(relative.parts) <= skill_index + 1:
                continue
            directory = PurePosixPath(*relative.parts[: skill_index + 1]).as_posix()
            expected_by_directory.setdefault(directory, set()).add(
                relative.parts[skill_index + 1]
            )
        else:
            expected_by_directory.setdefault(relative.parent.as_posix(), set()).add(
                relative.name
            )
    deletes: list[str] = []
    for directory_name, expected in expected_by_directory.items():
        directory = _validate_target_path(target_root, directory_name)
        identity = _path_identity(directory)
        if identity.kind == "missing":
            continue
        if identity.kind != "directory":
            raise ValueError(f"managed target is not a directory: {directory_name}")
        for item in directory.iterdir():
            if not _eligible_orphan(item.name) or item.name in expected:
                continue
            relative = item.relative_to(target_root).as_posix()
            deletes.extend(_walk_owned_tree(target_root, relative))
    return tuple(dict.fromkeys(deletes))


def _with_parent_paths(paths: set[str]) -> set[str]:
    expanded = set(paths)
    for value in list(paths):
        parent = PurePosixPath(value).parent
        while parent.parts:
            expanded.add(parent.as_posix())
            parent = parent.parent
    return expanded


def build_install_plan(
    source: SourceSnapshot, target_root: Path, harness: str
) -> InstallPlan:
    """Parse, adapt, derive, and preflight the complete target plan."""
    target_root = target_root.resolve(strict=True)
    if not target_root.is_dir():
        raise ValueError("target root is not a directory")
    inventory = _selected_inventory(source)
    targets = _build_targets(inventory, target_root, harness, source.revision)
    try:
        runtime_content = source.files[INSTALLER_RUNTIME_SOURCE]
    except KeyError as error:
        raise ValueError("selected source is missing syspilot/installer.py") from error
    targets[".syspilot/installer.py"] = runtime_content
    for relative, content in (("docs/index.rst", DOC_INDEX), ("docs/conf.py", DOC_CONF)):
        path = _validate_target_path(target_root, relative)
        if _path_identity(path).kind == "missing":
            targets[relative] = content
    deletes = _orphan_plan(target_root, targets)
    collisions = set(targets).intersection(deletes)
    if collisions:
        raise ValueError(f"target plan collision: {sorted(collisions)[0]}")
    mutable_names = _with_parent_paths(set(targets).union(deletes))
    expected: dict[str, PathIdentity] = {}
    for relative in sorted(mutable_names):
        path = _validate_target_path(target_root, relative)
        identity = _path_identity(path)
        if identity.kind in {"link", "other"}:
            raise ValueError(f"unsupported mutable target type: {relative}")
        expected[relative] = identity
    return InstallPlan(
        target_root=target_root,
        target_identity=_path_identity(target_root),
        harness=harness,
        writes=dict(targets),
        deletes=deletes,
        expected=expected,
        mutable_paths=tuple(sorted(mutable_names)),
    )


def _assert_identity(path: Path, expected: PathIdentity, relative: str) -> None:
    if _path_identity(path) != expected:
        raise RuntimeError(f"concurrent target change detected: {relative}")


def _execute_plan(
    plan: InstallPlan,
    summary: dict[str, DirectorySummary],
    last: dict[str, PathIdentity],
    *,
    failure_phase: str | None,
    phase_observer: Callable[[str], None],
    mutation_hook: Callable[[str, Path], None] | None,
) -> None:
    write_names = set(plan.writes)
    delete_names = set(plan.deletes)
    parent_names = set(plan.mutable_paths) - write_names - delete_names
    phase_observer("first_mutation")
    for relative in sorted(parent_names, key=lambda value: (value.count("/"), value)):
        path = _validate_target_path(plan.target_root, relative)
        _assert_identity(path, plan.expected[relative], relative)
        if plan.expected[relative].kind == "missing":
            _safe_mkdir(
                plan.target_root,
                relative,
                last,
                plan.target_identity,
                mutation_hook,
            )
            _validate_target_path(plan.target_root, relative)
        last[_canonical_checkpoint_relative(relative)] = _path_identity(path)

    ordered_writes = sorted(
        plan.writes.items(),
        key=lambda item: (item[0] != ".syspilot/installer.py", item[0]),
    )
    for relative, content in ordered_writes:
        path = _validate_target_path(plan.target_root, relative)
        _assert_identity(path, plan.expected[relative], relative)
        action = _atomic_write(
            path,
            content,
            target_root=plan.target_root,
            relative=relative,
            mutation_hook=mutation_hook,
            expected_paths=last,
            target_identity=plan.target_identity,
        )
        last[_canonical_checkpoint_relative(relative)] = _path_identity(path)
        row = summary.setdefault(_target_key(plan.target_root, path), DirectorySummary())
        if action == "installed":
            row.installed += 1
        elif action == "updated":
            row.updated += 1
        if relative == ".syspilot/installer.py":
            _inject_failure(failure_phase, "runtime_write")
    _inject_failure(failure_phase, "target_write")
    _inject_failure(failure_phase, "docs_bootstrap")

    for relative in plan.deletes:
        path = _validate_target_path(plan.target_root, relative)
        _assert_identity(path, plan.expected[relative], relative)
        identity = _path_identity(path)
        _safe_delete(
            plan.target_root,
            relative,
            identity,
            mutation_hook,
            expected_paths=last,
            target_identity=plan.target_identity,
        )
        last[_canonical_checkpoint_relative(relative)] = PathIdentity("missing")
        key = PurePosixPath(relative).parent.as_posix()
        summary.setdefault(key, DirectorySummary()).removed += 1
    _inject_failure(failure_phase, "orphan_cleanup")


def bootstrap_docs(target_root: Path) -> list[str]:
    """Create each missing minimal Sphinx file without overwriting either."""
    target_root = target_root.resolve(strict=True)
    target_identity = _path_identity(target_root)
    docs = _validate_target_path(target_root, "docs")
    docs_identity = _path_identity(docs)
    if docs_identity.kind == "missing":
        _safe_mkdir(
            target_root,
            "docs",
            {"docs": docs_identity},
            target_identity,
            None,
        )
        docs_identity = _path_identity(docs)
    elif docs_identity.kind != "directory":
        raise ValueError("unsupported mutable target type: docs")
    created: list[str] = []
    for relative, content in (("docs/index.rst", DOC_INDEX), ("docs/conf.py", DOC_CONF)):
        path = _validate_target_path(target_root, relative)
        current = _path_identity(path)
        if current.kind == "missing":
            _atomic_write(
                path,
                content,
                target_root=target_root,
                relative=relative,
                expected_paths={"docs": docs_identity, relative: current},
                target_identity=target_identity,
            )
            created.append(relative)
    return created


def create_checkpoint(
    target_root: Path,
    *,
    mutable_paths: list[Path],
    expected: Mapping[str, PathIdentity] | None = None,
    plan: InstallPlan | None = None,
) -> Checkpoint:
    """Capture and persist declared target bytes, directories, and Git index."""
    target_root = target_root.resolve(strict=True)
    now = _checkpoint_now()
    _cleanup_stale_checkpoints(now)
    files: dict[str, bytes] = {}
    directories: set[str] = set()
    display_paths: dict[str, str] = {}
    path_fingerprints: dict[str, PathIdentity] = {}
    for path in mutable_paths:
        # match target_root's own resolve() above, or a /var-vs-/private/var-style
        # symlink prefix mismatch (e.g. macOS) makes an owned path look foreign
        relative = path.resolve().relative_to(target_root)
        if relative.parts and relative.parts[0] == ".git":
            continue
        relative_name = relative.as_posix()
        _validate_target_path(target_root, relative_name)
        identity = _path_identity(path)
        if expected is not None and identity != expected[relative_name]:
            raise RuntimeError(f"target changed before checkpoint: {relative_name}")
        key = _canonical_checkpoint_relative(relative_name)
        if key in display_paths:
            raise ValueError("checkpoint contains a duplicate normalized mutable path")
        display_paths[key] = relative_name
        path_fingerprints[key] = identity
        if identity.kind == "directory":
            directories.add(key)
        elif identity.kind == "file":
            files[key] = path.read_bytes()
        elif identity.kind not in {"missing"}:
            raise ValueError(f"unsupported mutable target type: {relative_name}")
    _, git_index_path, git_head, git_ref = _discover_git_state(target_root)
    checkpoint = Checkpoint(
        identifier=str(uuid.uuid4()),
        target_root=target_root,
        files=files,
        directories=frozenset(directories),
        git_index=git_index_path.read_bytes()
        if git_index_path is not None and git_index_path.is_file()
        else None,
        git_head=git_head,
        git_ref=git_ref,
        mutable_paths=frozenset(display_paths),
        git_index_path=str(git_index_path) if git_index_path is not None else None,
        display_paths=display_paths,
        path_fingerprints=path_fingerprints,
        nonce=str(uuid.uuid4()),
        target_identity=_path_identity(target_root),
        created_at=now,
        expires_at=now + CHECKPOINT_TTL_SECONDS,
        plan_digest=_plan_digest(plan) if plan is not None else None,
    )
    secret = os.urandom(32)
    checkpoint = replace(
        checkpoint, binding=_checkpoint_binding(checkpoint, secret)
    )
    _store_checkpoint(checkpoint, secret)
    return checkpoint


def restore_checkpoint(
    checkpoint: Checkpoint,
    *,
    expected_current: Mapping[str, PathIdentity] | None = None,
    expected_git_head: str | None = None,
    expected_git_index: bytes | None = None,
    mutation_hook: Callable[[str, Path], None] | None = None,
) -> None:
    """Restore only checkpoint-owned paths and preserve concurrent conflicts."""
    if not checkpoint.leased:
        checkpoint = _lease_checkpoint(
            checkpoint.target_root, checkpoint.identifier
        )
    target_root = checkpoint.target_root
    _, discovered_index, current_head, current_ref = _discover_git_state(target_root)
    conflicts: list[str] = []
    if expected_current is None:
        restore_current = {
            key: _path_identity(
                _validate_target_path(target_root, checkpoint.display_paths[key])
            )
            for key in checkpoint.mutable_paths
        }
    else:
        restore_current = dict(expected_current)
    if discovered_index is not None and expected_git_head is not None:
        if current_head != expected_git_head or current_ref != checkpoint.git_ref:
            conflicts.append("<git-ref>")
        elif checkpoint.git_ref is not None:
            if checkpoint.git_head is None:
                command = [
                    "git",
                    "update-ref",
                    "-d",
                    checkpoint.git_ref,
                    expected_git_head,
                ]
            else:
                command = [
                    "git",
                    "update-ref",
                    checkpoint.git_ref,
                    checkpoint.git_head,
                    expected_git_head,
                ]
            if subprocess.run(command, cwd=target_root).returncode != 0:
                conflicts.append("<git-ref>")
        elif checkpoint.git_head is not None:
            command = [
                "git",
                "update-ref",
                "--no-deref",
                "HEAD",
                checkpoint.git_head,
                expected_git_head,
            ]
            if subprocess.run(command, cwd=target_root).returncode != 0:
                conflicts.append("<git-ref>")
    restorable: list[str] = []
    for key in checkpoint.mutable_paths:
        relative = checkpoint.display_paths[key]
        try:
            path = _validate_target_path(target_root, relative)
        except ValueError:
            conflicts.append(relative)
            continue
        if (
            expected_current is not None
            and _path_identity(path) != expected_current[key]
        ):
            conflicts.append(relative)
            continue
        restorable.append(key)
    for key in sorted(
        restorable,
        key=lambda value: (-checkpoint.display_paths[value].count("/"), value),
    ):
        if key in checkpoint.files or key in checkpoint.directories:
            continue
        relative = checkpoint.display_paths[key]
        try:
            path = _validate_target_path(target_root, relative)
        except ValueError:
            conflicts.append(relative)
            continue
        identity = _path_identity(path)
        if identity.kind in {"file", "directory"}:
            try:
                _safe_delete(
                    target_root,
                    relative,
                    identity,
                    mutation_hook,
                    phase="before_restore",
                    expected_paths=restore_current,
                    target_identity=checkpoint.target_identity,
                )
                restore_current[key] = PathIdentity("missing")
            except (OSError, RuntimeError, ValueError):
                conflicts.append(relative)
    for key in sorted(
        checkpoint.directories,
        key=lambda value: (checkpoint.display_paths[value].count("/"), value),
    ):
        if key not in restorable:
            continue
        relative = checkpoint.display_paths[key]
        try:
            path = _validate_target_path(target_root, relative)
            parent_identity = _path_identity(path.parent)
            if mutation_hook is not None:
                mutation_hook("before_restore", path)
            path = _validate_target_path(target_root, relative)
            if _path_identity(path.parent) != parent_identity:
                raise RuntimeError(f"target parent identity changed: {relative}")
            if expected_current is not None:
                _assert_identity(path, expected_current[key], relative)
        except (RuntimeError, ValueError):
            conflicts.append(relative)
            continue
        if _path_identity(path).kind == "missing":
            try:
                _safe_mkdir(
                    target_root,
                    relative,
                    restore_current,
                    checkpoint.target_identity,
                    mutation_hook,
                    phase="before_restore",
                )
            except (OSError, RuntimeError, ValueError):
                conflicts.append(relative)
                continue
            restore_current[key] = _path_identity(path)
            _validate_target_path(target_root, relative)
    for key, content in checkpoint.files.items():
        if key not in restorable:
            continue
        relative = checkpoint.display_paths[key]
        try:
            path = _validate_target_path(target_root, relative)
        except ValueError:
            conflicts.append(relative)
            continue
        if _path_identity(path).kind == "directory":
            try:
                _safe_delete(
                    target_root,
                    relative,
                    PathIdentity(
                        "directory",
                        device=_path_identity(path).device,
                        file_id=_path_identity(path).file_id,
                    ),
                    mutation_hook,
                    phase="before_restore",
                    expected_paths=restore_current,
                    target_identity=checkpoint.target_identity,
                )
                restore_current[key] = PathIdentity("missing")
            except (OSError, RuntimeError, ValueError):
                conflicts.append(relative)
                continue
        try:
            _atomic_write(
                path,
                content,
                target_root=target_root,
                relative=relative,
                mutation_hook=mutation_hook,
                preflight_phase="before_restore",
                expected_paths=restore_current,
                target_identity=checkpoint.target_identity,
            )
            restore_current[key] = _path_identity(path)
        except (RuntimeError, ValueError):
            conflicts.append(relative)
    if checkpoint.git_index_path is not None:
        git_index = Path(checkpoint.git_index_path)
        if discovered_index != git_index.absolute():
            conflicts.append("<git-index>")
        elif (
            expected_git_index is not None
            and (
                git_index.read_bytes() if git_index.is_file() else None
            )
            != expected_git_index
        ):
            conflicts.append("<git-index>")
        elif checkpoint.git_index is None:
            git_index.unlink(missing_ok=True)
        else:
            git_index.parent.mkdir(parents=True, exist_ok=True)
            git_index.write_bytes(checkpoint.git_index)
    _retire_checkpoint(checkpoint.identifier)
    if conflicts:
        raise RuntimeError(
            "incomplete rollback: rollback conflict at "
            + ", ".join(sorted(set(conflicts)))
        )


def check_dependencies() -> None:
    """Fail before mutation unless the two executable dependencies work."""
    for executable in ("uv", "git"):
        try:
            subprocess.run(
                [executable, "--version"],
                check=True,
                capture_output=True,
                text=True,
            )
        except (FileNotFoundError, subprocess.CalledProcessError) as error:
            raise DependencyError(
                f"Required executable is unavailable: {executable}"
            ) from error


def validate_sphinx(
    target_root: Path,
    *,
    output: Path | None = None,
    doctrees: Path | None = None,
) -> None:
    """Re-enter the installed PEP 723 runtime for Sphinx validation."""
    if output is None or doctrees is None:
        with tempfile.TemporaryDirectory(prefix="syspilot-sphinx-") as temporary:
            temporary_root = Path(temporary)
            validate_sphinx(
                target_root,
                output=output or temporary_root / "html",
                doctrees=doctrees or temporary_root / "doctrees",
            )
        return
    subprocess.run(
        [
            "uv",
            "run",
            "--no-project",
            ".syspilot/installer.py",
            "validate-sphinx",
            "--target",
            str(target_root.resolve()),
            "--output",
            str(output.resolve()),
            "--doctrees",
            str(doctrees.resolve()),
        ],
        cwd=target_root,
        check=True,
        capture_output=True,
        text=True,
    )


def _run_sphinx(target_root: Path, output: Path, doctrees: Path) -> None:
    """Run Sphinx inside the uv-resolved script environment."""
    from sphinx.cmd.build import build_main

    result = build_main(
        [
            "-W",
            "-d",
            str(doctrees),
            "-b",
            "html",
            str(target_root / "docs"),
            str(output),
        ]
    )
    if result != 0:
        raise RuntimeError(f"Sphinx validation failed with exit code {result}")


def _commit_install(target_root: Path, branch: str, harness: str) -> str | None:
    git_dir, _, _, _ = _discover_git_state(target_root)
    if git_dir is None:
        raise RuntimeError("target is not a Git repository")
    paths = [
        path
        for path in (
            HARNESS_ROOTS[harness],
            ".syspilot",
            "docs/index.rst",
            "docs/conf.py",
        )
        if (target_root / path).exists()
    ]
    subprocess.run(["git", "add", "-A", "--", *paths], cwd=target_root, check=True)
    staged = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=target_root
    ).returncode
    if staged == 0:
        return None
    subprocess.run(
        [
            "git",
            "commit",
            "--only",
            "-m",
            f"chore: install syspilot from {branch}",
            "--",
            *paths,
        ],
        cwd=target_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=target_root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _install_snapshot_attempt(
    source: SourceSnapshot,
    target_root: Path,
    *,
    initiating_harness: str,
    dependency_check: Callable[[], None] = check_dependencies,
    validator: Callable[[Path], None] = validate_sphinx,
    commit: bool = True,
    checkpoint_id: str | None = None,
    failure_phase: str | None = None,
    committer: Callable[[Path, str, str], str | None] | None = None,
    phase_observer: Callable[[str], None] | None = None,
    mutation_hook: Callable[[str, Path], None] | None = None,
    _claimed_checkpoint: Checkpoint | None = None,
) -> InstallResult:
    """Install one immutable source snapshot transactionally."""
    summary: dict[str, DirectorySummary] = {}
    observe = phase_observer or (lambda _phase: None)
    checkpoint = _claimed_checkpoint
    try:
        _inject_failure(failure_phase, "dependency_gate")
        dependency_check()
    except Exception as error:
        if checkpoint_id is not None:
            _retire_checkpoint(checkpoint_id)
        return InstallResult(False, source.branch, source.revision, error=str(error))

    try:
        _inject_failure(failure_phase, "yaml_parse")
        plan = build_install_plan(source, target_root, initiating_harness)
        observe("plan_validated")
    except Exception as error:
        if checkpoint_id is not None:
            _retire_checkpoint(checkpoint_id)
        return InstallResult(False, source.branch, source.revision, error=str(error))
    try:
        if checkpoint_id is None:
            created_checkpoint = create_checkpoint(
                plan.target_root,
                mutable_paths=[plan.target_root / relative for relative in plan.mutable_paths],
                expected=plan.expected,
                plan=plan,
            )
            checkpoint_id = created_checkpoint.identifier
            checkpoint = _lease_checkpoint(plan.target_root, checkpoint_id)
        observe("checkpoint_created")
        assert checkpoint is not None
        _validate_supplied_checkpoint(plan, checkpoint)
    except Exception as error:
        if checkpoint_id is not None:
            _retire_checkpoint(checkpoint_id)
        return InstallResult(False, source.branch, source.revision, error=str(error))
    last_states = {
        _canonical_checkpoint_relative(relative): identity
        for relative, identity in plan.expected.items()
    }
    created_git_head: str | None = None
    expected_git_index = checkpoint.git_index
    try:
        _execute_plan(
            plan,
            summary,
            last_states,
            failure_phase=failure_phase,
            phase_observer=observe,
            mutation_hook=mutation_hook,
        )
        validator(target_root)
        _inject_failure(failure_phase, "validation")
        _inject_failure(failure_phase, "summary")
        commit_operation = committer or _commit_install
        _inject_failure(failure_phase, "commit")
        commit_hash = (
            commit_operation(target_root, source.branch, initiating_harness)
            if commit
            else None
        )
        if commit_hash is not None:
            created_git_head = commit_hash
            _, current_index_path, _, _ = _discover_git_state(target_root)
            expected_git_index = (
                current_index_path.read_bytes()
                if current_index_path is not None and current_index_path.is_file()
                else None
            )
            observe("commit_created")
        if failure_phase == "post_commit_checkpoint_deletion":
            raise RuntimeError("injected failure before checkpoint deletion")
        _retire_checkpoint(checkpoint.identifier)
        package = plan.writes.get(QODER_ARCHIVE)
        return InstallResult(
            True,
            source.branch,
            source.revision,
            summary=summary,
            commit=commit_hash,
            status="staged" if initiating_harness == "qoder" else "installed",
            package_digest=(
                hashlib.sha256(package).hexdigest() if package is not None else None
            ),
        )
    except BaseException as error:
        rollback_error: Exception | None = None
        try:
            restore_checkpoint(
                checkpoint,
                expected_current=last_states,
                expected_git_head=created_git_head,
                expected_git_index=expected_git_index,
                mutation_hook=mutation_hook,
            )
        except Exception as restore_error:
            rollback_error = restore_error
        message = str(error)
        if rollback_error is not None:
            message = f"{message}; {rollback_error}"
        return InstallResult(
            False,
            source.branch,
            source.revision,
            summary=summary,
            error=message,
        )


def install_snapshot(
    source: SourceSnapshot,
    target_root: Path,
    *,
    initiating_harness: str,
    dependency_check: Callable[[], None] = check_dependencies,
    validator: Callable[[Path], None] = validate_sphinx,
    commit: bool = True,
    checkpoint_id: str | None = None,
    failure_phase: str | None = None,
    committer: Callable[[Path, str, str], str | None] | None = None,
    phase_observer: Callable[[str], None] | None = None,
    mutation_hook: Callable[[str, Path], None] | None = None,
    _claimed_checkpoint: Checkpoint | None = None,
) -> InstallResult:
    """Install one immutable source snapshot and retire supplied capability state."""
    checkpoint = _claimed_checkpoint
    owns_supplied_checkpoint = checkpoint is not None
    try:
        if checkpoint_id is not None and checkpoint is None:
            checkpoint = _lease_checkpoint(target_root, checkpoint_id)
            owns_supplied_checkpoint = True
        return _install_snapshot_attempt(
            source,
            target_root,
            initiating_harness=initiating_harness,
            dependency_check=dependency_check,
            validator=validator,
            commit=commit,
            checkpoint_id=checkpoint_id,
            failure_phase=failure_phase,
            committer=committer,
            phase_observer=phase_observer,
            mutation_hook=mutation_hook,
            _claimed_checkpoint=checkpoint,
        )
    except Exception as error:
        return InstallResult(False, source.branch, source.revision, error=str(error))
    finally:
        if owns_supplied_checkpoint and checkpoint_id is not None:
            _retire_checkpoint(checkpoint_id)


def install(
    repository: str,
    branch: str,
    target_root: Path,
    *,
    initiating_harness: str,
    checkpoint_id: str | None = None,
    dependency_check: Callable[[], None] = check_dependencies,
    source_acquirer: Callable[[str, str], SourceSnapshot] = acquire_source,
    failure_phase: str | None = None,
) -> InstallResult:
    """Acquire a selected source revision and execute the installation."""
    claimed = False
    if checkpoint_id is not None:
        try:
            _claim_checkpoint(checkpoint_id)
            claimed = True
        except Exception as error:
            return InstallResult(False, branch, "", error=str(error))
    try:
        if initiating_harness not in PRODUCTION_HARNESSES:
            raise ValueError(f"unsupported initiating harness: {initiating_harness}")
        _validated_branch(branch)
        _inject_failure(failure_phase, "dependency_gate")
        dependency_check()
        _inject_failure(failure_phase, "source_acquisition")
        source = source_acquirer(repository, branch)
        checkpoint = (
            _load_claimed_checkpoint(target_root, checkpoint_id)
            if checkpoint_id is not None
            else None
        )
        return install_snapshot(
            source,
            target_root,
            initiating_harness=initiating_harness,
            dependency_check=lambda: None,
            checkpoint_id=checkpoint_id,
            failure_phase=failure_phase,
            _claimed_checkpoint=checkpoint,
        )
    except Exception as error:
        return InstallResult(False, branch, "", error=str(error))
    finally:
        if claimed and checkpoint_id is not None:
            _retire_checkpoint(checkpoint_id)


def prepare_checkpoint(
    repository: str,
    branch: str,
    target_root: Path,
    *,
    initiating_harness: str,
    dependency_check: Callable[[], None] | None = None,
    source_acquirer: Callable[[str, str], SourceSnapshot] | None = None,
) -> dict[str, str]:
    """Create an authenticated checkpoint for a later install process."""
    (dependency_check or check_dependencies)()
    source = (source_acquirer or acquire_source)(repository, branch)
    plan = build_install_plan(source, target_root, initiating_harness)
    checkpoint = create_checkpoint(
        plan.target_root,
        mutable_paths=[plan.target_root / relative for relative in plan.mutable_paths],
        expected=plan.expected,
        plan=plan,
    )
    return {
        "checkpoint_id": checkpoint.identifier,
        "branch": source.branch,
        "revision": source.revision,
    }


def _result_json(result: InstallResult) -> str:
    payload = asdict(result)
    return json.dumps(payload, indent=2, sort_keys=True)


def _add_target_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--target", type=Path, default=Path.cwd())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    install_parser = commands.add_parser("install")
    install_parser.add_argument("--repository", default="hubertusgbecker/syspilot")
    install_parser.add_argument("--branch", default="main")
    _add_target_argument(install_parser)
    install_parser.add_argument("--harness", required=True)
    install_parser.add_argument("--checkpoint-id")

    checkpoint_parser = commands.add_parser("checkpoint")
    checkpoint_parser.add_argument("--repository", default="hubertusgbecker/syspilot")
    checkpoint_parser.add_argument("--branch", default="main")
    _add_target_argument(checkpoint_parser)
    checkpoint_parser.add_argument(
        "--harness", choices=PRODUCTION_HARNESSES, required=True
    )

    validation_parser = commands.add_parser("validate-sphinx")
    _add_target_argument(validation_parser)
    validation_parser.add_argument("--output", type=Path, required=True)
    validation_parser.add_argument("--doctrees", type=Path, required=True)

    arguments = parser.parse_args(argv)
    if (
        arguments.command == "install"
        and arguments.harness not in PRODUCTION_HARNESSES
        and arguments.checkpoint_id is None
    ):
        parser.error(
            f"argument --harness: invalid choice: {arguments.harness!r} "
            f"(choose from {', '.join(PRODUCTION_HARNESSES)})"
        )
    target_root = arguments.target.resolve()

    if arguments.command == "validate-sphinx":
        try:
            _run_sphinx(target_root, arguments.output, arguments.doctrees)
            return 0
        except Exception as error:
            print(str(error), file=sys.stderr)
            return 1

    if arguments.command == "checkpoint":
        try:
            payload = prepare_checkpoint(
                arguments.repository,
                arguments.branch,
                target_root,
                initiating_harness=arguments.harness,
            )
            print(json.dumps(payload, indent=2, sort_keys=True))
            return 0
        except Exception as error:
            print(str(error), file=sys.stderr)
            return 1

    result = install(
        arguments.repository,
        arguments.branch,
        target_root,
        initiating_harness=arguments.harness,
        checkpoint_id=arguments.checkpoint_id,
    )
    print(_result_json(result))
    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())