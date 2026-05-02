# Change Document: setup-user-changes-check

**Status**: in-progress
**Branch**: feature/setup-user-changes-check
**Created**: 2026-04-30
**Author**: System Designer

---

## Summary

The Setup Agent currently overwrites installed files without checking whether
the user has made local customizations. This change adds two safeguards to the
update workflow: (1) before overwriting, ask the user if they have customized
the installed files and, if so, gather what was changed and restore those
customizations after the update; (2) if the installed version already equals
the source version, ask the user whether to reinstall anyway rather than
silently doing nothing or silently overwriting.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_SETUP | Setup Manager Agent | modified | Added AC 5 (customization check) and AC 6 (same-version confirmation) |

### New User Stories

None. The new behavior stays within the existing actor/goal scope of
`SYSP_US_SETUP` (syspilot user wanting minimal-effort install/update).
A new US would be warranted only if the actor or the "so that" goal changed —
neither does here.

### Decisions

- **Decision 1 — No new US:** Both new behaviors (customization preservation
  and same-version gate) are sub-steps of the existing "update an existing
  project" goal already expressed in `SYSP_US_SETUP`. Extending the existing US
  with two new ACs is correct; adding a new US would create redundancy.
- **Decision 2 — Two new ACs:** AC 5 covers the customization-check-and-restore
  path. AC 6 covers the idempotent-update confirmation. They are distinct
  enough to warrant separate ACs.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_REQ_SETUP_DUTIES | Setup Manager Duties | modified | Added AC-6 (Customization Guard duty) |
| SYSP_REQ_SETUP_WORKFLOW | Setup Manager Workflow | modified | Added AC-5 (same-version check) and AC-6 (customization check before overwrite) |

### Decisions

- **Decision 1 — AC-5 in WORKFLOW:** The same-version gate is a workflow behaviour, not a duty; placed in SYSP_REQ_SETUP_WORKFLOW.
- **Decision 2 — AC-6 in both DUTIES and WORKFLOW:** The customization check is both a named duty (what the agent does) and a workflow step (when/how it does it).

### Horizontal Check (MECE)

- [x] No contradictions with existing requirements
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Specs

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_SPEC_SETUP_DUTIES | Setup Manager Duties | modified | Added duty 8: Customization Guard |
| SYSP_SPEC_SETUP_WORKFLOW | Setup Manager Workflow | modified | Step 2 expanded with same-version check (ask-questions, graceful stop); Step 4 expanded with customization check (ask-questions, save list, post-update reminder) |

### Design Decisions

- **Decision 1 — ask-questions skill for both interactions:** Both the same-version gate (step 2) and the customization check (step 4) use the ask-questions skill for consistent UX via VS Code quick-pick.
- **Decision 2 — Graceful stop message:** When user declines reinstall, the agent prints "Already up to date — nothing to do." and exits without error. This is explicit and user-friendly.
- **Decision 3 — Save-and-remind pattern:** The customization list is collected before the update and displayed again after, keeping user control without blocking the automated update.

### Horizontal Check (MECE)

- [x] No contradictions with existing design specs
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Final Consistency Check

**Status**: ⏳ not started
