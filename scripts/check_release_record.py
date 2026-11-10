import argparse
import re
import runpy
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = runpy.run_path(str(ROOT / "scripts" / "check_release_version.py"))
TAG_FORM = re.compile(CHECKER["VERSION"])
ARTIFACT_SECTION = "Artifacts, Ownership And Process Gates"
PROTECTED_SECTIONS = ("Objective And Scope", "Version", "Change Inventory")
PROTECTED_ROWS = ("Objective and scope", "Release start", "Version")
PROTECTED_COLUMNS = ("Artifact or gate", "Included", "Owner")


class Failure(Exception):
    """A failing condition; the message begins with the condition."""


def git(repo, *args, check=True):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    if check and result.returncode != 0:
        raise Failure(result.stderr.decode("utf-8", "replace").strip() or "git failed")
    return result


def blob(repo, commit, path):
    result = git(repo, "show", f"{commit}:{path}", check=False)
    if result.returncode != 0:
        return None
    return result.stdout.decode("utf-8").replace("\r\n", "\n")


def resolve(repo, name):
    result = git(repo, "rev-parse", "--verify", "--quiet", f"{name}^{{commit}}", check=False)
    if result.returncode != 0:
        raise Failure(f"{name} is not a commit of the repository")
    return result.stdout.decode().strip()


def section(text, name, where):
    lines = text.splitlines()
    try:
        start = lines.index(f"## {name}")
    except ValueError:
        raise Failure(f"template heading not found: '## {name}' in the record at {where}") from None
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return [line.rstrip() for line in lines[start:end]]


def trimmed(lines):
    while lines and not lines[-1]:
        lines = lines[:-1]
    return lines


def table(lines, where, what):
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines if line.startswith("|")]
    rows = [row for row in rows if not all(re.fullmatch(r":?-+:?", cell) for cell in row)]
    if len(rows) < 2:
        raise Failure(f"template table row not found: {what} in the record at {where}")
    header, body = rows[0], rows[1:]
    return header, body


def protected_content(text, where):
    content = {}
    first = next((line.rstrip() for line in text.splitlines() if line.startswith("- **Operation Mode")), None)
    if first is None:
        raise Failure(f"template row not found: the Operation Mode line in the record at {where}")
    content["Operation Mode"] = first
    for name in PROTECTED_SECTIONS:
        content[f"section {name}"] = trimmed(section(text, name, where))

    header, body = table(section(text, ARTIFACT_SECTION, where), where, "the artifact table")
    columns = []
    for name in PROTECTED_COLUMNS:
        if name not in header:
            raise Failure(f"template column not found: '{name}' in the artifact table of the record at {where}")
        columns.append(header.index(name))
    content["artifact table columns Artifact or gate, Included, Owner"] = [
        [row[i] if i < len(row) else None for i in columns] for row in body
    ]
    for name in PROTECTED_ROWS:
        rows = [row for row in body if row and row[0] == name]
        if len(rows) != 1:
            raise Failure(f"template table row not found: '{name}' in the artifact table of the record at {where}")
        content[f"artifact row {name}"] = rows[0]

    commands = [line for line in section(text, "Preflight", where) if re.match(r"\d+\. ", line)]
    if not commands:
        raise Failure(f"template row not found: the preflight command list in the record at {where}")
    content["preflight command list"] = commands

    tag_line = next(
        (line for line in section(text, "Release Verification", where) if line.startswith("**Version and tag:**")),
        None,
    )
    if tag_line is None:
        raise Failure(f"template row not found: 'Version and tag' of Release Verification in the record at {where}")
    content["version and tag text of Release Verification"] = tag_line
    return content


TEMPLATE = "docs/Syspilot Contracts/release.md"
TEMPLATE_MARKER = "## Canonical Release Contract Template"


def template_headings(repo, commit):
    text = blob(repo, commit, TEMPLATE)
    if text is None:
        raise Failure(f"template not found at R: {TEMPLATE}")
    lines = text.splitlines()
    if TEMPLATE_MARKER not in lines:
        raise Failure(f"template heading not found: '{TEMPLATE_MARKER}' in {TEMPLATE} at R")
    inside = lines[lines.index(TEMPLATE_MARKER) + 1:]
    return [line[3:].strip() for line in inside if line.startswith("## ")]


def require_template_headings(repo, commit, text):
    """Every second-level heading of the template is present at R; presence only, not order or content."""
    present = {line[3:].strip() for line in text.splitlines() if line.startswith("## ")}
    for heading in template_headings(repo, commit):
        if heading not in present:
            raise Failure(f"template heading missing at R: '## {heading}'")


def record_version(text):
    lines = section(text, "Version", "R")
    line = next((line for line in lines if line.startswith("**Version:**")), None)
    if line is None:
        raise Failure("template row not found: the 'Version' row in the record at R")
    return line[len("**Version:**"):].strip().split(" ", 1)[0]


def check(repo, preflighted, release, tag):
    if TAG_FORM.fullmatch(tag) is None:
        raise Failure(f"invalid release tag: {tag}")
    record = f"docs/changes/release-{tag}.md"
    p, r = resolve(repo, preflighted), resolve(repo, release)

    if git(repo, "merge-base", "--is-ancestor", p, r, check=False).returncode != 0:
        raise Failure(f"P is not an ancestor of R: {p} is not an ancestor of {r}")

    text_r = blob(repo, r, record)
    if text_r is None:
        raise Failure(f"record absent at R: {record}")

    tokens = git(repo, "diff", "--raw", "-M", "--no-abbrev", "-z", p, r).stdout.decode("utf-8").split("\0")
    entries, index = [], 0
    while index < len(tokens) and tokens[index].startswith(":"):
        meta = tokens[index].split()
        paths = 2 if meta[4][:1] in "RC" else 1
        entries.append((meta, tokens[index + 1:index + 1 + paths]))
        index += 1 + paths
    for meta, paths in entries:
        old_mode, new_mode, status = meta[0].lstrip(":"), meta[1], meta[4]
        if status[:1] in "RC":
            raise Failure(f"rename in the difference from P to R: {' -> '.join(paths)}")
        if status[:1] == "D":
            raise Failure(f"deletion in the difference from P to R: {paths[0]}")
        if status[:1] == "T" or (status[:1] == "M" and old_mode != new_mode):
            raise Failure(f"mode change in the difference from P to R: {paths[0]} {old_mode} -> {new_mode}")
        if paths[0] != record:
            raise Failure(f"path other than the record in the difference from P to R: {paths[0]}")
    if len(entries) != 1:
        raise Failure(f"the difference from P to R is not exactly {record}: it has {len(entries)} changed paths")

    text_p = blob(repo, p, record)
    if text_p is None:
        raise Failure(f"record absent at P: {record}, so no protected content can be compared")
    if not any(p in line for line in text_r.splitlines() if line.startswith("|")):
        raise Failure(f"full commit of P missing from the record at R: {p}")

    require_template_headings(repo, r, text_r)
    before, after = protected_content(text_p, "P"), protected_content(text_r, "R")
    for block in before:
        if before[block] != after[block]:
            raise Failure(f"protected content changed: {block}")

    notes = blob(repo, r, "docs/releasenotes.md")
    if notes is None:
        raise Failure("Version row disagrees with the release-notes heading of R: docs/releasenotes.md is absent at R")
    newest = CHECKER["newest_release_in_text"](notes)
    version = record_version(text_r)
    if newest != f"v{version}" or newest != tag:
        raise Failure(
            f"Version row disagrees with the release-notes heading of R: the row says {version}, "
            f"the newest heading is {newest}, the tag is {tag}"
        )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Check that the release commit R differs from the preflighted commit P only in "
            "the release record, and not in its protected content. Reads commits with git; writes nothing."
        )
    )
    parser.add_argument("preflighted", help="Preflighted commit P")
    parser.add_argument("release", help="Release commit R")
    parser.add_argument("tag", help="Release tag in vMAJOR.MINOR.PATCH form")
    parser.add_argument("--repo", type=Path, default=ROOT, help="Repository to read (default: this one)")
    args = parser.parse_args(argv)
    try:
        check(args.repo, args.preflighted, args.release, args.tag)
    except (Failure, UnicodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(f"PASS: {args.release} differs from {args.preflighted} only in docs/changes/release-{args.tag}.md, protected content unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
