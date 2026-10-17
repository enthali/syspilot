"""Contract tests for the Installer's harness adapter workflow."""

import json
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
import urllib.error
import uuid
import zipfile
from contextlib import redirect_stderr, redirect_stdout
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath
from unittest.mock import patch

import yaml

import syspilot.installer as installer_module

from syspilot.installer import (
    DependencyError,
    InstallResult,
    SourceSnapshot,
    acquire_source,
    adapt_agent,
    adapt_prompt,
    adapt_skill,
    bootstrap_docs,
    build_install_plan,
    create_checkpoint,
    enumerate_product,
    install,
    install_snapshot,
    load_checkpoint,
    main,
    parse_frontmatter,
    restore_checkpoint,
    validate_sphinx,
)


ROOT = Path(__file__).resolve().parents[1]
PROMPT_NAMES = ("cm", "design", "docu", "installer", "pm", "qm", "setup")


class QuietFileHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        pass


def frontmatter(metadata: str, body: bytes = b"") -> bytes:
    return b"---\n" + metadata.encode("utf-8") + b"\n---\n" + body


class TestExecutableHarnessAdapters(unittest.TestCase):
    def test_claude_agent_uses_native_identity_and_scoped_bindings(self):
        source = frontmatter(
            'description: "Manager: coordinates work"\n'
            "user-invocable: true\n"
            "agents:\n"
            "  - syspilot.implement\n"
            "  - syspilot.verify",
            b"# Manager\n\n"
            b"Soul reference: `syspilot.implement`.\n\n"
            b"## Workflow\n\n"
            b"1. SEND work to `syspilot.implement`.\n"
            b"2. SEND checks to `syspilot.verify`.\n\n"
            b"## Notes\n\n"
            b"Keep `syspilot.verify` as ordinary prose.\n",
        )

        adapted = adapt_agent(
            source, "claude", "syspilot/agents/syspilot.cm.agent.md"
        )
        metadata, body = parse_frontmatter(adapted)

        self.assertEqual(metadata["name"], "syspilot-cm")
        self.assertEqual(metadata["description"], "Manager: coordinates work")
        self.assertEqual(
            metadata["tools"],
            ["Agent(syspilot-implement, syspilot-verify)"],
        )
        self.assertIn(b"Soul reference: `syspilot.implement`.", body)
        self.assertIn(b"SEND work to `syspilot-implement`.", body)
        self.assertIn(b"SEND checks to `syspilot-verify`.", body)
        self.assertIn(b"Keep `syspilot.verify` as ordinary prose.", body)

    def test_claude_nested_spawner_and_leaf_use_documented_agent_tools(self):
        nested = frontmatter(
            'description: "Nested coordinator"\nagents: [syspilot.trace]',
            b"## Workflow\n\n1. SEND to `syspilot.trace`.\n",
        )
        leaf = frontmatter('description: "Leaf"\nagents: []', b"# Leaf\n")

        nested_metadata, _ = parse_frontmatter(
            adapt_agent(
                nested,
                "claude",
                "syspilot/agents/syspilot.verify.agent.md",
            )
        )
        leaf_metadata, _ = parse_frontmatter(
            adapt_agent(
                leaf,
                "claude",
                "syspilot/agents/syspilot.trace.agent.md",
            )
        )

        self.assertEqual(nested_metadata["tools"], ["Agent"])
        self.assertNotIn("tools", leaf_metadata)

    def test_opencode_permissions_are_a_map_and_body_bytes_are_exact(self):
        source = frontmatter(
            'description: "Manager: coordinates work"\n'
            "agents:\n"
            "  - syspilot.implement\n"
            "  - syspilot.verify",
            b"# Manager\nbody without terminal newline",
        )

        adapted = adapt_agent(source, "opencode")
        metadata, body = parse_frontmatter(adapted)

        self.assertEqual(metadata["mode"], "primary")
        self.assertEqual(
            metadata["permission"]["task"],
            {
                "*": "deny",
                "syspilot.implement": "allow",
                "syspilot.verify": "allow",
            },
        )
        self.assertIsInstance(metadata["permission"]["task"], dict)
        self.assertEqual(body, b"# Manager\nbody without terminal newline")
        self.assertFalse(adapted.startswith(b"\xef\xbb\xbf"))
        self.assertFalse(adapted.endswith(b"\n"))

    def test_opencode_resolves_display_names_to_agent_identities(self):
        source = frontmatter(
            'description: "Manager"\nagents: ["Dev Engineer"]',
            b"# Manager\n",
        )

        metadata, _ = parse_frontmatter(
            adapt_agent(
                source,
                "opencode",
                agent_identities={"Dev Engineer": "syspilot.implement"},
            )
        )

        self.assertEqual(
            metadata["permission"]["task"],
            {"*": "deny", "syspilot.implement": "allow"},
        )

    def test_user_invocable_opencode_agent_is_primary_without_allowlist(self):
        source = frontmatter(
            'description: "Setup"\nuser-invocable: true\nagents: []',
            b"# Setup\n",
        )

        metadata, body = parse_frontmatter(adapt_agent(source, "opencode"))

        self.assertEqual(metadata, {"description": "Setup", "mode": "primary"})
        self.assertEqual(body, b"# Setup\n")


def git(cwd: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def init_git(path: Path) -> None:
    git(path, "init", "-b", "main")
    git(path, "config", "user.email", "installer-tests@example.invalid")
    git(path, "config", "user.name", "Installer Tests")


def tree_bytes(path: Path) -> dict[str, bytes]:
    return {
        item.relative_to(path).as_posix(): item.read_bytes()
        for item in path.rglob("*")
        if item.is_file() and ".git" not in item.parts
    }


def tree_directories(path: Path) -> set[str]:
    return {
        item.relative_to(path).as_posix()
        for item in path.rglob("*")
        if item.is_dir() and ".git" not in item.parts
    }


class TestDeterministicInstaller(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source_root = self.base / "source"
        self.target = self.base / "target"
        self.target.mkdir()
        (self.target / ".opencode").mkdir()
        self._write_fixture_source()
        self.source = SourceSnapshot.from_directory(
            self.source_root, revision="fixture-revision", branch="feature/test"
        )

    def tearDown(self):
        checkpoint_root = Path(tempfile.gettempdir()) / "syspilot-checkpoints"
        for artifact in checkpoint_root.glob("*.json"):
            try:
                payload = json.loads(artifact.read_text(encoding="utf-8"))
                owner = Path(payload["target_root"])
                owner.relative_to(self.base)
            except (KeyError, TypeError, ValueError, json.JSONDecodeError):
                continue
            installer_module._retire_checkpoint(artifact.stem)
        try:
            checkpoint_root.rmdir()
        except OSError:
            pass

    def _write(self, relative: str, content: bytes) -> None:
        path = self.source_root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def _write_fixture_source(self) -> None:
        manager = frontmatter(
            'description: "Manager: coordinates work"\n'
            "agents:\n"
            "  - syspilot.implement\n"
            "  - syspilot.verify",
            b"# Manager\nbody without terminal newline",
        )
        engineer = frontmatter(
            'description: "Engineer"\nagents: []', b"# Engineer\nbody with newline\n"
        )
        setup = frontmatter(
            'description: "Setup"\nagents: [syspilot.installer]', b"# Setup\n"
        )
        self._write("syspilot/agents/syspilot.cm.agent.md", manager)
        self._write("syspilot/agents/syspilot.implement.agent.md", engineer)
        self._write("syspilot/agents/syspilot.setup.agent.md", setup)
        self._write("syspilot/agents/syspilot.installer.agent.md", engineer)
        for name in PROMPT_NAMES:
            agent_path = f"syspilot/agents/syspilot.{name}.agent.md"
            if not (self.source_root / agent_path).exists():
                self._write(agent_path, engineer)
            description = 'description: "Run command"\n' if name != "cm" else ""
            self._write(
                f"syspilot/prompts/syspilot.{name}.prompt.md",
                frontmatter(f"{description}agent: syspilot.{name}".rstrip()),
            )
        self._write(
            "syspilot/skills/syspilot.keep/SKILL.md",
            frontmatter(
                'name: syspilot.keep\ndescription: "Keep: quoted"\n'
                "tools: [read, edit]\ntriggers: [install]",
                b"# Skill\nexact body\n",
            ),
        )
        self._write(
            "syspilot/skills/syspilot.keep/scripts/helper.py",
            b"print('shared helper')\n",
        )
        for variant in ("subagent", "jarvis"):
            self._write(
                f"syspilot/skills/syspilot.orchestration-{variant}/SKILL.md",
                frontmatter(
                    f"name: syspilot.orchestration-{variant}\n"
                    "group: orchestration\n"
                    f'description: "{variant}"',
                    (
                        f"# {variant}\n\n## Verb Mappings\n\n"
                        "source binding\n\n## RECEIVE: Obtaining Your Assignment\n\n"
                        "shared semantics\n"
                    ).encode(),
                ),
            )
        self._write(
            "syspilot/skills/alternate-binding/SKILL.md",
            frontmatter(
                'name: alternate-binding\ngroup: orchestration\n'
                'description: "must be excluded by source group"',
                b"# Alternate\n",
            ),
        )
        self._write("syspilot/templates/change-document.md", b"template\n")
        self._write("syspilot/installer.py", b"fixture runtime\n")
        self._write(".github/agents/syspilot.fake.agent.md", b"wrong source\n")

    def _install(self, **overrides):
        options = {
            "initiating_harness": "opencode",
            "dependency_check": lambda: None,
            "validator": lambda _target: None,
            "commit": False,
        }
        options.update(overrides)
        return install_snapshot(self.source, self.target, **options)

    def _create_plan_checkpoint(self, target: Path | None = None):
        target = target or self.target
        plan = build_install_plan(self.source, target, "opencode")
        checkpoint = create_checkpoint(
            target,
            mutable_paths=[target / relative for relative in plan.mutable_paths],
            expected=plan.expected if target == self.target else None,
            plan=plan,
        )
        self.addCleanup(
            installer_module._retire_checkpoint, checkpoint.identifier
        )
        return plan, checkpoint

    @staticmethod
    def _checkpoint_artifact(identifier: str) -> Path:
        return Path(tempfile.gettempdir()) / "syspilot-checkpoints" / f"{identifier}.json"

    @staticmethod
    def _checkpoint_key_artifact(identifier: str) -> Path:
        return Path(tempfile.gettempdir()) / "syspilot-checkpoints" / f"{identifier}.key"

    @staticmethod
    def _checkpoint_lease_artifact(identifier: str) -> Path:
        return Path(tempfile.gettempdir()) / "syspilot-checkpoints" / f"{identifier}.lease"

    def _replay_checkpoint_in_subprocess(self, checkpoint_id: str) -> dict[str, object]:
        script = """
import json
import sys
from pathlib import Path
from syspilot.installer import SourceSnapshot, install_snapshot
source_root, target, checkpoint_id = sys.argv[1:]
source = SourceSnapshot.from_directory(Path(source_root), revision='fixture-revision', branch='feature/test')
result = install_snapshot(source, Path(target), initiating_harness='opencode', dependency_check=lambda: None, validator=lambda _target: None, commit=False, checkpoint_id=checkpoint_id)
print(json.dumps({'success': result.success, 'error': result.error}))
"""
        completed = subprocess.run(
            [
                sys.executable,
                "-c",
                script,
                str(self.source_root),
                str(self.target),
                checkpoint_id,
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(completed.stdout)

    def _assert_supplied_checkpoint_rejected(self, checkpoint_id: str, error: str):
        before = tree_bytes(self.target)
        before_head = git(self.target, "rev-parse", "HEAD")
        before_index = (self.target / ".git/index").read_bytes()
        before_status = git(self.target, "status", "--short")
        commit_calls: list[Path] = []

        result = self._install(
            checkpoint_id=checkpoint_id,
            commit=True,
            committer=lambda target, _branch, _harness: commit_calls.append(target),
        )

        self.assertFalse(result.success)
        self.assertIn(error, result.error)
        self.assertIsNone(result.commit)
        self.assertEqual(commit_calls, [])
        self.assertEqual(tree_bytes(self.target), before)
        self.assertEqual(git(self.target, "rev-parse", "HEAD"), before_head)
        self.assertEqual((self.target / ".git/index").read_bytes(), before_index)
        self.assertEqual(git(self.target, "status", "--short"), before_status)
        self.assertFalse(self._checkpoint_artifact(checkpoint_id).exists())
        self.assertFalse(self._checkpoint_key_artifact(checkpoint_id).exists())
        self.assertFalse(self._checkpoint_lease_artifact(checkpoint_id).exists())
        replay = self._replay_checkpoint_in_subprocess(checkpoint_id)
        self.assertFalse(replay["success"])
        self.assertRegex(str(replay["error"]), "does not exist|consumed")

    def _assert_preplan_failure_consumes_checkpoint(
        self,
        checkpoint_id: str,
        *,
        source: SourceSnapshot | None = None,
        harness: str = "opencode",
        error: str,
    ) -> None:
        before = tree_bytes(self.target)
        before_head = git(self.target, "rev-parse", "HEAD")
        before_index = (self.target / ".git/index").read_bytes()

        result = install_snapshot(
            source or self.source,
            self.target,
            initiating_harness=harness,
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=False,
            checkpoint_id=checkpoint_id,
        )

        self.assertFalse(result.success)
        self.assertIn(error, result.error or "")
        self.assertEqual(tree_bytes(self.target), before)
        self.assertEqual(git(self.target, "rev-parse", "HEAD"), before_head)
        self.assertEqual((self.target / ".git/index").read_bytes(), before_index)
        replay = self._replay_checkpoint_in_subprocess(checkpoint_id)
        self.assertFalse(replay["success"])
        self.assertRegex(str(replay["error"]), "does not exist|consumed")
        self.assertFalse(self._checkpoint_artifact(checkpoint_id).exists())
        self.assertFalse(self._checkpoint_key_artifact(checkpoint_id).exists())
        self.assertFalse(self._checkpoint_lease_artifact(checkpoint_id).exists())

    def _initialize_checkpoint_git_state(self):
        init_git(self.target)
        (self.target / "README.md").write_bytes(b"before supplied checkpoint\n")
        git(self.target, "add", "README.md")
        git(self.target, "commit", "-m", "before")
        (self.target / "staged.txt").write_bytes(b"staged before supplied checkpoint\n")
        git(self.target, "add", "staged.txt")

    def _replace_with_directory_link(self, directory: Path, outside: Path) -> None:
        backup = directory.with_name(directory.name + "-transaction-owned")
        directory.rename(backup)
        if os.name == "nt":
            completed = subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(directory), str(outside)],
                capture_output=True,
                text=True,
            )
            if completed.returncode != 0:
                backup.rename(directory)
                raise unittest.SkipTest("Windows junction creation is unavailable")
        else:
            directory.symlink_to(outside, target_is_directory=True)

    def _concurrent_commit_observer(self, target: Path, observed: dict[str, object]):
        def advance_after_install(phase: str) -> None:
            if phase != "commit_created":
                return
            observed["installer"] = git(target, "rev-parse", "HEAD")
            concurrent = target / "concurrent-after-install.txt"
            concurrent.write_bytes(b"preserve this commit\n")
            git(target, "add", concurrent.name)
            git(target, "commit", "-m", "concurrent commit")
            observed["concurrent"] = git(target, "rev-parse", "HEAD")
            index_path = Path(git(target, "rev-parse", "--git-path", "index"))
            if not index_path.is_absolute():
                index_path = target / index_path
            observed["index"] = index_path.read_bytes()

        return advance_after_install

    def test_all_harness_adapters_use_structured_yaml_and_exact_bodies(self):
        agent = (self.source_root / "syspilot/agents/syspilot.cm.agent.md").read_bytes()
        skill = (self.source_root / "syspilot/skills/syspilot.keep/SKILL.md").read_bytes()

        claude_meta, claude_body = parse_frontmatter(
            adapt_agent(
                agent,
                "claude",
                "syspilot/agents/syspilot.cm.agent.md",
            )
        )
        qoder_meta, qoder_body = parse_frontmatter(adapt_agent(agent, "qoder"))
        skill_meta, skill_body = parse_frontmatter(adapt_skill(skill, "opencode"))

        self.assertEqual(
            claude_meta,
            {
                "name": "syspilot-cm",
                "description": "Manager: coordinates work",
                "user-invocable": False,
                "tools": ["Agent"],
            },
        )
        self.assertEqual(qoder_meta, {"description": "Manager: coordinates work"})
        self.assertEqual(claude_body, qoder_body)
        self.assertFalse(claude_body.endswith(b"\n"))
        self.assertEqual(
            skill_meta,
            {"name": "syspilot.keep", "description": "Keep: quoted"},
        )
        self.assertEqual(skill_body, b"# Skill\nexact body\n")

    def test_empty_allowlist_is_subagent_and_nonempty_allowlist_is_primary(self):
        engineer = adapt_agent(
            (self.source_root / "syspilot/agents/syspilot.implement.agent.md").read_bytes(),
            "opencode",
        )
        setup = adapt_agent(
            (self.source_root / "syspilot/agents/syspilot.setup.agent.md").read_bytes(),
            "opencode",
        )
        engineer_meta, _ = parse_frontmatter(engineer)
        setup_meta, _ = parse_frontmatter(setup)

        self.assertEqual(engineer_meta, {"description": "Engineer", "mode": "subagent"})
        self.assertEqual(setup_meta["mode"], "primary")
        self.assertEqual(
            setup_meta["permission"]["task"],
            {"*": "deny", "syspilot.installer": "allow"},
        )

    def test_prompt_forwards_complete_opencode_arguments(self):
        prompt = (self.source_root / "syspilot/prompts/syspilot.cm.prompt.md").read_bytes()

        metadata, body = parse_frontmatter(
            adapt_prompt(prompt, "Manager: coordinates work")
        )

        self.assertEqual(
            metadata,
            {"description": "Manager: coordinates work", "agent": "syspilot.cm"},
        )
        self.assertEqual(body, b"$ARGUMENTS\n")

    def test_inventory_uses_only_product_roots(self):
        inventory = enumerate_product(self.source)

        self.assertIn("syspilot/agents/syspilot.cm.agent.md", inventory)
        self.assertNotIn(".github/agents/syspilot.fake.agent.md", inventory)
        self.assertTrue(
            all(
                path.startswith(
                    ("syspilot/agents/", "syspilot/prompts/", "syspilot/skills/", "syspilot/templates/")
                )
                for path in inventory
            )
        )

    def test_fresh_install_is_complete_idempotent_and_dot_preserving(self):
        first = self._install()
        first_tree = tree_bytes(self.target)
        second = self._install()

        self.assertTrue(first.success, first.error)
        self.assertTrue(second.success, second.error)
        self.assertEqual(first_tree, tree_bytes(self.target))
        self.assertEqual(sum(row.installed for row in second.summary.values()), 0)
        self.assertEqual(sum(row.updated for row in second.summary.values()), 0)
        self.assertEqual(
            sorted(path.name for path in (self.target / ".opencode/commands").iterdir()),
            [f"syspilot.{name}.md" for name in sorted(PROMPT_NAMES)],
        )

    def test_claude_reinstall_updates_and_removes_residue_in_isolation(self):
        first = self._install(initiating_harness="claude")
        opencode_before = tree_bytes(self.target / ".opencode")
        retired = self.target / ".claude/agents/syspilot.retired.md"
        retired.write_bytes(b"retired Claude agent\n")
        manager_path = self.source_root / "syspilot/agents/syspilot.cm.agent.md"
        manager_path.write_bytes(
            manager_path.read_bytes().replace(
                b"Manager: coordinates work", b"Manager: coordinates updates"
            )
        )
        updated_source = SourceSnapshot.from_directory(
            self.source_root,
            revision="updated-fixture-revision",
            branch="feature/test",
        )

        second = install_snapshot(
            updated_source,
            self.target,
            initiating_harness="claude",
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=False,
        )

        self.assertTrue(first.success, first.error)
        self.assertTrue(second.success, second.error)
        self.assertFalse(retired.exists())
        self.assertEqual(second.summary[".claude/agents"].removed, 1)
        self.assertGreaterEqual(second.summary[".claude/agents"].updated, 1)
        self.assertEqual(tree_bytes(self.target / ".opencode"), opencode_before)
        self.assertFalse((self.target / ".github").exists())

    def test_qoder_stages_one_deterministic_archive_without_live_tree(self):
        first = self._install(initiating_harness="qoder")
        archive = self.target / ".syspilot/qoder/syspilot-qoder-plugin.zip"
        first_bytes = archive.read_bytes() if archive.is_file() else None
        second = self._install(initiating_harness="qoder")

        self.assertTrue(first.success, first.error)
        self.assertTrue(second.success, second.error)
        self.assertTrue(archive.is_file())
        self.assertFalse((self.target / ".qoder").exists())
        self.assertEqual(first_bytes, archive.read_bytes())
        self.assertIn(".syspilot/qoder", first.summary)
        self.assertNotIn(".qoder/agents", first.summary)

        with zipfile.ZipFile(archive) as package:
            members = package.namelist()
            payload_digests = {
                member: hashlib.sha256(package.read(member)).hexdigest()
                for member in members
                if member != "plugin.json"
            }
            self.assertEqual(members, sorted(members))
            self.assertIn("plugin.json", members)
            self.assertTrue(any(member.startswith("agents/") for member in members))
            self.assertTrue(any(member.startswith("skills/") for member in members))
            self.assertFalse(any(member.startswith("prompts/") for member in members))
            self.assertTrue(all(not PurePosixPath(member).is_absolute() for member in members))
            self.assertTrue(all(".." not in PurePosixPath(member).parts for member in members))
            self.assertTrue(all(member.date_time == (1980, 1, 1, 0, 0, 0) for member in package.infolist()))
            manifest = json.loads(package.read("plugin.json"))

        self.assertEqual(manifest["id"], "syspilot-qoder")
        self.assertEqual(manifest["source_revision"], self.source.revision)
        self.assertEqual(manifest["members"], payload_digests)
        result = json.loads(installer_module._result_json(first))
        self.assertEqual(result["status"], "staged")
        self.assertEqual(result["package_digest"], hashlib.sha256(archive.read_bytes()).hexdigest())

    def test_qoder_failure_rolls_back_archive_and_preserves_global_identity(self):
        global_root = self.base / "global-qoder-state"
        global_file = global_root / "settings.json"
        global_directory = global_root / "plugins"
        before = {
            path: installer_module._path_identity(path)
            for path in (global_file, global_directory)
        }
        original_tree = tree_bytes(self.target)
        original_directories = tree_directories(self.target)

        with patch.dict(os.environ, {"HOME": str(global_root)}, clear=False):
            result = self._install(
                initiating_harness="qoder", failure_phase="target_write"
            )

        self.assertFalse(result.success)
        self.assertEqual(tree_bytes(self.target), original_tree)
        self.assertEqual(tree_directories(self.target), original_directories)
        self.assertFalse((self.target / ".syspilot/qoder/syspilot-qoder-plugin.zip").exists())
        self.assertFalse((self.target / ".qoder").exists())
        self.assertEqual(
            {
                path: installer_module._path_identity(path)
                for path in (global_file, global_directory)
            },
            before,
        )

    def test_shared_resources_use_stable_harness_neutral_paths(self):
        result = self._install()

        self.assertTrue(result.success, result.error)
        self.assertEqual(
            (self.target / ".syspilot/templates/change-document.md").read_bytes(),
            b"template\n",
        )
        self.assertEqual(
            (
                self.target
                / ".syspilot/skills/syspilot.keep/scripts/helper.py"
            ).read_bytes(),
            b"print('shared helper')\n",
        )
        self.assertTrue(
            (self.target / ".opencode/skills/syspilot.keep/SKILL.md").is_file()
        )
        self.assertFalse((self.target / ".opencode/templates").exists())
        self.assertFalse(
            (self.target / ".opencode/skills/syspilot.keep/scripts").exists()
        )

    def test_opencode_orchestration_uses_task_binding_only(self):
        result = self._install()

        self.assertTrue(result.success, result.error)
        installed = (
            self.target
            / ".opencode/skills/syspilot.orchestration-subagent/SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("native Task", installed)
        self.assertNotIn("runSubagent", installed)
        source_body = parse_frontmatter(
            (
                self.source_root
                / "syspilot/skills/syspilot.orchestration-subagent/SKILL.md"
            ).read_bytes()
        )[1]
        installed_body = parse_frontmatter(installed.encode("utf-8"))[1]
        source_suffix = source_body.split(b"## RECEIVE: Obtaining Your Assignment", 1)[1]
        installed_suffix = installed_body.split(
            b"## RECEIVE: Obtaining Your Assignment", 1
        )[1]
        self.assertEqual(installed_suffix, source_suffix)
        self.assertFalse(
            (self.target / ".opencode/skills/alternate-binding").exists()
        )

    def test_vscode_is_verbatim_and_other_harnesses_are_not_speculative(self):
        shutil.rmtree(self.target / ".opencode")

        result = self._install(initiating_harness="vscode")

        self.assertTrue(result.success)
        self.assertEqual(
            (self.target / ".github/agents/syspilot.cm.agent.md").read_bytes(),
            (self.source_root / "syspilot/agents/syspilot.cm.agent.md").read_bytes(),
        )
        self.assertFalse((self.target / ".claude").exists())
        self.assertFalse((self.target / ".opencode").exists())
        self.assertFalse((self.target / ".qoder").exists())

    def test_explicit_harness_does_not_populate_other_existing_harnesses(self):
        (self.target / ".claude").mkdir()
        (self.target / ".qoder").mkdir()

        result = self._install()

        self.assertTrue(result.success, result.error)
        self.assertTrue((self.target / ".opencode/agents/syspilot.cm.md").is_file())
        self.assertFalse((self.target / ".github").exists())
        self.assertEqual(list((self.target / ".claude").rglob("*")), [])
        self.assertEqual(list((self.target / ".qoder").rglob("*")), [])

    def test_every_vscode_product_target_preserves_source_bytes(self):
        result = self._install(initiating_harness="vscode")

        self.assertTrue(result.success, result.error)
        selected = enumerate_product(self.source)
        selected.pop(
            "syspilot/skills/syspilot.orchestration-jarvis/SKILL.md"
        )
        selected.pop("syspilot/skills/alternate-binding/SKILL.md")
        for source_path, expected in selected.items():
            relative = PurePosixPath(source_path)
            if relative.parts[1] == "templates":
                target = self.target / ".syspilot/templates" / Path(*relative.parts[2:])
            elif relative.parts[1] == "skills" and relative.name != "SKILL.md":
                target = self.target / ".syspilot/skills" / Path(*relative.parts[2:])
            else:
                target = self.target / ".github" / Path(*relative.parts[1:])
            with self.subTest(source_path=source_path):
                self.assertEqual(target.read_bytes(), expected)

    def test_orphans_are_removed_but_customer_and_tailoring_files_survive(self):
        agent_dir = self.target / ".opencode/agents"
        agent_dir.mkdir(parents=True)
        (agent_dir / "syspilot.retired.md").write_bytes(b"old")
        (agent_dir / "syspilot.cm.tailoring.md").write_bytes(b"tailoring")
        (agent_dir / "customer.md").write_bytes(b"customer")

        result = self._install()

        self.assertTrue(result.success, result.error)
        self.assertFalse((agent_dir / "syspilot.retired.md").exists())
        self.assertTrue((agent_dir / "syspilot.cm.tailoring.md").exists())
        self.assertTrue((agent_dir / "customer.md").exists())
        self.assertEqual(result.summary[".opencode/agents"].removed, 1)

    def test_docs_bootstrap_does_not_overwrite_or_add_bom(self):
        docs = self.target / "docs"
        docs.mkdir()
        (docs / "index.rst").write_bytes(b"custom index\n")

        created = bootstrap_docs(self.target)

        self.assertEqual((docs / "index.rst").read_bytes(), b"custom index\n")
        self.assertEqual(created, ["docs/conf.py"])
        self.assertIn(b'extensions = ["sphinx_needs"]', (docs / "conf.py").read_bytes())
        self.assertFalse((docs / "conf.py").read_bytes().startswith(b"\xef\xbb\xbf"))

    def test_relative_repository_shadow_never_becomes_a_local_source(self):
        shadow = self.base / "owner/repository"
        shutil.copytree(self.source_root, shadow)
        init_git(shadow)
        git(shadow, "add", ".")
        git(shadow, "commit", "-m", "malicious local shadow")
        previous = Path.cwd()
        os.chdir(self.base)
        self.addCleanup(os.chdir, previous)

        with patch(
            "syspilot.installer._request_json",
            side_effect=RuntimeError("remote GitHub requested"),
        ):
            with self.assertRaisesRegex(RuntimeError, "remote GitHub requested"):
                acquire_source("owner/repository", "feature/selected")

    def test_public_source_rejects_local_paths_and_non_github_urls(self):
        for repository in (
            ".",
            "../repository",
            str(self.source_root),
            self.source_root.as_uri(),
            "https://example.com/owner/repository",
            "http://github.com/owner/repository",
            "https://user@github.com/owner/repository",
            "https://github.com/owner/repository?ref=main",
        ):
            with self.subTest(repository=repository):
                with self.assertRaisesRegex(ValueError, "GitHub repository"):
                    acquire_source(repository, "main")

    def test_github_api_rejects_truncated_inventory_before_fetch(self):
        responses = [
            {"sha": "a" * 40},
            {"truncated": True, "tree": []},
        ]

        with patch("syspilot.installer._request_json", side_effect=responses), patch(
            "syspilot.installer.urllib.request.urlopen"
        ) as raw_fetch:
            with self.assertRaisesRegex(ValueError, "truncated"):
                acquire_source("owner/repository", "main")

        raw_fetch.assert_not_called()

    def test_github_api_rejects_missing_product_roots_before_fetch(self):
        responses = [
            {"sha": "b" * 40},
            {
                "truncated": False,
                "tree": [
                    {"path": "syspilot/installer.py", "type": "blob"},
                    {
                        "path": "syspilot/agents/syspilot.cm.agent.md",
                        "type": "blob",
                    },
                ],
            },
        ]

        with patch("syspilot.installer._request_json", side_effect=responses), patch(
            "syspilot.installer.urllib.request.urlopen"
        ) as raw_fetch:
            with self.assertRaisesRegex(ValueError, "missing product root"):
                acquire_source("owner/repository", "main")

        raw_fetch.assert_not_called()

    def test_dependency_failure_precedes_mutation(self):
        before = tree_bytes(self.target)

        result = self._install(
            dependency_check=lambda: (_ for _ in ()).throw(DependencyError("missing"))
        )

        self.assertFalse(result.success)
        self.assertEqual(tree_bytes(self.target), before)
        self.assertIsNone(result.commit)

    def test_source_acquisition_failure_precedes_mutation(self):
        before = tree_bytes(self.target)

        result = install(
            "fixture/repository",
            "main",
            self.target,
            initiating_harness="opencode",
            dependency_check=lambda: None,
            source_acquirer=lambda _repository, _branch: (_ for _ in ()).throw(
                RuntimeError("source acquisition failed")
            ),
        )

        self.assertFalse(result.success)
        self.assertIn("source acquisition failed", result.error)
        self.assertEqual(tree_bytes(self.target), before)
        self.assertIsNone(result.commit)

    def test_parse_plan_and_containment_finish_before_checkpoint(self):
        events: list[str] = []

        result = self._install(phase_observer=events.append)

        self.assertTrue(result.success, result.error)
        self.assertLess(events.index("plan_validated"), events.index("checkpoint_created"))
        self.assertLess(events.index("checkpoint_created"), events.index("first_mutation"))

    def test_malicious_source_escape_fails_before_checkpoint_or_mutation(self):
        malicious = dict(self.source.files)
        malicious["syspilot/agents/../../../../escaped.agent.md"] = frontmatter(
            'description: "escape"', b"escape\n"
        )
        source = SourceSnapshot(malicious, self.source.revision, self.source.branch)
        checkpoint_root = Path(tempfile.gettempdir()) / "syspilot-checkpoints"
        before = set(checkpoint_root.glob("*.json"))

        result = install_snapshot(
            source,
            self.target,
            initiating_harness="opencode",
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=False,
        )

        self.assertFalse(result.success)
        self.assertIn("invalid source path", result.error)
        self.assertFalse((self.base / "escaped.agent.md").exists())
        self.assertEqual(set(checkpoint_root.glob("*.json")), before)

    def test_link_ancestry_is_rejected_before_checkpoint(self):
        outside = self.base / "outside"
        outside.mkdir()
        shutil.rmtree(self.target / ".opencode")
        link = self.target / ".opencode"
        try:
            if os.name == "nt":
                completed = subprocess.run(
                    ["cmd", "/c", "mklink", "/J", str(link), str(outside)],
                    capture_output=True,
                    text=True,
                )
                if completed.returncode != 0:
                    self.skipTest("Windows junction creation is unavailable")
            else:
                link.symlink_to(outside, target_is_directory=True)
        except OSError as error:
            self.skipTest(f"link creation is unavailable: {error}")
        checkpoint_root = Path(tempfile.gettempdir()) / "syspilot-checkpoints"
        before = set(checkpoint_root.glob("*.json"))

        result = self._install()

        self.assertFalse(result.success)
        self.assertRegex(result.error, "symlink|junction|reparse|link-like")
        self.assertEqual(list(outside.iterdir()), [])
        self.assertEqual(set(checkpoint_root.glob("*.json")), before)

    def test_parent_swap_before_temp_creation_fails_closed(self):
        outside = self.base / "race-outside"
        outside.mkdir()
        sentinel = outside / "sentinel.txt"
        sentinel.write_bytes(b"external sentinel\n")
        swapped = False

        def swap_parent(phase: str, path: Path) -> None:
            nonlocal swapped
            if phase == "before_temp_create" and not swapped:
                self._replace_with_directory_link(path.parent, outside)
                swapped = True

        result = self._install(mutation_hook=swap_parent)

        self.assertFalse(result.success)
        self.assertTrue(swapped)
        self.assertRegex(result.error or "", "link-like|identity|reparse|junction")
        self.assertEqual(sentinel.read_bytes(), b"external sentinel\n")
        self.assertEqual(set(outside.iterdir()), {sentinel})

    def test_parent_identity_swap_before_temp_creation_fails_closed(self):
        swapped = False

        def swap_parent(phase: str, path: Path) -> None:
            nonlocal swapped
            if phase == "before_temp_create" and not swapped:
                path.parent.rename(path.parent.with_name(path.parent.name + "-original"))
                path.parent.mkdir()
                swapped = True

        result = self._install(mutation_hook=swap_parent)

        self.assertFalse(result.success)
        self.assertTrue(swapped)
        self.assertIn("parent identity changed", result.error or "")

    def test_parent_swap_before_replace_fails_closed(self):
        outside = self.base / "replace-outside"
        outside.mkdir()
        sentinel = outside / "sentinel.txt"
        sentinel.write_bytes(b"external sentinel\n")
        swapped = False

        def swap_parent(phase: str, path: Path) -> None:
            nonlocal swapped
            if phase == "before_replace" and not swapped:
                self._replace_with_directory_link(path.parent, outside)
                swapped = True

        result = self._install(mutation_hook=swap_parent)

        self.assertFalse(result.success)
        self.assertTrue(swapped)
        self.assertEqual(sentinel.read_bytes(), b"external sentinel\n")
        self.assertEqual(set(outside.iterdir()), {sentinel})

    @unittest.skipIf(os.name == "nt", "descriptor-relative operations are POSIX-specific")
    def test_posix_rename_is_descriptor_relative(self):
        # os.rename (not os.replace) is used because os.replace lacks dir_fd
        # support on macOS, while POSIX rename() already atomically replaces.
        rename_calls: list[dict[str, object]] = []
        real_rename = os.rename

        def record_rename(source, destination, *args, **kwargs):
            rename_calls.append(kwargs)
            return real_rename(source, destination, *args, **kwargs)

        with patch("syspilot.installer.os.rename", side_effect=record_rename) as mock_rename:
            # os.supports_dir_fd holds the real os.rename by identity; the capability
            # probe in _posix_directory_flags would otherwise see the mock as unsupported.
            os.supports_dir_fd.add(mock_rename)
            try:
                result = self._install()
            finally:
                os.supports_dir_fd.discard(mock_rename)

        self.assertTrue(result.success, result.error)
        self.assertTrue(
            any("src_dir_fd" in call and "dst_dir_fd" in call for call in rename_calls),
            rename_calls,
        )

    @unittest.skipIf(os.name == "nt", "descriptor-relative operations are POSIX-specific")
    def test_posix_late_parent_swap_keeps_replace_on_opened_parent(self):
        parent = self.target / "anchored-replace"
        parent.mkdir()
        destination = parent / "owned.txt"
        destination.write_bytes(b"before\n")
        outside = self.base / "external-replace"
        outside.mkdir()
        sentinel = outside / destination.name
        sentinel.write_bytes(b"external\n")
        expected = {
            "anchored-replace": installer_module._path_identity(parent),
            "anchored-replace/owned.txt": installer_module._path_identity(destination),
        }
        swapped = False

        def swap_after_validation(phase: str, _path: Path) -> None:
            nonlocal swapped
            if phase == "after_before_replace_validation" and not swapped:
                self._replace_with_directory_link(parent, outside)
                swapped = True

        action = installer_module._atomic_write(
            destination,
            b"after\n",
            target_root=self.target,
            relative="anchored-replace/owned.txt",
            mutation_hook=swap_after_validation,
            expected_paths=expected,
            target_identity=installer_module._path_identity(self.target),
        )

        self.assertEqual(action, "updated")
        self.assertTrue(swapped)
        self.assertEqual(sentinel.read_bytes(), b"external\n")
        self.assertEqual(
            (self.target / "anchored-replace-transaction-owned/owned.txt").read_bytes(),
            b"after\n",
        )

    @unittest.skipIf(os.name == "nt", "descriptor-relative operations are POSIX-specific")
    def test_posix_late_parent_swap_keeps_delete_on_opened_parent(self):
        parent = self.target / "anchored-delete"
        parent.mkdir()
        destination = parent / "owned.txt"
        destination.write_bytes(b"delete me\n")
        outside = self.base / "external-delete"
        outside.mkdir()
        sentinel = outside / destination.name
        sentinel.write_bytes(b"external\n")
        expected = {
            "anchored-delete": installer_module._path_identity(parent),
            "anchored-delete/owned.txt": installer_module._path_identity(destination),
        }

        def swap_after_validation(phase: str, _path: Path) -> None:
            if phase == "after_before_delete_validation" and not parent.is_symlink():
                self._replace_with_directory_link(parent, outside)

        installer_module._safe_delete(
            self.target,
            "anchored-delete/owned.txt",
            expected["anchored-delete/owned.txt"],
            swap_after_validation,
            expected_paths=expected,
            target_identity=installer_module._path_identity(self.target),
        )

        self.assertEqual(sentinel.read_bytes(), b"external\n")
        self.assertFalse(
            (self.target / "anchored-delete-transaction-owned/owned.txt").exists()
        )

    @unittest.skipIf(os.name == "nt", "descriptor-relative operations are POSIX-specific")
    def test_posix_late_parent_swap_keeps_cleanup_on_opened_parent(self):
        parent = self.target / "anchored-cleanup"
        parent.mkdir()
        directory = parent / "owned"
        directory.mkdir()
        outside = self.base / "external-cleanup"
        outside.mkdir()
        sentinel = outside / "sentinel.txt"
        sentinel.write_bytes(b"external\n")
        expected = {
            "anchored-cleanup": installer_module._path_identity(parent),
            "anchored-cleanup/owned": installer_module._path_identity(directory),
        }

        def swap_after_validation(phase: str, _path: Path) -> None:
            if phase == "after_before_delete_validation" and not parent.is_symlink():
                self._replace_with_directory_link(parent, outside)

        installer_module._safe_delete(
            self.target,
            "anchored-cleanup/owned",
            expected["anchored-cleanup/owned"],
            swap_after_validation,
            expected_paths=expected,
            target_identity=installer_module._path_identity(self.target),
        )

        self.assertEqual(sentinel.read_bytes(), b"external\n")
        self.assertFalse(
            (self.target / "anchored-cleanup-transaction-owned/owned").exists()
        )

    @unittest.skipIf(os.name == "nt", "descriptor-relative operations are POSIX-specific")
    def test_posix_late_parent_swap_keeps_restore_on_opened_parent(self):
        parent = self.target / "anchored-restore"
        parent.mkdir()
        destination = parent / "owned.txt"
        destination.write_bytes(b"transaction bytes\n")
        outside = self.base / "external-restore"
        outside.mkdir()
        sentinel = outside / destination.name
        sentinel.write_bytes(b"external\n")
        expected = {
            "anchored-restore": installer_module._path_identity(parent),
            "anchored-restore/owned.txt": installer_module._path_identity(destination),
        }

        def swap_after_validation(phase: str, _path: Path) -> None:
            if phase == "after_before_replace_validation" and not parent.is_symlink():
                self._replace_with_directory_link(parent, outside)

        installer_module._atomic_write(
            destination,
            b"checkpoint bytes\n",
            target_root=self.target,
            relative="anchored-restore/owned.txt",
            mutation_hook=swap_after_validation,
            preflight_phase="before_restore",
            expected_paths=expected,
            target_identity=installer_module._path_identity(self.target),
        )

        self.assertEqual(sentinel.read_bytes(), b"external\n")
        self.assertEqual(
            (self.target / "anchored-restore-transaction-owned/owned.txt").read_bytes(),
            b"checkpoint bytes\n",
        )

    def test_parent_swap_before_delete_fails_closed(self):
        orphan = self.target / ".opencode/agents/syspilot.retired.md"
        orphan.parent.mkdir(parents=True)
        orphan.write_bytes(b"owned orphan\n")
        outside = self.base / "delete-outside"
        outside.mkdir()
        sentinel = outside / "syspilot.retired.md"
        sentinel.write_bytes(b"external sentinel\n")
        swapped = False

        def swap_parent(phase: str, path: Path) -> None:
            nonlocal swapped
            if phase == "before_delete" and path.name == orphan.name and not swapped:
                self._replace_with_directory_link(path.parent, outside)
                swapped = True

        result = self._install(mutation_hook=swap_parent)

        self.assertFalse(result.success)
        self.assertTrue(swapped)
        self.assertEqual(sentinel.read_bytes(), b"external sentinel\n")

    def test_parent_swap_before_restore_fails_closed(self):
        outside = self.base / "restore-race-outside"
        outside.mkdir()
        sentinel = outside / "sentinel.txt"
        sentinel.write_bytes(b"external sentinel\n")
        swapped = False

        def swap_parent(phase: str, path: Path) -> None:
            nonlocal swapped
            if phase == "before_restore" and not swapped:
                self._replace_with_directory_link(path.parent, outside)
                swapped = True

        result = self._install(
            mutation_hook=swap_parent,
            failure_phase="target_write",
        )

        self.assertFalse(result.success)
        self.assertTrue(swapped)
        self.assertIn("incomplete rollback", result.error or "")
        self.assertEqual(sentinel.read_bytes(), b"external sentinel\n")

    def test_checkpoint_persists_only_declared_mutable_paths(self):
        owned = self.target / ".opencode/agents/syspilot.cm.md"
        owned.parent.mkdir(parents=True)
        owned.write_bytes(b"owned pre-state\n")
        sensitive = self.target / "private/unrelated-secret.bin"
        sensitive.parent.mkdir(parents=True)
        sensitive.write_bytes(b"sensitive-sentinel-" + b"x" * 1024 * 1024)

        checkpoint = create_checkpoint(self.target, mutable_paths=[owned])
        self.addCleanup(
            installer_module._retire_checkpoint, checkpoint.identifier
        )
        persisted = (
            Path(tempfile.gettempdir())
            / "syspilot-checkpoints"
            / f"{checkpoint.identifier}.json"
        ).read_bytes()

        self.assertEqual(checkpoint.files, {".opencode/agents/syspilot.cm.md": b"owned pre-state\n"})
        self.assertNotIn(b"sensitive-sentinel", persisted)
        self.assertLess(len(persisted), 32_000)

    def test_checkpoint_work_is_bounded_by_declared_paths(self):
        unrelated = self.target / "large-unrelated-tree"
        unrelated.mkdir()
        for number in range(500):
            (unrelated / f"item-{number:04}.bin").write_bytes(b"x" * 4096)
        owned = self.target / ".opencode/agents/syspilot.cm.md"
        owned.parent.mkdir(parents=True)
        owned.write_bytes(b"owned pre-state\n")
        threads_before = threading.active_count()

        checkpoint = create_checkpoint(self.target, mutable_paths=[owned])
        self.addCleanup(
            installer_module._retire_checkpoint, checkpoint.identifier
        )
        artifact_size = self._checkpoint_artifact(checkpoint.identifier).stat().st_size

        self.assertLess(artifact_size, 32_000)
        self.assertEqual(threading.active_count(), threads_before)
        self.assertNotIn("large-unrelated-tree", checkpoint.mutable_paths)

    def test_unrelated_concurrent_change_survives_rollback(self):
        unrelated = self.target / "customer/concurrent.txt"

        def fail_after_external_change(_target: Path) -> None:
            unrelated.parent.mkdir(parents=True)
            unrelated.write_bytes(b"concurrent customer bytes\n")
            raise RuntimeError("validation failed")

        result = self._install(validator=fail_after_external_change)

        self.assertFalse(result.success)
        self.assertEqual(unrelated.read_bytes(), b"concurrent customer bytes\n")

    def test_mutable_path_concurrent_conflict_is_preserved_and_reported(self):
        mutable = self.target / ".opencode/agents/syspilot.cm.md"

        def fail_after_conflict(_target: Path) -> None:
            mutable.write_bytes(b"concurrent owned-path bytes\n")
            raise RuntimeError("validation failed")

        result = self._install(validator=fail_after_conflict)

        self.assertFalse(result.success)
        self.assertIn("incomplete rollback", result.error)
        self.assertEqual(mutable.read_bytes(), b"concurrent owned-path bytes\n")

    def test_link_conflict_during_rollback_preserves_external_target_and_cleans_checkpoint(self):
        outside = self.base / "rollback-outside"
        outside.mkdir()
        agents = self.target / ".opencode/agents"
        checkpoint_root = Path(tempfile.gettempdir()) / "syspilot-checkpoints"
        before = set(checkpoint_root.glob("*.json"))

        def fail_after_link_replacement(_target: Path) -> None:
            shutil.rmtree(agents)
            if os.name == "nt":
                completed = subprocess.run(
                    ["cmd", "/c", "mklink", "/J", str(agents), str(outside)],
                    capture_output=True,
                    text=True,
                )
                if completed.returncode != 0:
                    raise unittest.SkipTest("Windows junction creation is unavailable")
            else:
                agents.symlink_to(outside, target_is_directory=True)
            raise RuntimeError("validation failed")

        result = self._install(validator=fail_after_link_replacement)

        self.assertFalse(result.success)
        self.assertIn("incomplete rollback", result.error)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertEqual(set(checkpoint_root.glob("*.json")), before)

    def test_checkpoint_and_each_post_checkpoint_failure_restore_exact_state(self):
        original = self.target / ".opencode/original.txt"
        original.write_bytes(b"original\r\n")
        checkpoint = create_checkpoint(
            self.target,
            mutable_paths=[
                original,
                self.target / ".github",
                self.target / ".github/new.txt",
            ],
        )
        original.write_bytes(b"changed")
        (self.target / ".github/new.txt").parent.mkdir(parents=True)
        (self.target / ".github/new.txt").write_bytes(b"new")
        restore_checkpoint(checkpoint)
        self.assertEqual(original.read_bytes(), b"original\r\n")
        self.assertFalse((self.target / ".github").exists())

        init_git(self.target)
        (self.target / "README.md").write_bytes(b"before\n")
        git(self.target, "add", ".")
        git(self.target, "commit", "-m", "before")
        staged = self.target / "staged.txt"
        staged.write_bytes(b"pre-existing staged state\n")
        git(self.target, "add", "staged.txt")
        original_head = git(self.target, "rev-parse", "HEAD")
        original_tree = tree_bytes(self.target)
        original_index = (self.target / ".git/index").read_bytes()

        for phase in (
            "runtime_write",
            "yaml_parse",
            "target_write",
            "docs_bootstrap",
            "orphan_cleanup",
            "validation",
            "summary",
            "commit",
        ):
            with self.subTest(phase=phase):
                result = self._install(
                    validator=lambda _target: None,
                    commit=True,
                    failure_phase=phase,
                )
                self.assertFalse(result.success)
                self.assertIsNone(result.commit)
                self.assertIn(f"injected failure at {phase}", result.error)
                self.assertEqual(git(self.target, "rev-parse", "HEAD"), original_head)
                self.assertEqual(tree_bytes(self.target), original_tree)
                self.assertEqual((self.target / ".git/index").read_bytes(), original_index)

    def test_post_commit_checkpoint_deletion_failure_removes_install_commit(self):
        init_git(self.target)
        (self.target / "README.md").write_bytes(b"before\n")
        git(self.target, "add", ".")
        git(self.target, "commit", "-m", "before")
        staged = self.target / "staged.txt"
        staged.write_bytes(b"pre-existing staged state\n")
        git(self.target, "add", "staged.txt")
        original_head = git(self.target, "rev-parse", "HEAD")
        original_ref = git(self.target, "symbolic-ref", "HEAD")
        original_tree = tree_bytes(self.target)
        original_directories = tree_directories(self.target)
        original_index = (self.target / ".git/index").read_bytes()

        result = self._install(
            commit=True,
            failure_phase="post_commit_checkpoint_deletion",
        )

        self.assertFalse(result.success)
        self.assertIsNone(result.commit)
        self.assertEqual(git(self.target, "rev-parse", "HEAD"), original_head)
        self.assertEqual(git(self.target, "symbolic-ref", "HEAD"), original_ref)
        self.assertEqual(tree_bytes(self.target), original_tree)
        self.assertEqual(tree_directories(self.target), original_directories)
        self.assertEqual((self.target / ".git/index").read_bytes(), original_index)

    def test_attached_rollback_preserves_concurrent_commit(self):
        init_git(self.target)
        (self.target / "README.md").write_bytes(b"before\n")
        git(self.target, "add", ".")
        git(self.target, "commit", "-m", "before")
        observed: dict[str, object] = {}

        result = self._install(
            commit=True,
            phase_observer=self._concurrent_commit_observer(self.target, observed),
            failure_phase="post_commit_checkpoint_deletion",
        )

        self.assertFalse(result.success)
        self.assertIn("rollback conflict", result.error or "")
        self.assertEqual(git(self.target, "rev-parse", "HEAD"), observed["concurrent"])
        self.assertEqual(
            subprocess.run(
                ["git", "merge-base", "--is-ancestor", observed["installer"], "HEAD"],
                cwd=self.target,
            ).returncode,
            0,
        )
        self.assertEqual((self.target / ".git/index").read_bytes(), observed["index"])

    def test_detached_rollback_preserves_concurrent_commit(self):
        init_git(self.target)
        (self.target / "README.md").write_bytes(b"before\n")
        git(self.target, "add", ".")
        git(self.target, "commit", "-m", "before")
        git(self.target, "checkout", "--detach", "HEAD")
        observed: dict[str, object] = {}

        result = self._install(
            commit=True,
            phase_observer=self._concurrent_commit_observer(self.target, observed),
            failure_phase="post_commit_checkpoint_deletion",
        )

        self.assertFalse(result.success)
        self.assertIn("rollback conflict", result.error or "")
        self.assertEqual(git(self.target, "rev-parse", "HEAD"), observed["concurrent"])
        self.assertNotEqual(
            subprocess.run(
                ["git", "symbolic-ref", "-q", "HEAD"], cwd=self.target
            ).returncode,
            0,
        )

    def test_post_commit_failure_restores_unborn_branch(self):
        init_git(self.target)
        staged = self.target / "staged.txt"
        staged.write_bytes(b"unborn staged state\n")
        git(self.target, "add", "staged.txt")
        original_ref = git(self.target, "symbolic-ref", "HEAD")
        original_tree = tree_bytes(self.target)
        original_directories = tree_directories(self.target)
        original_index = (self.target / ".git/index").read_bytes()

        result = self._install(
            commit=True,
            failure_phase="post_commit_checkpoint_deletion",
        )

        self.assertFalse(result.success)
        self.assertIsNone(result.commit)
        self.assertEqual(git(self.target, "symbolic-ref", "HEAD"), original_ref)
        self.assertNotEqual(
            subprocess.run(
                ["git", "rev-parse", "--verify", "HEAD"],
                cwd=self.target,
                capture_output=True,
            ).returncode,
            0,
        )
        self.assertEqual(tree_bytes(self.target), original_tree)
        self.assertEqual(tree_directories(self.target), original_directories)
        self.assertEqual((self.target / ".git/index").read_bytes(), original_index)

    def test_post_commit_failure_restores_detached_head(self):
        init_git(self.target)
        (self.target / "README.md").write_bytes(b"before\n")
        git(self.target, "add", ".")
        git(self.target, "commit", "-m", "before")
        original_head = git(self.target, "rev-parse", "HEAD")
        git(self.target, "checkout", "--detach", original_head)
        original_tree = tree_bytes(self.target)
        original_index = (self.target / ".git/index").read_bytes()

        result = self._install(
            commit=True,
            failure_phase="post_commit_checkpoint_deletion",
        )

        self.assertFalse(result.success)
        self.assertEqual(git(self.target, "rev-parse", "HEAD"), original_head)
        self.assertNotEqual(
            subprocess.run(
                ["git", "symbolic-ref", "-q", "HEAD"],
                cwd=self.target,
                capture_output=True,
            ).returncode,
            0,
        )
        self.assertEqual(tree_bytes(self.target), original_tree)
        self.assertEqual((self.target / ".git/index").read_bytes(), original_index)

    def test_install_succeeds_in_attached_linked_worktree(self):
        repository = self.base / "worktree-repository"
        linked = self.base / "linked-attached"
        repository.mkdir()
        init_git(repository)
        (repository / "README.md").write_bytes(b"linked fixture\n")
        git(repository, "add", ".")
        git(repository, "commit", "-m", "initial")
        git(repository, "worktree", "add", "-b", "linked-install", str(linked))

        result = install_snapshot(
            self.source,
            linked,
            initiating_harness="opencode",
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=True,
        )

        self.assertTrue((linked / ".git").is_file())
        self.assertTrue(result.success, result.error)
        self.assertIsNotNone(result.commit)
        self.assertTrue((linked / ".opencode/agents/syspilot.cm.md").is_file())

    def test_linked_worktree_rollback_preserves_concurrent_commit(self):
        repository = self.base / "concurrent-repository"
        linked = self.base / "linked-concurrent"
        repository.mkdir()
        init_git(repository)
        (repository / "README.md").write_bytes(b"linked fixture\n")
        git(repository, "add", ".")
        git(repository, "commit", "-m", "initial")
        git(repository, "worktree", "add", "-b", "linked-concurrent", str(linked))
        observed: dict[str, object] = {}

        result = install_snapshot(
            self.source,
            linked,
            initiating_harness="opencode",
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=True,
            phase_observer=self._concurrent_commit_observer(linked, observed),
            failure_phase="post_commit_checkpoint_deletion",
        )

        self.assertFalse(result.success)
        self.assertIn("rollback conflict", result.error or "")
        self.assertEqual(git(linked, "rev-parse", "HEAD"), observed["concurrent"])
        self.assertEqual(git(repository, "rev-parse", "main"), git(repository, "rev-parse", "HEAD"))

    def test_post_commit_failure_restores_detached_linked_worktree(self):
        repository = self.base / "detached-repository"
        linked = self.base / "linked-detached"
        repository.mkdir()
        init_git(repository)
        (repository / "README.md").write_bytes(b"linked fixture\n")
        git(repository, "add", ".")
        git(repository, "commit", "-m", "initial")
        original_head = git(repository, "rev-parse", "HEAD")
        git(repository, "worktree", "add", "--detach", str(linked), original_head)
        original_tree = tree_bytes(linked)

        result = install_snapshot(
            self.source,
            linked,
            initiating_harness="opencode",
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=True,
            failure_phase="post_commit_checkpoint_deletion",
        )

        self.assertFalse(result.success)
        self.assertEqual(git(linked, "rev-parse", "HEAD"), original_head)
        self.assertNotEqual(
            subprocess.run(
                ["git", "symbolic-ref", "-q", "HEAD"],
                cwd=linked,
                capture_output=True,
            ).returncode,
            0,
        )
        self.assertEqual(tree_bytes(linked), original_tree)

    def test_post_commit_failure_restores_unborn_linked_worktree(self):
        repository = self.base / "unborn-repository"
        linked = self.base / "linked-unborn"
        repository.mkdir()
        init_git(repository)
        (repository / "README.md").write_bytes(b"linked fixture\n")
        git(repository, "add", ".")
        git(repository, "commit", "-m", "initial")
        git(
            repository,
            "worktree",
            "add",
            "--orphan",
            "-b",
            "linked-unborn",
            str(linked),
        )
        original_ref = git(linked, "symbolic-ref", "HEAD")

        result = install_snapshot(
            self.source,
            linked,
            initiating_harness="opencode",
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=True,
            failure_phase="post_commit_checkpoint_deletion",
        )

        self.assertFalse(result.success)
        self.assertEqual(git(linked, "symbolic-ref", "HEAD"), original_ref)
        self.assertNotEqual(
            subprocess.run(
                ["git", "rev-parse", "--verify", "HEAD"],
                cwd=linked,
                capture_output=True,
            ).returncode,
            0,
        )

    def test_install_commit_excludes_unselected_harness_and_existing_index(self):
        init_git(self.target)
        unselected = self.target / ".github/customer.md"
        unselected.parent.mkdir(parents=True)
        unselected.write_bytes(b"original\n")
        (self.target / "README.md").write_bytes(b"before\n")
        git(self.target, "add", ".")
        git(self.target, "commit", "-m", "before")
        unselected.write_bytes(b"customer change\n")
        staged = self.target / "staged.txt"
        staged.write_bytes(b"pre-existing staged state\n")
        git(self.target, "add", "staged.txt")

        result = self._install(commit=True)

        self.assertTrue(result.success, result.error)
        committed_paths = git(self.target, "show", "--name-only", "--format=").splitlines()
        self.assertNotIn(".github/customer.md", committed_paths)
        self.assertNotIn("staged.txt", committed_paths)
        self.assertEqual(unselected.read_bytes(), b"customer change\n")
        self.assertIn("A  staged.txt", git(self.target, "status", "--short"))

    def test_checkpoint_spans_runtime_placement_and_install_failure(self):
        init_git(self.target)
        existing = self.target / ".opencode/agents/customer.md"
        existing.parent.mkdir(parents=True)
        existing.write_bytes(b"customer bytes\r\n")
        git(self.target, "add", ".")
        git(self.target, "commit", "-m", "before")
        staged = self.target / "staged.txt"
        staged.write_bytes(b"staged before install\n")
        git(self.target, "add", "staged.txt")
        original_head = git(self.target, "rev-parse", "HEAD")
        original_tree = tree_bytes(self.target)
        original_directories = tree_directories(self.target)
        original_index = (self.target / ".git/index").read_bytes()

        result = self._install(
            failure_phase="runtime_write",
            commit=True,
        )

        self.assertFalse(result.success)
        self.assertIsNone(result.commit)
        self.assertEqual(git(self.target, "rev-parse", "HEAD"), original_head)
        self.assertEqual(tree_bytes(self.target), original_tree)
        self.assertEqual(tree_directories(self.target), original_directories)
        self.assertEqual((self.target / ".git/index").read_bytes(), original_index)

    def test_success_removes_persisted_checkpoint(self):
        _, checkpoint = self._create_plan_checkpoint()

        result = self._install(checkpoint_id=checkpoint.identifier)

        self.assertTrue(result.success, result.error)
        with self.assertRaisesRegex(ValueError, "checkpoint does not exist"):
            load_checkpoint(self.target, checkpoint.identifier)

    def test_narrow_supplied_checkpoint_is_rejected_before_mutation(self):
        self._initialize_checkpoint_git_state()
        plan = build_install_plan(self.source, self.target, "opencode")
        checkpoint = create_checkpoint(
            self.target,
            mutable_paths=[
                self.target / relative
                for relative in plan.mutable_paths
                if relative != ".opencode/agents/syspilot.cm.md"
            ],
        )
        self.addCleanup(
            installer_module._retire_checkpoint, checkpoint.identifier
        )

        self._assert_supplied_checkpoint_rejected(
            checkpoint.identifier, "mutable paths do not match the frozen plan"
        )

    def test_over_broad_supplied_checkpoint_is_rejected_before_mutation(self):
        self._initialize_checkpoint_git_state()
        plan = build_install_plan(self.source, self.target, "opencode")
        checkpoint = create_checkpoint(
            self.target,
            mutable_paths=[
                *(self.target / relative for relative in plan.mutable_paths),
                self.target / "undeclared.txt",
            ],
        )
        self.addCleanup(
            installer_module._retire_checkpoint, checkpoint.identifier
        )

        self._assert_supplied_checkpoint_rejected(
            checkpoint.identifier, "mutable paths do not match the frozen plan"
        )

    def test_cross_target_supplied_checkpoint_is_rejected_before_mutation(self):
        self._initialize_checkpoint_git_state()
        before = tree_bytes(self.target)
        other_target = self.base / "other-target"
        other_target.mkdir()
        _, checkpoint = self._create_plan_checkpoint(other_target)

        self._assert_supplied_checkpoint_rejected(
            checkpoint.identifier, "does not belong to the target root"
        )
        self.assertEqual(tree_bytes(self.target), before)

    def test_supplied_checkpoint_rejects_normalized_duplicate_alias(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        artifact = self._checkpoint_artifact(checkpoint.identifier)
        self.addCleanup(artifact.unlink, missing_ok=True)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        aliased = next(
            path for path in payload["mutable_paths"] if path.count("/") >= 2
        )
        parent, name = aliased.rsplit("/", 1)
        payload["mutable_paths"].append(f"{parent}/./{name}")
        artifact.write_text(json.dumps(payload), encoding="utf-8")

        self._assert_supplied_checkpoint_rejected(
            checkpoint.identifier, "duplicate normalized mutable path"
        )

    @unittest.skipUnless(os.name == "nt", "case aliases are Windows-specific")
    def test_supplied_checkpoint_rejects_windows_case_duplicate_alias(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        artifact = self._checkpoint_artifact(checkpoint.identifier)
        self.addCleanup(artifact.unlink, missing_ok=True)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        aliased = next(path for path in payload["mutable_paths"] if path.islower())
        payload["mutable_paths"].append(aliased.upper())
        artifact.write_text(json.dumps(payload), encoding="utf-8")

        self._assert_supplied_checkpoint_rejected(
            checkpoint.identifier, "duplicate normalized mutable path"
        )

    @unittest.skipUnless(os.name == "nt", "case normalization is Windows-specific")
    def test_mixed_case_supplied_checkpoint_restores_without_residue(self):
        self._initialize_checkpoint_git_state()
        owned = self.target / ".opencode/skills/syspilot.keep/SKILL.md"
        owned.parent.mkdir(parents=True)
        owned.write_bytes(b"pre-install mixed-case bytes\n")
        _, checkpoint = self._create_plan_checkpoint()

        result = self._install(
            checkpoint_id=checkpoint.identifier,
            failure_phase="target_write",
        )

        self.assertFalse(result.success)
        self.assertNotIn("KeyError", result.error or "")
        self.assertEqual(owned.read_bytes(), b"pre-install mixed-case bytes\n")
        self.assertFalse(self._checkpoint_artifact(checkpoint.identifier).exists())

    def test_supplied_checkpoint_rejects_modified_owned_path_as_stale(self):
        self._initialize_checkpoint_git_state()
        owned = self.target / ".opencode/agents/syspilot.cm.md"
        owned.parent.mkdir(parents=True)
        owned.write_bytes(b"checkpoint bytes\n")
        _, checkpoint = self._create_plan_checkpoint()
        owned.write_bytes(b"newer bytes\n")

        self._assert_supplied_checkpoint_rejected(checkpoint.identifier, "stale")

    def test_supplied_checkpoint_rejects_created_owned_path_as_stale(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        created = self.target / ".opencode/agents/syspilot.cm.md"
        created.parent.mkdir(parents=True)
        created.write_bytes(b"created after checkpoint\n")

        self._assert_supplied_checkpoint_rejected(checkpoint.identifier, "stale")

    def test_supplied_checkpoint_rejects_deleted_owned_path_as_stale(self):
        self._initialize_checkpoint_git_state()
        owned = self.target / ".opencode/agents/syspilot.cm.md"
        owned.parent.mkdir(parents=True)
        owned.write_bytes(b"checkpoint bytes\n")
        _, checkpoint = self._create_plan_checkpoint()
        owned.unlink()

        self._assert_supplied_checkpoint_rejected(checkpoint.identifier, "stale")

    def test_supplied_checkpoint_rejects_git_movement_as_stale(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        movement = self.target / "concurrent.txt"
        movement.write_bytes(b"concurrent commit\n")
        git(self.target, "add", "concurrent.txt")
        git(self.target, "commit", "-m", "concurrent movement")

        self._assert_supplied_checkpoint_rejected(checkpoint.identifier, "stale")

    def test_supplied_checkpoint_rejects_nonce_tampering(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        artifact = self._checkpoint_artifact(checkpoint.identifier)
        self.addCleanup(artifact.unlink, missing_ok=True)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        payload["nonce"] = str(uuid.uuid4())
        artifact.write_text(json.dumps(payload), encoding="utf-8")

        self._assert_supplied_checkpoint_rejected(checkpoint.identifier, "authentication")

    def test_supplied_checkpoint_rejects_fingerprint_tampering(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        artifact = self._checkpoint_artifact(checkpoint.identifier)
        self.addCleanup(artifact.unlink, missing_ok=True)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        key = next(iter(payload["path_fingerprints"]))
        payload["path_fingerprints"][key]["kind"] = "other"
        artifact.write_text(json.dumps(payload), encoding="utf-8")

        self._assert_supplied_checkpoint_rejected(checkpoint.identifier, "authentication")

    def test_supplied_checkpoint_rejects_tampering_with_recomputed_public_hash(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        artifact = self._checkpoint_artifact(checkpoint.identifier)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        key = next(iter(payload["path_fingerprints"]))
        payload["path_fingerprints"][key]["kind"] = "other"
        public_fields = {
            name: payload[name]
            for name in (
                "identifier",
                "nonce",
                "target_root",
                "mutable_paths",
                "display_paths",
                "path_fingerprints",
                "git_head",
                "git_ref",
                "git_index_path",
                "git_index",
            )
        }
        payload["binding"] = hashlib.sha256(
            json.dumps(public_fields, separators=(",", ":"), sort_keys=True).encode()
        ).hexdigest()
        artifact.write_text(json.dumps(payload), encoding="utf-8")

        self._assert_supplied_checkpoint_rejected(checkpoint.identifier, "authentication")

    def test_supplied_checkpoint_rejects_same_paths_with_different_plan_content(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        changed_files = dict(self.source.files)
        changed_files["syspilot/installer.py"] = b"different runtime bytes\n"
        changed_source = SourceSnapshot(
            changed_files, "changed-revision", self.source.branch
        )
        before = tree_bytes(self.target)

        result = install_snapshot(
            changed_source,
            self.target,
            initiating_harness="opencode",
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=False,
            checkpoint_id=checkpoint.identifier,
        )

        self.assertFalse(result.success)
        self.assertIn("plan", result.error or "")
        self.assertEqual(tree_bytes(self.target), before)
        self.assertFalse(self._checkpoint_artifact(checkpoint.identifier).exists())

    def test_checkpoint_lease_has_exactly_one_claimant(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        barrier = threading.Barrier(2)
        claims: list[str] = []
        errors: list[str] = []

        def claim() -> None:
            barrier.wait()
            try:
                leased = installer_module._lease_checkpoint(
                    self.target, checkpoint.identifier
                )
                claims.append(leased.identifier)
            except ValueError as error:
                errors.append(str(error))

        threads = [threading.Thread(target=claim) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        self.assertEqual(claims, [checkpoint.identifier])
        self.assertEqual(len(errors), 1)
        self.assertRegex(errors[0], "leased|consumed")
        installer_module._retire_checkpoint(checkpoint.identifier)

    def test_checkpoint_lease_has_exactly_one_cross_process_claimant(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        script = """
import json
import sys
import time
from pathlib import Path
from syspilot.installer import SourceSnapshot, install_snapshot
source_root, target, checkpoint_id = sys.argv[1:]
source = SourceSnapshot.from_directory(Path(source_root), revision='fixture-revision', branch='feature/test')
result = install_snapshot(source, Path(target), initiating_harness='opencode', dependency_check=lambda: time.sleep(0.5), validator=lambda _target: None, commit=False, checkpoint_id=checkpoint_id)
print(json.dumps({'success': result.success, 'error': result.error}))
"""
        command = [
            sys.executable,
            "-c",
            script,
            str(self.source_root),
            str(self.target),
            checkpoint.identifier,
        ]
        processes = [
            subprocess.Popen(
                command,
                cwd=ROOT,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            for _ in range(2)
        ]
        results = []
        for process in processes:
            stdout, stderr = process.communicate(timeout=30)
            self.assertEqual(process.returncode, 0, stderr)
            results.append(json.loads(stdout))

        self.assertEqual(sum(bool(result["success"]) for result in results), 1)
        rejected = next(result for result in results if not result["success"])
        self.assertRegex(str(rejected["error"]), "leased|consumed")
        self.assertFalse(self._checkpoint_artifact(checkpoint.identifier).exists())
        self.assertFalse(self._checkpoint_key_artifact(checkpoint.identifier).exists())
        self.assertFalse(self._checkpoint_lease_artifact(checkpoint.identifier).exists())

    def test_expired_checkpoint_is_rejected_and_retired(self):
        self._initialize_checkpoint_git_state()
        with patch("syspilot.installer._checkpoint_now", return_value=100.0):
            _, checkpoint = self._create_plan_checkpoint()

        with patch(
            "syspilot.installer._checkpoint_now",
            return_value=100.0 + installer_module.CHECKPOINT_TTL_SECONDS + 1,
        ):
            result = self._install(checkpoint_id=checkpoint.identifier)

        self.assertFalse(result.success)
        self.assertIn("expired", result.error or "")
        self.assertFalse(self._checkpoint_artifact(checkpoint.identifier).exists())
        self.assertFalse(self._checkpoint_key_artifact(checkpoint.identifier).exists())
        replay = self._replay_checkpoint_in_subprocess(checkpoint.identifier)
        self.assertFalse(replay["success"])
        self.assertRegex(str(replay["error"]), "does not exist|consumed")

    def test_failed_attempt_cannot_replay_checkpoint(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()

        first = self._install(
            checkpoint_id=checkpoint.identifier,
            failure_phase="target_write",
        )
        second = self._install(checkpoint_id=checkpoint.identifier)

        self.assertFalse(first.success)
        self.assertFalse(second.success)
        self.assertRegex(second.error or "", "does not exist|consumed")

    def test_dependency_failure_consumes_supplied_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        before = tree_bytes(self.target)
        before_head = git(self.target, "rev-parse", "HEAD")
        before_index = (self.target / ".git/index").read_bytes()

        first = self._install(
            checkpoint_id=checkpoint.identifier,
            dependency_check=lambda: (_ for _ in ()).throw(
                DependencyError("dependency unavailable")
            ),
        )
        replay_result = self._replay_checkpoint_in_subprocess(checkpoint.identifier)

        self.assertFalse(first.success)
        self.assertIn("dependency unavailable", first.error or "")
        self.assertFalse(replay_result["success"])
        self.assertRegex(replay_result["error"] or "", "does not exist|consumed")
        self.assertEqual(tree_bytes(self.target), before)
        self.assertEqual(git(self.target, "rev-parse", "HEAD"), before_head)
        self.assertEqual((self.target / ".git/index").read_bytes(), before_index)
        self.assertFalse(self._checkpoint_artifact(checkpoint.identifier).exists())
        self.assertFalse(self._checkpoint_key_artifact(checkpoint.identifier).exists())
        self.assertFalse(self._checkpoint_lease_artifact(checkpoint.identifier).exists())

    def test_dependency_cancellation_retires_supplied_checkpoint(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        before = tree_bytes(self.target)

        with self.assertRaises(KeyboardInterrupt):
            self._install(
                checkpoint_id=checkpoint.identifier,
                dependency_check=lambda: (_ for _ in ()).throw(KeyboardInterrupt()),
            )

        self.assertEqual(tree_bytes(self.target), before)
        replay = self._replay_checkpoint_in_subprocess(checkpoint.identifier)
        self.assertFalse(replay["success"])
        self.assertRegex(str(replay["error"]), "does not exist|consumed")
        self.assertFalse(self._checkpoint_artifact(checkpoint.identifier).exists())
        self.assertFalse(self._checkpoint_key_artifact(checkpoint.identifier).exists())
        self.assertFalse(self._checkpoint_lease_artifact(checkpoint.identifier).exists())

    def test_install_dependency_failure_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        before = tree_bytes(self.target)

        result = install(
            "fixture/repository",
            "feature/test",
            self.target,
            initiating_harness="opencode",
            checkpoint_id=checkpoint.identifier,
            dependency_check=lambda: (_ for _ in ()).throw(
                DependencyError("dependency unavailable")
            ),
            source_acquirer=lambda _repository, _branch: self.source,
        )

        self.assertFalse(result.success)
        self.assertIn("dependency unavailable", result.error or "")
        self.assertEqual(tree_bytes(self.target), before)
        replay = self._replay_checkpoint_in_subprocess(checkpoint.identifier)
        self.assertFalse(replay["success"])
        self.assertRegex(str(replay["error"]), "does not exist|consumed")

    def test_source_acquisition_failure_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        before = tree_bytes(self.target)

        result = install(
            "fixture/repository",
            "feature/test",
            self.target,
            initiating_harness="opencode",
            checkpoint_id=checkpoint.identifier,
            dependency_check=lambda: None,
            source_acquirer=lambda _repository, _branch: (_ for _ in ()).throw(
                ValueError("source acquisition failed")
            ),
        )

        self.assertFalse(result.success)
        self.assertIn("source acquisition failed", result.error or "")
        self.assertEqual(tree_bytes(self.target), before)
        replay = self._replay_checkpoint_in_subprocess(checkpoint.identifier)
        self.assertFalse(replay["success"])
        self.assertRegex(str(replay["error"]), "does not exist|consumed")

    def test_source_parse_failure_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        files = dict(self.source.files)
        files["syspilot/agents/syspilot.cm.agent.md"] = b"malformed"
        malformed = SourceSnapshot(files, self.source.revision, self.source.branch)

        self._assert_preplan_failure_consumes_checkpoint(
            checkpoint.identifier,
            source=malformed,
            error="missing opening YAML frontmatter delimiter",
        )

    def test_source_transform_failure_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        files = dict(self.source.files)
        files["syspilot/agents/syspilot.cm.agent.md"] = frontmatter(
            "agents: [syspilot.implement]", b"# Manager\n"
        )
        malformed = SourceSnapshot(files, self.source.revision, self.source.branch)

        self._assert_preplan_failure_consumes_checkpoint(
            checkpoint.identifier,
            source=malformed,
            error="agent description is required",
        )

    def test_source_containment_failure_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        files = dict(self.source.files)
        files["syspilot/agents/../../../../escaped.agent.md"] = frontmatter(
            'description: "escape"', b"escape\n"
        )
        malicious = SourceSnapshot(files, self.source.revision, self.source.branch)

        self._assert_preplan_failure_consumes_checkpoint(
            checkpoint.identifier,
            source=malicious,
            error="invalid source path",
        )

    def test_malformed_repository_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()

        result = install(
            "../local-repository",
            "feature/test",
            self.target,
            initiating_harness="opencode",
            checkpoint_id=checkpoint.identifier,
            dependency_check=lambda: None,
        )

        self.assertFalse(result.success)
        self.assertIn("GitHub repository", result.error or "")
        replay = self._replay_checkpoint_in_subprocess(checkpoint.identifier)
        self.assertFalse(replay["success"])

    def test_malformed_branch_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()

        result = install(
            "fixture/repository",
            "",
            self.target,
            initiating_harness="opencode",
            checkpoint_id=checkpoint.identifier,
            dependency_check=lambda: None,
        )

        self.assertFalse(result.success)
        self.assertIn("branch", result.error or "")
        replay = self._replay_checkpoint_in_subprocess(checkpoint.identifier)
        self.assertFalse(replay["success"])

    def test_malformed_harness_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()

        self._assert_preplan_failure_consumes_checkpoint(
            checkpoint.identifier,
            harness="malformed",
            error="unsupported initiating harness",
        )

    def test_direct_internal_checkpoint_is_retired_after_success(self):
        identifiers: list[str] = []
        real_lease = installer_module._lease_checkpoint

        def record_lease(target_root: Path, identifier: str):
            identifiers.append(identifier)
            return real_lease(target_root, identifier)

        with patch("syspilot.installer._lease_checkpoint", side_effect=record_lease):
            result = self._install()

        self.assertTrue(result.success, result.error)
        self.assertEqual(len(identifiers), 1)
        with self.assertRaisesRegex(ValueError, "does not exist"):
            load_checkpoint(self.target, identifiers[0])

    def test_stale_checkpoint_cleanup_is_bounded(self):
        checkpoint_root = self.base / "checkpoint-cleanup"
        checkpoint_root.mkdir()
        for _ in range(installer_module.CHECKPOINT_CLEANUP_LIMIT + 5):
            identifier = str(uuid.uuid4())
            artifact = checkpoint_root / f"{identifier}.lease"
            artifact.touch()
            os.utime(artifact, (1, 1))

        with patch("syspilot.installer.CHECKPOINT_ROOT", checkpoint_root):
            installer_module._cleanup_stale_checkpoints(
                installer_module.CHECKPOINT_STALE_SECONDS + 2
            )

        self.assertEqual(len(list(checkpoint_root.iterdir())), 5)

    def test_checkpoint_secret_is_outside_target(self):
        _, checkpoint = self._create_plan_checkpoint()

        key_path = self._checkpoint_key_artifact(checkpoint.identifier)

        self.assertTrue(key_path.is_file())
        with self.assertRaises(ValueError):
            key_path.relative_to(self.target)
        self.assertFalse(any(path.suffix == ".key" for path in self.target.rglob("*")))

    def test_checkpoint_created_in_another_process_can_be_consumed(self):
        script = """
import sys
from pathlib import Path
from syspilot.installer import SourceSnapshot, build_install_plan, create_checkpoint
source_root, target = map(Path, sys.argv[1:])
source = SourceSnapshot.from_directory(source_root, revision='fixture-revision', branch='feature/test')
plan = build_install_plan(source, target, 'opencode')
checkpoint = create_checkpoint(target, mutable_paths=[target / path for path in plan.mutable_paths], expected=plan.expected, plan=plan)
print(checkpoint.identifier)
"""
        completed = subprocess.run(
            [sys.executable, "-c", script, str(self.source_root), str(self.target)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        result = self._install(checkpoint_id=completed.stdout.strip())

        self.assertTrue(result.success, result.error)

    def test_invalid_checkpoint_identifier_is_rejected_before_mutation(self):
        _, valid_checkpoint = self._create_plan_checkpoint()
        before = tree_bytes(self.target)

        invalid = self._install(checkpoint_id="../../outside")

        self.assertFalse(invalid.success)
        self.assertIn("invalid checkpoint identifier", invalid.error)
        self.assertEqual(tree_bytes(self.target), before)
        self.assertEqual(
            load_checkpoint(self.target, valid_checkpoint.identifier).identifier,
            valid_checkpoint.identifier,
        )

    def test_checkpoint_cli_creates_cross_process_handoff(self):
        output = io.StringIO()
        with (
            patch("syspilot.installer.acquire_source", return_value=self.source),
            patch("syspilot.installer.check_dependencies"),
            redirect_stdout(output),
        ):
            exit_code = main(
                [
                    "checkpoint",
                    "--repository",
                    "fixture/repository",
                    "--branch",
                    "feature/test",
                    "--target",
                    str(self.target),
                    "--harness",
                    "opencode",
                ]
            )

        payload = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(payload["revision"], "fixture-revision")
        self.assertTrue(self._checkpoint_artifact(payload["checkpoint_id"]).is_file())

    def test_install_cli_forwards_checkpoint_identifier(self):
        identifier = str(uuid.uuid4())
        observed: dict[str, object] = {}

        def record_install(repository, branch, target_root, **options):
            observed.update(
                repository=repository,
                branch=branch,
                target_root=target_root,
                options=options,
            )
            return InstallResult(True, branch, "fixture-revision")

        with patch("syspilot.installer.install", side_effect=record_install):
            exit_code = main(
                [
                    "install",
                    "--target",
                    str(self.target),
                    "--harness",
                    "opencode",
                    "--checkpoint-id",
                    identifier,
                ]
            )

        self.assertEqual(exit_code, 0)
        self.assertEqual(observed["options"]["checkpoint_id"], identifier)

    def test_install_cli_malformed_harness_consumes_checkpoint_before_replay(self):
        self._initialize_checkpoint_git_state()
        _, checkpoint = self._create_plan_checkpoint()
        output = io.StringIO()

        with (
            patch("syspilot.installer.acquire_source", return_value=self.source),
            patch("syspilot.installer.check_dependencies"),
            redirect_stdout(output),
        ):
            exit_code = main(
                [
                    "install",
                    "--repository",
                    "fixture/repository",
                    "--branch",
                    "feature/test",
                    "--target",
                    str(self.target),
                    "--harness",
                    "malformed",
                    "--checkpoint-id",
                    checkpoint.identifier,
                ]
            )

        result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 1)
        self.assertFalse(result["success"])
        self.assertIn("unsupported initiating harness", result["error"])
        replay = self._replay_checkpoint_in_subprocess(checkpoint.identifier)
        self.assertFalse(replay["success"])
        self.assertRegex(str(replay["error"]), "does not exist|consumed")


class TestRealProductAcceptance(unittest.TestCase):
    def _install_product(self, target: Path, harness: str = "opencode"):
        source = SourceSnapshot.from_directory(
            ROOT, revision="working-tree", branch="feature/harness-interop"
        )
        return install_snapshot(
            source,
            target,
            initiating_harness=harness,
            dependency_check=lambda: None,
            validator=lambda _target: None,
            commit=False,
        )

    def test_product_generates_13_agents_6_selected_skills_and_7_commands(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            result = self._install_product(target)

            self.assertTrue(result.success, result.error)
            self.assertEqual(len(list((target / ".opencode/agents").glob("*.md"))), 13)
            self.assertEqual(len(list((target / ".opencode/skills").glob("*/SKILL.md"))), 6)
            self.assertEqual(len(list((target / ".opencode/commands").glob("*.md"))), 7)

    def test_every_opencode_command_preserves_source_routing_behavior(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            result = self._install_product(target)
            self.assertTrue(result.success, result.error)
            same_request = "Implement the approved change and report the result"

            for source_path in sorted((ROOT / "syspilot/prompts").glob("*.prompt.md")):
                source_metadata, _ = parse_frontmatter(source_path.read_bytes())
                command_name = source_path.name.removesuffix(".prompt.md") + ".md"
                command_metadata, command_body = parse_frontmatter(
                    (target / ".opencode/commands" / command_name).read_bytes()
                )
                with self.subTest(source=source_path.name):
                    vscode_route = (source_metadata["agent"], same_request)
                    opencode_route = (command_metadata["agent"], same_request)
                    self.assertEqual(opencode_route, vscode_route)
                    self.assertTrue(command_metadata["description"])
                    self.assertEqual(command_body, b"$ARGUMENTS\n")

    def test_setup_frontmatter_matches_approved_runtime_contract(self):
        metadata, _ = parse_frontmatter(
            (ROOT / "syspilot/agents/syspilot.setup.agent.md").read_bytes()
        )

        self.assertEqual(metadata["tools"], ["execute"])
        self.assertEqual(metadata["agents"], [])
        self.assertEqual(metadata["version"], "v0.9.1.2")

    def test_vscode_change_manager_bootstrap_configuration(self):
        target_agent_files = (
            "syspilot.design.agent.md",
            "syspilot.uat.agent.md",
            "syspilot.implement.agent.md",
            "syspilot.mece.agent.md",
            "syspilot.trace.agent.md",
            "syspilot.docu.agent.md",
            "syspilot.pm.agent.md",
            "syspilot.qm.agent.md",
        )
        for agent_root in (ROOT / "syspilot/agents", ROOT / ".github/agents"):
            expected_names = [
                parse_frontmatter((agent_root / filename).read_bytes())[0]["name"]
                for filename in target_agent_files
            ]
            metadata, _ = parse_frontmatter(
                (agent_root / "syspilot.cm.agent.md").read_bytes()
            )
            with self.subTest(agent_root=agent_root):
                self.assertEqual(metadata["agents"], expected_names)

        settings_path = ROOT / ".vscode/settings.json"
        self.assertTrue(settings_path.is_file(), "workspace settings are missing")
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        self.assertIs(
            settings.get("chat.subagents.allowInvocationsFromSubagents"), True
        )

    def test_vscode_agent_allowlists_use_declared_display_names(self):
        for agent_root in (ROOT / "syspilot/agents", ROOT / ".github/agents"):
            agents = {
                path: parse_frontmatter(path.read_bytes())[0]
                for path in agent_root.glob("*.agent.md")
            }
            declared_names = {
                metadata["name"]
                for metadata in agents.values()
                if "name" in metadata
            }

            for path, metadata in agents.items():
                unresolved = set(metadata.get("agents") or []) - declared_names
                with self.subTest(agent=path.relative_to(ROOT)):
                    self.assertEqual(unresolved, set())

    def test_installed_change_launcher_locates_shared_template(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            init_git(target)
            (target / "README.md").write_bytes(b"launcher fixture\n")
            git(target, "add", ".")
            git(target, "commit", "-m", "initial")
            git(target, "checkout", "-b", "development")
            result = self._install_product(target)
            self.assertTrue(result.success, result.error)
            script = (
                target
                / ".syspilot/skills/syspilot.change-launcher/launch_change.py"
            )

            completed = subprocess.run(
                [
                    "uv",
                    "run",
                    "--no-project",
                    str(script),
                    "--name",
                    "shared-template-uat",
                    "--author",
                    "PM",
                    "--mode",
                    "autonomous",
                ],
                cwd=target,
                capture_output=True,
                text=True,
                timeout=60,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue((target / "docs/changes/shared-template-uat.md").is_file())

    @unittest.skipUnless(
        os.environ.get("SYSPILOT_RUN_NETWORK_TESTS") == "1",
        "real GitHub API test is network-conditional",
    )
    def test_real_github_api_source_acquisition(self):
        try:
            source = acquire_source(
                "hubertusgbecker/syspilot", "feature/harness-interop"
            )
        except urllib.error.URLError as error:
            self.skipTest(f"GitHub API unavailable: {error}")

        self.assertRegex(source.revision, r"^[0-9a-f]{40}$")
        self.assertIn("syspilot/installer.py", source.files)
        self.assertTrue(source.files["syspilot/installer.py"].startswith(b"# /// script\n"))

    def test_generated_claude_agents_parse_and_are_discoverable(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            result = self._install_product(target, harness="claude")
            self.assertTrue(result.success, result.error)

            agents = {
                path.stem: parse_frontmatter(path.read_bytes())[0]
                for path in (target / ".claude/agents").glob("*.md")
            }
            native_names = {
                metadata["name"] for metadata in agents.values()
            }
            self.assertEqual(len(agents), 13)
            self.assertEqual(len(native_names), 13)
            self.assertIn("syspilot.setup", agents)
            self.assertIn("syspilot.cm", agents)
            self.assertIn("syspilot.implement", agents)
            self.assertEqual(agents["syspilot.setup"]["name"], "syspilot-setup")
            self.assertEqual(agents["syspilot.pm"]["name"], "syspilot-pm")
            self.assertEqual(agents["syspilot.qm"]["name"], "syspilot-qm")
            self.assertEqual(agents["syspilot.cm"]["name"], "syspilot-cm")
            self.assertTrue(
                all(re.fullmatch(r"[a-z-]+", name) for name in native_names)
            )
            self.assertTrue(
                all(isinstance(metadata.get("description"), str) for metadata in agents.values())
            )
            source_agents = {
                path: parse_frontmatter(path.read_bytes())[0]
                for path in (ROOT / "syspilot/agents").glob("*.agent.md")
            }
            identity_by_name = {
                metadata["name"]: metadata["agent"]
                for metadata in source_agents.values()
                if "name" in metadata and "agent" in metadata
            }
            for source_path in (ROOT / "syspilot/agents").glob("*.agent.md"):
                source_metadata = source_agents[source_path]
                source_allowlist = source_metadata.get("agents") or []
                generated = agents[source_path.name.removesuffix(".agent.md")]
                mapped_targets = [
                    identity_by_name[target].replace(".", "-")
                    for target in source_allowlist
                ]
                self.assertTrue(set(mapped_targets).issubset(native_names))
                if source_allowlist and source_metadata.get("user-invocable") is True:
                    self.assertEqual(
                        generated["tools"],
                        [f"Agent({', '.join(mapped_targets)})"],
                    )
                elif source_allowlist:
                    self.assertEqual(generated["tools"], ["Agent"])
                else:
                    self.assertNotIn("tools", generated)

            orchestration = (
                target
                / ".claude/skills/syspilot.orchestration-subagent/SKILL.md"
            ).read_text(encoding="utf-8")
            self.assertIn("built-in Agent tool", orchestration)
            self.assertIn("`syspilot-<agent>`", orchestration)
            self.assertNotIn("runSubagent", orchestration)

    def test_generated_claude_agents_are_hidden_from_vscode_picker(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            result = self._install_product(target, harness="claude")
            self.assertTrue(result.success, result.error)

            claude_agents = {
                path.stem: parse_frontmatter(path.read_bytes())[0]
                for path in (target / ".claude/agents").glob("*.md")
            }
            self.assertEqual(len(claude_agents), 13)
            self.assertFalse(claude_agents["syspilot.release"]["user-invocable"])
            self.assertTrue(
                all(
                    metadata.get("user-invocable") is False
                    for metadata in claude_agents.values()
                )
            )

            source_agents = {
                path.stem.removesuffix(".agent"): parse_frontmatter(
                    path.read_bytes()
                )[0]
                for path in (ROOT / "syspilot/agents").glob("*.agent.md")
            }
            visible_source_roles = {
                name
                for name, metadata in source_agents.items()
                if metadata.get("user-invocable") is True
            }
            visible_claude_roles = {
                name
                for name, metadata in claude_agents.items()
                if metadata.get("user-invocable", True) is True
            }
            self.assertEqual(visible_source_roles, {"syspilot.cm", "syspilot.pm", "syspilot.qm", "syspilot.setup"})
            self.assertEqual(visible_claude_roles, set())

    def test_generated_opencode_agents_use_native_target_identities(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            result = self._install_product(target)
            self.assertTrue(result.success, result.error)

            expected_targets = {
                "syspilot.design.md": {"syspilot.mece"},
                "syspilot.pm.md": {"syspilot.cm", "syspilot.release"},
                "syspilot.qm.md": {
                    "syspilot.mece",
                    "syspilot.trace",
                    "syspilot.pm",
                },
            }
            for filename, expected in expected_targets.items():
                metadata, _ = parse_frontmatter(
                    (target / ".opencode/agents" / filename).read_bytes()
                )
                task_permissions = metadata["permission"]["task"]
                with self.subTest(agent=filename):
                    self.assertEqual(task_permissions["*"], "deny")
                    self.assertEqual(
                        {
                            name
                            for name, permission in task_permissions.items()
                            if permission == "allow"
                        },
                        expected,
                    )

    @unittest.skipUnless(shutil.which("opencode"), "OpenCode is not installed")
    def test_generated_opencode_configuration_parses(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            result = self._install_product(target)
            self.assertTrue(result.success, result.error)

            config_home = target / ".isolated-opencode-config"
            config_home.mkdir()
            environment = os.environ.copy()
            environment["XDG_CONFIG_HOME"] = str(config_home)

            completed = subprocess.run(
                [shutil.which("opencode"), "debug", "config"],
                cwd=target,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=environment,
                timeout=60,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            parsed = yaml.safe_load(completed.stdout)
            self.assertIn("agent", parsed)

    @unittest.skipUnless(
        shutil.which("opencode") and os.environ.get("SYSPILOT_LIVE_OPENCODE") == "1",
        "live OpenCode delegation is opt-in",
    )
    def test_live_opencode_command_forwards_request_and_delegates(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            source = SourceSnapshot.from_directory(
                ROOT, revision="working-tree", branch="feature/harness-interop"
            )
            files = dict(source.files)
            files["syspilot/agents/syspilot.cm.agent.md"] = frontmatter(
                'description: "OpenCode command forwarding UAT manager"\n'
                "agents: [syspilot.implement]",
                b"When invoked, copy the complete user request verbatim after "
                b"RECEIVED_REQUEST=. Then use native Task once to ask "
                b"syspilot.implement to reply exactly ENGINEER_OK, and finally "
                b"reply MANAGER_OK.\n",
            )
            result = install_snapshot(
                SourceSnapshot(files, source.revision, source.branch),
                target,
                initiating_harness="opencode",
                dependency_check=lambda: None,
                validator=lambda _target: None,
                commit=False,
            )
            self.assertTrue(result.success, result.error)
            request = "Round 6 request: preserve spaces, commas, and punctuation?"
            config_home = target / ".isolated-opencode-config"
            config_home.mkdir()
            environment = os.environ.copy()
            environment["XDG_CONFIG_HOME"] = str(config_home)

            completed = subprocess.run(
                [
                    shutil.which("opencode"),
                    "run",
                    "--pure",
                    "--format",
                    "json",
                    "--agent",
                    "syspilot.cm",
                    "--command",
                    "syspilot.cm",
                    f"Reply exactly RECEIVED_REQUEST={request}",
                ],
                cwd=target,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=environment,
                timeout=180,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn(f"RECEIVED_REQUEST={request}".upper(), completed.stdout.upper())

            delegated = subprocess.run(
                [
                    shutil.which("opencode"),
                    "run",
                    "--pure",
                    "--format",
                    "json",
                    "--agent",
                    "syspilot.cm",
                    "Use native Task once to ask syspilot.implement to reply "
                    "exactly ENGINEER_OK, then reply MANAGER_OK.",
                ],
                cwd=target,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=environment,
                timeout=180,
            )
            self.assertEqual(delegated.returncode, 0, delegated.stderr)
            events = [json.loads(line) for line in delegated.stdout.splitlines()]
            task_events = [
                event
                for event in events
                if event.get("type") == "tool_use"
                and event.get("part", {}).get("tool") == "task"
            ]
            self.assertEqual(len(task_events), 1, delegated.stdout)
            self.assertEqual(
                task_events[0]["part"]["state"]["input"]["subagent_type"],
                "syspilot.implement",
            )
            transcript = delegated.stdout.upper()
            self.assertIn("ENGINEER_OK", transcript)
            self.assertIn("MANAGER_OK", transcript)


class TestBootstrapContract(unittest.TestCase):
    def test_user_docs_publish_only_the_round_two_production_matrix(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        architecture = (ROOT / "docs/architecture.md").read_text(encoding="utf-8")

        self.assertIn(
            "Production harnesses: GitHub Copilot in VS Code, Claude Code, and OpenCode. Qoder is\n"
            "available as an explicitly disclosed experimental, installable harness.",
            readme,
        )
        self.assertNotIn("Claude Code and Qoder adapters are experimental", readme)
        self.assertIn("--harness claude", readme)
        self.assertIn("--harness qoder", readme)
        self.assertNotIn("Claude CLI", readme)
        self.assertIn("`.syspilot/skills/`", readme)
        self.assertIn("`.syspilot/templates/`", readme)
        self.assertIn("writes only the explicitly selected harness target", architecture)
        self.assertIn("bounded checkpoint", architecture)
        self.assertRegex(
            architecture, r"rejects\s+symlinks, junctions, and reparse points"
        )
        self.assertNotIn("writes `.github/` plus", architecture)

    def test_setup_executes_installed_runtime_without_nested_delegation(self):
        setup = (ROOT / "syspilot/agents/syspilot.setup.agent.md").read_bytes()
        metadata, body = parse_frontmatter(setup)
        text = body.decode("utf-8")

        self.assertEqual(metadata["agents"], [])
        self.assertNotIn("agent", metadata["tools"])
        self.assertIn("--harness <vscode|claude|opencode|qoder>", text)
        for forbidden in (
            "runSubagent",
            "Task",
            "Agent tool",
            "syspilot.installer",
            "--orchestration",
            "locally installed version is never authoritative",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, text)

    def test_obsolete_bootstrap_manifest_is_not_shipped(self):
        self.assertFalse((ROOT / "syspilot/bootstrap.json").exists())

    def test_installer_agent_is_optional_diagnostic_documentation(self):
        source = (ROOT / "syspilot/agents/syspilot.installer.agent.md").read_bytes()
        metadata, body = parse_frontmatter(source)
        text = body.decode("utf-8")

        self.assertFalse(metadata["user-invocable"])
        self.assertEqual(metadata["agents"], [])
        self.assertIn("documentation and diagnostic surface", text)
        self.assertIn("not a control-plane dependency", text)
        self.assertNotIn("invoked exclusively by the Setup Bootloader", text)
        self.assertNotIn("--orchestration", text)
        self.assertNotIn("Production harnesses are `vscode`, `opencode`, and `claude`", text)

    def test_setup_forwards_the_complete_production_selector_and_uses_claude_code(self):
        setup = (ROOT / "syspilot/agents/syspilot.setup.agent.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("<vscode|claude|opencode|qoder>", setup)
        self.assertIn("Claude Code", setup)
        self.assertNotIn("Claude CLI", setup)
        self.assertNotIn("experimental", setup.lower())
        self.assertNotIn("unsupported", setup.lower())


class TestUvOnlyRuntimeContract(unittest.TestCase):
    def test_installer_declares_pep_723_runtime_dependencies(self):
        source = (ROOT / "syspilot/installer.py").read_text(encoding="utf-8")

        self.assertTrue(source.startswith("# /// script\n"))
        self.assertIn('requires-python = ">=3.11,<3.15"', source)
        for dependency in ("PyYAML", "Sphinx", "sphinx-needs"):
            with self.subTest(dependency=dependency):
                self.assertRegex(source, rf'"{dependency}==[^\"]+"')

    def test_active_installation_guidance_uses_uv_only_commands(self):
        active_files = list((ROOT / "syspilot/agents").glob("*.md"))
        active_files.extend((ROOT / "syspilot/skills").glob("**/*"))
        command_pattern = re.compile(
            r"(?m)^\s*(?:#!.*\b|(?:\$\s*)?)(python3?|pip3?|sphinx-build)\b"
        )
        violations = []
        for path in active_files:
            if not path.is_file() or path.suffix not in {".md", ".py"}:
                continue
            text = path.read_text(encoding="utf-8")
            if command_pattern.search(text):
                violations.append(path.relative_to(ROOT).as_posix())

        self.assertEqual(violations, [])
        setup = (ROOT / "syspilot/agents/syspilot.setup.agent.md").read_text(
            encoding="utf-8"
        )
        installer = (ROOT / "syspilot/agents/syspilot.installer.agent.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("`uv --version` and `git --version`", setup)
        self.assertIn(
            "uv run --no-project .syspilot/installer.py install", setup
        )
        self.assertIn(
            "uv run --no-project .syspilot/installer.py install", installer
        )

        workflow = yaml.safe_load(
            (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
        )
        commands = [
            step["run"]
            for job in workflow["jobs"].values()
            for step in job["steps"]
            if "run" in step
        ]
        requirements = "--with-requirements docs/requirements.txt"
        self.assertIn(
            f"uv run --python 3.11 {requirements} "
            "python -m unittest discover -s tests -v",
            commands,
        )
        self.assertIn(
            f"uv run --python 3.11 {requirements} "
            "python -m unittest docs.test_docs_build",
            commands,
        )

        bare_executable = re.compile(
            r"(?:^|\n|&&|\|\||;|\|)\s*"
            r"(?:python(?:3(?:\.\d+)?)?|pip3?|sphinx-build)(?=\s|$)"
        )
        self.assertIsNone(
            bare_executable.search("uv run --python 3.11 python -m unittest")
        )
        self.assertIsNotNone(bare_executable.search("python -m unittest"))
        for command in commands:
            with self.subTest(command=command):
                self.assertIsNone(bare_executable.search(command))

    def test_validation_reenters_installed_script_through_uv(self):
        target = ROOT / "fixture-target"
        output = Path(tempfile.gettempdir()) / "syspilot-test-html"
        doctrees = Path(tempfile.gettempdir()) / "syspilot-test-doctrees"

        with patch("syspilot.installer.subprocess.run") as run:
            validate_sphinx(target, output=output, doctrees=doctrees)

        command = run.call_args.args[0]
        self.assertEqual(
            command[:4],
            ["uv", "run", "--no-project", ".syspilot/installer.py"],
        )
        self.assertEqual(command[4], "validate-sphinx")
        self.assertNotIn("python", command)
        self.assertNotIn("python3", command)
        self.assertNotIn("sphinx-build", command)
        self.assertEqual(run.call_args.kwargs["cwd"], target)
        self.assertFalse(output.is_relative_to(target))
        self.assertFalse(doctrees.is_relative_to(target))

    def test_public_cli_exposes_exactly_four_production_harnesses_and_no_legacy_controls(self):
        result = InstallResult(True, "main", "fixture")
        with patch("syspilot.installer.install", return_value=result):
            for harness in ("vscode", "claude", "opencode", "qoder"):
                with self.subTest(harness=harness):
                    self.assertEqual(main(["install", "--harness", harness]), 0)
            for arguments in (
                ["install", "--harness", "unsupported"],
                ["bootstrap", "--harness", "vscode", "--checkpoint-id", "unused"],
                [
                    "install",
                    "--harness",
                    "vscode",
                    "--orchestration",
                    "syspilot.orchestration-jarvis",
                ],
            ):
                with self.subTest(arguments=arguments), redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as raised:
                        main(arguments)
                    self.assertEqual(raised.exception.code, 2)

    def test_remote_runtime_rejects_local_source_without_residue(self):
        handler = partial(QuietFileHandler, directory=str(ROOT))
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(thread.join)
        self.addCleanup(server.shutdown)
        runtime_url = (
            f"http://127.0.0.1:{server.server_address[1]}/syspilot/installer.py"
        )
        checkpoint_root = Path(tempfile.gettempdir()) / "syspilot-checkpoints"
        checkpoints_before = set(checkpoint_root.glob("*.json"))

        for harness in ("vscode", "opencode"):
            with self.subTest(harness=harness), tempfile.TemporaryDirectory() as temporary:
                base = Path(temporary)
                source = base / "source"
                target = base / "target"
                shutil.copytree(ROOT / "syspilot", source / "syspilot")
                init_git(source)
                git(source, "add", ".")
                git(source, "commit", "-m", "fixture source")
                target.mkdir()
                init_git(target)
                (target / "README.md").write_text("fixture\n", encoding="utf-8")
                git(target, "add", ".")
                git(target, "commit", "-m", "fixture target")
                environment = os.environ.copy()
                environment.pop("VIRTUAL_ENV", None)
                environment.pop("PYTHONDONTWRITEBYTECODE", None)
                command = [
                    "uv",
                    "run",
                    "--no-project",
                    runtime_url,
                    "install",
                    "--repository",
                    str(source),
                    "--harness",
                    harness,
                ]

                completed = subprocess.run(
                    command,
                    cwd=target,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    env=environment,
                    timeout=240,
                )
                self.assertEqual(completed.returncode, 1, completed.stderr)
                result = json.loads(completed.stdout)
                self.assertFalse(result["success"])
                self.assertIn("GitHub repository", result["error"])
                self.assertFalse((target / ".syspilot").exists())
                harness_root = ".github" if harness == "vscode" else ".opencode"
                self.assertFalse((target / harness_root).exists())
                self.assertFalse((target / ".venv").exists())
                self.assertFalse((target / "docs/_build").exists())
                self.assertEqual(list(target.rglob("__pycache__")), [])

        self.assertEqual(set(checkpoint_root.glob("*.json")), checkpoints_before)

    def test_direct_uv_cli_rejects_local_source_before_mutation(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            source = base / "source"
            target = base / "target"
            shutil.copytree(ROOT / "syspilot", source / "syspilot")
            init_git(source)
            git(source, "add", ".")
            git(source, "commit", "-m", "fixture source")
            target.mkdir()
            (target / ".opencode").mkdir()
            init_git(target)
            (target / "README.md").write_text("fixture\n", encoding="utf-8")
            git(target, "add", ".")
            git(target, "commit", "-m", "fixture target")
            environment = os.environ.copy()
            environment.pop("VIRTUAL_ENV", None)

            command = [
                "uv",
                "run",
                "--no-project",
                "syspilot/installer.py",
                "install",
                "--repository",
                str(source),
                "--branch",
                "main",
                "--target",
                str(target),
                "--harness",
                "opencode",
            ]

            completed = subprocess.run(
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=environment,
                timeout=180,
            )

            self.assertEqual(completed.returncode, 1, completed.stderr)
            result = json.loads(completed.stdout)
            self.assertFalse(result["success"])
            self.assertIn("GitHub repository", result["error"])
            self.assertFalse((target / ".syspilot").exists())
            self.assertFalse((target / ".venv").exists())
            self.assertFalse((target / "docs/_build").exists())


if __name__ == "__main__":
    unittest.main()