# Change Document: operation-mode-signalling

**Status**: ready-for-merge
**Branch**: feature/operation-mode-signalling
**Created**: 2026-05-23
**Author**: PM

---

## Summary

Re-introduce a structural channel for PM to declare a CR's operation mode to CM. An earlier CR removed the `Authoring Mode` field from the Change Document template on the rationale "redundant since PM sets branch context", which is incorrect: the branch encodes the change, not the workflow style. Today PM signals mode either as freetext in the CR body (interpretive, easy to miss) or not at all, with CM having to ask at intake. **Motivation**: closes the structural gap left by the field removal, makes the CD a self-contained contract, and enables future ultra-minimal PM→CM dispatch (the CD path alone, with everything else read from the CD). **Acceptance criteria**: (AC1) The Change Document template contains an `Operation Mode:` header field next to `Status`, `Branch`, `Created`, `Author`, with allowed values `autonomous` | `user-guided`. (AC2) PM creates no CD without filling `Operation Mode`. (AC3) CM reads `Operation Mode` from the CD header as authoritative; the mode value (if any) in the dispatch message is a sanity check only. (AC4) When the dispatch message contains a mode value that disagrees with the CD header, CM stops and asks the user instead of silently picking a winner. (AC5) Existing CDs (already merged) are not migrated; the new field applies to all CDs created from merge-date forward.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_PM | Project Manager Agent | unchanged | User-facing intent already covers Change Initialization; Operation Mode is an internal detail |
| SYSP_US_CM | Change Manager Agent | unchanged | User-facing intent already covers end-to-end orchestration; mode reading is an internal detail |

### New User Stories

None — the existing user stories cover the intent at the correct abstraction level.

### Decisions

- Decision 1: No new user stories needed. The addition of a header field to the Change Document is an internal process mechanism, not a new user-facing capability. Both SYSP_US_PM and SYSP_US_CM remain unchanged.

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
| SYSP_REQ_PM_DUTIES | SYSP_US_PM | modified | AC-5 extended with Operation Mode in header fields list; AC-5a added (mandatory fill) |
| SYSP_REQ_PM_WORKFLOW | SYSP_US_PM | modified | AC-6 clarified to include Operation Mode in header |
| SYSP_REQ_CM_WORKFLOW | SYSP_US_CM | modified | AC-13 added (read from CD header as authoritative); AC-14 added (disagreement → ask user) |

### New Requirements

None — all ACs fit naturally into existing requirements (see Decisions).

### Conflicts Detected

None.

### Decisions

- Decision 1: Scatter ACs into existing SYSP_REQ_PM_DUTIES, SYSP_REQ_PM_WORKFLOW, SYSP_REQ_CM_WORKFLOW rather than creating a standalone REQ for "CD Operation Mode Field". Rationale: Operation Mode is one aspect of the existing Change Initialization responsibility (PM) and the existing Receive+Intent Gate (CM); a standalone REQ would fragment these concerns without adding traceability value.

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
| SYSP_SPEC_PM_DUTIES | SYSP_REQ_PM_DUTIES | modified | Change Initialization extended with Operation Mode field |
| SYSP_SPEC_PM_WORKFLOW | SYSP_REQ_PM_WORKFLOW | modified | Create Change Document step extended with Operation Mode in header |
| SYSP_SPEC_CM_DUTIES | SYSP_REQ_CM_DUTIES | modified | Mode prose rewritten: CD header is authoritative, dispatch-message is sanity check, disagreement → ask user |
| SYSP_SPEC_CM_WORKFLOW | SYSP_REQ_CM_WORKFLOW | modified | Receive+Intent Gate extended: read Operation Mode from CD header, handle disagreement |

### New Design Elements

None — all changes fit into existing SPEC elements.

### Conflicts Detected

None.

### Decisions

- Decision 1: The existing mode prose in SYSP_SPEC_CM_DUTIES (lines ~61-62) was rewritten rather than appended to, because the old text ("When a CR specifies autonomous mode...") was ambiguous about the source of truth. The new text clarifies CD header is authoritative.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| AC | Requirement(s) | Design Spec(s) | Complete? |
|----|----------------|----------------|-----------|
| AC1: CD template contains `Operation Mode:` header field | SYSP_REQ_PM_DUTIES AC-5, AC-5a | SYSP_SPEC_PM_DUTIES (Change Initialization) | ✅ |
| AC2: PM creates no CD without filling `Operation Mode` | SYSP_REQ_PM_DUTIES AC-5a | SYSP_SPEC_PM_DUTIES (Change Initialization), SYSP_SPEC_PM_WORKFLOW (step 8) | ✅ |
| AC3: CM reads `Operation Mode` from CD header as authoritative | SYSP_REQ_CM_WORKFLOW AC-13 | SYSP_SPEC_CM_DUTIES (mode prose), SYSP_SPEC_CM_WORKFLOW (Receive+Intent Gate) | ✅ |
| AC4: Disagreement between dispatch message and CD header → CM asks user | SYSP_REQ_CM_WORKFLOW AC-14 | SYSP_SPEC_CM_DUTIES (mode prose), SYSP_SPEC_CM_WORKFLOW (Receive+Intent Gate) | ✅ |
| AC5: Existing merged CDs are NOT migrated | Non-action — verified by absence | No migration spec exists | ✅ (verified by absence) |

### Artefakt-Removal-Check

This CR **adds** a field (`Operation Mode:`) rather than removing one. However, the prior `Authoring Mode` field removal (in CR `pm-owns-branch-and-change-setup`) is related context.

Project-wide grep on "Authoring Mode" confirms:
- **No active spec or template references** — the prior CR's Artefakt-Removal-Check correctly handled all class (a) and (b) references
- **Only historical CD references** remain (in `docs/changes/pm-owns-branch-and-change-setup.md`) — acceptable historic stranding, already documented there
- **No class (c) issue** introduced by this CR

- [x] No artefact removal in this CR — check is informational only
- [x] Prior removal of `Authoring Mode` was correctly handled (confirmed via grep)

### Issues Found

None.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Implementation: template + PM + CM agent files updated (commit `b0dfe7e`)
- [x] Docu: workflows.md updated (commit `e9813b9`)
- [x] sphinx-build clean (1 pre-existing unrelated warning)
- [x] Ready for QM targeted check + PM merge to development

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
