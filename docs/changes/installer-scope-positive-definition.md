# Change Document: installer-scope-positive-definition

**Status**: in-progress
**Branch**: feature/installer-scope-positive-definition
**Created**: 2026-05-16
**Author**: PM

---

## Summary

Define the Installer's installation scope explicitly and positively: only
`agents/`, `prompts/`, `skills/`, `templates/` from `syspilot/` are copied
to user projects. syspilot-internal sources (`docs/syspilot/`, change docs) are
never copied. Additionally, if the target project has no `docs/index.rst`, the
Installer creates a minimal starter one; existing docs structures are never
overwritten.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_INSTALLER | Installer Agent | modified | Add scope AC + doc-bootstrap AC |

### New User Stories

None.

### Decisions

- D-1: Scope defined as positive list (what IS installed), not negative list
- D-2: Scope covers product subdirs: `agents/`, `prompts/`, `skills/`, `templates/`
- D-3: Doc-bootstrap creates minimal `index.rst` only when none exists
- D-4: Existing `docs/index.rst` is never modified by the Installer

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies (scope definition is new; doc-bootstrap is new)
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_INSTALLER_DUTIES | SYSP_US_INSTALLER | modified | AC-1 scoped to installation scope |
| SYSP_REQ_INSTALLER_WORKFLOW | SYSP_US_INSTALLER | modified | New ACs for scope + doc-bootstrap |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_INSTALLER_SCOPE | Installer Installation Scope | SYSP_US_INSTALLER | mandatory |
| SYSP_REQ_INSTALLER_DOC_BOOTSTRAP | Installer Doc Bootstrap | SYSP_US_INSTALLER | mandatory |

### Decisions

- D-5: `SYSP_REQ_INSTALLER_SCOPE` is a separate REQ (not folded into Duties or Workflow)
- D-6: `SYSP_REQ_INSTALLER_DOC_BOOTSTRAP` is a separate REQ (distinct concern from scope)

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_INSTALLER_WORKFLOW | SYSP_REQ_INSTALLER_WORKFLOW | modified | Step 4 references scope; Step 5 adds doc-bootstrap |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_INSTALLER_SCOPE | Installer Scope Definition | SYSP_REQ_INSTALLER_SCOPE |
| SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP | Installer Doc Bootstrap | SYSP_REQ_INSTALLER_DOC_BOOTSTRAP |

### Decisions

- D-7: Scope table in SPEC lists exactly which syspilot/ subdirs are copied and which are excluded
- D-8: Doc-bootstrap spec prescribes minimal `index.rst` content

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ⏳ not started

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_SCOPE | SYSP_SPEC_INSTALLER_SCOPE | ✅ |
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_DOC_BOOTSTRAP | SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP | ✅ |
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_DUTIES (modified) | SYSP_SPEC_INSTALLER_DUTIES | ✅ |
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_WORKFLOW (modified) | SYSP_SPEC_INSTALLER_WORKFLOW (modified) | ✅ |

### Artefakt-Removal-Check

*No artefacts removed in this CR.*

### Issues Found

- M-6 (accepted as-is): AC-6 in SYSP_US_INSTALLER uses semicolon to separate two scenarios within one AC. Cosmetic only — both scenarios are testable. No change made per PM decision.

### Defer

- M-5 (deferred to `agent-md-spec-references-refactor`): DRY violation — scope table and index.rst template are inlined in Agent MD instead of referencing SPEC. Watch-item: Recipe-Implementation-Drift.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation
