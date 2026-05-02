# Change Document: qm-mece-per-level

**Status**: in-progress
**Branch**: feature/qm-mece-per-level
**Created**: 2026-05-01
**Author**: syspilot.cm

---

## Summary

QM dispatches separate MECE checks per specification level (L0, L1, L2)
rather than a single combined run. Each MECE invocation receives exactly one
level as input. The Findings Report shows per-level results.

---

## Change Request (from PM)

> **Intent (WHAT):**
> The QM Agent shall explicitly dispatch MECE checks as separate horizontal
> passes per specification level (L0 User Stories, L1 Requirements, L2 Design
> Specs) rather than combining them into a single MECE run.
>
> **Motivation (WHY):**
> Without this, QM instances combine all levels into one pass and miss the
> horizontal cross-element consistency check that the MECE Engineer is designed
> for. This was observed during the cm-merge-confirmation review where the
> initial QM check missed level-specific issues that a per-level dispatch
> would have caught.
>
> **Acceptance Criteria:**
> 1. QM SHALL dispatch separate MECE checks for each specification level (L0, L1, L2) within the scope of the change
> 2. The QM Findings Report SHALL clearly indicate per-level results (which level passed/failed)
> 3. The MECE Engineer invocation SHALL receive a single level as input parameter, not "all levels at once"

---

## Impact Analysis (CM)

**Performed**: 2026-05-01
**Method**: `get_need_links.py <id> --direction in --depth 1` from SYSP_US_QM, then depth 1 from relevant REQs.

**From SYSP_US_QM (relevant REQs):**
```
SYSP_REQ_QM_DUTIES, SYSP_REQ_QM_WORKFLOW
```

**From QM REQs (direct SPECs):**
```
SYSP_REQ_QM_DUTIES   → SYSP_SPEC_QM_DUTIES
SYSP_REQ_QM_WORKFLOW → SYSP_SPEC_QM_WORKFLOW
```

**In-scope elements:**
- SYSP_US_QM
- SYSP_REQ_QM_DUTIES, SYSP_REQ_QM_WORKFLOW
- SYSP_SPEC_QM_DUTIES, SYSP_SPEC_QM_WORKFLOW

**Out of scope:** SOUL (dispatch mechanism is not a character trait). FRONTMATTER/PROMPT.

**Agent file in scope:**
- `syspilot/agents/syspilot.qm.agent.md`

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/qm-mece-per-level |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | — | SYSP_US_QM: AC-4 modified, AC-6 added |
| Design (L1) | syspilot.design | ✅ | — | SYSP_REQ_QM_DUTIES: AC-1 mod, AC-6 added; SYSP_REQ_QM_WORKFLOW: AC-2, AC-3 mod |
| Design (L2) | syspilot.design | ✅ | — | SYSP_SPEC_QM_DUTIES: Duty 1 rewritten; SYSP_SPEC_QM_WORKFLOW: Steps 3-5 + flow updated |
| Implement | syspilot.implement | ✅ | f7f7cfd | — |
| Verify | syspilot.verify | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_QM` | Quality Manager Agent | modified | Per-level MECE dispatch |

### Designer Section

**Changes made to SYSP_US_QM:**

- **AC-4 modified**: Added "with clearly separated per-level results" to reflect CR-AC-2 (Findings Report shows per-level pass/fail).
- **AC-6 added**: "Given QM performs MECE checks, When it dispatches the MECE Engineer, Then each invocation targets exactly one specification level (L0, L1, or L2)" — covers CR-AC-1 and CR-AC-3.

**Rationale**: AC-4 now sets the user expectation that per-level results are visible in the report. AC-6 expresses the dispatch granularity from the user perspective (WHY: I want independent checks per level so issues at one level don't mask another).

---

## Level 1: Requirements

**Status**: ✅ done

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_QM_DUTIES` | `SYSP_US_QM` | modified | Per-level MECE dispatch duty |
| `SYSP_REQ_QM_WORKFLOW` | `SYSP_US_QM` | modified | Three separate MECE invocations + per-level results in report |

### Designer Section

**Changes made to SYSP_REQ_QM_DUTIES:**
- **AC-1 modified**: From "can dispatch MECE Engineer to check specification levels" to "SHALL dispatch the MECE Engineer separately for each specification level in scope (L0, L1, L2) — one invocation per level" (CR-AC-1).
- **AC-6 added**: "Each MECE Engineer invocation SHALL receive exactly one specification level as input — never combined levels" (CR-AC-3).

**Changes made to SYSP_REQ_QM_WORKFLOW:**
- **AC-2 modified**: Made explicit that dispatch is separate invocations, one per level (CR-AC-1).
- **AC-3 modified**: Findings Report now required to show per-level pass/fail status (CR-AC-2).

---

## Level 2: Design

**Status**: ✅ done

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_QM_DUTIES` | `SYSP_REQ_QM_DUTIES` | modified | — |
| `SYSP_SPEC_QM_WORKFLOW` | `SYSP_REQ_QM_WORKFLOW` | modified | — |

### Designer Section

**Changes made to SYSP_SPEC_QM_DUTIES:**
- **Duty 1 rewritten**: Replaces "check one or all specification levels" (ambiguous) with explicit per-level dispatch semantics: "each invocation receives exactly one level as input — never combined levels" (CR-AC-1, CR-AC-3).

**Changes made to SYSP_SPEC_QM_WORKFLOW:**
- **Step 3 (Dispatch) updated**: Made per-level dispatch explicit with three separate MECE invocations (CR-AC-1, CR-AC-3).
- **Step 4 (Collect) updated**: Explicitly collects per-level findings (CR-AC-2).
- **Step 5 (Report) updated**: Requires clearly separated per-level results with pass/fail status (CR-AC-2).
- **Process Flow diagram updated**: Three distinct MECE dispatch lines (L0, L1, L2) instead of single "all levels" line; Findings Report label now reads "per-level pass/fail" (CR-AC-2).

---

## Final Consistency Check

**Status**: ⏳ not started

### Traceability Verification

| Chain | Status |
|-------|--------|
| SYSP_US_QM → SYSP_REQ_QM_DUTIES → SYSP_SPEC_QM_DUTIES | ⏳ |
| SYSP_US_QM → SYSP_REQ_QM_WORKFLOW → SYSP_SPEC_QM_WORKFLOW | ⏳ |

---

## Sign-off

- [ ] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] PM approval received
- [ ] Merged to development
