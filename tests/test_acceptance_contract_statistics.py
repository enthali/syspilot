"""Acceptance tests of the contract-statistics skill, black box through its command line.

Traces: SYSP_REQ_CONTRACT_STATISTICS_SKILL_1..3, _RECORD_1, _CLOSURE_1, SYSP_REQ_SETUP_STATISTICS_1.
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_contract_statistics import (GATE_APPROVED, GATE_PENDING, SKILL, git, commit, make_store)

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "docs"


def cli(*args):
    return subprocess.run([sys.executable, str(SKILL), *args], capture_output=True, text=True, encoding="utf-8")


class CliCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "repo"
        self.repo.mkdir()
        git(self.repo, "init", "-q")
        self.store = Path(self.tmp.name) / "store.db"

    def run_cli(self, contract="demo", *extra, end="2026-01-03T00:00:00Z"):
        return cli(contract, "--repo", str(self.repo), "--store", str(self.store), "--end", end, *extra)

    def record(self, contract="demo"):
        return self.repo / ".syspilot" / "stats" / f"{contract}-stat.md"


class StartGateTests(CliCase):
    def test_start_comes_from_gate_not_commit_wording_and_survives_a_move(self):
        make_store(self.store, self.repo, n_calls=3, start="2026-01-02T10:00:00Z")
        commit(self.repo, "docs/changes/demo.md", GATE_PENDING, "2026-01-02T08:00:00Z", "Contract released and approved")
        commit(self.repo, "docs/changes/demo.md", GATE_APPROVED, "2026-01-02T09:00:00Z", "wip")
        (self.repo / "docs/changes/done").mkdir()
        git(self.repo, "mv", "docs/changes/demo.md", "docs/changes/done/demo.md")
        git(self.repo, "commit", "-m", "move", when="2026-01-02T11:00:00Z")
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        text = self.record().read_text(encoding="utf-8")
        self.assertIn("with the gate approved", text)
        gate_sha = subprocess.run(["git", "-C", str(self.repo), "log", "--all", "--format=%h", "--grep=^wip$"],
                                  capture_output=True, text=True).stdout.strip()
        self.assertIn(gate_sha, text)

    def test_release_gate_starts_a_release_window(self):
        make_store(self.store, self.repo)
        commit(self.repo, "docs/releases/r1.md", "| Release start | User | approved: go |\n", "2026-01-02T09:00:00Z")
        result = self.run_cli("r1")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("with the gate approved", self.record("r1").read_text(encoding="utf-8"))

    def test_pending_gate_is_not_a_start(self):
        make_store(self.store, self.repo)
        commit(self.repo, "docs/changes/demo.md", GATE_PENDING, "2026-01-02T08:00:00Z")
        result = self.run_cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.record().exists())


class FigureTests(CliCase):
    def test_explicit_window_totals_and_other_repo_excluded(self):
        make_store(self.store, self.repo, n_calls=5)
        commit(self.repo, "x.txt", "x", "2026-01-02T09:00:00Z")
        result = self.run_cli("demo", "--start", "2026-01-02T09:59:00Z")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = self.record().read_text(encoding="utf-8")
        self.assertIn("| **Total** | 5 |", text)
        self.assertIn("10.0", text)
        self.assertNotIn("Other", text)
        self.assertIn("Developer", text)

    def test_window_bounds_limit_the_calls(self):
        make_store(self.store, self.repo, n_calls=5, start="2026-01-02T10:00:00Z")
        # calls at 10:00 .. 10:04; the window keeps 10:01 .. 10:02
        result = self.run_cli("demo", "--start", "2026-01-02T10:01:00Z", end="2026-01-02T10:02:30Z")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("| **Total** | 2 |", self.record().read_text(encoding="utf-8"))

    def test_activity_counts_only_turns_and_files_inside_the_window(self):
        make_store(self.store, self.repo, n_calls=5, start="2026-01-02T10:00:00Z")
        # the one turn and file are at 10:00; a window from 10:01 must not count them
        self.assertEqual(self.run_cli("demo", "--start", "2026-01-02T10:01:00Z").returncode, 0)
        self.assertIn("| Developer | 0 | 0 | 0 |", self.record().read_text(encoding="utf-8"))
        self.assertEqual(self.run_cli("demo", "--start", "2026-01-02T09:59:00Z").returncode, 0)
        self.assertIn("| Developer | 1 | 1 | 0 |", self.record().read_text(encoding="utf-8"))

    def test_offset_less_timestamps_are_utc(self):
        make_store(self.store, self.repo, n_calls=3)
        result = self.run_cli("demo", "--start", "2026-01-02T09:59:00", end="2026-01-03T00:00:00")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("| **Total** | 3 |", self.record().read_text(encoding="utf-8"))


class FailureTests(CliCase):
    def assert_fails(self, result, cause):
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(cause, (result.stderr + result.stdout).lower())
        self.assertFalse(self.record().exists())

    def test_missing_store(self):
        commit(self.repo, "x.txt", "x", "2026-01-02T09:00:00Z")
        self.assert_fails(self.run_cli("demo", "--start", "2026-01-02T09:00:00Z"), "store")

    def test_missing_gate_without_start(self):
        make_store(self.store, self.repo)
        commit(self.repo, "x.txt", "x", "2026-01-02T09:00:00Z")
        self.assert_fails(self.run_cli(), "demo")

    def test_empty_window(self):
        make_store(self.store, self.repo)
        self.assert_fails(self.run_cli("demo", "--start", "2027-01-01T00:00:00Z", end="2027-01-02T00:00:00Z"), "no")

    def test_end_before_start(self):
        make_store(self.store, self.repo)
        self.assert_fails(self.run_cli("demo", "--start", "2026-01-02T12:00:00Z", end="2026-01-02T10:00:00Z"), "no")


class RecordTests(CliCase):
    def make_record(self):
        make_store(self.store, self.repo, n_calls=4)
        commit(self.repo, "docs/changes/demo.md", GATE_APPROVED, "2026-01-02T09:00:00Z")
        commit(self.repo, "docs/changes/demo.md", GATE_APPROVED + "**Current responsibility:** Quality<br>\n",
               "2026-01-02T10:01:30Z")
        self.assertEqual(self.run_cli().returncode, 0)
        return self.record().read_text(encoding="utf-8")

    def test_header_tables_totals_summaries_and_limits(self):
        text = self.make_record()
        for part in ("# Contract statistics: demo", "**Window:**", "**Window start:**", "**Commits in window",
                     "**Extracted:**", "## Usage per actor", "## Activity per actor", "| **Total**",
                     "**Summary:**", "## Limits"):
            self.assertIn(part, text)

    def test_phase_split_at_first_quality_commit(self):
        text = self.make_record()
        self.assertIn("Before first handover to Quality", text)
        self.assertIn("From first handover to Quality", text)

    def test_one_phase_without_quality_commit(self):
        make_store(self.store, self.repo, n_calls=4)
        commit(self.repo, "docs/changes/demo.md", GATE_APPROVED, "2026-01-02T09:00:00Z")
        self.assertEqual(self.run_cli().returncode, 0)
        self.assertIn("Whole window", self.record().read_text(encoding="utf-8"))


class DocumentationTests(unittest.TestCase):
    def read(self, rel):
        return (CONTRACTS / rel).read_text(encoding="utf-8")

    def test_setup_installs_skill_and_ignores_stats_idempotently(self):
        text = self.read("Syspilot Contracts/setup.md")
        self.assertIn("Statistics folder", text)
        self.assertIn(".syspilot/stats/", text)
        self.assertIn("only when no existing rule already ignores that folder", text)

    def test_closure_item_in_change_and_release_templates_and_examples(self):
        for rel in ("Syspilot Contracts/change.md", "Syspilot Contracts/release.md",
                    "Example Contracts/change.md", "Example Contracts/release.md"):
            with self.subTest(rel=rel):
                self.assertIn("contract-statistics", self.read(rel))


if __name__ == "__main__":
    unittest.main()
