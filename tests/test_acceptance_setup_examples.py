"""Requirement tests for the setup-examples Change, written from SYSP_REQ_EXAMPLES and the Change's Scope."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTORS = ROOT / "docs" / "Syspilot Actors"
EXAMPLE_ACTORS = ROOT / "docs" / "Example Actors"
CONTRACTS = ROOT / "docs" / "Syspilot Contracts"
EXAMPLE_CONTRACTS = ROOT / "docs" / "Example Contracts"
REQUIREMENTS = ROOT / "docs" / "syspilot" / "requirements"
DOCUMENTATION = ROOT / "docs" / "syspilot" / "documentation" / "index.rst"

ROLE_CARDS = {
    "Admin", "Architect", "Developer", "Project Manager", "Quality",
    "Release", "Research", "Technical Writer", "Tester",
}
EXAMPLE_CONTRACT_FILES = {
    "index.md", "contract-documents.md", "change.md", "release.md", "process-maintenance.md",
}
# Setup's Contract selection table: each installable Contract and what it requires.
REQUIRES = {
    "contract-documents.md": set(),
    "change.md": {"contract-documents.md"},
    "release.md": {"contract-documents.md"},
    "process-maintenance.md": {"contract-documents.md", "change.md"},
}
# Values that only hold for Syspilot's own repository.
SYSPILOT_SPECIFIC = (
    "enthali", "docs/Syspilot", "docs/Example", "release.yml", "Example sync",
    "setup.md", "setup-contract", "syspilot.code-workspace",
)


def read(path):
    return path.read_text(encoding="utf-8")


def normalized(path):
    return read(path).replace("\r\n", "\n").replace("\r", "\n")


def files_below(folder):
    return {path.relative_to(folder).as_posix() for path in folder.rglob("*") if path.is_file()}


def declared_deviations():
    text = normalized(EXAMPLE_ACTORS / "index.md")
    section = text.split("## Deviations", 1)[1].split("\n## ", 1)[0]
    rows = [line for line in section.splitlines() if line.startswith("|")][2:]
    return {row.split("|")[1].strip() for row in rows}


def differing_cards():
    return {name for name in ROLE_CARDS if normalized(ACTORS / f"{name}.md") != normalized(EXAMPLE_ACTORS / f"{name}.md")}


def need_block(rst, need_id):
    return re.search(rf"(?ms)^\.\. \w+::[^\n]*\n\s+:id: {need_id}\n(.*?)(?=^\.\. \w+::|\Z)", rst).group(0)


class FolderContentTests(unittest.TestCase):
    def test_example_actors_hold_exactly_the_nine_cards_and_the_index(self):
        self.assertEqual(files_below(EXAMPLE_ACTORS), {f"{name}.md" for name in ROLE_CARDS} | {"index.md"})

    def test_the_example_cards_are_the_nine_cards_of_the_actor_folder(self):
        self.assertTrue({f"{name}.md" for name in ROLE_CARDS} <= files_below(ACTORS))

    def test_example_contracts_hold_exactly_the_listed_files(self):
        self.assertEqual(files_below(EXAMPLE_CONTRACTS), EXAMPLE_CONTRACT_FILES)

    def test_setup_stays_with_the_syspilot_contracts(self):
        self.assertTrue((CONTRACTS / "setup.md").exists())
        self.assertFalse((EXAMPLE_CONTRACTS / "setup.md").exists())

    def test_the_example_registry_lists_what_the_folder_holds(self):
        index = read(EXAMPLE_CONTRACTS / "index.md")
        entries = set(re.findall(r"(?m)^(\S+)$", "\n".join(re.findall(r"```\{toctree\}\n(.*?)```", index, re.S))))
        listed = {f"{entry}.md" for entry in entries if not entry.startswith(":")}
        self.assertEqual(listed, EXAMPLE_CONTRACT_FILES - {"index.md"})
        self.assertNotIn("setup", index.replace("Setup", ""))

    def test_the_example_folder_is_flat(self):
        self.assertEqual([path.name for path in EXAMPLE_CONTRACTS.iterdir() if path.is_dir()], [])

    def test_every_link_between_example_contracts_points_at_a_required_contract(self):
        # An installed Contract must not link to a Contract the project may not have installed.
        for name, required in REQUIRES.items():
            for target in re.findall(r"\]\(([^)#]+?\.md)(?:#[^)]*)?\)", read(EXAMPLE_CONTRACTS / name)):
                if "://" in target:
                    continue
                with self.subTest(document=name, link=target):
                    self.assertIn(target, required | {"contract-documents.md"})
                    self.assertTrue((EXAMPLE_CONTRACTS / target).exists())

    def test_the_setup_selection_table_states_the_requirements_the_links_need(self):
        text = read(CONTRACTS / "setup.md")
        table = text.split("### Contract Selection", 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0]
        rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in table.splitlines() if line.startswith("|")][2:]
        stated = {}
        for _, file, selection, requires in rows:
            stated[file.strip("`")] = {
                f"{name}.md" for name, md in (("contract-documents", "Contract Documents"), ("change", "Change Process"))
                if md in requires
            }
            if file.strip("`") == "contract-documents.md":
                self.assertEqual(selection, "always installed")
        self.assertEqual(stated, REQUIRES)

    def test_setup_generates_the_registry_from_the_example_preamble(self):
        text = read(CONTRACTS / "setup.md")
        row = next(line for line in text.splitlines() if line.startswith("| Contract registry |"))
        self.assertIn("generated instance", row)
        self.assertIn("docs/Syspilot Contracts/index.md", row)
        index = read(EXAMPLE_CONTRACTS / "index.md")
        self.assertIn("\n## Processes", index)

    def test_setup_installs_selected_contracts_under_their_own_names_without_the_registry(self):
        text = read(CONTRACTS / "setup.md")
        row = next(line for line in text.splitlines() if line.startswith("| Contract processes |"))
        self.assertIn("copy selected files", row)
        self.assertIn("directly below `docs/Example Contracts/`", row)
        self.assertIn("seeded copy", row)
        self.assertIn("no unselected Contract file exists", row)


class DeviationTests(unittest.TestCase):
    def test_every_card_is_identical_unless_declared(self):
        self.assertEqual(differing_cards() - declared_deviations(), set(), "undeclared difference")

    def test_every_declared_deviation_names_a_card_that_differs(self):
        self.assertEqual(declared_deviations() - differing_cards(), set(), "declared deviation without a difference")

    def test_every_deviation_names_a_role_card_and_a_reason(self):
        self.assertTrue(declared_deviations() <= ROLE_CARDS)
        text = normalized(EXAMPLE_ACTORS / "index.md")
        section = text.split("## Deviations", 1)[1].split("\n## ", 1)[0]
        for row in [line for line in section.splitlines() if line.startswith("|")][2:]:
            self.assertTrue(row.split("|")[2].strip(), row)


class GenericContractTests(unittest.TestCase):
    def test_no_syspilot_specific_value_remains_in_the_contract_examples(self):
        for path in EXAMPLE_CONTRACTS.rglob("*.md"):
            text = read(path)
            for value in SYSPILOT_SPECIFIC:
                with self.subTest(document=str(path.relative_to(EXAMPLE_CONTRACTS)), value=value):
                    self.assertNotIn(value, text)

    def test_the_release_example_leaves_project_values_to_fill_in(self):
        text = read(EXAMPLE_CONTRACTS / "release.md")
        for placeholder in ("{integration branch}", "{release branch}", "{tag form}", "{publication workflow}"):
            with self.subTest(placeholder=placeholder):
                self.assertIn(placeholder, text)

    def test_the_example_change_names_the_integration_branch_as_a_value(self):
        self.assertIn("{integration branch}", read(EXAMPLE_CONTRACTS / "change.md"))

    def test_the_contract_examples_differ_from_the_syspilot_contracts(self):
        for name in ("change.md", "release.md"):
            with self.subTest(document=name):
                self.assertNotEqual(normalized(CONTRACTS / name), normalized(EXAMPLE_CONTRACTS / name))

    def test_the_example_folders_are_plain_markdown_without_needs_markup(self):
        for folder in (EXAMPLE_ACTORS, EXAMPLE_CONTRACTS):
            for path in folder.rglob("*.md"):
                text = read(path)
                with self.subTest(document=str(path.relative_to(ROOT))):
                    self.assertNotRegex(text, r"(?m)^\s*```\{(?!toctree\})")
                    self.assertNotRegex(text, r"(?m)^\.\. \w+::")
                    self.assertNotRegex(text, r"\{need(_\w+)?\}")


class DocNeedTests(unittest.TestCase):
    CASES = (
        ("SYSP_DOC_EXAMPLE_ACTORS", "docs/Example Actors/index.md",
         ["SYSP_REQ_ACTOR_MODEL", "SYSP_REQ_PROJECT_MANAGER", "SYSP_REQ_ARCHITECT", "SYSP_REQ_DEVELOPER",
          "SYSP_REQ_TESTER", "SYSP_REQ_QUALITY", "SYSP_REQ_RELEASE", "SYSP_REQ_RESEARCH",
          "SYSP_REQ_TECHNICAL_WRITER", "SYSP_REQ_ADMIN", "SYSP_REQ_EXAMPLES"]),
        ("SYSP_DOC_EXAMPLE_CONTRACTS", "docs/Example Contracts/index.md",
         ["SYSP_REQ_CONTRACT_DOCUMENTS", "SYSP_REQ_CHANGE_CONTRACT", "SYSP_REQ_RELEASE_CONTRACT",
          "SYSP_REQ_PROCESS_MAINTENANCE", "SYSP_REQ_EXAMPLES"]),
    )

    def test_each_folder_is_a_doc_need_that_includes_the_requirements_it_carries(self):
        rst = read(DOCUMENTATION)
        for need_id, realized_by, requirements in self.CASES:
            block = need_block(rst, need_id)
            with self.subTest(need=need_id):
                self.assertTrue(block.startswith(".. doc::"))
                self.assertIn(f":realized_by: {realized_by}", block)
                self.assertTrue((ROOT / realized_by).exists())
                included = re.search(r":includes: (.*)", block).group(1)
                self.assertEqual({item.strip() for item in included.split(",")}, set(requirements))

    def test_every_included_requirement_exists_as_a_need(self):
        defined = set()
        for path in REQUIREMENTS.glob("*.rst"):
            defined |= set(re.findall(r":id: (SYSP_REQ_\w+)", read(path)))
        for _, _, requirements in self.CASES:
            for requirement in requirements:
                with self.subTest(requirement=requirement):
                    self.assertIn(requirement, defined)

    def test_the_requirement_does_not_list_the_folders_itself(self):
        # included_in is the incoming link of the doc Needs' includes, so it must not be maintained by hand.
        self.assertNotIn(":included_in:", read(REQUIREMENTS / "req_examples.rst"))

    def test_the_example_requirement_is_approved_and_verified(self):
        text = read(REQUIREMENTS / "req_examples.rst")
        self.assertIn(":id: SYSP_REQ_EXAMPLES", text)
        self.assertIn(":verifies: SYSP_REQ_EXAMPLES", text)


class ProcessRuleTests(unittest.TestCase):
    def test_the_change_template_carries_the_example_sync_row_owned_by_the_technical_writer(self):
        text = read(CONTRACTS / "change.md")
        row = next(line for line in text.splitlines() if line.startswith("| Example sync |"))
        cells = [cell.strip() for cell in row.split("|")]
        self.assertIn("yes (default)", cells[2])
        self.assertIn("not applicable", cells[2])
        self.assertEqual(cells[3], "Technical Writer")
        self.assertRegex(text, r"(?m)^## Example Sync$")

    def test_the_example_sync_row_covers_both_folders(self):
        text = read(CONTRACTS / "change.md")
        row = next(line for line in text.splitlines() if line.startswith("| Example sync |"))
        self.assertIn("Example Actors", row)
        self.assertIn("Example Contracts", row)

    def test_the_release_process_verifies_the_rows_instead_of_merging(self):
        text = " ".join(read(CONTRACTS / "release.md").split())
        self.assertIn("`Example sync`", text)
        self.assertRegex(text, r"\| Change \| Integrated commit \| Contract closed \| Example sync \|")
        requirement = " ".join(read(REQUIREMENTS / "req_release_contract.rst").split())
        self.assertRegex(requirement, r"verifies the ``Example sync`` row of each")

    def test_the_setup_inventory_names_the_example_folders_as_the_source(self):
        text = read(CONTRACTS / "setup.md")
        rows = {line.split("|")[1].strip(): line for line in text.splitlines() if line.startswith("| Actor role cards") or line.startswith("| Contract processes")}
        self.assertIn("docs/Example Actors/", rows["Actor role cards"])
        self.assertIn("docs/Example Contracts/", rows["Contract processes"])
        for row in rows.values():
            self.assertIn("seeded copy", row)
            self.assertNotIn("release-owned", row)

    def test_the_setup_requirement_names_the_example_folders(self):
        text = " ".join(read(REQUIREMENTS / "req_setup.rst").split())
        self.assertIn("``docs/Example Actors/``", text)
        self.assertIn("``docs/Example Contracts/``", text)
        self.assertIn("seeded copies", text)

    def test_the_technical_writer_card_names_the_maintenance_duty_in_syspilots_own_card_only(self):
        own = read(ACTORS / "Technical Writer.md")
        example = read(EXAMPLE_ACTORS / "Technical Writer.md")
        self.assertIn("docs/Example Actors/", own)
        self.assertNotIn("docs/Example Actors/", example)
        requirement = " ".join(read(REQUIREMENTS / "req_technical_writer.rst").split())
        self.assertIn("``Deviations`` table of ``docs/Example Actors/index.md``", requirement)

    def test_process_maintenance_names_the_moved_location(self):
        text = " ".join(read(REQUIREMENTS / "req_process_maintenance.rst").split())
        self.assertIn("docs/Example Contracts/", text)
        self.assertIn("docs/Example Contracts/process-maintenance.md", text)
        self.assertNotIn("examples/process-maintenance", text)
        self.assertNotIn("docs/Syspilot Contracts/examples", text)


if __name__ == "__main__":
    unittest.main()
