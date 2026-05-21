# Change Document: setup-agent-installs-templates

**Status**: in-progress
**Branch**: feature/setup-agent-installs-templates
**Created**: 2026-05-21
**Author**: PM

---

## Summary

Setup Agent must sync `syspilot/templates/*` → `.github/templates/*` during instance install and update, analogous to how it already handles `syspilot/agents/`, `syspilot/prompts/`, and `syspilot/skills/`. Today `.github/templates/change-document.md` exists only because CR `pm-owns-branch-and-change-setup` placed it manually as a one-off; this CR makes Setup Agent the single source of truth for that sync so the file (and any future template) is reproducibly present in every installed instance, including customer projects that have no `syspilot/` folder. Motivation: without sync logic, the product source (`syspilot/templates/`) and the installed-instance copy (`.github/templates/`) will drift silently, and customer projects — which only contain `.github/` — will break PM/CM agent references that point to `.github/templates/change-document.md`. Acceptance: (1) Setup Agent specification (`syspilot/agents/syspilot.setup.agent.md` and corresponding design spec) describes the template sync responsibility on install and update; (2) Setup Agent copies every file under `syspilot/templates/` to `.github/templates/` on install and update, and is idempotent (re-running yields the same end-state); (3) Setup Agent removes orphan files in `.github/templates/` that no longer exist in `syspilot/templates/`, so no stale templates accumulate; (4) the sync action is observable in Setup Agent's run summary (installed / updated / removed counts, so PM can verify).

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_INSTALLER | Installer Agent | modified | Added AC7 (orphan cleanup) and AC8 (observable summary) |

### New User Stories

_None required — existing US covers the scope._

### Decisions

- Decision 1: `SYSP_US_SETUP` not impacted — the Setup Bootloader delegates all file copy work to the Installer; no change to the Bootloader US.
- Decision 2: Orphan cleanup and observable summary are new acceptance criteria on `SYSP_US_INSTALLER` (AC7, AC8), not new User Stories, because they extend the existing "file copy" responsibility.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

Found via links from User Stories above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_INSTALLER_SCOPE | SYSP_US_INSTALLER | modified | Target for `templates/` changed from `.syspilot/templates/` to `.github/templates/`; added AC5 (idempotency), AC6 (orphan cleanup), AC7 (observable summary) |
| SYSP_REQ_INSTALLER_DUTIES | SYSP_US_INSTALLER | modified | Added AC6 (idempotent sync), AC7 (orphan cleanup), AC8 (observable summary) |
| SYSP_REQ_INSTALLER_WORKFLOW | SYSP_US_INSTALLER | modified | Added AC9 (orphan detection/removal during Install/Update), AC10 (run summary output) |

### New Requirements

_None required — existing REQs cover all ACs after modification._

### Conflicts Detected

_None._

### Decisions

- Decision 1: Template target changed from `.syspilot/templates/` to `.github/templates/` — aligns with AC2 of the CR and makes templates consistent with the other three scope directories (all under `.github/`). The prior CR flagged this explicitly as a follow-up.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_INSTALLER_SCOPE | SYSP_REQ_INSTALLER_SCOPE | modified | Target for `templates/` changed from `.syspilot/templates/` to `.github/templates/` |
| SYSP_SPEC_INSTALLER_DUTIES | SYSP_REQ_INSTALLER_DUTIES | modified | Added duties: Idempotent Sync, Orphan Cleanup, Observable Summary |
| SYSP_SPEC_INSTALLER_WORKFLOW | SYSP_REQ_INSTALLER_WORKFLOW | modified | Added steps 6 (Orphan Cleanup) and 7 (Summary); renumbered Validate→8, Commit→9 |

### New Design Elements

_None required — existing SPECs cover all REQ changes after modification._

### Conflicts Detected

_None._

### Decisions

- Decision 1: Orphan Cleanup is a separate workflow step (step 6) rather than being embedded inside Install/Update (step 4) — this ensures orphan removal is always performed regardless of whether files were updated, and makes testing easier.
- Decision 2: Summary (step 7) runs after orphan cleanup so it can report all three categories (installed, updated, removed) in one pass.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_SCOPE | SYSP_SPEC_INSTALLER_SCOPE | ✅ |
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_DUTIES | SYSP_SPEC_INSTALLER_DUTIES | ✅ |
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_WORKFLOW | SYSP_SPEC_INSTALLER_WORKFLOW | ✅ |

### Artefakt-Removal-Check

_Not applicable — this CR does not remove any artefact. It changes a mapping target (`.syspilot/templates/` → `.github/templates/`) but `.syspilot/templates/` was never actually created in any installation (prior CR flagged it as deferred)._

### Issues Found

- [x] No issues found

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

## UAT Execution

**Status**: ⏳ PENDING — all rows must be executed by the human tester.

This CR has two test modes: **inspection** (verifying that spec file content and the agent file reflect the CR ACs) and **execution** (invoking the Setup Agent and verifying file-system state). Execution rows require the Implement subagent to have completed its work before they can be run.

**Precondition (all rows):** Branch `feature/setup-agent-installs-templates` is checked out. All committed changes are present (Design commit `0b976df`, implementation commit from Implement subagent).

**Precondition (execution rows UAT_005–UAT_008):** A working syspilot repo. The Setup Agent (`@syspilot.setup`) is invocable in the session. Run all execution rows from the repo root (`c:\workspace\syspilot`).

| UAT-ID | AC | Inspection / Execution Step | Expected | Status |
|--------|----|-----------------------------|----------|--------|
| UAT_001 | AC1 | Open `docs/syspilot/design/spec_installer.rst`. Find `:id: SYSP_SPEC_INSTALLER_SCOPE`. Read the installation scope table. | The table contains a row with source `templates/` and destination `.github/templates/`. No entry for `.syspilot/templates/` remains. | PENDING |
| UAT_002 | AC1 | In the same file, find `:id: SYSP_SPEC_INSTALLER_DUTIES`. Read the duty bullet list. | Three new duties are present: **Idempotent Sync** (re-running with unchanged source yields identical end-state), **Orphan Cleanup** (target files with no corresponding source file are removed during every run), and **Observable Summary** (every run outputs a per-directory summary of installed / updated / removed file counts). | PENDING |
| UAT_003 | AC1 | In the same file, find `:id: SYSP_SPEC_INSTALLER_WORKFLOW`. Read steps 6 and 7. | Step 6 is titled **Orphan Cleanup** and describes removing target files with no corresponding source file for each scope directory. Step 7 is titled **Summary** and includes the per-directory table format with `Installed`, `Updated`, `Removed` columns — `templates/` appears as a row in the example table. Former step 6 (Validate) is now renumbered to step 8. | PENDING |
| UAT_004 | AC1 | Open `syspilot/agents/syspilot.installer.agent.md`. Read the Install/Update scope table (workflow step 4) and the list of workflow steps. | The scope table row for `templates/` shows destination `.github/templates/` (not `.syspilot/templates/`). The workflow includes an **Orphan Cleanup** step and a **Summary** step with the per-directory table format. No reference to `.syspilot/templates/` remains anywhere in the file. | PENDING |
| UAT_005 | AC2 | **Setup:** `Remove-Item .github/templates/change-document.md -ErrorAction SilentlyContinue` (remove installed copy to force a detectable fresh-install). Confirm `syspilot/templates/change-document.md` exists as the source. **Action:** Invoke Setup Agent in a new chat session; choose reinstall. **Verify:** Run `Test-Path .github/templates/change-document.md` and `Compare-Object (Get-Content syspilot/templates/change-document.md) (Get-Content .github/templates/change-document.md)`. | `Test-Path` returns `True`. `Compare-Object` returns no output — the installed copy is byte-for-byte identical to the source. | PENDING |
| UAT_006 | AC2 | **Precondition:** UAT_005 passed (`.github/templates/change-document.md` is present). **Setup:** Record `$before = (Get-FileHash .github/templates/change-document.md).Hash`. **Action:** Invoke Setup Agent again (reinstall) without modifying any file in `syspilot/templates/`. **Verify:** `(Get-FileHash .github/templates/change-document.md).Hash -eq $before`. | Hash is identical before and after the second run. No errors reported. No duplicate files created. Idempotency confirmed. | PENDING |
| UAT_007 | AC3 | **Setup:** `New-Item -Path .github/templates/orphan-test.md -Value "orphan" -Force`. Confirm `syspilot/templates/orphan-test.md` does NOT exist (no source counterpart). **Action:** Invoke Setup Agent (reinstall). **Verify:** `-not (Test-Path .github/templates/orphan-test.md)`. **Cleanup (if agent fails):** `Remove-Item .github/templates/orphan-test.md -ErrorAction SilentlyContinue`. | `Test-Path .github/templates/orphan-test.md` returns `False` — the orphan was removed. No other files in `.github/templates/` are removed. | PENDING |
| UAT_008 | AC4 | **Action:** Invoke Setup Agent (reinstall). Observe the text output in the chat window. | The output includes a summary table with a `templates/` row showing integer values in the `Installed`, `Updated`, and `Removed` columns. The row is present even when all counts are zero (e.g. pure idempotent run). | PENDING |

### AC Coverage

| AC | Description (abbreviated) | UAT-IDs |
|----|---------------------------|---------|
| AC1 | Spec files and agent file describe template sync, orphan cleanup, and observable summary | UAT_001, UAT_002, UAT_003, UAT_004 |
| AC2 | Installer copies `syspilot/templates/` → `.github/templates/`; idempotent on re-run | UAT_005, UAT_006 |
| AC3 | Installer removes orphan files from `.github/templates/` | UAT_007 |
| AC4 | Run summary includes `templates/` row with installed / updated / removed counts | UAT_008 |

---

*Generated by syspilot Change Agent*
