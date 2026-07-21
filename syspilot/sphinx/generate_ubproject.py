#!/usr/bin/env python3
"""Generate docs/ubproject.toml from .syspilot/ontology.toml.

Strips all TOML sections except [needs] and its sub-tables/arrays,
producing the sphinx-needs projection used by conf.py.

Usage:
    python syspilot/sphinx/generate_ubproject.py           # generate
    python syspilot/sphinx/generate_ubproject.py --compare  # check freshness

Requires Python 3.11+ (tomllib).
"""

from __future__ import annotations

import argparse
import difflib
import sys
import textwrap
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    sys.exit("Error: Python 3.11+ is required (tomllib not found).")


HEADER = (
    "# Generated from .syspilot/ontology.toml — do not edit directly\n"
    "# Run: python syspilot/sphinx/generate_ubproject.py\n"
)

# Resolve paths relative to the repository root (two levels up from this script)
REPO_ROOT = Path(__file__).resolve().parents[2]
ONTOLOGY_PATH = REPO_ROOT / ".syspilot" / "ontology.toml"
UBPROJECT_PATH = REPO_ROOT / "docs" / "ubproject.toml"


def _format_value(value: object) -> str:
    """Format a single TOML value as a string."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list) and all(isinstance(v, str) for v in value):
        items = ", ".join(f'"{v}"' for v in value)
        return f"[{items}]"
    return repr(value)


def _write_table(lines: list[str], table: dict, prefix: str = "") -> None:
    """Recursively serialise a TOML table into *lines*."""
    # Separate scalars/simple-lists from sub-tables and arrays-of-tables
    scalars: list[tuple[str, object]] = []
    sub_tables: list[tuple[str, dict]] = []
    arrays_of_tables: list[tuple[str, list[dict]]] = []

    for key, val in table.items():
        if isinstance(val, dict):
            sub_tables.append((key, val))
        elif isinstance(val, list) and val and isinstance(val[0], dict):
            arrays_of_tables.append((key, val))
        else:
            scalars.append((key, val))

    for key, val in scalars:
        lines.append(f"{key} = {_format_value(val)}")

    for key, sub in sub_tables:
        full_key = f"{prefix}.{key}" if prefix else key
        lines.append("")
        lines.append(f"[{full_key}]")
        _write_table(lines, sub, full_key)

    for key, arr in arrays_of_tables:
        full_key = f"{prefix}.{key}" if prefix else key
        for entry in arr:
            lines.append("")
            lines.append(f"[[{full_key}]]")
            _write_table(lines, entry, full_key)


def generate(ontology: dict) -> str:
    """Return the ubproject.toml content string from the parsed ontology."""
    if "needs" not in ontology:
        sys.exit("Error: [needs] section not found in ontology.toml.")

    lines: list[str] = ["[needs]"]
    _write_table(lines, ontology["needs"], "needs")
    lines.append("")  # trailing newline

    return HEADER + "\n" + "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate docs/ubproject.toml from .syspilot/ontology.toml"
    )
    parser.add_argument(
        "--compare",
        action="store_true",
        help="Compare generated content to committed file; exit 1 if stale.",
    )
    args = parser.parse_args()

    if not ONTOLOGY_PATH.exists():
        sys.exit(f"Error: {ONTOLOGY_PATH} not found.")

    with ONTOLOGY_PATH.open("rb") as f:
        ontology = tomllib.load(f)

    content = generate(ontology)

    if args.compare:
        if not UBPROJECT_PATH.exists():
            print("STALE: docs/ubproject.toml does not exist.")
            sys.exit(1)
        existing = UBPROJECT_PATH.read_text(encoding="utf-8")
        if existing == content:
            print("OK: docs/ubproject.toml is up to date")
            sys.exit(0)
        else:
            diff = difflib.unified_diff(
                existing.splitlines(keepends=True),
                content.splitlines(keepends=True),
                fromfile="docs/ubproject.toml (committed)",
                tofile="docs/ubproject.toml (generated)",
            )
            print("STALE: docs/ubproject.toml differs from .syspilot/ontology.toml")
            sys.stdout.writelines(diff)
            sys.exit(1)
    else:
        UBPROJECT_PATH.write_text(content, encoding="utf-8")
        print("Generated docs/ubproject.toml from .syspilot/ontology.toml")


if __name__ == "__main__":
    main()
