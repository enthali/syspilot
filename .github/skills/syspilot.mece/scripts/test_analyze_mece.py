import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("analyze_mece.py")


class MeceCliTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.needs_dir = self.root / "needs_id"
        self.needs_dir.mkdir()
        self.ontology = self.root / "ontology.toml"
        self.ontology.write_text(
            '[[needs.types]]\ndirective = "capability"\ntitle = "Capability"\nprefix = "CAP_"\ncolor = "#fff"\nstyle = "node"\n',
            encoding="utf-8",
        )
        self.write_need(
            "A",
            docname="one",
            quality_claims={"shared": True, "conflict": "allow"},
            expected_coverage=["shared", "conflict", "missing"],
            responsibility="owner",
        )
        self.write_need(
            "B",
            docname="one",
            quality_claims={"shared": True, "conflict": "deny"},
            responsibility="owner",
        )
        self.write_need("C", docname="two", quality_claims={"other": True})
        self.write_need("OTHER", need_type="different", docname="one")

    def tearDown(self):
        self.temp_dir.cleanup()

    def write_need(self, need_id, need_type="capability", **fields):
        need = {"id": need_id, "type": need_type, "title": need_id, **fields}
        payload = {"versions": {"": {"needs": {need_id: need}}}}
        (self.needs_dir / f"{need_id}.json").write_text(json.dumps(payload), encoding="utf-8")

    def run_cli(self, need_id, scope):
        return subprocess.run(
            [sys.executable, str(SCRIPT), need_id, "--scope", scope, "--ontology", str(self.ontology), "--needs-dir", str(self.needs_dir)],
            capture_output=True,
            text=True,
        )

    def test_peer_scopes_are_exact_and_deterministic(self):
        same_file = self.run_cli("A", "same-document")
        repeated = self.run_cli("A", "same-document")
        all_type = self.run_cli("A", "all-type")
        self.assertEqual(same_file.returncode, 0, same_file.stderr)
        self.assertEqual(same_file.stdout, repeated.stdout)
        self.assertEqual(json.loads(same_file.stdout)["peers"], ["B"])
        self.assertEqual(json.loads(all_type.stdout)["peers"], ["B", "C"])

    def test_structured_negative_findings_are_reported(self):
        result = self.run_cli("A", "same-document")
        payload = json.loads(result.stdout)
        kinds = {finding["kind"] for finding in payload["findings"]}
        self.assertEqual(kinds, {"overlap", "contradiction", "missing-coverage", "responsibility-collision"})
        self.assertIn("semantic-content-review-required", payload["limitations"])

    def test_missing_peer_data_is_an_explicit_limitation(self):
        result = self.run_cli("C", "same-document")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("no-comparable-peers-discovered", json.loads(result.stdout)["limitations"])

    def test_missing_or_undeclared_inputs_fail(self):
        missing = self.run_cli("UNKNOWN", "all-type")
        undeclared = self.run_cli("OTHER", "all-type")
        self.assertNotEqual(missing.returncode, 0)
        self.assertNotEqual(undeclared.returncode, 0)

    def test_current_v2_data_discovers_requirement_peers(self):
        project_root = Path(__file__).resolve().parents[4]
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "SYSP_REQ_QUALITY", "--scope", "same-document", "--ontology", str(project_root / ".syspilot" / "ontology.toml"), "--needs-dir", str(project_root / "docs" / "_build" / "html" / "needs_id")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["type"], "req")


if __name__ == "__main__":
    unittest.main()