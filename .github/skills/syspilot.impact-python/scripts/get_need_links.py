#!/usr/bin/env python3
"""
Sphinx-Needs Link Discovery Script

Simple script to query Sphinx-Needs elements and their links.
Reads from _build/html/needs_id/*.json after sphinx-build.

For commercial/fast solution with live parsing, see ubiTrace from Useblocks.

Usage:
    python .github/skills/syspilot.impact-python/scripts/get_need_links.py <NEED_ID> [--depth N] [--direction in|out|both]
    python .github/skills/syspilot.impact-python/scripts/get_need_links.py SYSPILOT_US_CORE_SPEC_AS_CODE --depth 2
    python .github/skills/syspilot.impact-python/scripts/get_need_links.py SYSPILOT_REQ_CHG_ANALYSIS_AGENT --direction out

Links: SYSPILOT_SPEC_INST_FILE_OWNERSHIP
"""

import argparse
import json
import subprocess
import sys
import tomllib
from pathlib import Path

# Find docs directory relative to script location
# Script is at: .github/skills/syspilot.impact-python/scripts/get_need_links.py
# Project root is 4 levels up (scripts -> impact-python -> skills -> syspilot -> workspace root)
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
NEEDS_ID_DIR = DOCS_DIR / "_build" / "html" / "needs_id"
ONTOLOGY_PATH = PROJECT_ROOT / ".syspilot" / "ontology.toml"


def ensure_build(needs_dir: Path) -> bool:
    """Run sphinx-build if needs_id directory is missing or empty.
    
    Returns True if build was needed and successful.
    """
    if needs_dir.exists() and any(needs_dir.glob("*.json")):
        return True
    
    print("Building docs (needs_id not found)...", file=sys.stderr)
    
    # Try uv first, fallback to direct sphinx-build
    build_commands = [
        ["uv", "run", "sphinx-build", "-b", "html", ".", "_build/html"],
        ["sphinx-build", "-b", "html", ".", "_build/html"],
    ]
    
    for cmd in build_commands:
        try:
            result = subprocess.run(
                cmd,
                cwd=DOCS_DIR,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("Build complete.", file=sys.stderr)
                return True
        except FileNotFoundError:
            continue
    
    print("ERROR: Could not run sphinx-build", file=sys.stderr)
    return False


def load_link_options(ontology_path: Path) -> list[str]:
    """Load all configured extra-link option names from the active ontology."""
    try:
        with ontology_path.open("rb") as ontology_file:
            ontology = tomllib.load(ontology_file)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"Cannot read ontology {ontology_path}: {error}") from error

    needs = ontology.get("needs")
    if not isinstance(needs, dict):
        raise ValueError(f"Invalid ontology {ontology_path}: [needs] table is missing")

    extra_links = needs.get("extra_links", [])
    if not isinstance(extra_links, list):
        raise ValueError(
            f"Invalid ontology {ontology_path}: [needs] extra_links must be a list"
        )

    options = []
    for link in extra_links:
        option = link.get("option") if isinstance(link, dict) else None
        if not isinstance(option, str) or not option:
            raise ValueError(
                f"Invalid ontology {ontology_path}: every extra link needs an option"
            )
        options.append(option)
    return options


def get_need(need_id: str, needs_dir: Path) -> dict | None:
    """Get a single need by ID from its JSON file."""
    json_file = needs_dir / f"{need_id}.json"
    
    if not json_file.exists():
        return None
    
    with open(json_file, encoding="utf-8") as f:
        data = json.load(f)
    
    # Extract the need from the nested structure
    # Structure: {versions: {"": {needs: {NEED_ID: {...}}}}}
    versions = data.get("versions", {})
    for version_data in versions.values():
        needs = version_data.get("needs", {})
        if need_id in needs:
            return needs[need_id]
    
    return None


def linked_ids(need: dict, link_options: list[str], direction: str) -> list[str]:
    """Return de-duplicated linked IDs for standard and configured link fields."""
    suffix = "_back" if direction == "in" else ""
    fields = [f"links{suffix}", *(f"{option}{suffix}" for option in link_options)]
    return sorted(
        {
            linked_id
            for field in fields
            for linked_id in need.get(field, [])
            if isinstance(linked_id, str)
        }
    )


def get_links(
    need_id: str,
    needs_dir: Path,
    link_options: list[str],
    direction: str = "both",
) -> dict:
    """Get outgoing and/or incoming links for a need.
    
    Args:
        need_id: The Sphinx-Needs ID (e.g., "SYSPILOT_REQ_EVT_001")
        direction: "in" (incoming), "out" (outgoing), or "both"
    
    Returns:
        Dict with id, type, title, status, and requested links
    """
    need = get_need(need_id, needs_dir)
    
    if not need:
        return {"error": f"Need {need_id} not found"}
    
    result = {
        "id": need_id,
        "type": need.get("type"),
        "type_name": need.get("type_name"),
        "title": need.get("title"),
        "status": need.get("status"),
        "docname": need.get("docname"),
    }
    
    if direction in ("out", "both"):
        result["links_outgoing"] = linked_ids(need, link_options, "out")
    
    if direction in ("in", "both"):
        result["links_incoming"] = linked_ids(need, link_options, "in")
    
    return result


def trace_impact(
    need_id: str,
    needs_dir: Path,
    link_options: list[str],
    depth: int = 2,
    direction: str = "out",
) -> dict:
    """Trace impact to given depth.
    
    Args:
        need_id: Starting point
        depth: How many levels to traverse (default 2)
        direction: "out" (follow links), "in" (follow links_back), "both"
    
    Returns:
        Nested dict showing impact tree
    """
    minimum_depth_by_id: dict[str, int] = {}
    
    def trace(nid: str, current_depth: int) -> dict:
        previous_depth = minimum_depth_by_id.get(nid)
        if current_depth > depth or (
            previous_depth is not None and previous_depth <= current_depth
        ):
            return {"id": nid, "truncated": True}
        
        minimum_depth_by_id[nid] = current_depth
        need = get_need(nid, needs_dir)
        
        if not need:
            return {"id": nid, "error": "not found"}
        
        result = {
            "id": nid,
            "type": need.get("type"),
            "title": need.get("title"),
            "status": need.get("status"),
        }
        
        if current_depth < depth:
            # Get children based on direction
            if direction in ("out", "both"):
                children_out = linked_ids(need, link_options, "out")
                if children_out:
                    result["links"] = [
                        trace(c, current_depth + 1) for c in children_out
                    ]
            
            if direction in ("in", "both"):
                children_in = linked_ids(need, link_options, "in")
                if children_in:
                    result["linked_from"] = [
                        trace(c, current_depth + 1) for c in children_in
                    ]
        
        return result
    
    return trace(need_id, 0)


def get_all_linked_ids(
    need_id: str,
    needs_dir: Path,
    link_options: list[str],
    depth: int = 2,
    direction: str = "out",
) -> list[str]:
    """Get flat list of all linked IDs within depth.
    
    Useful for quickly getting all impacted elements.
    """
    result = trace_impact(need_id, needs_dir, link_options, depth, direction)
    
    ids = set()
    
    def extract_ids(node: dict):
        if "id" in node and not node.get("truncated"):
            ids.add(node["id"])
        for child in node.get("links", []):
            extract_ids(child)
        for child in node.get("linked_from", []):
            extract_ids(child)
    
    extract_ids(result)
    ids.discard(need_id)  # Remove the starting point
    
    return sorted(ids)


def main():
    parser = argparse.ArgumentParser(
        description="Query Sphinx-Needs elements and their links"
    )
    parser.add_argument("need_id", help="The Need ID to query (e.g., SYSPILOT_US_CORE_SPEC_AS_CODE)")
    parser.add_argument(
        "--depth", "-d", type=int, default=2,
        help="How many levels to traverse (default: 2)"
    )
    parser.add_argument(
        "--direction", "-r", choices=["in", "out", "both"], default="both",
        help="Link direction: in (incoming), out (outgoing), both (default)"
    )
    parser.add_argument(
        "--flat", "-f", action="store_true",
        help="Return flat list of IDs instead of tree"
    )
    parser.add_argument(
        "--simple", "-s", action="store_true",
        help="Simple output: just links for the given ID"
    )
    parser.add_argument(
        "--ontology", type=Path, default=ONTOLOGY_PATH,
        help="Active ontology TOML path (default: .syspilot/ontology.toml)"
    )
    parser.add_argument(
        "--needs-dir", type=Path, default=NEEDS_ID_DIR,
        help="Built per-ID Needs JSON directory"
    )
    parser.add_argument(
        "--no-build", action="store_true",
        help="Do not attempt a documentation build when Needs data is missing"
    )
    
    args = parser.parse_args()
    
    try:
        link_options = load_link_options(args.ontology)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(2)
    
    if not args.needs_dir.exists() or not any(args.needs_dir.glob("*.json")):
        build_succeeded = not args.no_build and ensure_build(args.needs_dir)
        data_available = args.needs_dir.exists() and any(
            args.needs_dir.glob("*.json")
        )
        if not build_succeeded or not data_available:
            print(
                f"ERROR: Needs data not available at {args.needs_dir}",
                file=sys.stderr,
            )
            sys.exit(3)

    if get_need(args.need_id, args.needs_dir) is None:
        print(f"ERROR: Need {args.need_id} not found", file=sys.stderr)
        sys.exit(4)
    
    if args.simple:
        result = get_links(
            args.need_id, args.needs_dir, link_options, args.direction
        )
    elif args.flat:
        result = get_all_linked_ids(
            args.need_id,
            args.needs_dir,
            link_options,
            args.depth,
            args.direction,
        )
    else:
        result = trace_impact(
            args.need_id,
            args.needs_dir,
            link_options,
            args.depth,
            args.direction,
        )
    
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
