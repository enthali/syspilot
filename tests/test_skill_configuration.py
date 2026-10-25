import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
COMMANDS = (
    ("syspilot.impact-python", "get_need_links.py", ["ROOT", "--flat", "--no-build"]),
    ("syspilot.mece", "analyze_mece.py", ["ROOT", "--scope", "all-type"]),
    ("syspilot.trace", "analyze_trace.py", ["ROOT", "--depth", "1"]),
)


class AdoptedProjectConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        for skill, script, _ in COMMANDS:
            relative = Path(".github") / "skills" / skill / "scripts" / script
            destination = self.root / relative
            destination.parent.mkdir(parents=True)
            shutil.copyfile(PROJECT_ROOT / relative, destination)
        self.conf = self.root / "docs" / "conf.py"
        self.conf.parent.mkdir()
        self.conf.write_text(
            'raise RuntimeError("configuration must not execute")\n'
            'needs_from_toml = "../model/customer ontology.toml"\n',
            encoding="utf-8",
        )
        self.ontology = self.root / "model" / "customer ontology.toml"
        self.ontology.parent.mkdir()
        self.ontology.write_text(
            '[[needs.types]]\ndirective = "capability"\n'
            '[[needs.extra_links]]\noption = "customer_rel"\n', encoding="utf-8"
        )
        needs_dir = self.root / "docs" / "_build" / "html" / "needs_id"
        needs_dir.mkdir(parents=True)
        for need_id, links in (("ROOT", ["PEER"]), ("PEER", [])):
            need = {"id": need_id, "type": "capability", "customer_rel": links}
            (needs_dir / f"{need_id}.json").write_text(
                json.dumps({"versions": {"": {"needs": {need_id: need}}}}),
                encoding="utf-8",
            )

    def run_cli(self, skill, script, args):
        return subprocess.run(
            [sys.executable, str(self.root / ".github" / "skills" / skill / "scripts" / script), *args],
            cwd=self.root.parent, capture_output=True, text=True,
        )

    def test_all_default_clis_use_project_binding_from_any_working_directory(self):
        for skill, script, args in COMMANDS:
            with self.subTest(skill=skill):
                result = self.run_cli(skill, script, args)
                self.assertEqual(result.returncode, 0, result.stderr)
                payload = json.loads(result.stdout)
                if skill == "syspilot.impact-python":
                    self.assertEqual(payload, ["PEER"])
                elif skill == "syspilot.mece":
                    self.assertEqual(payload["peers"], ["PEER"])
                else:
                    self.assertEqual(payload["edges"][0]["option"], "customer_rel")

    def test_missing_binding_fails_without_silent_fallback(self):
        self.conf.write_text("", encoding="utf-8")
        for skill, script, args in COMMANDS:
            with self.subTest(skill=skill):
                result = self.run_cli(skill, script, args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("needs_from_toml", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_shipped_script_folders_contain_runtime_only(self):
        for skill, script, _ in COMMANDS:
            with self.subTest(skill=skill):
                scripts_dir = PROJECT_ROOT / ".github" / "skills" / skill / "scripts"
                self.assertEqual({path.name for path in scripts_dir.glob("*.py")}, {script})

    def test_explicit_override_bypasses_missing_configuration(self):
        self.conf.unlink()
        for skill, script, args in COMMANDS:
            with self.subTest(skill=skill):
                result = self.run_cli(skill, script, [*args, "--ontology", str(self.ontology)])
                self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()