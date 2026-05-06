# Change Document: bootloader-tools-fix

**Status**: in-progress
**Branch**: feature/bootloader-tools-fix
**Created**: 2026-05-06
**Author**: Change Manager

---

## Summary

Defect fix for the Bootloader/Installer split. Live testing revealed three defects
that prevented the Bootloader from correctly invoking the Installer as a subagent:
(1) missing `agent` and `vscode/askQuestions` in Bootloader `tools:`,
(2) missing `"syspilot.installer"` in Bootloader `agents:`,
(3) Installer preserve logic re-injecting old instance `tools:` into the Bootloader on update.
A fourth improvement adds user-facing guidance when `runSubagent` is unavailable.

Pure product file fix — no spec changes required.

---

## Scope

**Product files only** — no spec elements (US/REQ/SPEC) impacted.

| File | Change |
|------|--------|
| `syspilot/agents/syspilot.setup.agent.md` | Add `agent`, `vscode/askQuestions` to `tools:`; add `"syspilot.installer"` to `agents:`; add runSubagent unavailability guidance |
| `syspilot/agents/syspilot.installer.agent.md` | Exclude Bootloader from `tools:` preserve logic |

---

## Defects Fixed

### D-1: Bootloader `tools:` missing `agent` and `vscode/askQuestions`

**Root cause:** Initial Bootloader frontmatter was copied from the Installer but
`agent` (needed for `runSubagent()`) and `vscode/askQuestions` (needed for user
interaction fallback) were not added.

**Fix:** Add both entries to `tools:` in `syspilot/agents/syspilot.setup.agent.md`.

### D-2: Bootloader `agents:` empty

**Root cause:** `agents: []` was not populated after the Installer agent was created.

**Fix:** Set `agents: ["syspilot.installer"]` in `syspilot/agents/syspilot.setup.agent.md`.

### D-3: Installer preserve logic overwrites Bootloader `tools:`

**Root cause:** The Installer's update-mode `tools:` preservation reads the instance
`tools:` value and re-injects it — but when updating the Bootloader, the instance has
the old (short) `tools:` list, overwriting the correct product list on every update.

**Fix:** Exclude `syspilot.setup.agent.md` from the `tools:` preserve logic in the
Installer — always copy Bootloader `tools:` from the product source.

### D-4: No guidance when `runSubagent` unavailable

**Root cause:** No fallback message existed for sessions where `agent` tool is not enabled.

**Fix:** Add explicit guidance in the Bootloader Workflow step 4.

---

## Quality Gates

- [ ] Sphinx build: clean (0 warnings, 0 errors)
- [ ] QM CLEARED
- [ ] PM Merge Approval ⏳

---

## Traceability

No new spec elements. Fixes defects in product implementation files only.
