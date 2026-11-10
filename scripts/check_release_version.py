import argparse
import re
import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_NOTES = ROOT / "docs" / "releasenotes.md"
DEFAULT_CONF = ROOT / "docs" / "conf.py"
VERSION = r"v(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"


def _lines(notes_path):
    return Path(notes_path).read_text(encoding="utf-8").splitlines()


def newest_release_in_text(text):
    """Return the tag named by the first version heading of release-notes text, or None."""
    heading = re.compile(rf"^## ({VERSION})(?:\s+-\s+.+)?$")
    for line in text.splitlines():
        match = heading.fullmatch(line)
        if match:
            return match.group(1)
    return None


def newest_release(notes_path):
    """Return the tag named by the first version heading of the release notes."""
    newest = newest_release_in_text(Path(notes_path).read_text(encoding="utf-8"))
    if newest is None:
        raise ValueError(f"No version heading found in {notes_path}")
    return newest


def extract_release_notes(tag, notes_path):
    if re.fullmatch(VERSION, tag) is None:
        raise ValueError(f"Invalid release tag: {tag}")

    lines = _lines(notes_path)
    heading = re.compile(rf"^## {re.escape(tag)}(?:\s+-\s+.+)?$")
    starts = [index for index, line in enumerate(lines) if heading.fullmatch(line)]
    if len(starts) != 1:
        raise ValueError(
            f"Expected exactly one release-note heading for {tag}, found {len(starts)}"
        )

    start = starts[0]
    end = next(
        (index for index in range(start + 1, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    return "\n".join(lines[start:end]).rstrip() + "\n"


def check_release(tag, notes_path, conf_path):
    """Return the release text of the tag, or raise ValueError naming the failing condition."""
    text = extract_release_notes(tag, notes_path)
    newest = newest_release(notes_path)
    if tag != newest:
        raise ValueError(f"Release {tag} is not the newest release-notes heading ({newest})")
    documented = runpy.run_path(str(conf_path)).get("release")
    if documented != tag[1:]:
        raise ValueError(
            f"Documentation release {documented!r} in {conf_path} differs from {tag[1:]!r}"
        )
    return text


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Check a release tag against the release notes and the documentation release. "
            "Writes nothing unless --write-notes is given."
        )
    )
    parser.add_argument("tag", help="Release tag in vMAJOR.MINOR.PATCH form")
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES, help="Release-notes file (UTF-8)")
    parser.add_argument("--conf", type=Path, default=DEFAULT_CONF, help="Documentation configuration file")
    parser.add_argument(
        "--write-notes", type=Path, default=None,
        help="After a passing check, write the release text of the tag to this file",
    )
    args = parser.parse_args(argv)
    try:
        text = check_release(args.tag, args.notes, args.conf)
        if args.write_notes is not None:
            args.write_notes.write_text(text, encoding="utf-8")
    except (ValueError, OSError, UnicodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(f"PASS: {args.tag} is the newest release-notes heading in {args.notes} and matches {args.conf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())