import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT_FILES = (ROOT / "README.md", ROOT / "docs" / "getting-started.md")


def prompt(path):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(r"```text\n(Install Syspilot into this project\..*?)```", text, flags=re.S)
    assert match, f"no Setup prompt in {path.name}"
    return match.group(1)


class SetupBootstrapPromptTests(unittest.TestCase):
    def test_both_prompts_are_identical(self):
        self.assertEqual(prompt(PROMPT_FILES[0]), prompt(PROMPT_FILES[1]))

    def test_the_prompt_looks_up_version_tags_and_not_releases(self):
        for path in PROMPT_FILES:
            with self.subTest(path.name):
                step_one = prompt(path).split("\n2. ", 1)[0]
                self.assertIn("Look up the version tags of https://github.com/enthali/syspilot", step_one)
                self.assertNotIn("releases", step_one.lower())

    def test_the_prompt_fetches_the_contract_from_the_selected_tag(self):
        for path in PROMPT_FILES:
            with self.subTest(path.name):
                self.assertIn("Fetch `docs/Syspilot Contracts/setup.md` from that exact tag.", prompt(path))


if __name__ == "__main__":
    unittest.main()
