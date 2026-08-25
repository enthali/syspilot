import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("get_need_links.py")


class ImpactQueryCliTests(unittest.TestCase):
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
option = "implements"
incoming = "implemented by"
outgoing = "implements"
[[needs.extra_links]]
option = "customer_rel"
incoming = "customer incoming"
outgoing = "customer outgoing"
""".strip(),
            encoding="utf-8",
        )
        needs = {
            "ROOT": {
                "id": "ROOT",
                "type": "root",
                "title": "Root",
                "status": "approved",
                "links": ["STANDARD"],
                "links_back": [],
                "implements": ["TYPED"],
                "implements_back": ["BACK"],
                "customer_rel": ["CUSTOM", "TYPED"],
                "customer_rel_back": [],
            },
            "TYPED": self.need("TYPED", implements=["ROOT"]),
            "CUSTOM": self.need("CUSTOM", customer_rel=["ROOT"]),
            "STANDARD": self.need("STANDARD", links=["ROOT"]),
            "BACK": self.need("BACK", implements=["ROOT"]),
        }
        for need_id, need in needs.items():
            payload = {"versions": {"": {"needs": {need_id: need}}}}
            (self.needs_dir / f"{need_id}.json").write_text(
                json.dumps(payload), encoding="utf-8"
            )

    def tearDown(self):
        self.temp_dir.cleanup()

    @staticmethod
    def need(need_id, **links):
        need = {
            "id": need_id,
            "type": "req",
            "title": need_id,
            "status": "approved",
            "links": [],
            "links_back": [],
            "implements": [],
            "implements_back": [],
            "customer_rel": [],
            "customer_rel_back": [],
        }
        need.update(links)
        return need

    def run_cli(self, *args, ontology=None, needs_dir=None, no_build=True, env=None):
        command = [
            sys.executable,
            str(SCRIPT),
            *args,
            "--ontology",
            str(ontology or self.ontology),
            "--needs-dir",
            str(needs_dir or self.needs_dir),
        ]
        if no_build:
            command.append("--no-build")
        return subprocess.run(command, capture_output=True, text=True, env=env)

    def test_flat_traverses_standard_v2_and_customer_links_once(self):
        result = self.run_cli("ROOT", "--direction", "out", "--depth", "1", "--flat")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), ["CUSTOM", "STANDARD", "TYPED"])

    def test_standard_links_work_without_extra_link_configuration(self):
        standard_only_ontology = self.root / "standard-only.toml"
        standard_only_ontology.write_text("[needs]\n", encoding="utf-8")

        result = self.run_cli(
            "ROOT",
            "--direction",
            "out",
            "--depth",
            "1",
            "--flat",
            ontology=standard_only_ontology,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), ["STANDARD"])

    def test_converging_shorter_path_still_expands_descendants(self):
        converging_needs = {
            "ROOT": self.need("ROOT", links=["A", "X"]),
            "A": self.need("A", links=["X"]),
            "X": self.need("X", links=["Y"]),
            "Y": self.need("Y"),
        }
        for need_id, need in converging_needs.items():
            payload = {"versions": {"": {"needs": {need_id: need}}}}
            (self.needs_dir / f"{need_id}.json").write_text(
                json.dumps(payload), encoding="utf-8"
            )

        result = self.run_cli(
            "ROOT", "--direction", "out", "--depth", "2", "--flat"
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), ["A", "X", "Y"])

    def test_simple_and_nested_preserve_direction_and_cycle_protection(self):
        simple = self.run_cli("ROOT", "--direction", "in", "--simple")
        self.assertEqual(simple.returncode, 0, simple.stderr)
        self.assertEqual(json.loads(simple.stdout)["links_incoming"], ["BACK"])

        nested = self.run_cli("ROOT", "--direction", "out", "--depth", "2")
        self.assertEqual(nested.returncode, 0, nested.stderr)
        tree = json.loads(nested.stdout)
        child_ids = [child["id"] for child in tree["links"]]
        self.assertEqual(child_ids, ["CUSTOM", "STANDARD", "TYPED"])
        self.assertTrue(
            any(
                grandchild.get("truncated")
                for child in tree["links"]
                for grandchild in child.get("links", [])
            )
        )

    def test_unknown_need_is_non_success(self):
        result = self.run_cli("UNKNOWN")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not found", result.stderr)

    def test_missing_or_invalid_ontology_is_non_success(self):
        missing = self.run_cli("ROOT", ontology=self.root / "missing.toml")
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("ontology", missing.stderr.lower())

        invalid_path = self.root / "invalid.toml"
        invalid_path.write_text("not = [valid", encoding="utf-8")
        invalid = self.run_cli("ROOT", ontology=invalid_path)
        self.assertNotEqual(invalid.returncode, 0)
        self.assertIn("ontology", invalid.stderr.lower())

        malformed_links_path = self.root / "malformed-links.toml"
        malformed_links_path.write_text(
            '[needs]\nextra_links = "implements"\n', encoding="utf-8"
        )
        malformed_links = self.run_cli("ROOT", ontology=malformed_links_path)
        self.assertNotEqual(malformed_links.returncode, 0)
        self.assertIn("extra_links must be a list", malformed_links.stderr)

    def test_missing_needs_data_without_build_is_non_success(self):
        result = self.run_cli("ROOT", needs_dir=self.root / "missing-needs")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Needs data", result.stderr)

    def test_unusable_build_prerequisite_is_non_success(self):
        environment = os.environ.copy()
        environment["PATH"] = ""
        result = self.run_cli(
            "ROOT",
            needs_dir=self.root / "missing-needs",
            no_build=False,
            env=environment,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Could not run sphinx-build", result.stderr)
        self.assertIn("Needs data", result.stderr)


if __name__ == "__main__":
    unittest.main()
