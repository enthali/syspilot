import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("analyze_trace.py")


class TraceCliTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.needs_dir = self.root / "needs_id"
        self.needs_dir.mkdir()
        self.ontology = self.root / "ontology.toml"
        self.ontology.write_text(
            """
[needs]
[[needs.extra_links]]
option = "flows_to"
incoming = "flows from"
outgoing = "flows to"
[[needs.extra_links]]
option = "bad_rel"
incoming = "bad from"
outgoing = "bad to"
[[syspilot.type_links]]
from = "capability"
to = "capability"
rel = "flows_to"
""".strip(),
            encoding="utf-8",
        )
        for index in range(7):
            links = [f"N{index + 1}"] if index < 6 else []
            self.write_need(f"N{index}", flows_to=links)

    def tearDown(self):
        self.temp_dir.cleanup()

    def write_need(self, need_id, need_type="capability", **fields):
        need = {"id": need_id, "type": need_type, "title": need_id, "links": [], "links_back": [], "flows_to": [], "flows_to_back": [], "bad_rel": [], "bad_rel_back": [], **fields}
        payload = {"versions": {"": {"needs": {need_id: need}}}}
        (self.needs_dir / f"{need_id}.json").write_text(json.dumps(payload), encoding="utf-8")

    def run_cli(self, need_id="N0", depth=1):
        return subprocess.run(
            [sys.executable, str(SCRIPT), need_id, "--depth", str(depth), "--direction", "out", "--ontology", str(self.ontology), "--needs-dir", str(self.needs_dir)],
            capture_output=True,
            text=True,
        )

    def test_depths_one_through_four_and_deeper_are_exact(self):
        for depth in (1, 2, 3, 4, 6):
            with self.subTest(depth=depth):
                result = self.run_cli(depth=depth)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)["neighborhood"], [f"N{index}" for index in range(depth + 1)])

    def test_typed_edges_are_permitted_by_synthetic_ontology(self):
        payload = json.loads(self.run_cli(depth=2).stdout)
        self.assertTrue(payload["edges"])
        self.assertTrue(all(edge["permitted"] for edge in payload["edges"]))
        self.assertIn("semantic-content-review-required", payload["limitations"])

    def test_absent_permitted_relationship_is_not_reported(self):
        self.write_need("OPTIONAL")
        payload = json.loads(self.run_cli("OPTIONAL", depth=1).stdout)
        self.assertEqual(payload["findings"], [{"kind": "orphan", "object": "OPTIONAL"}])

    def test_unresolved_and_undeclared_edges_are_reported(self):
        self.write_need("BAD", flows_to=["MISSING"], bad_rel=["N0"])
        result = self.run_cli("BAD", depth=1)
        self.assertEqual(result.returncode, 0, result.stderr)
        kinds = {finding["kind"] for finding in json.loads(result.stdout)["findings"]}
        self.assertIn("unresolved-target", kinds)
        self.assertIn("undeclared-relationship", kinds)

    def test_orphan_is_reported_without_requiredness_finding(self):
        self.write_need("ORPHAN")
        result = self.run_cli("ORPHAN", depth=1)
        self.assertEqual(json.loads(result.stdout)["findings"], [{"kind": "orphan", "object": "ORPHAN"}])

    def test_current_v2_uses_typed_impact_discovery(self):
        project_root = Path(__file__).resolve().parents[4]
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "SYSP_REQ_QUALITY", "--depth", "1", "--direction", "both", "--ontology", str(project_root / ".syspilot" / "ontology.toml"), "--needs-dir", str(project_root / "docs" / "_build" / "html" / "needs_id")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        options = {edge["option"] for edge in json.loads(result.stdout)["edges"]}
        self.assertIn("implements", options)
        self.assertIn("specializes", options)

    def test_current_v2_requirement_without_specializes_has_no_missing_finding(self):
        project_root = Path(__file__).resolve().parents[4]
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "SYSP_REQ_MECE_ANALYSIS", "--depth", "1", "--direction", "both", "--ontology", str(project_root / ".syspilot" / "ontology.toml"), "--needs-dir", str(project_root / "docs" / "_build" / "html" / "needs_id")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        kinds = {finding["kind"] for finding in json.loads(result.stdout)["findings"]}
        self.assertNotIn("missing-expected-relationship", kinds)


if __name__ == "__main__":
    unittest.main()