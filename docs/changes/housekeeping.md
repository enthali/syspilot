# Change Document: housekeeping

**Status**: approved
**Branch**: feature/housekeeping
**Created**: 2026-03-30
**Author**: Georg Doll

---

## Summary

Two housekeeping items:
1. **Remove version from copilot-instructions.md** — The memory agent currently updates the version
   in copilot-instructions.md, but this duplicates what the release agent already does in
   `syspilot/version.json`. The spec `SYSPILOT_SPEC_MEM_UPDATE_PROCESS` and
   `SYSPILOT_SPEC_MEM_INSTRUCTIONS_STRUCTURE` need to be updated to exclude version maintenance.
2. **Archive v0.2.2 change documents** — Files `release-kiss.md`, `setup-dep-check.md` and their
   val-reports are loose in `docs/changes/archive/` instead of `docs/changes/archive/v0.2.2/`.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

No User Stories need modification. `SYSPILOT_US_DX_PROJECT_MEMORY` is correctly scoped —
what constitutes "project knowledge" is defined at Level 2.

### Decisions

- Item 1 (version in copilot-instructions) is a Level 2 refinement
- Item 2 (archive v0.2.2 files) is a file operation executing existing policy

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

No Requirements need modification. `SYSPILOT_REQ_DX_MEMORY_AGENT` ACs are generic
(detect changes, update, remove outdated, document patterns). Version exclusion is
a Level 2 design refinement.

---

## Level 2: Design Specs

**Status**: ✅ completed

### Modified Specs

#### SYSPILOT_SPEC_MEM_UPDATE_PROCESS
- Remove "Version: Has version.json been bumped?" from Step 2 gap checks

#### SYSPILOT_SPEC_MEM_CONTENT_CATEGORIES
- Add version to Exclude list (release artifact, not project knowledge)

#### SYSPILOT_SPEC_MEM_INSTRUCTIONS_STRUCTURE
- Remove "version" from Project Overview line in target structure

### Also Changed
- `copilot-instructions.md`: Remove `**Version**:` line and footer version reference
- Move 4 v0.2.2 archive files to `docs/changes/archive/v0.2.2/`
