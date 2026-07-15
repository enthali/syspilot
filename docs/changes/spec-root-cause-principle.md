# Change Document: spec-root-cause-principle

**Status**: complete
**Branch**: feature/spec-root-cause-principle
**Created**: 2026-07-15
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

During a Jarvis QM review session, a pattern emerged 3/3 times: when a code-level defect is found, the spec — not the code — is the primary suspect. In all three cases the symptom was "code is wrong" but the actual root cause was upstream — wrong/missing spec text, or a missing cross-link that hid an affected consumer from impact analysis (a spec-coverage gap, not a coding error). Formalize this as a named principle anchored in at least two agent specs: (1) Quality Manager (`syspilot.qm`) — as a verification duty: trace a code-level defect upward to the spec before filing it as a pure implementation slip; (2) Dev Engineer (`syspilot.implement`) — as an explicit guardrail: reject a direct code patch that would diverge from an approved spec, and escalate for a spec correction instead. Acceptance criteria: both specs carry an explicit duty/guardrail requiring root-cause attribution to the spec layer before a code-level defect is classified as a pure implementation slip. Not Jarvis-specific — a general spec-driven-development discipline. Exact wording/placement style (Duty bullet vs. Soul/guardrail vs. workflow step) is left to the System Designer's judgment per agent-file conventions; suggested draft wording is in GH #46 as a non-binding reference.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_QM | Quality Manager Agent | modified | Added duty bullet + AC-9 for spec-layer root-cause attribution |
| SYSP_US_IMPLEMENT | Dev Engineer Agent | modified | Added duty bullet + AC-5 for spec-divergence escalation |

### New User Stories

None.

### Decisions

- Decision 1: No new US elements — the principle adds duties to existing agents, not new capability requests
- Decision 2: QM gets the *verification* facet (trace upward), Dev Engineer gets the *escalation* facet (refuse to patch around)

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
| SYSP_REQ_QM_DUTIES | SYSP_US_QM | modified | Added AC-8 for spec-layer root-cause assessment |
| SYSP_REQ_IMPLEMENT_DUTIES | SYSP_US_IMPLEMENT | modified | Added AC-5 for spec-divergence escalation |

### New Requirements

None.

### Conflicts Detected

None.

### Decisions

- Decision 1: Both are additional ACs on existing REQ elements — the principle is an additional duty facet, not a new requirement category

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
| SYSP_SPEC_QM_DUTIES | SYSP_REQ_QM_DUTIES | modified | Added "Spec-Layer Root-Cause Attribution" duty bullet |
| SYSP_SPEC_IMPLEMENT_DUTIES | SYSP_REQ_IMPLEMENT_DUTIES | modified | Added "Spec-Divergence Escalation" duty bullet |

### New Design Elements

None.

### Conflicts Detected

None.

### Decisions

- Decision 1: Placed as Duty bullets (not Guardrails, not Workflow steps) — permanent obligations that apply in every relevant situation

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_QM | SYSP_REQ_QM_DUTIES (AC-8) | SYSP_SPEC_QM_DUTIES | ✅ |
| SYSP_US_IMPLEMENT | SYSP_REQ_IMPLEMENT_DUTIES (AC-5) | SYSP_SPEC_IMPLEMENT_DUTIES | ✅ |

### Artefakt-Removal-Check

N/A — no artefact removed.

- [x] N/A

### Issues Found

None.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## UAT

**Status**: ✅ completed

### Summary

Commit `05edcd1`. `SYSP_US_UAT_SPEC_ROOT_CAUSE_PRINCIPLE` (+ req/spec) — 3 executable scenarios: QM traces defect upward before classifying it, Dev Engineer escalates rather than patching around a spec-diverging defect, and a regression replay of the actual installer-frontmatter-sync incident confirming the new QM duty would have routed it correctly. Toctree warnings noted (pre-existing, unrelated to UAT files) — fixed by Documentation Engineer.

### Issues Found

None.

---

## Implementation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `syspilot/agents/syspilot.qm.agent.md` | Product source — new "Spec-Layer Root-Cause Attribution" duty bullet |
| `.github/agents/syspilot.qm.agent.md` | Installed instance — kept in sync |
| `syspilot/agents/syspilot.implement.agent.md` | Product source — new "Spec-Divergence Escalation" duty bullet |
| `.github/agents/syspilot.implement.agent.md` | Installed instance — kept in sync |

### Issues Found

None.

---

## Documentation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `docs/index.rst` | Fold-in fix: added 2 pre-existing experience docs to Field Notes toctree (committed `55164ab`, predating this branch) — sphinx-build now 0 warnings |

### Reviewed, No Change Needed

- `docs/architecture.md` — no per-agent duty content to update
- `docs/methodology.md` — no root-cause-attribution description
- `docs/workflows.md` — no relevant content

### Issues Found

None.

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** QM
**Review date:** 2026-07-15

#### Findings

None. Independently verified all three risk areas (not relying on the CD narrative alone):

- **Traceability chain completeness at all three levels** — verified via grep + needs.json spot-check:
  - QM: `SYSP_US_QM` (links pre-existing, unchanged) → `SYSP_REQ_QM_DUTIES` (AC-8 added) → `SYSP_SPEC_QM_DUTIES` (duty bullet added)
  - Dev Engineer: `SYSP_US_IMPLEMENT` (links pre-existing, unchanged) → `SYSP_REQ_IMPLEMENT_DUTIES` (AC-5 added as new, distinct from pre-existing second AC-5) → `SYSP_SPEC_IMPLEMENT_DUTIES` (duty bullet added)
  - All 6 elements exist with correct links; chains complete ✅
- **Agent file duty bullets match spec wording verbatim (product + instance)** — spot-checked duty bullet text:
  - QM agent (`syspilot/agents/` + `.github/agents/`): "**Spec-Layer Root-Cause Attribution** — Given a code-level defect is found, QM traces the defect upward to the specification layer before classifying it as a pure implementation slip — no code-level finding is closed without verifying whether wrong or missing spec text, or a missing cross-link, is the actual root cause."  matches `SYSP_SPEC_QM_DUTIES` exactly ✅
  - Dev Engineer agent (`syspilot/agents/` + `.github/agents/`): "**Spec-Divergence Escalation** — When a code-level defect implies the approved spec is wrong or incomplete, the Dev Engineer does not patch around the discrepancy but escalates for spec correction — no code change silently diverges from an approved spec." matches `SYSP_SPEC_IMPLEMENT_DUTIES` exactly ✅
  - Product and instance files confirmed byte-identical via `Compare-Object` ✅
- **Regression test genuineness** — AC-3 references the `installer-frontmatter-sync` incident (real repo history):
  - Confirmed via `git log` + `git branch`: feature/installer-frontmatter-sync branch exists with commits showing Finding 1 (HIGH, ed5104b) and Round 2 fix verification (934589c)
  - Historical state reproduced: Installer agent file had stale "Local Customization Preservation" duty contradicting its already-corrected spec, missed by `remove-tools-frontmatter`'s impact analysis (missing-link class gap, exactly as described in UAT AC-3)
  - This is the genuine incident class GH #46 was created to prevent ✅
- **Schema validation** — sphinx-build `-W --keep-going` returned 0 warnings ✅
- **Documentation** — docs/index.rst toctree fold-in fix confirmed (pre-existing experience docs added to Field Notes), committed in commit 7c42ecd ✅

**Verdict:** Clean. No findings raised.

#### PM Decisions

N/A — no findings to decide on.

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
