#!/usr/bin/env python3
"""Report Impact-discovered typed edges and unresolved targets."""

import argparse
import importlib.util
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[4]
NEEDS_ID_DIR = PROJECT_ROOT / "docs" / "_build" / "html" / "needs_id"
IMPACT_SCRIPT = PROJECT_ROOT / ".github" / "skills" / "syspilot.impact-python" / "scripts" / "get_need_links.py"


def load_impact_module():
    spec = importlib.util.spec_from_file_location("syspilot_impact", IMPACT_SCRIPT)
    if spec is None or spec.loader is None:
        raise ValueError(f"Cannot load Impact discovery from {IMPACT_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def analyze(need_id: str, depth: int, direction: str, ontology_path: Path | None, needs_dir: Path) -> dict:
    impact = load_impact_module()
    if ontology_path is None:
        ontology_path = impact.resolve_ontology_path()
    link_options = impact.load_link_options(ontology_path)
    root = impact.get_need(need_id, needs_dir)
    if not root:
        raise ValueError(f"Need {need_id} not found")
    edges = impact.trace_typed_edges(need_id, needs_dir, link_options, depth, direction)
    object_ids = {need_id}
    for edge in edges:
        object_ids.update((edge["source"], edge["target"]))
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
        assessed_edges.append(assessed)
        if not assessed["resolved"]:
            findings.append({"kind": "unresolved-target", "edge": edge})

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
    parser.add_argument("--ontology", type=Path, help="Default: needs_from_toml in docs/conf.py")
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