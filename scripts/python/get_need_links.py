#!/usr/bin/env python3
"""
Sphinx-Needs Link Discovery Script

Simple script to query Sphinx-Needs elements and their links.
Reads from _build/html/needs_id/*.json after sphinx-build.

For commercial/fast solution with live parsing, see ubiTrace from Useblocks.

Usage:
    python .syspilot/scripts/python/get_need_links.py <NEED_ID> [--depth N] [--direction in|out|both]
    python .syspilot/scripts/python/get_need_links.py US_CORE_SPEC_AS_CODE --depth 2
    python .syspilot/scripts/python/get_need_links.py REQ_CHG_ANALYSIS_AGENT --direction out

Links: SPEC_INST_FILE_OWNERSHIP
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

# Find docs directory relative to script location
# Script is at: scripts/python/get_need_links.py
# Project root is 2 levels up
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
NEEDS_ID_DIR = DOCS_DIR / "_build" / "html" / "needs_id"


def ensure_build() -> bool:
    """Run sphinx-build if needs_id directory is missing or empty.
    
    Returns True if build was needed and successful.
    """
    if NEEDS_ID_DIR.exists() and any(NEEDS_ID_DIR.glob("*.json")):
        return False
    
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


def get_need(need_id: str) -> dict | None:
    """Get a single need by ID from its JSON file."""
    json_file = NEEDS_ID_DIR / f"{need_id}.json"
    
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


def get_links(need_id: str, direction: str = "both") -> dict:
    """Get outgoing and/or incoming links for a need.
    
    Args:
        need_id: The Sphinx-Needs ID (e.g., "REQ_EVT_001")
        direction: "in" (incoming), "out" (outgoing), or "both"
    
    Returns:
        Dict with id, type, title, status, and requested links
    """
    need = get_need(need_id)
    
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
        result["links_outgoing"] = need.get("links", [])
    
    if direction in ("in", "both"):
        result["links_incoming"] = need.get("links_back", [])
    
    return result


def trace_impact(need_id: str, depth: int = 2, direction: str = "out") -> dict:
    """Trace impact to given depth.
    
    Args:
        need_id: Starting point
        depth: How many levels to traverse (default 2)
        direction: "out" (follow links), "in" (follow links_back), "both"
    
    Returns:
        Nested dict showing impact tree
    """
    visited = set()
    
    def trace(nid: str, current_depth: int) -> dict:
        if current_depth > depth or nid in visited:
            return {"id": nid, "truncated": True}
        
        visited.add(nid)
        need = get_need(nid)
        
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
                children_out = need.get("links", [])
                if children_out:
                    result["links"] = [
                        trace(c, current_depth + 1) for c in children_out
                    ]
            
            if direction in ("in", "both"):
                children_in = need.get("links_back", [])
                if children_in:
                    result["linked_from"] = [
                        trace(c, current_depth + 1) for c in children_in
                    ]
        
        return result
    
    return trace(need_id, 0)


def get_all_linked_ids(need_id: str, depth: int = 2, direction: str = "out") -> list[str]:
    """Get flat list of all linked IDs within depth.
    
    Useful for quickly getting all impacted elements.
    """
    result = trace_impact(need_id, depth, direction)
    
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
    parser.add_argument("need_id", help="The Need ID to query (e.g., US_CORE_SPEC_AS_CODE)")
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
    
    args = parser.parse_args()
    
    # Ensure docs are built
    ensure_build()
    
    if not NEEDS_ID_DIR.exists():
        print(json.dumps({"error": "needs_id directory not found after build"}))
        sys.exit(1)
    
    if args.simple:
        result = get_links(args.need_id, args.direction)
    elif args.flat:
        result = get_all_linked_ids(args.need_id, args.depth, args.direction)
    else:
        result = trace_impact(args.need_id, args.depth, args.direction)
    
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
