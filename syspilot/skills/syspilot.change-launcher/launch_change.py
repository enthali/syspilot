#!/usr/bin/env python3
"""Automate CR scaffolding: branch, template copy, header pre-fill, commit.

Usage:
    python launch_change.py --name <change-name> --author <author> --mode <mode>

Requires Python 3.11+.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from datetime import date, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
TEMPLATE = REPO_ROOT / "syspilot" / "templates" / "change-document.md"
CHANGES_DIR = REPO_ROOT / "docs" / "changes"


def _run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT, **kwargs)


def _current_branch() -> str:
    r = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return r.stdout.strip()


def _branch_exists(name: str) -> bool:
    r = _run(["git", "rev-parse", "--verify", f"refs/heads/{name}"])
    return r.returncode == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a Change Document")
    parser.add_argument("--name", required=True, help="Change name (kebab-case)")
    parser.add_argument("--author", required=True, help="Author string for header")
    parser.add_argument(
        "--mode",
        required=True,
        choices=["autonomous", "user-guided"],
        help="Operation mode",
    )
    args = parser.parse_args()

    name: str = args.name
    author: str = args.author
    mode: str = args.mode
    branch = f"feature/{name}"
    target = CHANGES_DIR / f"{name}.md"

    # 1. Validate preconditions
    if _current_branch() != "development":
        print("ERROR: Must be on 'development' branch.", file=sys.stderr)
        sys.exit(1)

    if not TEMPLATE.exists():
        print(f"ERROR: Template not found: {TEMPLATE}", file=sys.stderr)
        sys.exit(1)

    if target.exists():
        print(f"ERROR: Change Document already exists: {target}", file=sys.stderr)
        sys.exit(1)

    # 2. Create or switch to branch
    if _branch_exists(branch):
        print(f"WARNING: Branch '{branch}' already exists — switching to it.")
        _run(["git", "checkout", branch])
    else:
        _run(["git", "checkout", "-b", branch])

    # 3. Copy template
    CHANGES_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TEMPLATE, target)

    # 4. Pre-fill header fields
    content = target.read_text(encoding="utf-8")
    today = date.today().isoformat()

    content = content.replace("{NAME}", name)
    content = re.sub(
        r"draft \| in-progress \| review \| approved \| merged",
        "in-progress",
        content,
        count=1,
    )
    content = re.sub(
        r"user-guided \(default\) \| autonomous",
        mode,
        content,
        count=1,
    )
    content = content.replace("{DATE}", today)
    content = content.replace("{AUTHOR(S)}", author)

    target.write_text(content, encoding="utf-8")

    # 5. Commit
    _run(["git", "add", str(target.relative_to(REPO_ROOT))])
    _run(
        [
            "git",
            "commit",
            "-m",
            f'pm(cr): scaffold Change Document for {name}',
        ]
    )

    print(f"Created Change Document: {target.relative_to(REPO_ROOT)}")
    print(f"Branch: {branch}")


if __name__ == "__main__":
    main()
