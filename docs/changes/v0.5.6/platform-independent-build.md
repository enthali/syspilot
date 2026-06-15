# Change Request: platform-independent-build

**Status**: draft
**Created**: 2026-06-03
**Author**: PM

---

## WHY

The repository maintains two platform-specific build scripts for each build operation — `.sh` for Unix/macOS and `.ps1` for Windows. Every change to build logic must be applied twice, in two different scripting languages. Contributors on a single platform cannot easily test the other variant. This duplication increases maintenance cost and the risk of the two variants drifting out of sync.

A single cross-platform Python script eliminates this duplication. Python 3 is already a project dependency (Sphinx runs on it), and `uv` is the project's required Python toolchain.

---

## WHAT

Replace all platform-specific build scripts in the repository with platform-independent Python scripts named `docs-build.py`, preserving identical functionality. Specifically:

- `docs/build.sh` + `docs/build.ps1` → `docs/docs-build.py`
- `syspilot/sphinx/build.sh` + `syspilot/sphinx/build.ps1` → `syspilot/sphinx/docs-build.py`

The replacement scripts shall:

- Accept an optional `clean` argument equivalent to the existing `-Clean` / `clean` flags
- Use `uv run sphinx-build` to invoke Sphinx (never call sphinx-build directly)
- Print the same informational output (success/failure messages, output path)
- Exit with a non-zero code on failure
- Work on macOS, Linux, and Windows without modification

After the replacement, the `.sh` and `.ps1` files shall be deleted from the repository.

Any documentation or references pointing to the old script names shall be updated accordingly.

---

## Acceptance Criteria

- Running `uv run python docs/docs-build.py` produces a Sphinx HTML build identical in outcome to running the old `build.sh` / `build.ps1`.
- Running `uv run python docs/docs-build.py clean` removes the `_build` directory before building.
- Running `uv run python syspilot/sphinx/docs-build.py` and `uv run python syspilot/sphinx/docs-build.py clean` behave equivalently for the product template scripts.
- `docs/build.sh`, `docs/build.ps1`, `syspilot/sphinx/build.sh`, and `syspilot/sphinx/build.ps1` no longer exist in the repository.
- All documentation and README references to the old scripts are updated to reference `build.py`.
- The scripts run without error on macOS and are structured to work on Windows and Linux.
