"""Acceptance of SYSP_REQ_RELEASE_CONTRACT, SYSP_VC_RELEASE_CONTRACT_1: the release record check on real release records.

The record is built from the canonical template of docs/Syspilot Contracts/release.md, the check is run through its
command line on temporary git repositories, and each rejection of the verification criterion is exercised one at a time.
tests/test_release_record.py holds the Developer's unit tests; this file does not repeat their fixtures.
"""
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_PROCESS = ROOT / "docs" / "Syspilot Contracts" / "release.md"
SCRIPT = ROOT / "scripts" / "check_release_record.py"
TAG = "v1.2.3"
RECORD = f"docs/changes/release-{TAG}.md"
NOTES = "# Release notes\n\n## v1.2.3 - New\n\nText\n\n## v1.2.2 - Old\n\nOld\n"
HAND_PLACEHOLDER = "| Preflighted commit P | {sha} |"


def template_record():
    """A release record as the Project Manager initializes it: the canonical template, tailored to the version."""
    text = RELEASE_PROCESS.read_text(encoding="utf-8").replace("\r\n", "\n")
    record = text.split("## Canonical Release Contract Template\n\n", 1)[1]
    record = record.replace("{VERSION}", "1.2.3").replace("{version}", "1.2.3")
    return record.replace("**Version:** 1.2.3 - {reason}", "**Version:** 1.2.3 - first release")


def row(record, name):
    return next(line for line in record.splitlines() if line.startswith(f"| {name} |"))


def with_cell(record, name, index, value):
    """The record with one cell of the artifact table row of the given name replaced."""
    line = row(record, name)
    cells = line.strip("|").split("|")
    cells[index] = f" {value} "
    return record.replace(line, "|" + "|".join(cells) + "|")


class Repo:
    def __init__(self, folder):
        self.path = Path(folder) / "repo"
        self.path.mkdir()
        self.git("init", "-q", "-b", "main")
        self.p = None

    def git(self, *args):
        result = subprocess.run(
            ["git", "-C", str(self.path), "-c", "user.name=t", "-c", "user.email=t@example.com",
             "-c", "core.autocrlf=false", "-c", "core.fileMode=false", *args], capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
        return result.stdout.strip()

    def write(self, path, text):
        target = self.path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode("utf-8"))

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "--allow-empty", "-m", message)
        return self.git("rev-parse", "HEAD")

    def preflighted(self, record, notes=NOTES, extra=None):
        self.write(RECORD, record)
        self.write("docs/releasenotes.md", notes)
        self.write("docs/Syspilot Contracts/release.md", RELEASE_PROCESS.read_text(encoding="utf-8"))
        for path, text in (extra or {}).items():
            self.write(path, text)
        self.p = self.commit("P")
        return self.p

    def release(self, record, extra=None):
        self.write(RECORD, record)
        for path, text in (extra or {}).items():
            self.write(path, text)
        return self.commit("R")

    def run(self, r="HEAD", p=None, tag=TAG):
        return subprocess.run(
            [sys.executable, str(SCRIPT), p or self.p, r, tag, "--repo", str(self.path)],
            capture_output=True, text=True)


def evidence_only(record, p):
    """Every kind of change that the Requirement allows after P, applied together."""
    record = record.replace("**Status:** proposed | approved | active | blocked | published | closed<br>",
                            "**Status:** published<br>", 1)
    record = record.replace("**Current responsibility:** Project Manager<br>", "**Current responsibility:** Release<br>", 1)
    record = re.sub(r"\*\*Current blocker:\*\* none \|[^\n]*<br>", "**Current blocker:** none<br>", record, count=1)
    record = record.replace("|--|--|--|--|--|\n", "|--|--|--|--|--|\n| 2026-11-10 | 09:00 | Release | Quality | Preflight passed. |\n", 1)
    record = with_cell(record, "Preflight", 3, "Four checks pass on P")
    record = with_cell(record, "Preflight", 4, "complete")
    record = with_cell(record, "Release notes", 4, "complete")
    record = record.replace("| {check} | {command} @ {sha} | pass / fail: {failing item} |",
                            f"| 1 | `uv run python docs/test_docs_build.py -v` @ {p} | pass |")
    record = record.replace("**Status:** pending | in progress | proceed | blocked", "**Status:** proceed", 1)
    record = record.replace("| {artifact} | {observable issue} | {positive condition needed for proceed} |",
                            "| None | None | None |")
    record = record.replace("| Preflighted commit P | {sha} |", f"| Preflighted commit P | {p} |")
    record = record.replace("| Workflow run | {link or id} |", "| Workflow run | 12345 |")
    return record.replace("- [ ] Current blocker is `none`.", "- [x] Current blocker is `none`.")


def with_p(record, p):
    return record.replace(HAND_PLACEHOLDER, f"| Preflighted commit P | {p} |")


class ReleaseRecordAcceptanceTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Repo(temp.name)
        self.base = template_record()
        self.p = self.repo.preflighted(self.base)

    def assert_rejected(self, expected, result):
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        first = result.stderr.splitlines()[0] if result.stderr else ""
        self.assertTrue(first.startswith(expected), f"first line {first!r} does not begin with {expected!r}")
        self.assertNotIn("Traceback", result.stderr)

    def assert_changes_nothing(self):
        self.assertEqual(self.repo.git("status", "--porcelain"), "")

    def test_the_canonical_template_is_accepted_when_only_evidence_changed_and_nothing_is_written(self):
        self.repo.release(evidence_only(self.base, self.p))
        result = self.repo.run()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.startswith("PASS"))
        self.assert_changes_nothing()

    def test_each_allowed_change_is_accepted_alone(self):
        changes = {
            "header status": lambda r: r.replace("**Status:** proposed | approved | active | blocked | published | closed<br>", "**Status:** published<br>", 1),
            "header responsibility": lambda r: r.replace("**Current responsibility:** Project Manager<br>", "**Current responsibility:** Release<br>", 1),
            "handover log": lambda r: r.replace("|--|--|--|--|--|\n", "|--|--|--|--|--|\n| 2026-11-10 | 09:00 | Release | Quality | Done. |\n", 1),
            "preflight row evidence": lambda r: with_cell(r, "Preflight", 3, "Four checks pass on P"),
            "other row status": lambda r: with_cell(r, "Release notes", 4, "complete"),
            "release verification": lambda r: r.replace("**Status:** pending | in progress | proceed | blocked", "**Status:** proceed", 1),
            "publication evidence": lambda r: r.replace("| Workflow run | {link or id} |", "| Workflow run | 12345 |"),
            "closure": lambda r: r.replace("- [ ] Current blocker is `none`.", "- [x] Current blocker is `none`."),
            "preflight result": lambda r: r.replace("| {check} | {command} @ {sha} | pass / fail: {failing item} |", "| 1 | cmd @ x | pass |"),
        }
        for label, change in changes.items():
            with self.subTest(change=label):
                record = change(self.base)
                self.assertNotEqual(record, self.base, "the change did not alter the record")
                self.repo.git("checkout", "-q", "--detach", self.p)
                self.repo.release(with_p(record, self.p))
                result = self.repo.run()
                self.assertEqual(result.returncode, 0, result.stderr)
    def test_each_protected_alteration_is_rejected_alone_naming_the_condition(self):
        base = with_p(self.base, self.p)
        alterations = {
            "operation mode": base.replace("autonomous | user-guided; select one", "user-guided; select one"),
            "objective and scope section": base.replace("{Why this release exists and what it makes available to users.}", "Something else."),
            "version section": base.replace("**Version:** 1.2.3 - first release", "**Version:** 1.2.3 - other reason"),
            "change inventory section": base.replace("| {change} | {sha} |", "| other | abc |"),
            "owner of a row": with_cell(base, "Preflight", 2, "Quality"),
            "included of a row": with_cell(base, "Release notes", 1, "no"),
            "artifact name of a row": base.replace("| Release notes | yes |", "| Release text | yes |"),
            "release start status": with_cell(base, "Release start", 4, "approved"),
            "release start evidence": with_cell(base, "Release start", 3, "Another authorization"),
            "objective and scope row": with_cell(base, "Objective and scope", 3, "Changed evidence"),
            "version row": with_cell(base, "Version", 3, "Changed evidence"),
            "preflight command list": base.replace("2. `uv run python docs/docs-build.py clean`", "2. `uv run python docs/docs-build.py`"),
            "version and tag text": base.replace("**Version and tag:** 1.2.3 / v1.2.3", "**Version and tag:** 1.2.3 / v1.2.4"),
        }
        for label, record in alterations.items():
            with self.subTest(alteration=label):
                self.assertNotEqual(record, base, "the alteration did not change the record")
                self.repo.git("checkout", "-q", "--detach", self.p)
                self.repo.release(record)
                self.assert_rejected("protected content changed", self.repo.run())

    def test_a_record_that_was_not_preflighted_with_the_commit_of_p_is_rejected(self):
        self.repo.release(self.base.replace("**Status:** proposed | approved | active | blocked | published | closed<br>", "**Status:** published<br>", 1))
        self.assert_rejected("full commit of P missing", self.repo.run())

    def test_a_missing_record_and_a_release_commit_without_p_as_ancestor_are_rejected(self):
        self.repo.git("rm", "-q", RECORD)
        self.repo.commit("R")
        self.assert_rejected("record absent at R", self.repo.run())
        self.repo.git("checkout", "-q", "--orphan", "other")
        self.repo.git("rm", "-rq", "--cached", ".")
        self.repo.write(RECORD, with_p(self.base, self.p))
        self.repo.write("docs/releasenotes.md", NOTES)
        self.repo.write("docs/Syspilot Contracts/release.md", RELEASE_PROCESS.read_text(encoding="utf-8"))
        self.repo.commit("R2")
        self.assert_rejected("P is not an ancestor of R", self.repo.run())

    def test_a_second_changed_path_a_rename_a_mode_change_and_a_deletion_are_each_rejected(self):
        self.repo = Repo(self.repo.path.parent.parent / "second") if False else self.repo
        cases = {
            "second file": ("path other than the record", {"docs/other.md": "new\n"}, None),
            "release notes": ("path other than the record", {"docs/releasenotes.md": NOTES + "\nMore\n"}, None),
        }
        for label, (expected, files, _) in cases.items():
            with self.subTest(case=label):
                self.repo.git("checkout", "-q", "--detach", self.p)
                self.repo.release(with_p(self.base, self.p), files)
                self.assert_rejected(expected, self.repo.run())

    def test_rename_mode_change_and_deletion_of_another_file(self):
        with tempfile.TemporaryDirectory() as folder:
            repo = Repo(folder)
            repo.write("scripts/tool.sh", "echo\n")
            repo.write("docs/spare.md", "spare\n")
            p = repo.preflighted(self.base, extra={"scripts/tool.sh": "echo\n", "docs/spare.md": "spare\n"})
            record = with_p(self.base, p)
            repo.git("checkout", "-q", "--detach", p)
            repo.write(RECORD, record)
            repo.git("mv", "docs/spare.md", "docs/moved.md")
            repo.commit("rename")
            self.assert_rejected("rename", repo.run(p=p))
            repo.git("checkout", "-q", "--detach", p)
            repo.write(RECORD, record)
            repo.git("rm", "-q", "docs/spare.md")
            repo.commit("delete")
            self.assert_rejected("deletion", repo.run(p=p))
            repo.git("checkout", "-q", "--detach", p)
            repo.write(RECORD, record)
            repo.git("update-index", "--chmod=+x", "scripts/tool.sh")
            repo.commit("mode")
            self.assert_rejected("mode change", repo.run(p=p))

    def test_a_version_row_that_disagrees_with_the_release_notes_heading_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            newer = "# Release notes\n\n## v1.2.4 - Newer\n\nText\n\n## v1.2.3 - New\n\nText\n"
            repo = Repo(folder)
            p = repo.preflighted(self.base, notes=newer)
            repo.release(with_p(self.base, p))
            self.assert_rejected("Version row disagrees with the release-notes heading of R", repo.run(p=p))
        with tempfile.TemporaryDirectory() as folder:
            record = self.base.replace("**Version:** 1.2.3 - first release", "**Version:** 1.2.4 - first release")
            repo = Repo(folder)
            p = repo.preflighted(record)
            repo.release(with_p(record, p))
            self.assert_rejected("Version row disagrees with the release-notes heading of R", repo.run(p=p))

    def test_a_record_absent_at_p_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            repo = Repo(folder)
            repo.write("docs/releasenotes.md", NOTES)
            repo.write("docs/Syspilot Contracts/release.md", RELEASE_PROCESS.read_text(encoding="utf-8"))
            p = repo.commit("P")
            repo.release(with_p(self.base, p))
            self.assert_rejected("record absent at P", repo.run(p=p))

    def test_the_compared_version_is_the_version_line_and_the_table_row_is_only_protected_content(self):
        with tempfile.TemporaryDirectory() as folder:
            record = self.base.replace("**Version:** 1.2.3 - first release", "**Version:** 1.2.2 - first release")
            repo = Repo(folder)
            p = repo.preflighted(record)
            repo.release(with_p(record, p))
            self.assert_rejected("Version row disagrees with the release-notes heading of R", repo.run(p=p))
        self.repo.release(with_p(with_cell(self.base, "Version", 3, "Evidence says 9.9.9"), self.p))
        self.assert_rejected("protected content changed", self.repo.run())

    def test_every_template_heading_must_be_present_at_r_and_the_template_must_exist(self):
        headings = [line for line in self.base.splitlines() if line.startswith("## ")]
        self.assertGreaterEqual(len(headings), 12)
        for heading in headings:
            with self.subTest(heading=heading):
                self.repo.git("checkout", "-q", "--detach", self.p)
                record = with_p(self.base, self.p)
                record = record.replace(heading + "\n", "", 1)
                self.repo.release(record)
                self.assert_rejected("template heading missing at R", self.repo.run())
        with tempfile.TemporaryDirectory() as folder:
            repo = Repo(folder)
            repo.write(RECORD, self.base)
            repo.write("docs/releasenotes.md", NOTES)
            p = repo.commit("P")
            repo.release(with_p(self.base, p))
            self.assert_rejected("template not found at R", repo.run(p=p))

    def test_a_template_heading_or_row_that_cannot_be_found_fails_and_never_passes(self):
        cases = {
            "preflight heading": self.base.replace("## Preflight\n", "## Checks\n", 1),
            "release start row": "\n".join(line for line in self.base.splitlines() if not line.startswith("| Release start |")),
            "artifact table column": self.base.replace("| Artifact or gate |", "| Artifact |", 1),
            "version and tag line": self.base.replace("**Version and tag:**", "**Version:**"),
        }
        for label, broken in cases.items():
            with self.subTest(case=label), tempfile.TemporaryDirectory() as folder:
                repo = Repo(folder)
                p = repo.preflighted(broken)
                repo.release(with_p(broken, p))
                result = repo.run(p=p)
                self.assertEqual(result.returncode, 1, result.stdout)
                self.assertTrue(result.stderr.startswith("template"), result.stderr)

    def test_the_published_repository_has_the_one_reader_of_the_record_and_the_build_excludes_it(self):
        conf = (ROOT / "docs" / "conf.py").read_text(encoding="utf-8")
        self.assertRegex(conf, r"exclude_patterns\s*=\s*\[[^\]]*changes")
        readers = []
        for folder in ("scripts", "docs", ".github"):
            for path in (ROOT / folder).rglob("*"):
                if path.suffix in (".py", ".yml", ".toml") and path.is_file() and "changes/release-" in path.read_text(encoding="utf-8", errors="replace"):
                    readers.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(readers, ["scripts/check_release_record.py"])


if __name__ == "__main__":
    unittest.main()
