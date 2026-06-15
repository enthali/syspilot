"""Tests for docs-build.py — run with: uv run python -m pytest docs/test_docs_build.py -v"""
import sys
import shutil
import subprocess
import importlib
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

DOCS_BUILD = Path(__file__).parent / "docs-build.py"


def _load_module():
    """Import docs-build.py as a module (handles hyphen in filename)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("docs_build", DOCS_BUILD)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestDocsBuild(unittest.TestCase):

    def _run_main(self, argv, run_returncode=0):
        """Call main() with patched sys.argv, subprocess.run, and shutil.rmtree."""
        mock_result = MagicMock()
        mock_result.returncode = run_returncode

        mod = _load_module()

        with patch.object(sys, "argv", ["docs-build.py"] + argv), \
             patch("subprocess.run", return_value=mock_result) as mock_run, \
             patch("shutil.rmtree") as mock_rm, \
             patch.object(Path, "exists", return_value=True):
            try:
                mod.main()
            except SystemExit as exc:
                return mock_run, mock_rm, exc.code
            return mock_run, mock_rm, 0

    # ------------------------------------------------------------------
    # Test 1: no args → sphinx-build called with correct arguments
    # ------------------------------------------------------------------
    def test_no_args_calls_sphinx_build(self):
        mock_run, mock_rm, exit_code = self._run_main([])

        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]

        self.assertEqual(cmd[0], "uv")
        self.assertEqual(cmd[1], "run")
        self.assertEqual(cmd[2], "sphinx-build")
        self.assertIn("-b", cmd)
        self.assertIn("html", cmd)
        self.assertIn("-W", cmd)
        self.assertIn("--keep-going", cmd)
        self.assertEqual(exit_code, 0)

    # ------------------------------------------------------------------
    # Test 2: clean arg → build dir deleted before build
    # ------------------------------------------------------------------
    def test_clean_arg_removes_build_dir(self):
        mock_run, mock_rm, exit_code = self._run_main(["clean"])

        mock_rm.assert_called_once()
        # The path passed to rmtree must end with "_build"
        removed_path = mock_rm.call_args[0][0]
        self.assertTrue(str(removed_path).endswith("_build"))
        # sphinx-build must still be called afterwards
        mock_run.assert_called_once()
        self.assertEqual(exit_code, 0)

    # ------------------------------------------------------------------
    # Test 3: sphinx-build fails → script exits with non-zero code
    # ------------------------------------------------------------------
    def test_sphinx_failure_exits_nonzero(self):
        mock_run, mock_rm, exit_code = self._run_main([], run_returncode=1)

        self.assertNotEqual(exit_code, 0)

    # ------------------------------------------------------------------
    # Test 4: output path printed on success
    # ------------------------------------------------------------------
    def test_success_prints_output_path(self):
        import io
        mock_result = MagicMock()
        mock_result.returncode = 0

        mod = _load_module()

        with patch.object(sys, "argv", ["docs-build.py"]), \
             patch("subprocess.run", return_value=mock_result), \
             patch("shutil.rmtree"), \
             patch.object(Path, "exists", return_value=True):
            captured = io.StringIO()
            with patch("builtins.print", side_effect=lambda *a, **kw: captured.write(" ".join(str(x) for x in a) + "\n")):
                mod.main()

        output = captured.getvalue()
        self.assertIn("index.html", output)
        self.assertIn("[OK]", output)


if __name__ == "__main__":
    unittest.main()
