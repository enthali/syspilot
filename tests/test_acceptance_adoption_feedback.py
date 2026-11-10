"""Requirement tests for the vse-adoption-feedback Change, written from its Scope only."""

import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "docs" / "Syspilot Contracts"
ACTORS = ROOT / "docs" / "Syspilot Actors"
EXAMPLE_CONTRACTS = ROOT / "docs" / "Example Contracts"
CLIS = (
    ("syspilot.impact-python", "get_need_links.py", ["SYSP_REQ_ADMIN", "--flat", "--no-build"]),
    ("syspilot.mece", "analyze_mece.py", ["SYSP_REQ_ADMIN", "--scope", "all-type"]),
    ("syspilot.trace", "analyze_trace.py", ["SYSP_REQ_ADMIN", "--depth", "1"]),
)
INVALID_BINDINGS = {
    "computed": "import os\nneeds_from_toml = os.path.join('a', 'b.toml')\n",
    "empty": 'needs_from_toml = ""\n',
    "syntax error": "needs_from_toml = (\n",
    "nested in a block": "if True:\n    needs_from_toml = 'a.toml'\n",
}


def read(path):
    return path.read_text(encoding="utf-8")


def listed_kinds():
    """Contract documents both registries list under Processes and Examples, as (section, path)."""
    kinds = []
    for folder in (CONTRACTS, EXAMPLE_CONTRACTS):
        for block in re.split(r"(?m)^## ", read(folder / "index.md"))[1:]:
            section = block.splitlines()[0].strip()
            if section not in ("Processes", "Examples"):
                continue
            for toctree in re.findall(r"```\{toctree\}\n(.*?)```", block, re.S):
                for line in toctree.splitlines():
                    entry = line.strip()
                    if entry and not entry.startswith(":") and entry != "contract-documents":
                        kinds.append((section, folder / f"{entry}.md"))
    return kinds


class SharedContractRulesTests(unittest.TestCase):
    """Every Contract kind in the registry carries the five shared rules of contract-documents.md."""

    def test_registry_lists_the_known_kinds(self):
        names = {path.stem for _, path in listed_kinds()}
        self.assertTrue({"change", "release", "setup", "process-maintenance"} <= names)
        for _, path in listed_kinds():
            self.assertTrue(path.exists(), path)

    def test_each_kind_carries_the_handover_log(self):
        for _, path in listed_kinds():
            text = read(path)
            with self.subTest(kind=path.stem):
                self.assertRegex(text, r"(?m)^## Handover log$")
                self.assertIn("| Date | Time | From | To | Note |", text)
                self.assertIn("system clock", text)

    def test_each_handover_log_states_the_date_and_time_formats(self):
        for _, path in listed_kinds():
            section = read(path).split("## Handover log", 1)[1].split("\n## ", 1)[0]
            with self.subTest(kind=path.stem):
                self.assertIn("`YYYY-MM-DD`", section)
                self.assertIn("`HH:MM`", section)
                self.assertIn("24-hour local time", section)

    def test_the_method_states_the_formats_once_for_all_kinds(self):
        rule = read(CONTRACTS / "contract-documents.md").split("Shared Rules Of Every Contract Kind", 1)[1]
        rule = rule.split("2. **Scope change.**", 1)[0]
        for needle in ("`YYYY-MM-DD`", "`HH:MM`", "24-hour local time"):
            with self.subTest(needle=needle):
                self.assertIn(needle, rule)

    def test_each_kind_states_the_scope_change_rule(self):
        for _, path in listed_kinds():
            text = read(path)
            with self.subTest(kind=path.stem):
                self.assertTrue(
                    "**Scope change:**" in text or "widens the approved scope" in text,
                    "no scope-change statement",
                )

    def test_each_kind_states_the_single_ownership_statement(self):
        for _, path in listed_kinds():
            text = read(path)
            with self.subTest(kind=path.stem):
                self.assertTrue(
                    "**Ownership:**" in text or "only statement of who owns" in text,
                    "no ownership statement",
                )

    def test_each_kind_presents_the_contract_at_the_user_owned_gate(self):
        for section, path in listed_kinds():
            text = read(path)
            marker = "Present" if path.stem == "process-maintenance" else "User's editor"
            with self.subTest(kind=path.stem):
                self.assertIn(marker, text)

    def test_each_handover_log_states_what_a_note_holds(self):
        for _, path in listed_kinds():
            section = read(path).split("## Handover log", 1)[1].split("\n## ", 1)[0]
            with self.subTest(kind=path.stem):
                self.assertIn("facts that change the next owner's situation", section)
                self.assertRegex(section, r"evidence stays in the ")

    def test_the_method_states_what_a_note_holds_once_for_all_kinds(self):
        rule = read(CONTRACTS / "contract-documents.md").split("Shared Rules Of Every Contract Kind", 1)[1]
        rule = rule.split("2. **Scope change.**", 1)[0]
        self.assertIn("facts that change the next owner's situation", rule)
        self.assertIn("evidence stays in the owner's section and remaining work in the open rows", rule)

    def test_the_requirements_of_the_kinds_carry_what_a_note_holds(self):
        requirements = ROOT / "docs" / "syspilot" / "requirements"
        for name in ("req_contract_documents", "req_change_contract", "req_setup"):
            text = " ".join(read(requirements / f"{name}.rst").split())
            with self.subTest(requirement=name):
                self.assertIn("next owner's situation", text)
        release = " ".join(read(requirements / "req_release_contract.rst").split())
        self.assertIn("Handover log with its short note", release)

    def test_the_handoff_message_carries_the_contract_path_and_the_commit_only(self):
        instruction = read(ROOT / ".github" / "instructions" / "syspilot.contract-handling.instructions.md")
        handoff = next(line for line in instruction.splitlines() if line.startswith("- **HANDOFF**"))
        self.assertIn("Contract path and the commit", handoff)
        self.assertIn("the completed outcome is the last Handover-log line", handoff)
        self.assertIn("remaining work is in the open rows", handoff)
        self.assertNotIn("completed outcome, and remaining work", handoff)
        example = " ".join(read(EXAMPLE_CONTRACTS / "process-maintenance.md").split())
        self.assertIn("before sending the Contract path and the commit", example)
        self.assertNotIn("sending its path, commit, completed outcome", example)
        requirement = " ".join(read(ROOT / "docs" / "syspilot" / "requirements" / "req_contract_handling.rst").split())
        self.assertIn("names the Contract path and the committed state in the ``HANDOFF`` message", requirement)

    def test_setup_names_the_executor_as_sole_owner_of_the_phase_5_gates(self):
        setup = read(CONTRACTS / "setup.md")
        phase = setup.split("## Phase 5: Verify Installed Outcome", 1)[1].split("\n## ", 1)[0]
        self.assertIn("owns every gate", phase)
        self.assertIn("the User owns none", phase)
        table_end = max(index for index, line in enumerate(phase.splitlines()) if line.startswith("|"))
        sentence = next(index for index, line in enumerate(phase.splitlines()) if "owns every gate" in line)
        self.assertGreater(sentence, table_end, "ownership sentence belongs directly under the gate table")
        self.assertRegex(
            read(ROOT / "docs" / "syspilot" / "requirements" / "req_setup.rst"),
            r"verification-gate ownership\s+naming the executor as sole owner",
        )

    def test_refresh_on_acknowledgement_is_stated_once_for_all_kinds(self):
        instructions = read(ROOT / ".github" / "instructions" / "syspilot.contract-handling.instructions.md")
        self.assertIn("re-read your own `context.md`", instructions)
        self.assertIn("Contract instance", instructions)

    def test_the_shared_rules_are_listed_in_the_method(self):
        method = read(CONTRACTS / "contract-documents.md")
        self.assertIn("Shared Rules Of Every Contract Kind", method)


class ProcessMaintenanceExampleTests(unittest.TestCase):
    """Package E: the example states what the Needs graph checks, and who presents the outcome."""

    def setUp(self):
        self.example = read(EXAMPLE_CONTRACTS / "process-maintenance.md")

    def test_the_needs_graph_boundary_is_stated_without_overstatement(self):
        opening = self.example.split("\n## ", 1)[0]
        self.assertIn("Needs graph covers specification Needs and their realization links", opening)
        self.assertIn("Quality's recorded review verifies the Markdown content", opening)
        for text in (self.example, read(EXAMPLE_CONTRACTS / "index.md")):
            self.assertNotRegex(text, r"specification consistency[^.]*Needs graph")

    def test_the_project_manager_presents_the_verified_outcome(self):
        steps = self.example.split("## Initialization And Handoffs", 1)[1].split("\n## ", 1)[0]
        step = re.search(r"(?m)^5\. (.+)$", steps).group(1)
        self.assertIn("Quality communicates its `proceed` judgment and supporting evidence directly to the Project Manager", step)
        self.assertIn("The Project Manager then presents the verified outcome to the User", step)

    def test_the_requirement_names_the_same_presenter(self):
        requirement = read(ROOT / "docs" / "syspilot" / "requirements" / "req_process_maintenance.rst")
        self.assertRegex(requirement, r"names the Project Manager as the actor that presents the verified outcome")

    def test_the_example_lies_directly_in_the_flat_example_folder(self):
        index = read(EXAMPLE_CONTRACTS / "index.md")
        self.assertNotIn("examples/", index)
        self.assertNotIn("## Examples", index)
        self.assertTrue((EXAMPLE_CONTRACTS / "process-maintenance.md").exists())
        self.assertFalse((EXAMPLE_CONTRACTS / "examples").exists())
        self.assertFalse((CONTRACTS / "examples").exists())


class ReleaseVersionCheckTests(unittest.TestCase):
    """The automated version check of the Release Process preflight, tested through its command line."""

    CHECKER = ROOT / "scripts" / "check_release_version.py"

    def run_check(self, tag, notes_text, conf_text="matching", extra=()):
        """Run the checker on a notes file and a documentation configuration that live outside the checked folder."""
        with tempfile.TemporaryDirectory() as folder, tempfile.TemporaryDirectory() as other:
            root = Path(folder)
            notes = root / "releasenotes.md"
            notes.write_bytes(notes_text.encode("utf-8"))
            conf = Path(other) / "conf.py"
            conf.write_text(f'release = "{tag[1:]}"\n' if conf_text == "matching" else conf_text, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(self.CHECKER), tag, "--notes", str(notes), "--conf", str(conf), *extra],
                cwd=root, capture_output=True, text=True,
            )
            self.assertEqual(sorted(path.name for path in root.iterdir()), ["releasenotes.md"], "check wrote a file")
            self.assertEqual(notes.read_bytes(), notes_text.encode("utf-8"))
            return result
    def test_one_heading_with_or_without_title_passes(self):
        for heading in ("## v1.2.3", "## v1.2.3 - Title"):
            with self.subTest(heading=heading):
                self.assertEqual(self.run_check("v1.2.3", f"# Notes\n\n{heading}\n\nText\n").returncode, 0)

    def test_wrong_duplicated_or_missing_heading_fails(self):
        cases = {
            "missing": "# Notes\n\n## v1.2.2\n",
            "duplicated": "## v1.2.3\n\n## v1.2.3 - Again\n",
            "longer version only": "## v1.2.30\n",
            "no v prefix": "## 1.2.3\n",
            "wrong level": "### v1.2.3\n",
        }
        for label, notes in cases.items():
            with self.subTest(case=label):
                result = self.run_check("v1.2.3", notes)
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("Traceback", result.stderr)

    def test_a_tag_that_is_not_the_newest_heading_fails_and_names_it(self):
        result = self.run_check("v1.2.3", "## v1.2.4\n\n## v1.2.3\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("v1.2.4", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_a_documentation_release_that_differs_from_the_tag_fails_and_names_both(self):
        for label, conf in {"other version": 'release = "1.2.2"\n', "no release": "project = 'x'\n"}.items():
            with self.subTest(case=label):
                result = self.run_check("v1.2.3", "## v1.2.3\n", conf_text=conf)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("1.2.3", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_the_release_text_is_written_only_after_a_passing_check(self):
        notes = "## v1.2.3 - T\n\nBody\n\n## v1.2.2\n\nOld\n"
        for label, tag_conf, expected in (("pass", "matching", "## v1.2.3 - T\n\nBody\n"), ("fail", 'release = "9.9.9"\n', None)):
            with self.subTest(case=label), tempfile.TemporaryDirectory() as out:
                target = Path(out) / "current.md"
                result = self.run_check("v1.2.3", notes, conf_text=tag_conf, extra=("--write-notes", str(target)))
                if expected is None:
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(target.exists())
                else:
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(target.read_text(encoding="utf-8"), expected)
    def test_malformed_tags_fail_even_with_a_matching_heading(self):
        for tag in ("v1.2", "1.2.3", "v01.2.3", "v1.2.3-rc1", "V1.2.3", "v1.2.3.4", ""):
            with self.subTest(tag=tag):
                result = self.run_check(tag, f"## {tag}\n")
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("Traceback", result.stderr)

    def test_missing_notes_file_fails_without_a_traceback(self):
        result = subprocess.run(
            [sys.executable, str(self.CHECKER), "v1.2.3", "--notes", str(ROOT / "no-such-notes.md")],
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Traceback", result.stderr)

    def test_the_published_notes_pass_for_their_latest_version(self):
        latest = re.search(r"(?m)^## (v\d+\.\d+\.\d+)", read(ROOT / "docs" / "releasenotes.md")).group(1)
        result = subprocess.run(
            [sys.executable, str(self.CHECKER), latest], capture_output=True, text=True, cwd=ROOT,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


class SkillBindingFailureTests(unittest.TestCase):
    """Package C: an unusable binding is an explicit failure for every skill, never a fallback."""

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name) / "project"
        for skill, script, _ in CLIS:
            relative = Path(".github") / "skills" / skill / "scripts" / script
            (self.root / relative).parent.mkdir(parents=True)
            shutil.copyfile(ROOT / relative, self.root / relative)
        (self.root / "docs").mkdir()
        # A fixed default location must not rescue a failed binding.
        (self.root / ".syspilot").mkdir()
        shutil.copyfile(ROOT / ".syspilot" / "ontology.toml", self.root / ".syspilot" / "ontology.toml")

    def run_cli(self, skill, script, args):
        path = self.root / ".github" / "skills" / skill / "scripts" / script
        return subprocess.run(
            [sys.executable, str(path), *args],
            cwd=self.root.parent, capture_output=True, text=True,
        )

    def test_unusable_binding_fails_with_guidance_for_every_skill(self):
        for label, source in INVALID_BINDINGS.items():
            (self.root / "docs" / "conf.py").write_text(source, encoding="utf-8")
            for skill, script, args in CLIS:
                with self.subTest(binding=label, skill=skill):
                    result = self.run_cli(skill, script, args)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("--ontology", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)

    def test_absent_configuration_fails_for_every_skill(self):
        for skill, script, args in CLIS:
            with self.subTest(skill=skill):
                result = self.run_cli(skill, script, args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("needs_from_toml", result.stderr)


class ActorRosterTests(unittest.TestCase):
    """Package A: nine role cards, each registered and each required by Setup."""

    def test_role_cards_registry_and_setup_agree_on_nine(self):
        cards = sorted(path.stem for path in ACTORS.glob("*.md") if path.name != "index.md")
        self.assertEqual(len(cards), 9)
        self.assertIn("Admin", cards)
        registry = read(ACTORS / "index.md")
        setup = read(CONTRACTS / "setup.md")
        for name in cards:
            with self.subTest(actor=name):
                self.assertIn(f"{name.replace(' ', '%20')}.md", registry)
                self.assertIn(f"docs/<Project name> Actors/{name}.md", setup)

    def test_role_cards_name_no_project(self):
        for path in ACTORS.glob("*.md"):
            with self.subTest(card=path.name):
                self.assertNotRegex(read(path), r"Jarvis-VSE|\bVSE\b")


class ChangeTemplateTests(unittest.TestCase):
    """Package B: the canonical Change template carries the adopted rules."""

    def setUp(self):
        self.template = read(CONTRACTS / "change.md")

    def test_adopted_sections_and_rules_are_present(self):
        for needle in (
            "## Handover log",
            "## Infrastructure Impact",
            "### Ontology Binding",
            "**Scope change:**",
            "**Ownership:**",
            "open the Contract document in the User's editor",
            "system clock",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, self.template)

    def test_handover_log_has_separate_date_and_time_columns(self):
        self.assertIn("| Date | Time | From | To | Note |", self.template)

    def test_owner_is_named_only_in_the_artifact_table(self):
        self.assertNotRegex(self.template, r"(?m)^\*\*Owner:\*\*")

    def test_missing_automation_is_an_open_quality_issue(self):
        self.assertIn("A missing automation is an open issue", self.template)


class ReleaseProcessTests(unittest.TestCase):
    """Package B: the Release Process states only what the release workflow does."""

    def setUp(self):
        self.process = read(CONTRACTS / "release.md")
        self.workflow = read(ROOT / ".github" / "workflows" / "release.yml")

    def test_process_is_registered_and_installed_by_setup(self):
        self.assertRegex(read(CONTRACTS / "index.md"), r"(?m)^release$")
        self.assertIn("Release Process", read(CONTRACTS / "setup.md"))

    def test_preflight_commands_run_in_the_release_workflow_in_the_same_order(self):
        commands = (
            "uv run python docs/test_docs_build.py -v",
            "uv run python docs/docs-build.py clean",
            "uv run python -m unittest discover -s tests -v",
        )
        positions = []
        for command in commands:
            with self.subTest(command=command):
                self.assertIn(command, self.process)
                self.assertIn(command, self.workflow)
                positions.append((self.process.index(command), self.workflow.index(command)))
        self.assertEqual(positions, sorted(positions))

    def test_version_check_follows_the_three_commands_and_precedes_the_validation_run(self):
        check = "uv run python scripts/check_release_version.py v{version}"
        self.assertTrue((ROOT / "scripts" / "check_release_version.py").exists())
        order = [
            self.process.index("uv run python -m unittest discover -s tests -v"),
            self.process.index(check),
            self.process.index("validation-only `workflow_dispatch` run"),
        ]
        self.assertEqual(order, sorted(order))

    def test_publication_verifies_the_record_rule_before_the_push(self):
        publication = self.process.split("## Publication")[1]
        auth = publication.split("\n1. ", 1)[1].split("\n2. ", 1)[0]
        check = publication.split("\n2. ", 1)[1].split("\n3. ", 1)[0]
        later = publication.split("\n6. ", 1)[1].split("\n\n", 1)[0]
        for fragment in ("commit it on `development` as a commit that changes only this record",
                         "after P and before the merge", "so that R contains it"):
            self.assertIn(fragment, auth)
        for fragment in ("P is an ancestor of R", "exactly `docs/changes/release-v{version}.md`",
                         "no change in the protected content", "stops the release",
                         "every second-level heading of the Release Contract template is present at R",
                         "Quality and Release therefore review the complete difference from P to R before publication",
                         "uv run python scripts/check_release_record.py {preflighted commit} {release commit} v{version}",
                         "exits 0 or 1 with the failing condition first on stderr"):
            self.assertIn(fragment, check)
        self.assertIn("a later commit that changes only this record", later)
        self.assertIn("It does not move the tag", later)
        self.assertNotIn("git diff --quiet", publication)
        self.assertLess(publication.index("Record the User's explicit authorization"), publication.index("Merge `development` into `main`"))
        self.assertLess(publication.index("P is an ancestor of R"), publication.index("Push `main` first"))

    def test_the_failure_guarantee_is_limited_to_prerequisites_and_a_partial_publication_is_named(self):
        process = " ".join(self.process.split())
        self.assertIn("This includes a partial publication, in which the documentation was published and a later job failed", process)
        requirement = " ".join(read(ROOT / "docs" / "syspilot" / "requirements" / "req_release_contract.rst").split())
        self.assertIn("A failure of the validation or of the documentation build after the tag publishes nothing", process)
        self.assertIn("leaves a partial publication that the failure path in Publication handles", process)
        self.assertIn("a failure of the validation or of the documentation build after the tag publishes nothing", requirement)
        self.assertIn("leaves a partial publication", requirement)
        for text in (process, requirement):
            self.assertNotRegex(text, r"(?i)(?<!validation or of the documentation build )after the tag publishes (nothing|anything)(?!, because publication follows)")
    def test_workflow_supports_the_validation_only_run_the_process_relies_on(self):
        self.assertIn("workflow_dispatch:", self.workflow)
        for job in ("publish-docs", "create-release"):
            with self.subTest(job=job):
                block = self.workflow.split(f"  {job}:")[1].split("\n  create-release:")[0]
                self.assertIn("github.event_name == 'push'", block)

    def test_trigger_list_excepts_the_release_notes_only_while_heading_parsing_stays_in_two_files(self):
        row = next(line for line in self.process.splitlines() if line.startswith("| Workflow input changed |"))
        self.assertIn("except `docs/releasenotes.md`", row)
        self.assertIn("only while release-heading parsing stays in `scripts/check_release_version.py` and `docs/conf.py`", row)
        self.assertIn("a file that takes over such parsing joins the list", row)

    def test_release_headings_are_parsed_only_by_the_version_checker_and_imported_by_the_documentation_configuration(self):
        conf = read(ROOT / "docs" / "conf.py")
        self.assertIn("check_release_version.py", conf)
        self.assertIn('_checker["newest_release"]', conf)
        parsers = []
        for folder in ("scripts", "docs", ".github"):
            for path in (ROOT / folder).rglob("*"):
                if path.suffix in (".py", ".yml", ".toml") and path.is_file():
                    if re.search(r"## v|newest_release", path.read_text(encoding="utf-8", errors="replace")):
                        parsers.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(sorted(parsers), ["docs/conf.py", "scripts/check_release_record.py", "scripts/check_release_version.py"])

    def test_release_notes_headings_follow_the_published_form(self):
        headings = re.findall(r"(?m)^## (v\d+\.\d+\.\d+.*)$", read(ROOT / "docs" / "releasenotes.md"))
        self.assertTrue(headings)
        pattern = re.compile(r"v(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:\s+-\s+.+)?")
        for heading in headings:
            with self.subTest(heading=heading):
                self.assertRegex(heading, pattern)
        self.assertEqual(len(headings), len(set(h.split()[0] for h in headings)))


if __name__ == "__main__":
    unittest.main()
