# Change Document: hygiene-workflow-req-links

**Status**: ready-for-merge
**Branch**: feature/hygiene-workflow-req-links
**Created**: 2026-07-17
**Author**: PM + User
**GH Issue**: #41
**Operation Mode**: autonomous

---

## Summary

All per-agent workflow requirements (e.g. `SYSP_REQ_PM_WORKFLOW`, `SYSP_REQ_CM_WORKFLOW`, etc.) should carry an outgoing `:links:` to `SYSP_REQ_AGENT_ARCH_WORKFLOW` to indicate they implement the agent architecture contract. Currently only frontmatter REQs do this correctly — workflow REQs don't. Discovered as an out-of-scope follow-up during the `generic-agent-workflow-pattern` CR (2026-06-29).

Motivation: same traceability-consistency principle already applied to frontmatter REQs via the `agent-spec-base-toolset-links` CR — extending it to workflow REQs closes a known gap and would let a doc-build cross-check make the gap visible going forward.

Acceptance criteria: every per-agent `SYSP_REQ_*_WORKFLOW` requirement links to `SYSP_REQ_AGENT_ARCH_WORKFLOW`; sphinx-build `-W` passes clean.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

No User Stories modified. The following existing US are related context (their per-agent workflow REQs now properly trace to the architecture contract):

SYSP_US_AGENT_ARCH, SYSP_US_CM, SYSP_US_IMPLEMENT, SYSP_US_DOCU, SYSP_US_MECE, SYSP_US_QM, SYSP_US_TRACE, SYSP_US_RELEASE, SYSP_US_SETUP, SYSP_US_DESIGN, SYSP_US_UAT, SYSP_US_VERIFY

### New User Stories

None.

### Decisions

- No L0 changes needed — this is a pure traceability hygiene fix at L1.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_CM_WORKFLOW | SYSP_US_CM | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_IMPLEMENT_WORKFLOW | SYSP_US_IMPLEMENT | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_DOCU_WORKFLOW | SYSP_US_DOCU | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_MECE_WORKFLOW | SYSP_US_MECE | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_QM_WORKFLOW | SYSP_US_QM | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_TRACE_WORKFLOW | SYSP_US_TRACE | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_RELEASE_WORKFLOW | SYSP_US_RELEASE | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_INSTALLER_WORKFLOW | SYSP_US_INSTALLER | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_DESIGN_WORKFLOW | SYSP_US_DESIGN | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_UAT_WORKFLOW | SYSP_US_UAT | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |
| SYSP_REQ_VERIFY_WORKFLOW | SYSP_US_VERIFY | :links: added | Added `SYSP_REQ_AGENT_ARCH_WORKFLOW` |

### New Requirements

None.

### Conflicts Detected

None.

### Decisions

- SYSP_REQ_PM_WORKFLOW already had the link — confirmed, no change needed.
- SYSP_REQ_DOC_WORKFLOWS excluded — it is a documentation REQ, not a per-agent workflow REQ.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

None — this CR only adds `:links:` at L1.

### New Design Elements

None.

### Conflicts Detected

None.

### Decisions

- No L2 changes needed — traceability links are an L1 concern.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

All 11 per-agent `SYSP_REQ_*_WORKFLOW` requirements now link to `SYSP_REQ_AGENT_ARCH_WORKFLOW`. Combined with the pre-existing `SYSP_REQ_PM_WORKFLOW` link, all 12 per-agent workflow REQs are traceable to the architecture contract.

### Artefakt-Removal-Check

Not applicable — no artefacts removed.

### Issues Found

None. MECE and Trace checks both clean on first review round.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for merge
- [x] Test Designer: not applicable (no new behavior; only AC is sphinx-build -W, already confirmed clean)
- [x] Dev Engineer: not applicable (no code changes)
- [x] Documentation Engineer: not applicable (internal spec hygiene, no user-facing doc impact)

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-07-17

#### Findings

None. All 12 per-agent workflow REQs accounted for, exclusion list correct, no redundancy, no broken links.

---

---

*Generated by syspilot Change Agent*
