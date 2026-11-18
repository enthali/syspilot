"""Tests of the contract-statistics skill against a fixture store and temporary git repositories."""
import importlib.util
import sqlite3
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".github" / "skills" / "syspilot.contract-statistics" / "scripts" / "contract_stats.py"
spec = importlib.util.spec_from_file_location("contract_stats", SKILL)
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)

GATE_PENDING = "| Contract release | User | pending |\n"
GATE_APPROVED = "| Contract release | User | approved: the User released it |\n"
ENV = {"GIT_AUTHOR_NAME": "t", "GIT_COMMITTER_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_EMAIL": "t@t"}


def git(repo, *args, when=None):
    env = dict(**ENV)
    if when:
        env.update(GIT_AUTHOR_DATE=when, GIT_COMMITTER_DATE=when)
    import os
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, env={**os.environ, **env})


def commit(repo, rel, text, when, message="m"):
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-m", message, when=when)


def make_store(path, repo, n_calls=3, start="2026-01-02T10:00:00Z"):
    con = sqlite3.connect(path)
    con.executescript(
        """
        CREATE TABLE sessions(id TEXT, cwd TEXT, summary TEXT);
        CREATE TABLE turns(session_id TEXT, timestamp TEXT);
        CREATE TABLE session_files(session_id TEXT, first_seen_at TEXT);
        CREATE TABLE assistant_usage_events(session_id TEXT, created_at TEXT, duration_ms INT, total_nano_aiu INT,
          request_multiplier REAL, input_tokens INT, cache_read_tokens INT, cache_write_tokens INT, output_tokens INT,
          reasoning_tokens INT, initiator TEXT, parent_tool_call_id TEXT, model TEXT, reasoning_effort TEXT);
        """
    )
    con.execute("INSERT INTO sessions VALUES('s1', ?, 'You are the Actor \"Developer\"')", (str(repo),))
    con.execute("INSERT INTO sessions VALUES('s2', 'C:\\\\elsewhere', 'Actor \"Other\"')")
    base = int(cs.parse_ts(start).timestamp())
    for i in range(n_calls):
        ts = cs.datetime.fromtimestamp(base + 60 * i, cs.timezone.utc).isoformat()
        con.execute(
            "INSERT INTO assistant_usage_events VALUES('s1', ?, 2000, 2000000000, 1, 100, 50, 10, 20, 5, 'user', NULL, 'm', 'high')",
            (ts,),
        )
    con.execute("INSERT INTO assistant_usage_events VALUES('s2', ?, 1, 1000000000, 1, 1, 1, 1, 1, 1, 'user', NULL, 'm', 'high')", (start,))
    con.execute("INSERT INTO turns VALUES('s1', ?)", (start,))
    con.execute("INSERT INTO session_files VALUES('s1', ?)", (start,))
    con.commit()
    con.close()


class StatsCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "repo"
        self.repo.mkdir()
        git(self.repo, "init", "-q")
        self.store = Path(self.tmp.name) / "store.db"

    def args(self, contract="demo", **kw):
        values = dict(contract=contract, repo=str(self.repo), start=None, end="2026-01-03T00:00:00Z",
                      contract_file=None, store=str(self.store))
        values.update(kw)
        return type("A", (), values)

    def record(self, contract="demo"):
        return self.repo / ".syspilot" / "stats" / f"{contract}-stat.md"


class WindowStartTests(StatsCase):
    def test_start_is_first_commit_with_gate_approved_even_after_move(self):
        commit(self.repo, "docs/changes/demo.md", GATE_PENDING, "2026-01-02T08:00:00Z", "approved elsewhere in words")
        commit(self.repo, "docs/changes/demo.md", GATE_APPROVED, "2026-01-02T09:00:00Z", "unrelated message")
        (self.repo / "docs/changes/done").mkdir()
        git(self.repo, "mv", "docs/changes/demo.md", "docs/changes/done/demo.md")
        git(self.repo, "commit", "-m", "move", when="2026-01-02T11:00:00Z")
        path = cs.locate_contract(self.repo, "demo")
        self.assertEqual(path, "docs/changes/done/demo.md")
        found = cs.find_marker(self.repo, path, cs.gate_approved)
        self.assertEqual(found[1], cs.parse_ts("2026-01-02T09:00:00Z"))

    def test_release_gate_and_phase_marker(self):
        commit(self.repo, "docs/releases/r.md", "| Release start | User | approved |\n", "2026-01-02T09:00:00Z")
        commit(self.repo, "docs/releases/r.md", "**Current responsibility:** Quality<br>\n", "2026-01-02T10:00:00Z")
        self.assertTrue(cs.find_marker(self.repo, "docs/releases/r.md", cs.gate_approved))
        self.assertEqual(cs.find_marker(self.repo, "docs/releases/r.md", cs.holds_quality)[1], cs.parse_ts("2026-01-02T10:00:00Z"))


class RunTests(StatsCase):
    def test_explicit_times_give_calls_and_aiu(self):
        make_store(self.store, self.repo, n_calls=5)
        commit(self.repo, "x.txt", "x", "2026-01-02T09:00:00Z")
        cs.run(self.args(start="2026-01-02T09:59:00Z"))
        text = self.record().read_text(encoding="utf-8")
        self.assertIn("| **Total** | 5 |", text)
        self.assertIn("10.0", text)
        self.assertNotIn("Other", text)

    def test_record_has_header_tables_phases_summaries_and_limits(self):
        make_store(self.store, self.repo)
        commit(self.repo, "docs/changes/demo.md", GATE_APPROVED, "2026-01-02T09:00:00Z")
        commit(self.repo, "docs/changes/demo.md", GATE_APPROVED + "**Current responsibility:** Quality<br>\n", "2026-01-02T10:01:00Z")
        cs.run(self.args())
        text = self.record().read_text(encoding="utf-8")
        for part in ("# Contract statistics: demo", "**Window:**", "**Window start:**", "## Usage per actor",
                     "## Activity per actor", "## AIU by phase", "## Limits", "| **Total** |"):
            self.assertIn(part, text)
        self.assertEqual(text.count("**Summary:**"), 3)
        self.assertIn("Before first handover to Quality", text)
        self.assertIn("From first handover to Quality", text)

    def test_contract_name_that_is_not_a_plain_file_name_is_rejected(self):
        make_store(self.store, self.repo)
        for name in ("../../x", "a/b", "a\\b", "..", "", "/abs"):
            with self.assertRaises(cs.StatsError, msg=name):
                cs.run(self.args(contract=name, start="2026-01-02T09:59:00Z"))
        self.assertFalse((self.repo / ".syspilot").exists())
        self.assertFalse((Path(self.tmp.name) / "x-stat.md").exists())

    def test_missing_store_fails_without_record(self):
        with self.assertRaises(cs.StatsError):
            cs.run(self.args(start="2026-01-02T00:00:00Z"))
        self.assertFalse(self.record().exists())

    def test_missing_gate_without_start_fails_without_record(self):
        make_store(self.store, self.repo)
        commit(self.repo, "docs/changes/demo.md", GATE_PENDING, "2026-01-02T09:00:00Z")
        with self.assertRaises(cs.StatsError):
            cs.run(self.args())
        self.assertFalse(self.record().exists())

    def test_empty_window_fails_without_record(self):
        make_store(self.store, self.repo)
        commit(self.repo, "x.txt", "x", "2026-01-02T09:00:00Z")
        with self.assertRaises(cs.StatsError):
            cs.run(self.args(start="2026-02-01T00:00:00Z", end="2026-02-02T00:00:00Z"))
        self.assertFalse(self.record().exists())


class SetupTextTests(unittest.TestCase):
    def test_setup_installs_stats_folder_with_ignore_exception(self):
        text = (ROOT / "docs" / "Syspilot Contracts" / "setup.md").read_text(encoding="utf-8")
        self.assertIn("| Statistics folder |", text)
        self.assertIn("not duplicated", text)
        self.assertIn("`.syspilot/stats/` is meant to be ignored and is not a generated destination", text)

    def test_closure_checklists_name_the_skill(self):
        for name in ("change.md", "release.md"):
            text = (ROOT / "docs" / "Syspilot Contracts" / name).read_text(encoding="utf-8")
            self.assertIn("syspilot.contract-statistics", text)


if __name__ == "__main__":
    unittest.main()
