#!/usr/bin/env python3
"""Evaluate Impact-discovered typed edges against active ontology rules."""

import argparse
import importlib.util
import json
import sys
import tomllib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[4]
ONTOLOGY_PATH = PROJECT_ROOT / ".syspilot" / "ontology.toml"
NEEDS_ID_DIR = PROJECT_ROOT / "docs" / "_build" / "html" / "needs_id"
IMPACT_SCRIPT = PROJECT_ROOT / ".github" / "skills" / "syspilot.impact-python" / "scripts" / "get_need_links.py"


def load_impact_module():
    spec = importlib.util.spec_from_file_location("syspilot_impact", IMPACT_SCRIPT)
    if spec is None or spec.loader is None:
        raise ValueError(f"Cannot load Impact discovery from {IMPACT_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_rules(ontology_path: Path) -> list[dict]:
    try:
        with ontology_path.open("rb") as ontology_file:
            ontology = tomllib.load(ontology_file)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"Cannot read ontology {ontology_path}: {error}") from error
    rules = ontology.get("syspilot", {}).get("type_links")
    if not isinstance(rules, list):
        raise ValueError(f"Invalid ontology {ontology_path}: syspilot.type_links is missing")
    for rule in rules:
        if not isinstance(rule, dict) or not all(isinstance(rule.get(key), str) for key in ("from", "to", "rel")):
            raise ValueError(f"Invalid ontology {ontology_path}: malformed type link")
    return rules


def analyze(need_id: str, depth: int, direction: str, ontology_path: Path, needs_dir: Path) -> dict:
    impact = load_impact_module()
    link_options = impact.load_link_options(ontology_path)
    rules = load_rules(ontology_path)
    root = impact.get_need(need_id, needs_dir)
    if not root:
        raise ValueError(f"Need {need_id} not found")
    edges = impact.trace_typed_edges(need_id, needs_dir, link_options, depth, direction)
    object_ids = {need_id}
    object_depths = {need_id: 0}
    for edge in edges:
        object_ids.update((edge["source"], edge["target"]))
        neighbor_id = edge["source"] if edge["direction"] == "in" else edge["target"]
        object_depths[neighbor_id] = min(object_depths.get(neighbor_id, edge["depth"]), edge["depth"])
    objects = {object_id: impact.get_need(object_id, needs_dir) for object_id in sorted(object_ids)}

    findings = []
    assessed_edges = []
    for edge in edges:
        source = objects[edge["source"]]
        target = objects[edge["target"]]
        assessed = dict(edge)
        assessed["source_type"] = source.get("type") if source else None
        assessed["target_type"] = target.get("type") if target else None
        assessed["resolved"] = source is not None and target is not None
        assessed["permitted"] = assessed["resolved"] and any(
            rule["from"] == assessed["source_type"]
            and rule["to"] == assessed["target_type"]
            and rule["rel"] == edge["option"]
            for rule in rules
        )
        assessed_edges.append(assessed)
        if not assessed["resolved"]:
            findings.append({"kind": "unresolved-target", "edge": edge})
        elif not assessed["permitted"]:
            findings.append({"kind": "undeclared-relationship", "edge": edge})

    for object_id, need in objects.items():
        if not need or object_depths.get(object_id, depth) >= depth:
            continue
        object_type = need.get("type")
        expected = [rule for rule in rules if rule["from"] == object_type or rule["to"] == object_type]
        incident = [edge for edge in assessed_edges if edge["source"] == object_id or edge["target"] == object_id]
        if expected and not incident:
            findings.append({"kind": "orphan", "object": object_id})

    return {
        "object": need_id,
        "depth": depth,
        "direction": direction,
        "neighborhood": sorted(object_ids),
        "edges": assessed_edges,
        "findings": findings,
        "limitations": ["semantic-content-review-required"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("need_id")
    parser.add_argument("--depth", type=int, required=True)
    parser.add_argument("--direction", choices=["in", "out", "both"], default="both")
    parser.add_argument("--ontology", type=Path, default=ONTOLOGY_PATH)
    parser.add_argument("--needs-dir", type=Path, default=NEEDS_ID_DIR)
    args = parser.parse_args()
    if args.depth < 1:
        parser.error("--depth must be at least 1")
    try:
        result = analyze(args.need_id, args.depth, args.direction, args.ontology, args.needs_dir)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(2) from error
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()