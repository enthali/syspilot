"""Unit tests for the Setup Contract realization of SYSP_REQ_SETUP_CONTINUATION, _ACTORS, _GATES, and _DOCS."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETUP = (ROOT / "docs" / "Syspilot Contracts" / "setup.md").read_text(encoding="utf-8")


def section(heading):
    return SETUP.split(heading, 1)[1].split("\n## ", 1)[0]


class ToolsAndVersionTests(unittest.TestCase):
    def test_minimum_jarvis_version_and_no_removed_tool_as_instruction(self):
        self.assertIn("Jarvis Core 0.32.0 or newer", SETUP)
        self.assertNotIn("0.25", SETUP)
        for line in SETUP.splitlines():
            if "jarvis_listChatSessions" in line:
                self.assertIn("no longer offers", line)

    def test_each_tool_is_recorded_by_name_and_createactor_gates_target_writes(self):
        phase = section("## Phase 1")
        for tool in ("jarvis_createActor", "jarvis_listActors", "jarvis_sendMessage", "jarvis_receiveMessage"):
            self.assertIn(f"`{tool}`", phase)
        self.assertIn("before any write to the target other than this record", phase)
        self.assertIn("jarvis_core_createActor", phase)
        self.assertIn("manual creation path", phase)

    def test_before_state_is_a_scan_recorded_before_the_tool_check(self):
        phase = section("## Phase 1")
        self.assertIn("This is a scan and not a listing", phase)
        self.assertLess(phase.index("6. Confirm the project name"), phase.index("7. Record the Actors folder scan"))
        self.assertLess(phase.index("7. Record the Actors folder scan"), phase.index("8. Record, per tool name"))
        self.assertIn("A resumed Setup keeps this recorded scan", phase)


    def test_jarvis_core_is_established_in_the_hosting_instance_with_consent(self):
        phase = section("## Phase 1")
        step = phase.split("5. Verify VS Code", 1)[1].split("\n6. ", 1)[0]
        self.assertIn("from the shell's ancestry", step)
        self.assertIn("`--user-data-dir`", step)
        self.assertIn("`--extensions-dir`", step)
        self.assertIn("not from the first `code` command on the search path", step)
        self.assertIn("accept no version read anywhere else", step)
        self.assertIn("cannot be identified", step)
        self.assertIn("install nothing, claim no version", step)
        self.assertIn("ask for consent there. Install nothing without it", step)
        self.assertIn("the Marketplace as its source", step)
        self.assertIn("install only `enthali.jarvis-core`", step)
        self.assertIn("edit no User or project setting", step)
        self.assertIn("exit status", step)
        self.assertIn("Read the extension list again with the same tool and directories", step)
        self.assertLess(step.index("Identify the hosting instance"), step.index("Read the extension list with"))
        self.assertLess(step.index("ask for consent"), step.index("install only"))

    def test_reload_is_a_distinct_condition_asked_only_when_tools_are_missing_after_install(self):
        phase = section("## Phase 1")
        self.assertIn("installed extension whose tools the session does not offer as a distinct condition", phase)
        self.assertIn("ask the User to reload the window only then", phase)
        self.assertIn("keeps the recorded before scan", phase)
        self.assertIn("Record that the reload was requested and that the resume prompt was given", phase)
        self.assertIn("to continue the Pristine Syspilot Setup recorded in `.syspilot/setup-contract.md` and to read that record first", phase)
        self.assertIn("composed under the language rule of the Transfer To The Admin section", phase)
        self.assertIn("reads the Jarvis version and its tools again", phase)
        self.assertIn("| Jarvis Core instance and installation | pending | pending |", SETUP)


class ActorCreationTests(unittest.TestCase):
    def test_setup_writes_no_actor_files_and_uses_no_initial_message(self):
        text = SETUP.split("### Syspilot Actor Setup", 1)[1].split("\n## ", 1)[0]
        self.assertIn("Setup writes no `actor.yaml` or `context.md` itself", text)
        self.assertIn("without `initialMessage`", text)
        self.assertIn("leave the Admin to the Transfer To The Admin section", text)
        self.assertNotIn("Setup writes these files directly", SETUP)
        self.assertNotIn("does not call `jarvis_createActor`", SETUP)

    def test_references_are_root_relative_code_spans_not_links(self):
        text = SETUP.split("### Syspilot Actor Setup", 1)[1].split("\n## ", 1)[0]
        self.assertIn("project-root-relative", text)
        self.assertIn("never as relative links", text)
        self.assertNotIn("../", text)

    def test_pre_existing_actors_and_manual_path(self):
        text = SETUP.split("### Syspilot Actor Setup", 1)[1].split("\n## ", 1)[0]
        self.assertIn("`created: false`", text)
        self.assertIn("pre-existing", text)
        self.assertIn("`+` command of the Jarvis ACTORS view", text)
        self.assertIn("name by name", text)
        self.assertIn("any ambiguous or colliding state", text.replace("Any other Actor, and any", "any"))

    def test_nine_role_cards_are_named(self):
        for name in ("Project Manager", "Architect", "Developer", "Tester", "Quality",
                     "Release", "Research", "Technical Writer", "Admin"):
            self.assertIn(f"`docs/<Project name> Actors/{name}.md`", SETUP)


class TransferTests(unittest.TestCase):
    def setUp(self):
        self.text = SETUP.split("### Transfer To The Admin", 1)[1].split("\n## ", 1)[0]

    def test_header_commit_precedes_the_admin_creation_and_setup_never_writes_the_queue(self):
        self.assertLess(self.text.index("3. Make the transfer"), self.text.index("4. Create the Admin"))
        self.assertLess(self.text.index("2. Add `Admin` to"), self.text.index("3. Make the transfer"))
        self.assertIn("so that a request never exists for a record that does not name the Admin", self.text)
        self.assertIn("Setup never writes the queue file", self.text)

    def test_autodelivery_is_preserved_malformed_files_stop_and_the_limit_is_stated(self):
        self.assertIn(".jarvis/messages/queue.json", self.text)
        self.assertIn(".jarvis/messages/autodelivery.json", self.text)
        self.assertIn("read it back", self.text)
        self.assertIn("not a JSON array", self.text)
        self.assertIn("this is a limit and not a safe path", self.text)
        self.assertIn("the request text as `initialMessage`", self.text)

    def test_existing_admin_gets_a_consented_direct_queue_append_after_the_commit(self):
        self.assertIn("ask the User in this step whether Setup may append the request", self.text)
        self.assertIn("no read back can show it", self.text)
        step5 = self.text.split("5. When the Admin already exists", 1)[1].split("\n6. ", 1)[0]
        self.assertIn("After the commit of step 3 and with the User's consent from step 1", step5)
        self.assertIn("every entry read before the write is unchanged", step5)
        self.assertIn("not a JSON array", step5)
        self.assertIn("When the User withholds the consent, write nothing to the queue", step5)

    def test_language_rule_and_continuation_evidence(self):
        self.assertIn("in English when that language is ambiguous", self.text)
        self.assertIn("The only evidence of continuation is the Admin's acknowledgement row", self.text)
        self.assertIn("120 seconds", self.text)
        self.assertIn("No case is reported as delivered", self.text)
        self.assertIn("acknowledgement is a row in the Evidence Summary", self.text)
        self.assertIn("manual prompt", self.text)

    def test_header_and_log_admit_the_admin_as_executor(self):
        header = SETUP.split("## Handover log", 1)[0]
        self.assertIn("**Executor:** initiating Copilot session | Admin", header)
        self.assertRegex(header, r"\*\*Current responsibility:\*\*[^\n]*Admin[^\n]*Project Manager")


class GateTests(unittest.TestCase):
    def setUp(self):
        self.phase = section("## Phase 5: Verify Installed Outcome")

    def test_every_gate_row_has_one_of_three_statuses(self):
        rows = [line for line in self.phase.splitlines() if line.startswith("|")][2:]
        self.assertEqual(len(rows), 8)
        for row in rows:
            self.assertEqual(row.split("|")[2].strip(), "pending", row)

    def test_no_conditional_status_and_blocking_rule(self):
        self.assertIn("exactly one status: `pending`, `passed`, or `failed`", self.phase)
        self.assertIn("No other status exists, such as `conditional`", self.phase)
        self.assertIn('`baseline_status` stays `"preparing"`', self.phase)
        self.assertIn("warning count above zero", self.phase)
        self.assertNotIn("jarvis_listChatSessions", self.phase)

    def test_verified_and_handed_off_conditions_and_final_reread(self):
        seal = section("## Phase 6")
        self.assertIn("Re-read this record and `.syspilot/project.toml`", seal)
        self.assertIn("only after every gate is `passed`", seal)
        handoff = section("## Phase 7")
        self.assertIn("Otherwise keep Contract status `verified`, set `Current responsibility` to `Project Manager`", handoff)
        self.assertIn("record the Evidence Summary row `PM handoff` as `pending`", handoff)
        self.assertIn("in one commit, which Contract handling requires before the message is sent", handoff)
        self.assertIn("the Project Manager's own first commit on the record sets Contract status `handed off`", handoff)
        self.assertIn("reports completion to the User only after that acknowledgement", handoff)
        self.assertIn("If sending the message fails, leave the record unchanged", handoff)
        self.assertIn("`PM handoff` is a delivery row and not a Phase 5 gate", handoff)
        self.assertIn("The mandatory gates are exactly the rows of the table above", self.phase)
        self.assertIn("The row `PM handoff` is a delivery row outside them", section("## Evidence Summary"))
        self.assertNotIn("record the delivery blocker in the Evidence Summary", handoff)
        self.assertLess(handoff.index("Complete the Git integration"), handoff.index("Send `Installation complete"))
        self.assertNotIn("keeping Contract status `verified`", handoff)

    def test_manual_route_paths_come_from_the_second_scan(self):
        text = SETUP.split("### Syspilot Actor Setup", 1)[1].split("\n## ", 1)[0]
        self.assertIn("skip an Actor that the manual creation path below has created", text)
        self.assertIn("the path the second folder scan finds for an Actor the User created", text)


class ProjectNameTests(unittest.TestCase):
    def setUp(self):
        self.step = section("## Phase 1").split("\n6. Confirm the project name", 1)[1].split("\n7. ", 1)[0]

    def test_name_is_confirmed_in_phase_1_recorded_in_the_header_and_validated_not_altered(self):
        header = SETUP.split("## Handover log", 1)[0]
        self.assertIn("**Project name:** pending | {confirmed project name}", header)
        self.assertIn("before any destination is verified or written", self.step)
        self.assertIn("Propose the name of the target project folder", self.step)
        self.assertIn("letters, digits, spaces, hyphens, underscores, and dots that are neither leading nor trailing", self.step)
        self.assertIn("no name that consists of dots only", self.step)
        for device in ("CON", "PRN", "AUX", "NUL", "COM1", "LPT9"):
            self.assertIn(device, self.step)
        self.assertIn("asked for again and never altered", self.step)
        self.assertIn("A later change is a widened scope", self.step)
        self.assertIn("before the Actors folder scan and the tool check", self.step)
        self.assertIn("A resumed Setup keeps the recorded name", self.step)
        self.assertIn("the first write to an installed destination in Phase 4", self.step)
        self.assertIn("the branch, the header of this record, and the dry run are not such a write", self.step)
        self.assertIn("a changed project name", SETUP)

    def test_every_installed_path_carries_the_project_name_and_none_names_syspilot(self):
        inventory = SETUP.split("| Job | Mode |", 1)[1].split("\n\nGenerate `.syspilot/project.toml`", 1)[0]
        for destination in ("docs/<Project name> Actors/index.md", "docs/<Project name> Contracts/index.md"):
            self.assertIn(destination, inventory)
        for line in inventory.splitlines():
            if line.startswith(("| Actor", "| Contract registry", "| Contract processes")):
                self.assertNotIn("`docs/Syspilot Actors/", line)
        self.assertIn("`docs/<Project name> Contracts/index.md` at the start of every session", SETUP)
        self.assertIn("with the recorded name", SETUP)
        self.assertIn("`docs/<Project name> Contracts/`", section("## Phase 7"))
        self.assertIn("no folder named after Syspilot", section("## Phase 5"))

    def test_the_seeded_copies_are_not_substituted(self):
        self.assertNotIn("substitut", SETUP.lower())


class DocumentationScaffoldTests(unittest.TestCase):
    def setUp(self):
        text = SETUP.split("### Documentation Scaffold", 1)[1].split("\n### ", 1)[0]
        self.text = text
        self.conf = re.search(r"```python\n(.*?)```", text, re.S).group(1)

    def test_conf_binds_the_ontology_as_a_literal_string(self):
        self.assertRegex(self.conf, r'(?m)^needs_from_toml = "[^"\n]+"$')
        self.assertIn("without executing `conf.py`", self.text)

    def test_conf_is_neutral(self):
        for forbidden in ("syspilot", "templates_path", "html_static_path", "html_logo", "intersphinx",
                          "ontology-reference", "builder-inited", "tomllib"):
            self.assertNotIn(forbidden, self.conf)
        self.assertIn('"changes/*"', self.conf)
        self.assertIn('suppress_warnings = ["needs.deprecated"]', self.conf)
        self.assertIn('extensions = ["myst_parser", "sphinx_needs"]', self.conf)

    def test_index_lists_only_the_registries_and_registries_hide_a_toctree(self):
        self.assertIn("`<Project name> Actors/index` and `<Project name> Contracts/index`", self.text)
        self.assertIn(":hidden:", self.text)
        self.assertIn("Install no `docs/ontology-reference.md`", self.text)


class SphinxNeedsVersionTests(unittest.TestCase):
    def test_version_is_recorded_and_older_than_4_1_0_blocks_only_a_setup_binding(self):
        self.assertIn("Record the Sphinx-Needs version of the environment in use", SETUP)
        self.assertIn("older than 4.1.0", SETUP)
        self.assertIn("bind nothing against that environment", SETUP)
        self.assertIn("An existing configured ontology and its environment stay untouched whatever the version", SETUP)

    def test_shipped_requirements_meet_the_minimum(self):
        text = (ROOT / "docs" / "requirements.txt").read_text(encoding="utf-8")
        self.assertIn("sphinx-needs>=4.1.0", text)


if __name__ == "__main__":
    unittest.main()
