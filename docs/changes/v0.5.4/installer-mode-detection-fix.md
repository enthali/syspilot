# Change Request: installer-mode-detection-fix

**Status**: merged
**Created**: 2026-05-13
**Branch**: feature/installer-mode-detection-fix
**Commit (feature)**: 98f5846
**Merge commit**: d1a69b2

---

## WHY

The Installer Agent Workflow Step 2 "Detect Mode" compared the installed version against `syspilot/version.json`. This file was intentionally removed in v0.5.3 when the version source was moved to the Setup Agent frontmatter. The Installer was never updated, causing mode detection to fail at runtime on any fresh or update install.

---

## WHAT

Installer Workflow Step 2 shall read the installed version from `.github/agents/syspilot.setup.agent.md` `version:` field and compare it against the source version from `syspilot/agents/syspilot.setup.agent.md` `version:` field. No reference to `version.json` shall remain in either installer agent.

---

## Acceptance Criteria

- Installer Workflow Step 2 reads version from Setup Agent frontmatter (installed vs. source).
- `version.json` is not referenced in `syspilot/agents/syspilot.installer.agent.md`.
- `version.json` is not referenced in `.github/agents/syspilot.installer.agent.md`.
- Both product source and installed instance are updated identically.

---

## Files Changed

- `syspilot/agents/syspilot.installer.agent.md` — Workflow Step 2 updated
- `.github/agents/syspilot.installer.agent.md` — Workflow Step 2 updated (instance)

---

## Traceability

No spec changes required — runtime behavior fix only. Both installer copies (product + instance) updated in sync.
