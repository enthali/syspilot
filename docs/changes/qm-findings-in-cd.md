# Change Document: qm-findings-in-cd

**Status**: review
**Branch**: feature/qm-findings-in-cd
**Created**: 2026-06-18
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

QM findings currently live only in ephemeral Jarvis messages. Once read, they are gone. The Change Document records a short final disposition per finding, but not the original finding text, iteration history, or PM rationale. This is an audit-trail gap.

This CR adds a `## QM Findings` section to the Change Document template. QM writes structured findings there directly (in addition to the Jarvis notification). PM records decisions in the same section. Multiple review rounds are appended as sub-sections. Closes GitHub issue #27.

---

## WHY

After a release, reconstructing why a spec says what it says is impossible from the archived CD alone. The QM session that produced the findings is gone; the Jarvis messages are consumed and lost; only the short "Issues Found" summary in the CD survives.

This blocks post-hoc learning, audit, and onboarding of new contributors who want to understand past decisions.

---

## WHAT

Add a `## QM Findings` section to the Change Document template (`syspilot/templates/change-document.md`). Update QM spec duties and workflow to require writing findings into the CD. Update PM spec to require recording decisions in the CD.

The CD Markdown file becomes the single durable audit record for every CR.

---

## Acceptance Criteria

- `syspilot/templates/change-document.md` contains a `## QM Findings` section with documented structure for findings and PM decisions
- QM spec (duties + workflow) describes the obligation to write findings into the CD `## QM Findings` section
- PM spec describes the obligation to record fix/defer/accept-as-is decisions in the same section
- Multiple QM rounds are supported (appended as sub-sections, e.g. `### Round 1`, `### Round 2`)
- Existing CDs without the section are unaffected (section is additive, not required retroactively)

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_QM | Quality Manager Agent | modified | Added Findings Durability duty bullet (German) + AC-8 for CD-based findings |
| SYSP_US_PM | Project Manager Agent | modified | Added Entscheidungs-Dokumentation duty bullet (German) + AC-8 for CD-based decision recording |

### New User Stories

None — the existing user stories are broad enough to cover this additive behavior.

### Decisions

- Decision 1: No new user stories required. Both SYSP_US_QM and SYSP_US_PM already describe the respective agent's duties at a level that encompasses audit trail responsibilities. We extend the existing duties lists rather than creating separate stories.

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
| SYSP_REQ_QM_DUTIES | SYSP_US_QM | modified | Added AC-7: QM writes findings into CD ## QM Findings section |
| SYSP_REQ_QM_WORKFLOW | SYSP_US_QM | modified | Added AC-6: CD write step per review round |
| SYSP_REQ_PM_DUTIES | SYSP_US_PM | modified | Added AC-9: PM records decision with rationale in CD |

### New Requirements

None.

### Conflicts Detected

None.

### Decisions

- Decision 1: PM_WORKFLOW is touched indirectly (the QM Findings Review sub-workflow gains a Record step), but the requirement `SYSP_REQ_PM_WORKFLOW` already covers the workflow broadly; adding a new AC to `SYSP_REQ_PM_DUTIES` is sufficient and avoids duplication.

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
| SYSP_SPEC_QM_DUTIES | SYSP_REQ_QM_DUTIES | modified | Added Findings Durability duty |
| SYSP_SPEC_QM_WORKFLOW | SYSP_REQ_QM_WORKFLOW | modified | Step 5 updated; process flow diagram updated |
| SYSP_SPEC_PM_DUTIES | SYSP_REQ_PM_DUTIES | modified | Added QM Decision Recording duty |
| SYSP_SPEC_PM_WORKFLOW | SYSP_REQ_PM_WORKFLOW | modified | QM Findings Review sub-workflow: step 4 Record added, old step 4 → step 5 |

### New Design Elements

None — the change document template section is an artefact, not a spec element.

### Conflicts Detected

None.

### Decisions

- Decision 1: Both the product template (`syspilot/templates/change-document.md`) and the installed template (`.github/templates/change-document.md`) are updated in this CR so the feature is active immediately without waiting for a release + Setup Agent run.
- Decision 2: The `## QM Findings` section is placed between the Final Consistency Check (CM territory) and the Appendix. This makes it naturally additive — existing CDs stop before that section and are unaffected.
- Decision 3: The round sub-structure (`### Round N`, `#### Findings`, `#### PM Decisions`) was chosen to support multi-round review without ambiguity while remaining simple to append.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_QM | SYSP_REQ_QM_DUTIES | SYSP_SPEC_QM_DUTIES | ✅ |
| SYSP_US_QM | SYSP_REQ_QM_WORKFLOW | SYSP_SPEC_QM_WORKFLOW | ✅ |
| SYSP_US_PM | SYSP_REQ_PM_DUTIES | SYSP_SPEC_PM_DUTIES | ✅ |
| SYSP_US_PM | SYSP_REQ_PM_WORKFLOW | SYSP_SPEC_PM_WORKFLOW | ✅ |

### Artefakt-Removal-Check

*Not applicable — this CR only adds artefacts (new section to templates, new duty/workflow bullets). No artefact is removed.*

### Issues Found

None.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## QM Findings

### Round 1

**Reviewed by:** QM  
**Review date:** 2026-06-18

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | CD | Final Consistency Check — Row 4 | Traceability table claims `SYSP_SPEC_PM_WORKFLOW` links to `SYSP_REQ_PM_DUTIES`, but the actual `:links:` field in the spec reads `SYSP_REQ_PM_WORKFLOW`. The spec link itself is correct and semantically valid; only the CD table entry is wrong. | high |
| 2 | L1 | SYSP_REQ_QM_DUTIES AC-7 | AC-7 states "QM writes findings into `## QM Findings` section" but does not specify the Round-N sub-section structure or cardinality, while SYSP_REQ_QM_WORKFLOW AC-6 does. Minor scope inconsistency between DUTIES and WORKFLOW ACs; all CR acceptance criteria are satisfied. | low |
| 3 | L1 | SYSP_REQ_PM_WORKFLOW AC-9 | AC-9 describes the QM Findings Review step (evaluate + merge decision) but does not explicitly mention "record decision with rationale in CD". This obligation is covered by SYSP_REQ_PM_DUTIES AC-9 (new) and fully detailed in SYSP_SPEC_PM_WORKFLOW Step 4. The gap is defensible but leaves the WORKFLOW AC incomplete relative to the DUTIES. | low |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | CD table entry corrected (SYSP_REQ_PM_DUTIES → SYSP_REQ_PM_WORKFLOW). 1-line fix, no spec change. |
| 2 | 2 | accept-as-is | Separation of concerns is valid: DUTIES = obligation, WORKFLOW = structure. AC-7 states the obligation; AC-6 defines the structure. No duplication risk. |
| 3 | 3 | accept-as-is | SYSP_SPEC_PM_WORKFLOW Step 4 is explicit. REQ-level need not repeat every SPEC detail. SYSP_REQ_PM_DUTIES AC-9 owns the obligation. |

### Round 2

**Reviewed by:** QM  
**Review date:** 2026-06-18

#### Findings

No findings. F1 fix verified: CD table row 4 corrected to `SYSP_REQ_PM_WORKFLOW` — matches actual `:links:` in spec. Fix commit 9396864 touches CD only (+4/-4 lines); no spec files modified. Schema clean (unchanged since last build). F2/F3 accept-as-is rationale accepted: DUTIES/WORKFLOW separation is a valid architectural choice; SYSP_SPEC_PM_WORKFLOW Step 4 provides implementation-level detail that REQ level is not required to repeat.

#### PM Decisions

*(No new findings — no decisions required.)*

---

## Appendix: Link Discovery Results

```
SYSP_REQ_QM_DUTIES → linked_from: [SYSP_SPEC_QM_DUTIES]
SYSP_REQ_QM_WORKFLOW → linked_from: [SYSP_SPEC_QM_WORKFLOW]
SYSP_REQ_PM_DUTIES → linked_from: [SYSP_SPEC_PM_DUTIES]
SYSP_REQ_PM_WORKFLOW → linked_from: [SYSP_SPEC_PM_WORKFLOW]
SYSP_REQ_QM_DUTIES → links: [SYSP_US_QM]
SYSP_REQ_PM_DUTIES → links: [SYSP_US_PM]
```

---

*Generated by syspilot Change Agent*
