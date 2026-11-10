import re
import runpy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_release_record.py"
MODULE = runpy.run_path(str(SCRIPT))
TAG = "v1.2.3"
RECORD = f"docs/changes/release-{TAG}.md"
NOTES = "# Notes\n\n## v1.2.3 - New\nText\n\n## v1.2.2 - Old\nOld\n"

RECORD_TEXT = """# Release Contract: 1.2.3

**Status:** active<br>
**Current responsibility:** Release<br>
- **Operation Mode**: user-guided

## Handover log

| Date | Time | From | To | Note |
|--|--|--|--|--|

## Objective And Scope

**Status:** approved<br>

Ship the thing.

## Artifacts, Ownership And Process Gates

| Artifact or gate | Included | Owner | Completion evidence | Status |
|---|---|---|---|---|
| Objective and scope | yes | Project Manager | Approved | approved |
| Release start | yes | User | Authorized on 2026-11-09 | approved |
| Version | yes | Release | Tag and heading agree | complete |
| Preflight | yes | Release | Four checks pass | pending |

## Change Inventory

**Status:** complete

| Change | Integrated commit | Contract closed | Example sync |
|---|---|---|---|
| one | abc | yes | complete |

## Version

**Status:** complete

**Version:** 1.2.3 - first reason

## Preflight

**Status:** pending

1. `uv run python docs/test_docs_build.py -v`
2. `uv run python scripts/check_release_version.py v1.2.3`

| Check | Command and commit | Result |
|---|---|---|
| 1 | command @ {P} | pending |

## Release Notes

**Status:** pending

## User-Facing Documentation

**Status:** pending

## Infrastructure Impact

**Status:** pending

## Release Verification

**Status:** pending

**Version and tag:** 1.2.3 / v1.2.3 (protected content)

## Publication

| Evidence | Value |
|---|---|
| Preflighted commit P | {P} |

## Closure

**Status:** pending
"""
TEMPLATE_TEXT = "# Process\n\n## Canonical Release Contract Template\n\n" + RECORD_TEXT


def git(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.com", *args],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout.strip()


class Repository:
    def __init__(self, folder):
        self.root = Path(folder)
        git(self.root, "init", "-q", "-b", "main")
        self.write(RECORD, RECORD_TEXT.replace("{P}", "pending"))
        self.write("docs/releasenotes.md", NOTES)
        self.write("docs/Syspilot Contracts/release.md", TEMPLATE_TEXT)
        self.write("code.txt", "code\n")
        self.p = self.commit("P")

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode("utf-8"))

    def commit(self, message):
        git(self.root, "add", "-A")
        git(self.root, "commit", "-q", "--allow-empty", "-m", message)
        return git(self.root, "rev-parse", "HEAD")

    def release(self, record=None):
        """Commit R with the record carrying the full P; return R."""
        text = (record if record is not None else RECORD_TEXT).replace("{P}", self.p)
        self.write(RECORD, text)
        return self.commit("R")

    def run(self, r, tag=TAG, p=None):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), p or self.p, r, tag, "--repo", str(self.root)],
            capture_output=True, text=True,
        )
        return result


class ReleaseRecordTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.repo = Repository(self.folder.name)

    def assert_fails(self, r, condition, **kwargs):
        result = self.repo.run(r, **kwargs)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertTrue(result.stderr.startswith(condition), result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_evidence_only_changes_pass_and_nothing_is_written(self):
        text = (RECORD_TEXT
                .replace("**Status:** active", "**Status:** published")
                .replace("**Current responsibility:** Release", "**Current responsibility:** Quality")
                .replace("|--|--|--|--|--|\n", "|--|--|--|--|--|\n| 2026-11-09 | 21:00 | Release | Quality | note |\n")
                .replace("| Preflight | yes | Release | Four checks pass | pending |", "| Preflight | yes | Release | Four checks pass; evidence | passed |")
                .replace("| 1 | command @ {P} | pending |", "| 1 | command @ {P} | pass |")
                .replace("**Status:** pending\n\n**Version and tag", "**Status:** proceed\n\n**Version and tag"))
        r = self.repo.release(text)
        before = git(self.repo.root, "status", "--porcelain")
        result = self.repo.run(r)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(git(self.repo.root, "status", "--porcelain"), before)

    def test_p_not_an_ancestor_of_r(self):
        git(self.repo.root, "checkout", "-q", "--orphan", "other")
        r = self.repo.commit("unrelated")
        self.assert_fails(r, "P is not an ancestor of R")

    def test_a_second_changed_file_fails(self):
        self.repo.write("code.txt", "changed\n")
        r = self.repo.release()
        self.assert_fails(r, "path other than the record")

    def test_release_notes_change_fails_as_another_path(self):
        self.repo.write("docs/releasenotes.md", NOTES + "\nmore\n")
        self.assert_fails(self.repo.release(), "path other than the record")

    def test_deletion_of_another_file_fails(self):
        git(self.repo.root, "rm", "-q", "code.txt")
        self.repo.write(RECORD, RECORD_TEXT.replace("{P}", self.repo.p))
        self.assert_fails(self.repo.commit("R"), "deletion in the difference")

    def test_rename_fails(self):
        git(self.repo.root, "mv", "code.txt", "moved.txt")
        self.repo.write(RECORD, RECORD_TEXT.replace("{P}", self.repo.p))
        self.assert_fails(self.repo.commit("R"), "rename in the difference")

    def test_mode_change_fails(self):
        self.repo.write(RECORD, RECORD_TEXT.replace("{P}", self.repo.p))
        git(self.repo.root, "add", "-A")
        git(self.repo.root, "update-index", "--chmod=+x", RECORD)
        git(self.repo.root, "commit", "-q", "-m", "R")
        self.assert_fails(git(self.repo.root, "rev-parse", "HEAD"), "mode change in the difference")

    def test_no_change_at_all_is_not_exactly_the_record(self):
        r = self.repo.commit("empty")
        self.assert_fails(r, "the difference from P to R is not exactly")

    def test_full_commit_of_p_must_be_in_the_record(self):
        r = self.repo.release(RECORD_TEXT.replace("{P}", "short"))
        self.assert_fails(r, "full commit of P missing from the record at R")
        result = self.repo.run(self.repo.release(RECORD_TEXT.replace("{P}", self.repo.p[:12])))
        self.assertEqual(result.returncode, 1)

    def test_each_protected_block_names_itself_when_changed(self):
        cases = {
            "Operation Mode": ("- **Operation Mode**: user-guided", "- **Operation Mode**: autonomous"),
            "section Objective And Scope": ("Ship the thing.", "Ship another thing."),
            "section Change Inventory": ("| one | abc | yes | complete |", "| two | abc | yes | complete |"),
            "section Version": ("first reason", "second reason"),
            "artifact table columns": ("| Release start | yes | User |", "| Release start | yes | Release |"),
            "artifact row Release start": ("Authorized on 2026-11-09 | approved", "Authorized on 2026-11-10 | approved"),
            "artifact row Version": ("Tag and heading agree | complete", "Tag and heading agree | pending"),
            "artifact row Objective and scope": ("Approved | approved", "Approved | draft"),
            "preflight command list": ("2. `uv run python scripts/check_release_version.py v1.2.3`", "2. `true`"),
            "version and tag text of Release Verification": ("**Version and tag:** 1.2.3 / v1.2.3", "**Version and tag:** 1.2.3 / v1.2.4"),
        }
        for block, (old, new) in cases.items():
            with self.subTest(block):
                self.assertIn(old, RECORD_TEXT)
                git(self.repo.root, "checkout", "-q", self.repo.p)
                r = self.repo.release(RECORD_TEXT.replace(old, new))
                self.assert_fails(r, f"protected content changed: {block}")

    def test_an_added_artifact_row_changes_the_protected_columns(self):
        text = RECORD_TEXT.replace(
            "| Preflight | yes | Release | Four checks pass | pending |",
            "| Preflight | yes | Release | Four checks pass | pending |\n| Extra | yes | Admin | x | pending |")
        self.assert_fails(self.repo.release(text), "protected content changed: artifact table columns")

    def test_record_absent_at_r(self):
        git(self.repo.root, "rm", "-q", RECORD)
        self.assert_fails(self.repo.commit("R"), "record absent at R")

    def test_version_row_changed_after_p_is_protected_content(self):
        r = self.repo.release(RECORD_TEXT.replace("**Version:** 1.2.3", "**Version:** 1.2.4"))
        self.assert_fails(r, "protected content changed: section Version")

    def test_version_row_that_disagrees_with_the_notes_heading_fails_when_unchanged(self):
        repo = self.repo
        text = RECORD_TEXT.replace("**Version:** 1.2.3", "**Version:** 1.2.4")
        repo.write(RECORD, text.replace("{P}", "pending"))
        repo.p = repo.commit("P2")
        self.assert_fails(repo.release(text), "Version row disagrees with the release-notes heading of R")

    def test_missing_template_structure_fails_and_never_passes(self):
        cases = {
            "heading": RECORD_TEXT.replace("## Change Inventory", "## Inventory"),
            "operation mode": RECORD_TEXT.replace("- **Operation Mode**", "- **Mode**"),
            "table": RECORD_TEXT.replace("| Artifact or gate | Included | Owner |", "| Artifact | Included | Owner |"),
            "row": RECORD_TEXT.replace("| Release start |", "| Start |"),
            "commands": RECORD_TEXT.replace("1. `uv", "- `uv").replace("2. `uv", "- `uv"),
            "tag line": RECORD_TEXT.replace("**Version and tag:**", "**Tag:**"),
        }
        for name, text in cases.items():
            with self.subTest(name):
                repo_folder = tempfile.TemporaryDirectory()
                self.addCleanup(repo_folder.cleanup)
                repo = Repository(repo_folder.name)
                repo.write(RECORD, text.replace("{P}", "pending"))
                repo.p = repo.commit("P2")
                result = repo.run(repo.release(text))
                self.assertEqual(result.returncode, 1, name)
                self.assertTrue(result.stderr.startswith("template "), result.stderr)

    def test_each_missing_template_heading_fails_and_names_itself(self):
        headings = re.findall(r"^## (.+)$", RECORD_TEXT, flags=re.M)
        self.assertEqual(len(headings), 12)
        for heading in headings:
            with self.subTest(heading):
                text = RECORD_TEXT.replace(f"## {heading}\n", "")
                result = self.repo.run(self.repo.release(text))
                self.assertEqual(result.returncode, 1, result.stdout)
                self.assertTrue(result.stderr.startswith("template "), result.stderr)
                self.assertIn(heading, result.stderr)

    def test_a_deleted_publication_section_fails(self):
        text = RECORD_TEXT[:RECORD_TEXT.index("## Publication")] + RECORD_TEXT[RECORD_TEXT.index("## Closure"):]
        self.assert_fails(self.repo.release(text), "template heading missing at R: '## Publication'")

    def test_invalid_tag_and_unknown_commit(self):
        r = self.repo.release()
        self.assert_fails(r, "invalid release tag", tag="1.2.3")
        self.assert_fails(r, "deadbeef is not a commit", p="deadbeef")

    def test_the_canonical_template_has_the_structure_the_check_reads(self):
        text = (ROOT / "docs/Syspilot Contracts/release.md").read_text(encoding="utf-8")
        template = text.split("## Canonical Release Contract Template\n", 1)[1]
        content = MODULE["protected_content"](template.replace("\r\n", "\n"), "the template")
        self.assertIn("preflight command list", content)
        self.assertEqual(len(content["preflight command list"]), 4)

    def test_the_canonical_template_headings_are_all_found(self):
        headings = MODULE["template_headings"](ROOT, "HEAD")
        self.assertEqual(len(headings), 12)
        self.assertIn("Publication", headings)
        self.assertEqual(headings[-1], "Closure")


if __name__ == "__main__":
    unittest.main()
