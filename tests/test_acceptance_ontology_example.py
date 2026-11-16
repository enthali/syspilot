"""Requirement tests for the ontology-example Change, written from SYSP_REQ_EXAMPLE_ONTOLOGY, SYSP_REQ_ONTOLOGY_LOCATION,
SYSP_REQ_SETUP_ONTOLOGY and the Change's observable outcome."""

import json
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "docs" / "Example Ontology"
OWN = ROOT / "docs" / "Syspilot Ontology"
SKILLS = ROOT / ".github" / "skills"
TRACE = SKILLS / "syspilot.trace" / "scripts" / "analyze_trace.py"
MECE = SKILLS / "syspilot.mece" / "scripts" / "analyze_mece.py"
IMPACT = SKILLS / "syspilot.impact-python" / "scripts" / "get_need_links.py"
SETUP = ROOT / "docs" / "Syspilot Contracts" / "setup.md"

TYPES = {"root", "story", "req", "design", "ac", "vc", "doc"}
LINKS = {"tracked_by", "implements", "specializes", "details", "validates", "verifies", "includes"}

SAMPLE = """Spec
====

.. root:: Root
   :id: SMP_ROOT
   :status: approved

.. story:: Story
   :id: SMP_US_ONE
   :status: approved
   :tracked_by: SMP_ROOT

.. req:: General
   :id: SMP_REQ_GEN
   :status: approved
   :implements: SMP_US_ONE

.. req:: Concrete
   :id: SMP_REQ_CON
   :status: approved
   :implements: SMP_US_ONE
   :specializes: SMP_REQ_GEN

.. design:: Design
   :id: SMP_DES_ONE
   :status: approved
   :details: SMP_REQ_CON

.. ac:: Criterion
   :id: SMP_AC_ONE
   :status: approved
   :validates: SMP_US_ONE

.. vc:: Verifies a requirement
   :id: SMP_VC_REQ
   :status: approved
   :verifies: SMP_REQ_CON, SMP_REQ_GEN

.. vc:: Verifies a design
   :id: SMP_VC_DES
   :status: approved
   :verifies: SMP_DES_ONE

.. doc:: Documentation
   :id: SMP_DOC_ONE
   :status: approved
   :includes: SMP_REQ_CON
"""
CONF = (
    "project = 'Sample'\n"
    "extensions = ['myst_parser', 'sphinx_needs', 'sphinxcontrib.mermaid']\n"
    "needs_from_toml = 'Acme Ontology/ontology.toml'\n"
    "suppress_warnings = ['needs.deprecated']\n"
    "exclude_patterns = ['_build']\n"
)
INDEX = "Sample\n======\n\n.. toctree::\n\n   Acme Ontology/ontology\n   spec\n"


def load(path):
    return tomllib.loads(Path(path).read_text(encoding="utf-8"))


def build(root, quiet=True):
    # The details of a needs.warnings failure are printed only without -q.
    return subprocess.run(
        [sys.executable, "-m", "sphinx", "-b", "html", "docs", "build", "-W", "--keep-going", *(["-q"] if quiet else [])],
        cwd=root, capture_output=True, text=True,
    )


def sample_project(folder, spec=SAMPLE):
    docs = Path(folder) / "docs"
    shutil.copytree(EXAMPLE, docs / "Acme Ontology")
    (docs / "conf.py").write_text(CONF, encoding="utf-8")
    (docs / "index.rst").write_text(INDEX, encoding="utf-8")
    (docs / "spec.rst").write_text(spec, encoding="utf-8")
    return Path(folder)


def skill(script, *args, cwd):
    result = subprocess.run([sys.executable, str(script), *args], cwd=cwd, capture_output=True, text=True)
    return result, (json.loads(result.stdout) if result.stdout.strip().startswith("{") else None)


class ExampleOntologyDefinitionTests(unittest.TestCase):
    """SYSP_VC_EXAMPLE_ONTOLOGY_1."""

    def test_exactly_the_seven_types_and_seven_links(self):
        data = load(EXAMPLE / "ontology.toml")["needs"]
        self.assertEqual({t["directive"] for t in data["types"]}, TYPES)
        self.assertEqual(len(data["types"]), 7)
        self.assertEqual({l["option"] for l in data["extra_links"]}, LINKS)
        self.assertEqual(len(data["extra_links"]), 7)

    def test_statuses_options_and_settings_equal_syspilots_own_ontology(self):
        own, example = load(OWN / "ontology.toml")["needs"], load(EXAMPLE / "ontology.toml")["needs"]
        self.assertEqual(own["statuses"], example["statuses"])
        self.assertEqual(own["extra_options"], example["extra_options"])
        for key in set(own) - {"types", "statuses", "extra_links", "extra_options", "warnings", "schema_definitions"}:
            with self.subTest(setting=key):
                self.assertEqual(own[key], example.get(key))

    def test_design_exists_only_in_the_example_ontology(self):
        own = {t["directive"] for t in load(OWN / "ontology.toml")["needs"]["types"]}
        self.assertNotIn("design", own)
        self.assertNotIn("details", {l["option"] for l in load(OWN / "ontology.toml")["needs"]["extra_links"]})

    def test_the_page_describes_every_type_and_link_with_no_markup_and_no_folder_name(self):
        page = (EXAMPLE / "ontology.md").read_text(encoding="utf-8")
        for name in TYPES | LINKS:
            with self.subTest(name=name):
                self.assertIn(name, page)
        self.assertNotRegex(page, r"(?m)^\s*\.\. \w+::")
        self.assertNotRegex(page, r"(?m)^\s*```\{(?!toctree|mermaid)")
        self.assertNotIn("Example", page)
        self.assertNotIn("Syspilot", page.replace("Syspilot's", ""))

    def test_the_diagram_is_a_mermaid_directive_with_every_type_and_one_edge_per_endpoint_pair(self):
        # SYSP_VC_EXAMPLE_ONTOLOGY_3: one node per type, so a node id is its type and `req -->|specializes| req` draws specialization.
        page = (EXAMPLE / "ontology.md").read_text(encoding="utf-8")
        block = re.search(r"```\{mermaid\}\n(.*?)```", page, re.S)
        self.assertIsNotNone(block, "the diagram must be a {mermaid} directive block")
        nodes = re.findall(r'(?m)^\s+(\w+)\["(\w+):', block.group(1))
        self.assertEqual(sorted(label for _, label in nodes), sorted(TYPES), "exactly one node per type")
        self.assertTrue(all(node_id == label for node_id, label in nodes))
        drawn = set(re.findall(r"(?m)^\s+(\w+) -->\|(\w+)\| (\w+)$", block.group(1)))
        expected = {("story", "tracked_by", "root"), ("req", "implements", "story"), ("req", "specializes", "req"),
                    ("design", "details", "req"), ("ac", "validates", "story"), ("vc", "verifies", "req"),
                    ("vc", "verifies", "design"), ("doc", "includes", "req")}
        self.assertEqual(drawn, expected)

    def test_the_example_folder_holds_exactly_the_two_files(self):
        self.assertEqual(sorted(p.name for p in EXAMPLE.rglob("*") if p.is_file()), ["ontology.md", "ontology.toml"])


class SampleProjectTests(unittest.TestCase):
    """SYSP_VC_EXAMPLE_ONTOLOGY_2: every type and link builds strictly; Impact, MECE and Trace run on the result."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = sample_project(cls.tmp.name)
        cls.result = build(cls.root)
        cls.needs = cls.root / "build" / "needs_id"
        cls.ontology = "docs/Acme Ontology/ontology.toml"

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_strict_build_has_zero_warnings(self):
        self.assertEqual(self.result.returncode, 0, self.result.stdout + self.result.stderr)
        self.assertNotIn("WARNING", self.result.stdout + self.result.stderr)

    def test_every_type_and_link_is_present_in_the_built_needs(self):
        data = json.loads((self.root / "build" / "needs.json").read_text(encoding="utf-8"))
        needs = next(iter(data["versions"].values()))["needs"]
        self.assertEqual({n["type"] for n in needs.values()}, TYPES)
        self.assertEqual({l for n in needs.values() for l in LINKS if n.get(l)}, LINKS)

    def test_trace_reaches_every_type_and_reports_every_link_resolved(self):
        result, out = skill(TRACE, "SMP_DES_ONE", "--depth", "3", "--ontology", self.ontology,
                            "--needs-dir", str(self.needs), cwd=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(out["neighborhood"]), 9)
        self.assertEqual({e["option"] for e in out["edges"]}, LINKS)
        self.assertTrue(all(e["resolved"] for e in out["edges"]))

    def test_an_installed_skill_resolves_the_ontology_from_the_literal_binding_without_an_argument(self):
        # The skills resolve the default from their own location, so they are installed into the sample project first.
        installed = self.root / ".github" / "skills"
        if not installed.exists():
            shutil.copytree(SKILLS, installed, ignore=shutil.ignore_patterns("__pycache__"))
        script = installed / "syspilot.trace" / "scripts" / "analyze_trace.py"
        result, out = skill(script, "SMP_DES_ONE", "--depth", "1", "--needs-dir", str(self.needs), cwd=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SMP_REQ_CON", out["neighborhood"])

    def test_impact_exposes_the_new_details_link_in_both_directions(self):
        _, out = skill(IMPACT, "SMP_REQ_CON", "--typed", "--no-build", "--ontology", self.ontology,
                       "--needs-dir", str(self.needs), cwd=self.root)
        self.assertIn(("SMP_DES_ONE", "SMP_REQ_CON", "details"), {(e["source"], e["target"], e["option"]) for e in out["edges"]})
        _, out = skill(IMPACT, "SMP_DES_ONE", "--typed", "--no-build", "--ontology", self.ontology,
                       "--needs-dir", str(self.needs), cwd=self.root)
        self.assertIn(("SMP_VC_DES", "SMP_DES_ONE", "verifies"), {(e["source"], e["target"], e["option"]) for e in out["edges"]})

    def test_mece_pairs_the_vcs_that_verify_a_requirement_and_a_design(self):
        result, out = skill(MECE, "SMP_VC_DES", "--scope", "all-type", "--ontology", self.ontology,
                            "--needs-dir", str(self.needs), cwd=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(out["type"], "vc")
        self.assertEqual(out["peers"], ["SMP_VC_REQ"])
        result, out = skill(MECE, "SMP_DES_ONE", "--scope", "all-type", "--ontology", self.ontology,
                            "--needs-dir", str(self.needs), cwd=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(out["type"], "design")


def block(kind, title, ident, **links):
    lines = [f".. {kind}:: {title}", f"   :id: {ident}", "   :status: approved"]
    lines += [f"   :{option}: {target}" for option, target in links.items()]
    return "\n".join(lines) + "\n\n"


class LinkObligationTests(unittest.TestCase):
    """SYSP_VC_ONTOLOGY_LINK_OBLIGATIONS_1: a Need lacking a mandatory link fails the strict build and is named."""

    CASES = {
        "story_lacks_incoming_validates": ("SMP_US_X", block("story", "S", "SMP_US_X", tracked_by="SMP_ROOT")
                                           + block("req", "R", "SMP_REQ_X", implements="SMP_US_X")
                                           + block("vc", "V", "SMP_VC_X", verifies="SMP_REQ_X")),
        "story_lacks_incoming_implements": ("SMP_US_X", block("story", "S", "SMP_US_X", tracked_by="SMP_ROOT")
                                            + block("ac", "A", "SMP_AC_X", validates="SMP_US_X")),
        "req_lacks_incoming_verifies": ("SMP_REQ_X", block("req", "R", "SMP_REQ_X", implements="SMP_US_ONE")),
        "req_lacks_outgoing_implements": ("SMP_REQ_X", block("req", "R", "SMP_REQ_X")
                                          + block("vc", "V", "SMP_VC_X", verifies="SMP_REQ_X")),
        "design_lacks_incoming_verifies": ("SMP_DES_X", block("design", "D", "SMP_DES_X", details="SMP_REQ_CON")),
        "design_lacks_outgoing_details": ("SMP_DES_X", block("design", "D", "SMP_DES_X")
                                          + block("vc", "V", "SMP_VC_X", verifies="SMP_DES_X")),
    }

    def test_each_missing_link_fails_the_strict_build_naming_the_need_and_the_link(self):
        for key, (need, extra) in self.CASES.items():
            with self.subTest(obligation=key), tempfile.TemporaryDirectory() as folder:
                result = build(sample_project(folder, SAMPLE + "\n" + extra), quiet=False)
                output = result.stdout + result.stderr
                self.assertNotEqual(result.returncode, 0, output)
                self.assertIn(need, output)
                self.assertIn(key, output)

    WRONG_TYPE = {
        # A vc validating a story must not satisfy the story's incoming `validates` from an ac.
        "validates_from_ac": ("SMP_VC_W", block("story", "S", "SMP_US_W", tracked_by="SMP_ROOT")
                              + block("req", "R", "SMP_REQ_W", implements="SMP_US_W")
                              + block("vc", "V", "SMP_VC_W", verifies="SMP_REQ_W", validates="SMP_US_W")),
        "validates_to_story": ("SMP_AC_W", block("ac", "A", "SMP_AC_W", validates="SMP_REQ_CON")),
        # A design implementing a story must not satisfy the story's incoming `implements` from a req.
        "implements_from_req": ("SMP_DES_W", block("story", "S", "SMP_US_W", tracked_by="SMP_ROOT")
                                + block("ac", "A", "SMP_AC_W", validates="SMP_US_W")
                                + block("design", "D", "SMP_DES_W", details="SMP_REQ_CON", implements="SMP_US_W")
                                + block("vc", "V", "SMP_VC_W", verifies="SMP_DES_W")),
        "implements_to_story": ("SMP_REQ_W", block("req", "R", "SMP_REQ_W", implements="SMP_REQ_CON")
                                + block("vc", "V", "SMP_VC_W", verifies="SMP_REQ_W")),
        "verifies_from_vc": ("SMP_AC_W", block("ac", "A", "SMP_AC_W", validates="SMP_US_ONE", verifies="SMP_REQ_GEN")),
        "verifies_to_req_or_design": ("SMP_VC_W", block("vc", "V", "SMP_VC_W", verifies="SMP_US_ONE")),
        "details_from_design": ("SMP_REQ_W", block("req", "R", "SMP_REQ_W", implements="SMP_US_ONE", details="SMP_REQ_GEN")
                                + block("vc", "V", "SMP_VC_W", verifies="SMP_REQ_W")),
        "details_to_req": ("SMP_DES_W", block("design", "D", "SMP_DES_W", details="SMP_US_ONE")
                           + block("vc", "V", "SMP_VC_W", verifies="SMP_DES_W")),
    }

    def test_a_link_with_a_wrong_endpoint_type_fails_the_strict_build_naming_the_need_and_the_rule(self):
        for key, (need, extra) in self.WRONG_TYPE.items():
            with self.subTest(rule=key), tempfile.TemporaryDirectory() as folder:
                result = build(sample_project(folder, SAMPLE + "\n" + extra), quiet=False)
                output = result.stdout + result.stderr
                self.assertNotEqual(result.returncode, 0, output)
                self.assertIn(need, output)
                self.assertIn(key, output)

    def test_the_complete_sample_builds_clean(self):
        with tempfile.TemporaryDirectory() as folder:
            result = build(sample_project(folder))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_syspilots_ontology_carries_the_obligations_without_design(self):
        warnings = load(OWN / "ontology.toml")["needs"]["warnings"]
        self.assertEqual(len(warnings), 4)
        self.assertFalse([name for name in warnings if name.startswith("design")])
        self.assertEqual(len(load(EXAMPLE / "ontology.toml")["needs"]["warnings"]), 6)
        schemas = {s["id"] for s in load(OWN / "ontology.toml")["needs"]["schema_definitions"]["schemas"]}
        self.assertFalse([name for name in schemas if name.startswith("details")])
        self.assertIn("details_to_req", {s["id"] for s in load(EXAMPLE / "ontology.toml")["needs"]["schema_definitions"]["schemas"]})


class SampleProjectNegativeControls(unittest.TestCase):
    """The sample build and the skills are strict enough to see what the ontology forbids or the graph lacks."""

    def test_an_unknown_type_fails_the_strict_build(self):
        with tempfile.TemporaryDirectory() as folder:
            root = sample_project(folder, SAMPLE + "\n.. spec:: Not here\n   :id: SMP_SPEC_ONE\n")
            self.assertNotEqual(build(root).returncode, 0)

    def test_the_installed_page_needs_the_mermaid_extension_under_the_strict_build(self):
        # SYSP_VC_SETUP_DOCS_5 negative control: without the extension the {mermaid} directive is unknown and the build fails.
        with tempfile.TemporaryDirectory() as folder:
            root = sample_project(folder)
            conf = root / "docs" / "conf.py"
            conf.write_text(CONF.replace(", 'sphinxcontrib.mermaid'", ""), encoding="utf-8")
            result = build(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("mermaid", result.stdout + result.stderr)

    def test_the_design_link_is_not_available_on_a_requirement_in_syspilots_ontology(self):
        # The sample bound to Syspilot's ontology must fail: `design` and `details` exist only in the Example Ontology.
        with tempfile.TemporaryDirectory() as folder:
            root = sample_project(folder)
            shutil.copy(OWN / "ontology.toml", root / "docs" / "Acme Ontology" / "ontology.toml")
            self.assertNotEqual(build(root).returncode, 0)

    def test_trace_reports_a_design_whose_requirement_does_not_exist_as_unresolved(self):
        with tempfile.TemporaryDirectory() as folder:
            root = sample_project(folder)
            spec = root / "docs" / "spec.rst"
            spec.write_text(SAMPLE.replace(":details: SMP_REQ_CON", ":details: SMP_REQ_GONE"), encoding="utf-8")
            build(root)
            _, out = skill(TRACE, "SMP_DES_ONE", "--depth", "1", "--ontology", "docs/Acme Ontology/ontology.toml",
                           "--needs-dir", str(root / "build" / "needs_id"), cwd=root)
            self.assertTrue(any(not e["resolved"] for e in out["edges"]), out)


class SyspilotBindingTests(unittest.TestCase):
    """SYSP_VC_ONTOLOGY_LOCATION_1 and _2."""

    def test_no_syspilot_folder_and_no_tracked_files_at_the_old_locations(self):
        self.assertFalse((ROOT / ".syspilot").exists())
        tracked = subprocess.run(["git", "ls-files", ".syspilot", "docs/ontology-reference.md"],
                                 cwd=ROOT, capture_output=True, text=True).stdout
        self.assertEqual(tracked.strip(), "")

    def test_conf_binds_the_literal_new_location_and_the_file_exists(self):
        conf = (ROOT / "docs" / "conf.py").read_text(encoding="utf-8")
        self.assertRegex(conf, r'(?m)^needs_from_toml = "Syspilot Ontology/ontology\.toml"$')
        self.assertTrue((OWN / "ontology.toml").is_file())

    def test_the_generated_page_is_untracked_and_lists_every_configured_type(self):
        ignored = subprocess.run(["git", "check-ignore", "docs/Syspilot Ontology/ontology.md"],
                                 cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(ignored.returncode, 0)
        page = OWN / "ontology.md"
        if not page.exists():
            self.skipTest("page is generated by the documentation build; run docs/docs-build.py first")
        text = page.read_text(encoding="utf-8")
        for need_type in load(OWN / "ontology.toml")["needs"]["types"]:
            with self.subTest(type=need_type["directive"]):
                self.assertIn(need_type["directive"], text)

    def test_the_generated_diagram_has_one_node_per_type_and_one_edge_per_declared_link(self):
        # SYSP_VC_ONTOLOGY_LOCATION_3
        data = load(OWN / "ontology.toml")
        page = OWN / "ontology.md"
        if not page.exists():
            self.skipTest("page is generated by the documentation build; run docs/docs-build.py first")
        text = page.read_text(encoding="utf-8")
        self.assertIn("```{mermaid}", text)
        directives = {t["directive"] for t in data["needs"]["types"]}
        links = {l["option"] for l in data["needs"]["extra_links"]}
        edges = data["syspilot"]["diagram_edges"]
        for edge in edges:
            self.assertIn(edge["link"], links)
            self.assertIn(edge["from"], directives)
            self.assertIn(edge["to"], directives)
            self.assertIn("    %s -->|%s| %s" % (edge["from"], edge["link"], edge["to"]), text)
        self.assertEqual({e["link"] for e in edges}, links)
        for directive in directives:
            self.assertEqual(text.count("    %s[\"" % directive), 1)

    def test_every_observed_type_link_type_triple_of_the_built_graph_has_an_edge(self):
        # SYSP_VC_ONTOLOGY_LOCATION_3: the descriptive edges must not drift from what the graph actually holds.
        built = ROOT / "docs" / "_build" / "html" / "needs.json"
        if not built.exists():
            self.skipTest("needs.json is produced by the documentation build; run docs/docs-build.py first")
        needs = next(iter(json.loads(built.read_text(encoding="utf-8"))["versions"].values()))["needs"]
        links = {l["option"] for l in load(OWN / "ontology.toml")["needs"]["extra_links"]}
        observed = {(n["type"], link, needs[target]["type"])
                    for n in needs.values() for link in links for target in n.get(link) or [] if target in needs}
        declared = {(e["from"], e["link"], e["to"]) for e in load(OWN / "ontology.toml")["syspilot"]["diagram_edges"]}
        self.assertTrue(observed)
        self.assertEqual(observed, declared)

    def test_no_live_artifact_still_names_the_old_ontology_path(self):
        files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
        offenders = []
        for name in files:
            # The location requirement states that the old path no longer exists; Change records and release notes are history.
            if name.startswith(("docs/changes/", "docs/releases/", "docs/releasenotes", "docs/syspilot/requirements/req_ontology_management.rst", "tests/test_acceptance_ontology_example")):
                continue
            path = ROOT / name
            if path.suffix in {".md", ".rst", ".py", ".toml", ".yml", ".yaml", ".json"} and path.is_file():
                if ".syspilot/ontology.toml" in path.read_text(encoding="utf-8", errors="ignore"):
                    offenders.append(name)
        self.assertEqual(offenders, [])

    def test_the_skill_names_no_fixed_path_or_syspilot_type_list(self):
        skill_text = (SKILLS / "syspilot.ontology" / "SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn(".syspilot/ontology.toml", skill_text)
        self.assertIn("needs_from_toml", skill_text)


class SetupOntologyTests(unittest.TestCase):
    """SYSP_VC_SETUP_ONTOLOGY_1: the fallback is the Example Ontology under the project-named folder; an existing ontology stays."""

    def setUp(self):
        self.text = SETUP.read_text(encoding="utf-8").replace("\r\n", "\n")

    def test_fallback_copies_the_example_folder_and_never_a_syspilot_ontology(self):
        self.assertIn("copy `docs/Example Ontology/` of the verified commit to `docs/<Project name> Ontology/`", self.text)
        self.assertIn("copy no Syspilot-owned ontology", self.text)
        self.assertIn("Install no `docs/Syspilot Ontology/ontology.md`", self.text)
        self.assertNotIn(".syspilot/ontology.toml", self.text)

    def test_existing_ontology_is_preserved_and_the_copy_happens_only_without_one(self):
        self.assertIn("Preserve it unchanged when present. Only when no ontology exists", self.text)
        self.assertIn("Existing ontology remains unchanged, or the folder", self.text)

    def test_mermaid_is_loaded_supplied_and_offered_only_as_an_additive_edit_for_existing_builds(self):
        template = re.search(r"```python\n(.*?)```", self.text.split("### Documentation Scaffold", 1)[1], re.S).group(1)
        self.assertIn('"sphinxcontrib.mermaid"', template)
        self.assertIn("sphinxcontrib-mermaid", (ROOT / "docs" / "requirements.txt").read_text(encoding="utf-8"))
        self.assertIn("the `sphinxcontrib.mermaid` extension only as additive edits that the User approves", self.text)

    def test_the_seeded_copy_is_identical_to_the_source_and_binds_in_a_generated_conf(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "docs" / "Acme Widgets Ontology"
            shutil.copytree(EXAMPLE, target)
            for name in ("ontology.toml", "ontology.md"):
                self.assertEqual((target / name).read_bytes(), (EXAMPLE / name).read_bytes())
            template = re.search(r"```python\n(.*?)```", self.text.split("### Documentation Scaffold", 1)[1], re.S).group(1)
            conf = template.replace("{ontology path relative to conf.py}", "Acme Widgets Ontology/ontology.toml")
            self.assertRegex(conf, r'(?m)^needs_from_toml = "Acme Widgets Ontology/ontology\.toml"$')


if __name__ == "__main__":
    unittest.main()
