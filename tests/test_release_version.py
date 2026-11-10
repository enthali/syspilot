import ast
import os
import re
import runpy
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check_release_version.py"
EXTRACT = runpy.run_path(str(CHECKER))["extract_release_notes"]
LEGACY_CHECK = textwrap.dedent("""\
    import os
    import re
    from pathlib import Path

    tag = os.environ["GITHUB_REF_NAME"]
    match = re.fullmatch(
        r"v(?:0|[1-9]\\d*)\\."
        r"(?:0|[1-9]\\d*)\\."
        r"(?:0|[1-9]\\d*)",
        tag,
    )
    if match is None:
        raise SystemExit(f"Invalid release tag: {tag}")

    lines = Path("docs/releasenotes.md").read_text(encoding="utf-8").splitlines()
    heading = re.compile(rf"^## {re.escape(tag)}(?:\\s+-\\s+.+)?$")
    starts = [index for index, line in enumerate(lines) if heading.fullmatch(line)]
    if len(starts) != 1:
        raise SystemExit(
            f"Expected exactly one release-note heading for {tag}, found {len(starts)}"
        )

    start = starts[0]
    end = next(
        (index for index in range(start + 1, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    Path("release-notes-current.md").write_text(
        "\\n".join(lines[start:end]).rstrip() + "\\n",
        encoding="utf-8",
    )
""")


class ReleaseVersionTests(unittest.TestCase):
    def assert_equivalent(self, tag, content):
        """Extraction keeps the behaviour of the earlier inline workflow script."""
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            notes = root / "docs" / "releasenotes.md"
            notes.parent.mkdir()
            notes.write_bytes(content.encode("utf-8"))
            output = root / "release-notes-current.md"
            legacy = subprocess.run(
                [sys.executable, "-c", LEGACY_CHECK], cwd=root,
                env={**os.environ, "GITHUB_REF_NAME": tag},
                capture_output=True, text=True,
            )
            expected = output.read_text(encoding="utf-8") if output.exists() else None
            if legacy.returncode == 0:
                self.assertEqual(EXTRACT(tag, notes), expected)
            else:
                with self.assertRaises(ValueError) as raised:
                    EXTRACT(tag, notes)
                self.assertEqual(str(raised.exception).strip(), legacy.stderr.strip())

    def run_checker(self, tag, notes_text, conf_text, *extra):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            notes = root / "releasenotes.md"
            conf = root / "conf.py"
            notes.write_bytes(notes_text.encode("utf-8"))
            conf.write_text(conf_text, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(CHECKER), tag, "--notes", str(notes), "--conf", str(conf), *extra],
                cwd=root, capture_output=True, text=True,
            )
            written = sorted(path.name for path in root.iterdir())
            return result, written, notes.read_bytes(), root

    def test_workflow_runs_the_checker_and_not_a_copy_of_its_logic(self):
        workflow = yaml.safe_load((ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8"))
        step = next(
            step for step in workflow["jobs"]["validate"]["steps"]
            if step["name"] == "Validate tag and extract release notes"
        )
        self.assertIn("scripts/check_release_version.py", step["run"])
        self.assertNotIn("re.fullmatch", step["run"])
        self.assertNotIn("<<", step["run"])

    def test_all_real_release_headings_match_legacy(self):
        notes = (ROOT / "docs/releasenotes.md").read_text(encoding="utf-8")
        tags = re.findall(r"^## (v\S+)", notes, re.MULTILINE)
        self.assertTrue(tags)
        for tag in tags:
            with self.subTest(tag=tag):
                self.assert_equivalent(tag, notes)

    def test_bare_titled_headings_and_section_boundaries(self):
        for newline in ("\n", "\r\n"):
            for heading in ("## v1.2.3", "## v1.2.3 - A title", "## v1.2.3\t-\tA title"):
                for end in ("", "\n## v1.2.2 - Older\nOlder text\n"):
                    with self.subTest(newline=repr(newline), heading=heading, end=end):
                        notes = f"# Notes\n\n{heading}\n\nUnicode: caf\u00e9\n### Detail\nBody\n\n{end}"
                        self.assert_equivalent("v1.2.3", notes.replace("\n", newline))

    def test_malformed_tags_match_legacy_failure(self):
        for tag in ("1.2.3", "v01.2.3", "v1.02.3", "v1.2.03", "v1.2", "v1.2.3-rc.1", "v1.2.3+build", "v1.2.3\n"):
            with self.subTest(tag=tag):
                self.assert_equivalent(tag, "## v1.2.3\nNotes\n")

    def test_missing_duplicate_and_wrong_headings_match_legacy_failure(self):
        for notes in (
            "# Notes\n",
            "## v1.2.4\nWrong version\n",
            "### v1.2.3\nWrong level\n",
            "## v1.2.3 -\nMissing title\n",
            "## v1.2.3\nFirst\n## v1.2.3 - Again\nSecond\n",
        ):
            with self.subTest(notes=notes):
                self.assert_equivalent("v1.2.3", notes)

    def test_default_notes_and_conf_pass_for_the_newest_release_from_unrelated_directory(self):
        notes = (ROOT / "docs/releasenotes.md").read_text(encoding="utf-8")
        tag = re.search(r"^## (v\S+)", notes, re.MULTILINE).group(1)
        with tempfile.TemporaryDirectory() as folder:
            result = subprocess.run(
                [sys.executable, str(CHECKER), tag], cwd=folder,
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_documentation_states_no_literal_release(self):
        tree = ast.parse((ROOT / "docs/conf.py").read_text(encoding="utf-8"))
        assignments = [
            node for node in tree.body
            if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "release" for t in node.targets)
        ]
        self.assertEqual(len(assignments), 1)
        self.assertNotIsInstance(assignments[0].value, ast.Constant)
        conf = runpy.run_path(str(ROOT / "docs/conf.py"))
        notes = (ROOT / "docs/releasenotes.md").read_text(encoding="utf-8")
        self.assertEqual("v" + conf["release"], re.search(r"^## (v\S+)", notes, re.MULTILINE).group(1))

    def test_matching_case_passes_and_writes_nothing(self):
        result, written, notes, _ = self.run_checker(
            "v1.2.3", "# Notes\n\n## v1.2.3 - New\nText\n## v1.2.2 - Old\nOld\n", "release = '1.2.3'\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(written, ["conf.py", "releasenotes.md"])

    def test_write_notes_writes_only_the_release_text_after_a_pass(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "out.md"
            result, _, _, _ = self.run_checker(
                "v1.2.3", "## v1.2.3 - New\nText\n## v1.2.2 - Old\nOld\n", "release = '1.2.3'\n",
                "--write-notes", str(target))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(target.read_text(encoding="utf-8"), "## v1.2.3 - New\nText\n")
            target.unlink()
            result, _, _, _ = self.run_checker(
                "v1.2.3", "## v1.2.3 - New\nText\n", "release = '9.9.9'\n", "--write-notes", str(target))
            self.assertEqual(result.returncode, 1)
            self.assertFalse(target.exists())

    def test_each_failing_condition_is_named(self):
        cases = {
            "missing heading": ("v1.2.3", "## v1.2.4 - Other\n", "release = '1.2.3'\n", "exactly one release-note heading for v1.2.3, found 0"),
            "duplicate heading": ("v1.2.3", "## v1.2.3\nA\n## v1.2.3 - Again\nB\n", "release = '1.2.3'\n", "found 2"),
            "not the newest": ("v1.2.2", "## v1.2.3 - New\nA\n## v1.2.2 - Old\nB\n", "release = '1.2.2'\n", "not the newest"),
            "documentation differs": ("v1.2.3", "## v1.2.3 - New\nA\n", "release = '0.1.0'\n", "Documentation release '0.1.0'"),
            "no release in configuration": ("v1.2.3", "## v1.2.3 - New\nA\n", "project = 'x'\n", "Documentation release None"),
            "malformed tag": ("1.2.3", "## v1.2.3 - New\nA\n", "release = '1.2.3'\n", "Invalid release tag"),
        }
        for name, (tag, notes, conf, message) in cases.items():
            with self.subTest(name):
                result, written, _, _ = self.run_checker(tag, notes, conf)
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(written, ["conf.py", "releasenotes.md"])

    def test_missing_or_invalid_utf8_file_has_clear_error(self):
        with tempfile.TemporaryDirectory() as folder:
            notes = Path(folder) / "missing.md"
            for content in (None, b"\xff"):
                if content is not None:
                    notes.write_bytes(content)
                result = subprocess.run(
                    [sys.executable, str(CHECKER), "v1.2.3", "--notes", str(notes)],
                    capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 1)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()