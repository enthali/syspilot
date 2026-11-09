"""Requirement tests for the setup-feedback-2 Change: the generated documentation scaffold is built in a pristine fixture,
and the Setup Contract, its Requirements, and the neighbouring artifacts are checked against each other."""

import ast
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = "Acme Widgets"
SETUP = ROOT / "docs" / "Syspilot Contracts" / "setup.md"
EXAMPLE_ACTORS = ROOT / "docs" / "Example Actors"
EXAMPLE_CONTRACTS = ROOT / "docs" / "Example Contracts"
REQUIREMENTS = ROOT / "docs" / "syspilot" / "requirements"
IMPACT = ROOT / ".github" / "skills" / "syspilot.impact-python" / "scripts" / "get_need_links.py"
ROLE_CARDS = (
    "Project Manager", "Architect", "Developer", "Tester", "Quality",
    "Release", "Research", "Technical Writer", "Admin",
)
# Setup's Contract selection table: each installable Contract and the Contracts it requires.
SELECTIONS = {
    "contract documents only": ["contract-documents"],
    "change process": ["contract-documents", "change"],
    "release process": ["contract-documents", "release"],
    "process maintenance with its requirement": ["contract-documents", "change", "process-maintenance"],
    "every Contract": ["contract-documents", "change", "release", "process-maintenance"],
}


def read(path):
    return Path(path).read_text(encoding="utf-8")


def setup_text():
    return read(SETUP).replace("\r\n", "\n")


def scaffold_conf(ontology="../.syspilot/ontology.toml", name=PROJECT):
    """The docs/conf.py that Setup generates, filled from the definition the Contract carries."""
    section = setup_text().split("### Documentation Scaffold", 1)[1]
    template = re.search(r"```python\n(.*?)```", section, re.S).group(1)
    return template.replace("{confirmed project name}", name).replace("{ontology path relative to conf.py}", ontology)


def scaffold_index(name=PROJECT):
    """The generated docs/index.rst: the project name as title and a table of contents of the two registries."""
    return f"{name}\n{'=' * len(name)}\n\n.. toctree::\n   :maxdepth: 1\n\n   {PROJECT} Actors/index\n   {PROJECT} Contracts/index\n"


def registry_actors():
    roster = read(EXAMPLE_ACTORS / "index.md").split("## Roster", 1)[1].split("```{toctree}", 1)[0]
    entries = "\n".join(ROLE_CARDS)
    return f"# {PROJECT} Actors\n\n## Roster{roster}```{{toctree}}\n:hidden:\n\n{entries}\n```\n"


def registry_contracts(installed, hidden=True):
    index = read(EXAMPLE_CONTRACTS / "index.md").replace("\r\n", "\n")
    preamble = index.split("## Processes", 1)[0].replace("# Contracts", f"# {PROJECT} Contracts", 1)
    option = ":hidden:" if hidden else ":maxdepth: 1"
    return f"{preamble}## Processes\n\n```{{toctree}}\n{option}\n\n" + "\n".join(installed) + "\n```\n"


def build_target(folder, installed, hidden_actor_toctree=True, extra_conf=""):
    """Lay out a pristine target as Setup describes it and return the strict build's result."""
    root = Path(folder)
    docs = root / "docs"
    (root / ".syspilot").mkdir(parents=True)
    shutil.copy(ROOT / ".syspilot" / "ontology.toml", root / ".syspilot" / "ontology.toml")
    (docs / f"{PROJECT} Actors").mkdir(parents=True)
    (docs / f"{PROJECT} Contracts").mkdir(parents=True)
    (docs / "conf.py").write_text(scaffold_conf() + extra_conf, encoding="utf-8")
    (docs / "index.rst").write_text(scaffold_index(), encoding="utf-8")
    for card in ROLE_CARDS:
        shutil.copy(EXAMPLE_ACTORS / f"{card}.md", docs / f"{PROJECT} Actors" / f"{card}.md")
    actors = registry_actors()
    if not hidden_actor_toctree:
        actors = actors.split("```{toctree}", 1)[0]
    (docs / f"{PROJECT} Actors" / "index.md").write_text(actors, encoding="utf-8")
    for name in installed:
        shutil.copy(EXAMPLE_CONTRACTS / f"{name}.md", docs / f"{PROJECT} Contracts" / f"{name}.md")
    (docs / f"{PROJECT} Contracts" / "index.md").write_text(registry_contracts(installed), encoding="utf-8")
    return subprocess.run(
        [sys.executable, "-m", "sphinx", "-b", "html", str(docs), str(root / "build"), "-W", "--keep-going", "-q"],
        cwd=root, capture_output=True, text=True,
    )


def load_resolver():
    spec = importlib.util.spec_from_file_location("get_need_links", IMPACT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.resolve_ontology_path


class GeneratedScaffoldBuildTests(unittest.TestCase):
    """SYSP_REQ_SETUP_DOCS, SYSP_AC_SETUP_3: a pristine target builds with zero warnings for every Contract selection."""

    DEPRECATED = 'suppress_warnings = ["needs.deprecated"]\n'

    def test_every_contract_selection_builds_without_a_warning(self):
        for label, installed in SELECTIONS.items():
            with self.subTest(selection=label), tempfile.TemporaryDirectory() as folder:
                result = build_target(Path(folder) / "target", installed)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertNotIn("WARNING", result.stdout + result.stderr)

    def test_the_only_warnings_of_the_generated_scaffold_are_the_ontology_deprecations(self):
        # Locates the cause of a failure above: the shipped ontology uses options that the current Sphinx-Needs deprecates,
        # and Syspilot's own docs/conf.py suppresses them while the generated conf.py does not.
        for label, installed in SELECTIONS.items():
            with self.subTest(selection=label), tempfile.TemporaryDirectory() as folder:
                result = build_target(Path(folder) / "target", installed, extra_conf=self.DEPRECATED)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_a_registry_without_the_hidden_table_of_contents_is_orphaned(self):
        # Negative control: the build is strict enough to see what the hidden table of contents prevents.
        with tempfile.TemporaryDirectory() as folder:
            result = build_target(Path(folder) / "target", ["contract-documents"], hidden_actor_toctree=False,
                                  extra_conf=self.DEPRECATED)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("toctree", result.stdout + result.stderr)

    def test_a_contract_without_its_required_contract_breaks_the_build(self):
        # Negative control for the Requires column: process maintenance links the Change Process.
        with tempfile.TemporaryDirectory() as folder:
            result = build_target(Path(folder) / "target", ["contract-documents", "process-maintenance"],
                                  extra_conf=self.DEPRECATED)
            self.assertNotEqual(result.returncode, 0)

    def test_the_generated_conf_binds_a_literal_the_shipped_skills_resolve(self):
        with tempfile.TemporaryDirectory() as folder:
            docs = Path(folder) / "docs"
            docs.mkdir()
            (Path(folder) / ".syspilot").mkdir()
            ontology = Path(folder) / ".syspilot" / "ontology.toml"
            ontology.write_text("", encoding="utf-8")
            (docs / "conf.py").write_text(scaffold_conf(), encoding="utf-8")
            self.assertEqual(load_resolver()(docs / "conf.py"), ontology.resolve())

    def test_the_skills_reject_a_computed_binding_the_scaffold_must_not_use(self):
        with tempfile.TemporaryDirectory() as folder:
            conf = Path(folder) / "conf.py"
            conf.write_text("import os\nneeds_from_toml = os.path.join('..', 'o.toml')\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_resolver()(conf)

    def test_the_scaffold_names_no_source_project_value(self):
        conf = scaffold_conf(name=PROJECT)
        self.assertNotRegex(conf, r"\{[^}]*\}")
        tree = ast.parse(conf)
        assigned = {target.id for node in tree.body if isinstance(node, ast.Assign) for target in node.targets}
        project = [n.value.value for n in tree.body if isinstance(n, ast.Assign) and n.targets[0].id == "project"]
        self.assertEqual(project, [PROJECT])
        self.assertEqual(assigned, {"project", "extensions", "exclude_patterns", "needs_from_toml", "suppress_warnings"})
        # The ontology path itself names the .syspilot folder, which the target has after installation.
        for value in ("Syspilot", "logo", "templates", "static", "intersphinx", "ontology-reference"):
            self.assertNotIn(value, conf)
        self.assertNotIn("syspilot", conf.replace(".syspilot/ontology.toml", ""))
        self.assertNotIn("ontology-reference", scaffold_index())

    def test_the_scaffold_extensions_are_provided_by_the_installed_requirements(self):
        requirements = read(ROOT / "docs" / "requirements.txt")
        self.assertIn("myst-parser", requirements)
        self.assertIn("sphinx-needs", requirements)


class ContractTextCrossChecks(unittest.TestCase):
    """The Setup Contract, the Requirements, and the user guides must say the same thing."""

    def test_requirements_and_contract_agree_on_the_wait_times_and_paths(self):
        requirements = " ".join(read(REQUIREMENTS / "req_setup.rst").split())
        setup = " ".join(setup_text().split())
        for value in ("120 seconds", "60 seconds", ".jarvis/messages/queue.json", ".jarvis/messages/autodelivery.json",
                      "jarvis_createActor", "jarvis_core_createActor"):
            with self.subTest(value=value):
                self.assertIn(value, requirements)
                self.assertIn(value, setup)

    def test_the_transfer_uses_initial_message_only_for_the_admin_creation_and_never_writes_the_queue(self):
        transfer = setup_text().split("### Transfer To The Admin", 1)[1].split("\n## ", 1)[0]
        self.assertIn("Setup never writes the queue file", transfer)
        for match in re.finditer(r"initialMessage", transfer):
            context = transfer[max(0, match.start() - 80):match.start()]
            with self.subTest(context=context):
                self.assertRegex(context, r"(request text as|drops an) `$")

    def test_the_user_guide_says_end_to_end_installation_is_not_yet_verified(self):
        guide = " ".join(read(ROOT / "docs" / "getting-started.md").split())
        self.assertRegex(guide, r"End-to-end installation, actor discovery, target build, baseline[^.]*not")

    def test_the_old_session_gate_is_gone_from_every_normative_artifact(self):
        for path in (SETUP, REQUIREMENTS / "req_setup.rst", ROOT / "docs" / "syspilot" / "userstories" / "us_setup.rst",
                     ROOT / "docs" / "getting-started.md", ROOT / "docs" / "operations.md"):
            text = " ".join(read(path).split())
            for match in re.finditer(r"jarvis_listChatSessions", text):
                context = text[max(0, match.start() - 160):match.end() + 160]
                with self.subTest(document=path.name):
                    self.assertRegex(context, r"no longer|removed|does not exist")

    def test_every_setup_requirement_has_a_verification_criterion_and_a_realization(self):
        text = read(REQUIREMENTS / "req_setup.rst")
        for need in ("SETUP", "SETUP_CONTINUATION", "SETUP_ACTORS", "SETUP_GATES", "SETUP_DOCS", "SETUP_JARVIS"):
            with self.subTest(need=need):
                self.assertRegex(text, rf":verifies: SYSP_REQ_{need}\b")
                block = re.search(rf"\.\. req::[^\n]*\n\s+:id: SYSP_REQ_{need}\n(.*?)\n\n", text, re.S).group(1)
                self.assertIn(":realized_by: docs/Syspilot Contracts/setup.md", block)

    def test_every_gate_requirement_status_word_is_the_one_the_contract_uses(self):
        requirement = read(REQUIREMENTS / "req_setup.rst")
        gates = requirement.split("SYSP_REQ_SETUP_GATES", 1)[1].split(".. vc::", 1)[0]
        for status in ("pending", "passed", "failed", "blocked", "verified", "handed off"):
            with self.subTest(status=status):
                self.assertIn(status, gates)
        phase = setup_text().split("## Phase 5: Verify Installed Outcome", 1)[1].split("\n## ", 1)[0]
        rows = [line for line in phase.splitlines() if line.startswith("|")][2:]
        self.assertEqual(len(rows), 8)
        discovery = [row for row in rows if "discovery" in row.lower()]
        documentation = [row for row in rows if "documentation" in row.lower()]
        self.assertTrue(discovery and documentation)


class SetupJarvisExtensionScenario(unittest.TestCase):
    """SYSP_AC_SETUP_5, SYSP_REQ_SETUP_JARVIS: each element of the criterion is realized in Phase 1 of the Contract.

    Text level only: no run of Setup in an instance that lacks Jarvis Core exists, so detection in the hosting
    instance, the consent, the installation and the reload are not demonstrated here.
    """

    @staticmethod
    def phase_one():
        return " ".join(setup_text().split("## Phase 1", 1)[1].split("## Phase 2", 1)[0].split())

    def test_the_missing_extension_is_detected_in_the_instance_that_hosts_the_session(self):
        phase = self.phase_one()
        self.assertIn("from evidence about the running host and not from the first `code` command on the search path", phase)
        self.assertIn("the shell's ancestry", phase)
        self.assertIn("`--user-data-dir` and `--extensions-dir`", phase)
        self.assertIn("accept no version read anywhere else", phase)

    def test_nothing_is_installed_without_consent_that_names_the_receiving_instance(self):
        phase = self.phase_one()
        for fragment in ("the extension identifier `enthali.jarvis-core`", "the Marketplace as its source",
                         "the instance and profile that receive it", "Install nothing without it"):
            self.assertIn(fragment, phase)
        self.assertLess(phase.index("Install nothing without it"), phase.index("After consent, install only"))

    def test_the_installation_is_rechecked_with_the_same_tool_and_the_tools_the_session_offers(self):
        phase = self.phase_one()
        self.assertIn("Read the extension list again with the same tool and directories", phase)
        self.assertIn("an installed extension is not an available tool", phase)

    def test_a_reload_is_asked_only_for_an_extension_installed_in_this_run_whose_tools_are_missing(self):
        phase = self.phase_one()
        self.assertIn("ask the User to reload the window only then", phase)
        self.assertIn("When the tools are offered after the installation, continue without a reload", phase)
        self.assertIn("a new chat in the reloaded window to continue the Pristine Syspilot Setup recorded in `.syspilot/setup-contract.md`",
                      phase)

    def test_a_refusal_a_failed_installation_and_an_unidentified_instance_are_blockers_with_the_manual_path(self):
        phase = self.phase_one()
        self.assertIn("When the User refuses, stop with a recorded blocker and the manual path above", phase)
        self.assertIn("record the exit status and the tool's output as a blocker, give the manual path, and do not continue as if it had succeeded",
                      phase)
        self.assertIn("When the hosting instance cannot be identified with such evidence", phase)
        self.assertIn("claim no version", phase)

    def test_the_requirement_and_the_criterion_name_the_same_conditions(self):
        text = " ".join(read(ROOT / "docs" / "syspilot" / "userstories" / "us_setup.rst").split())
        criterion = text.split(":id: SYSP_AC_SETUP_5", 1)[1]
        for fragment in ("another VS Code installation on the machine has it", "only after the User's consent",
                         "asks for a reload only when the installed extension's tools are not offered",
                         "a refusal or a failed installation as a blocker with a manual path"):
            self.assertIn(fragment, criterion)
        requirement = " ".join(read(REQUIREMENTS / "req_setup.rst").split())
        self.assertIn(":implements: SYSP_US_SETUP :specializes: SYSP_REQ_SETUP :realized_by: docs/Syspilot Contracts/setup.md",
                      requirement.split(":id: SYSP_REQ_SETUP_JARVIS", 1)[1])
        self.assertIn(":verifies: SYSP_REQ_SETUP_JARVIS", requirement)


class ProjectNamedFoldersScenario(unittest.TestCase):
    """SYSP_AC_SETUP_6, SYSP_REQ_SETUP_NAMING: installed folders carry the confirmed project name, never Syspilot's."""

    @staticmethod
    def text():
        return " ".join(setup_text().split())

    def test_the_name_is_confirmed_before_any_write_and_validated_as_a_folder_name(self):
        text = self.text()
        step = text.split("6. Confirm the project name", 1)[1].split(" 7. ", 1)[0]
        for fragment in ("before any destination is verified or written", "ask the User to confirm or change it",
                         "`Project name` header field", "reserved Windows device name", "is asked for again and never altered",
                         "before the Actors folder scan and the tool check", "A resumed Setup keeps the recorded name",
                         "The name stays fixed once the first write to an installed destination in Phase 4"):
            self.assertIn(fragment, step)

    def test_every_installed_destination_is_project_named_and_none_names_syspilot(self):
        text = setup_text().split("## Phase 6", 1)[0]
        paths = set(re.findall(r"`(docs/[^`]*?(?:Actors|Contracts)/[^`]*)`", text))
        paths = {path for path in paths if not path.startswith(("docs/Example", "docs/Syspilot Contracts/"))}
        self.assertTrue(paths)
        for path in sorted(paths):
            with self.subTest(path=path):
                self.assertTrue(path.startswith(("docs/<Project name> Actors/", "docs/<Project name> Contracts/")), path)
        self.assertNotIn("docs/Syspilot Actors/", text)
        # The source folder of this Contract is named only to exclude it from the copied files.
        for line in text.splitlines():
            if "`docs/Syspilot Contracts/`" in line:
                self.assertIn("are not among them", line)
    def test_seeded_copies_stay_unchanged_while_the_generated_registries_take_the_name(self):
        text = self.text()
        self.assertIn("seeded copy", text)
        self.assertIn("titled `<Project name> Actors`", text)
        self.assertIn("titled `<Project name> Contracts`", text)
        self.assertIn("each identical to its source", text)

    def test_a_target_with_a_spaced_project_name_builds_strictly_and_a_stale_reference_does_not(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "target"
            result = build_target(target, ["contract-documents"], extra_conf=GeneratedScaffoldBuildTests.DEPRECATED)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue((target / "docs" / f"{PROJECT} Actors" / "index.md").is_file())
            self.assertFalse((target / "docs" / "Syspilot Actors").exists())
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "target"
            build_target(target, ["contract-documents"], extra_conf=GeneratedScaffoldBuildTests.DEPRECATED)
            index = target / "docs" / "index.rst"
            index.write_text(index.read_text(encoding="utf-8").replace(f"{PROJECT} Actors/index", "Syspilot Actors/index"),
                             encoding="utf-8")
            again = subprocess.run([sys.executable, "-m", "sphinx", "-b", "html", str(target / "docs"), str(target / "b2"),
                                    "-W", "--keep-going", "-q"], cwd=target, capture_output=True, text=True)
            self.assertNotEqual(again.returncode, 0)


class UserStoryTests(unittest.TestCase):
    def test_every_acceptance_criterion_validates_the_setup_story_and_has_a_scenario(self):
        text = read(ROOT / "docs" / "syspilot" / "userstories" / "us_setup.rst")
        ids = re.findall(r":id: (SYSP_AC_SETUP_\d+)", text)
        self.assertEqual(ids, [f"SYSP_AC_SETUP_{number}" for number in range(1, 7)])
        self.assertEqual(len(re.findall(r":validates: SYSP_US_SETUP", text)), 6)


if __name__ == "__main__":
    unittest.main()
