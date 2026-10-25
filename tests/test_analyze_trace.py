import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / ".github" / "skills" / "syspilot.trace" / "scripts" / "analyze_trace.py"


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

    def run_cli(self, need_id="N0", depth=1, direction="out"):
        return subprocess.run(
            [sys.executable, str(SCRIPT), need_id, "--depth", str(depth), "--direction", direction, "--ontology", str(self.ontology), "--needs-dir", str(self.needs_dir)],
            capture_output=True,
            text=True,
        )

    def test_depths_one_through_four_and_deeper_are_exact(self):
        for depth in (1, 2, 3, 4, 6):
            with self.subTest(depth=depth):
                result = self.run_cli(depth=depth)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)["neighborhood"], [f"N{index}" for index in range(depth + 1)])

    def test_typed_edges_are_observed_without_syspilot_graph_metadata(self):
        payload = json.loads(self.run_cli(depth=2).stdout)
        self.assertTrue(payload["edges"])
        self.assertTrue(all(edge["option"] == "flows_to" and edge["resolved"] for edge in payload["edges"]))
        self.assertTrue(all("permitted" not in edge for edge in payload["edges"]))
        self.assertIn("semantic-content-review-required", payload["limitations"])

    def test_isolated_object_is_observed_without_defect(self):
        self.write_need("OPTIONAL")
        payload = json.loads(self.run_cli("OPTIONAL", depth=1).stdout)
        self.assertEqual(payload["neighborhood"], ["OPTIONAL"])
        self.assertEqual(payload["edges"], [])
        self.assertEqual(payload["findings"], [])

    def test_same_type_edge_does_not_infer_semantic_orientation(self):
        self.write_need("GENERAL", need_type="req", flows_to=["SPECIFIC"])
        self.write_need("SPECIFIC", need_type="req")
        result = self.run_cli("GENERAL", depth=1)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(any(edge["source"] == "GENERAL" and edge["target"] == "SPECIFIC" and edge["option"] == "flows_to" for edge in payload["edges"]))
        self.assertEqual(payload["findings"], [])
        self.assertIn("semantic-content-review-required", payload["limitations"])

    def test_unresolved_target_and_other_named_edges_are_observed(self):
        self.write_need("BAD", flows_to=["MISSING"], bad_rel=["N0"])
        result = self.run_cli("BAD", depth=1)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual([finding["kind"] for finding in payload["findings"]], ["unresolved-target"])
        self.assertEqual({edge["option"] for edge in payload["edges"]}, {"flows_to", "bad_rel"})
        self.assertTrue(any(edge["option"] == "bad_rel" and edge["resolved"] for edge in payload["edges"]))

    def test_incoming_edge_preserves_source_target_and_name(self):
        self.write_need("N1", flows_to_back=["N0"])
        result = self.run_cli("N1", depth=1, direction="in")
        self.assertEqual(result.returncode, 0, result.stderr)
        edges = json.loads(result.stdout)["edges"]
        self.assertTrue(any(edge["source"] == "N0" and edge["target"] == "N1" and edge["option"] == "flows_to" and edge["direction"] == "in" for edge in edges))

    def test_current_v2_uses_typed_impact_discovery(self):
        project_root = PROJECT_ROOT
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
        project_root = PROJECT_ROOT
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