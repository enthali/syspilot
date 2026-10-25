import argparse
import re
import sys
from pathlib import Path


DEFAULT_NOTES = Path(__file__).resolve().parents[1] / "docs" / "releasenotes.md"


def extract_release_notes(tag, notes_path):
    if re.fullmatch(r"v(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", tag) is None:
        raise ValueError(f"Invalid release tag: {tag}")

    lines = Path(notes_path).read_text(encoding="utf-8").splitlines()
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


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check a release tag and its unique release-notes heading without writing files."
    )
    parser.add_argument("tag", help="Release tag in vMAJOR.MINOR.PATCH form")
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES, help="Release-notes file (UTF-8)")
    args = parser.parse_args(argv)
    try:
        extract_release_notes(args.tag, args.notes)
    except (ValueError, OSError, UnicodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(f"PASS: {args.tag} has exactly one release-note heading in {args.notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())