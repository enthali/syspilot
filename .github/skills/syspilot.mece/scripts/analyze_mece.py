#!/usr/bin/env python3
"""Discover comparable peers and report deterministic MECE evidence."""

import argparse
import json
import sys
import tomllib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[4]
ONTOLOGY_PATH = PROJECT_ROOT / ".syspilot" / "ontology.toml"
NEEDS_ID_DIR = PROJECT_ROOT / "docs" / "_build" / "html" / "needs_id"


def load_types(ontology_path: Path) -> set[str]:
    try:
        with ontology_path.open("rb") as ontology_file:
            ontology = tomllib.load(ontology_file)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"Cannot read ontology {ontology_path}: {error}") from error
    entries = ontology.get("needs", {}).get("types")
    if not isinstance(entries, list):
        raise ValueError(f"Invalid ontology {ontology_path}: needs.types is missing")
    types = {
        entry.get("directive")
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("directive"), str)
    }
    if not types:
        raise ValueError(f"Invalid ontology {ontology_path}: no Need types declared")
    return types


def load_needs(needs_dir: Path) -> dict[str, dict]:
    if not needs_dir.is_dir():
        raise ValueError(f"Needs data not available at {needs_dir}")
    needs = {}
    try:
        for json_path in sorted(needs_dir.glob("*.json")):
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            for version in payload.get("versions", {}).values():
                needs.update(version.get("needs", {}))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Cannot read Needs data at {needs_dir}: {error}") from error
    if not needs:
        raise ValueError(f"Needs data not available at {needs_dir}")
    return needs


def analyze(need_id: str, scope: str, types: set[str], needs: dict[str, dict]) -> dict:
    subject = needs.get(need_id)
    if not subject:
        raise ValueError(f"Need {need_id} not found")
    subject_type = subject.get("type")
    if subject_type not in types:
        raise ValueError(f"Need {need_id} has undeclared type {subject_type!r}")

    peers = [
        need
        for peer_id, need in needs.items()
        if peer_id != need_id
        and need.get("type") == subject_type
        and (scope == "all-type" or need.get("docname") == subject.get("docname"))
    ]
    peers.sort(key=lambda need: need["id"])
    analyzed = [subject, *peers]
    findings = []

    claims: dict[str, list[tuple[str, object]]] = {}
    for need in analyzed:
        for key, value in need.get("quality_claims", {}).items():
            claims.setdefault(key, []).append((need["id"], value))
    for key, entries in sorted(claims.items()):
        values = {json.dumps(value, sort_keys=True) for _, value in entries}
        if len(entries) > 1 and len(values) == 1:
            findings.append({"kind": "overlap", "key": key, "objects": sorted(item[0] for item in entries)})
        elif len(values) > 1:
            findings.append({"kind": "contradiction", "key": key, "objects": sorted(item[0] for item in entries)})

    expected = subject.get("expected_coverage", [])
    if isinstance(expected, list):
        for key in sorted(set(expected) - set(claims)):
            findings.append({"kind": "missing-coverage", "key": key, "objects": []})

    responsibilities: dict[str, list[str]] = {}
    for need in analyzed:
        responsibility = need.get("responsibility")
        if isinstance(responsibility, str) and responsibility:
            responsibilities.setdefault(responsibility, []).append(need["id"])
    for responsibility, object_ids in sorted(responsibilities.items()):
        if len(object_ids) > 1:
            findings.append({"kind": "responsibility-collision", "key": responsibility, "objects": sorted(object_ids)})

    limitations = ["semantic-content-review-required"]
    if not peers:
        limitations.append("no-comparable-peers-discovered")
    if not claims:
        limitations.append("structured-coverage-data-unavailable")

    return {
        "object": need_id,
        "type": subject_type,
        "scope": scope,
        "peers": [peer["id"] for peer in peers],
        "examined": [need["id"] for need in analyzed],
        "findings": findings,
        "limitations": limitations,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("need_id")
    parser.add_argument("--scope", choices=["same-document", "all-type"], required=True)
    parser.add_argument("--ontology", type=Path, default=ONTOLOGY_PATH)
    parser.add_argument("--needs-dir", type=Path, default=NEEDS_ID_DIR)
    args = parser.parse_args()
    try:
        result = analyze(args.need_id, args.scope, load_types(args.ontology), load_needs(args.needs_dir))
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(2) from error
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()