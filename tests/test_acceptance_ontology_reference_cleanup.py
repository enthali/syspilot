"""Acceptance tests of the tracked Syspilot ontology reference page, read independently from the ontology file.

Traces: SYSP_REQ_ONTOLOGY_LOCATION (_2, _3), SYSP_REQ_ONTOLOGY_SCHEMA, SYSP_REQ_SETUP_DOCS.
"""
import re
import subprocess
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "docs" / "Syspilot Ontology"
PAGE = FOLDER / "ontology.md"
NEEDS = tomllib.loads((FOLDER / "ontology.toml").read_text(encoding="utf-8"))["needs"]


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


class PageMatchesOntologyTests(unittest.TestCase):
    def setUp(self):
        self.text = PAGE.read_text(encoding="utf-8")

    def test_every_type_with_its_prefix_and_title_is_catalogued(self):
        for t in NEEDS["types"]:
            with self.subTest(type=t["directive"]):
                self.assertRegex(self.text, rf"\|\s*`{re.escape(t['directive'])}`\s*\|\s*{re.escape(t['title'])}\s*\|\s*`{re.escape(t['prefix'])}`")

    def test_every_extra_link_and_option_and_status_is_named(self):
        for link in NEEDS["extra_links"]:
            self.assertIn(f"`{link['option']}`", self.text, link["option"])
        for option in NEEDS["extra_options"]:
            self.assertIn(f"`{option}`", self.text, option)
        for status in NEEDS["statuses"]:
            self.assertIn(status["name"], self.text, status["name"])

    def test_page_names_no_type_the_ontology_does_not_define(self):
        directives = {t["directive"] for t in NEEDS["types"]}
        catalogue = self.text.split("## Type Catalogue")[1].split("\n## ")[0]
        listed = set(re.findall(r"^\|\s*`(\w+)`\s*\|", catalogue, re.M))
        self.assertEqual(listed, directives)

    def test_every_diagram_edge_uses_a_configured_link_between_configured_types(self):
        directives = {t["directive"] for t in NEEDS["types"]}
        options = {link["option"] for link in NEEDS["extra_links"]} | {"links"}
        block = re.search(r"```\{mermaid\}(.*?)```", self.text, re.S).group(1)
        edges = re.findall(r"^\s*(\w+)\s*--+>?\|([^|]+)\|\s*>?\s*(\w+)", block, re.M)
        self.assertTrue(edges)
        for source, link, target in edges:
            self.assertIn(source, directives)
            self.assertIn(target, directives)
            self.assertIn(link.strip(), options)


class NoGeneratorTests(unittest.TestCase):
    def test_conf_has_no_reference_generation(self):
        conf = (ROOT / "docs" / "conf.py").read_text(encoding="utf-8")
        for word in ("diagram_edges", "builder-inited", "write_text", "connect("):
            self.assertNotIn(word, conf)

    def test_page_is_tracked_and_not_ignored(self):
        self.assertIn("docs/Syspilot Ontology/ontology.md", git("ls-files", "docs/Syspilot Ontology").stdout)
        self.assertNotEqual(git("check-ignore", "-q", "docs/Syspilot Ontology/ontology.md").returncode, 0)

    def test_ontology_file_carries_no_generator_metadata(self):
        self.assertNotIn("diagram_edges", (FOLDER / "ontology.toml").read_text(encoding="utf-8"))

    def test_setup_contract_and_requirements_no_longer_call_the_page_generated(self):
        setup = (ROOT / "docs" / "Syspilot Contracts" / "setup.md").read_text(encoding="utf-8")
        self.assertNotRegex(setup, r"(?i)syspilot's own generated reference")
        schema = (ROOT / "docs" / "syspilot" / "requirements" / "req_ontology_management.rst").read_text(encoding="utf-8")
        self.assertNotRegex(schema, r"(?i)generated (diagram|reference|page)")
        self.assertIn("holds no ``[[syspilot.diagram_edges]]``", schema)


if __name__ == "__main__":
    unittest.main()
