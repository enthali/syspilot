# Change Document: qm-auditor-only

**Status**: in-progress
**Branch**: feature/qm-auditor-only
**Created**: 2026-05-01
**Author**: syspilot.cm

---

## Summary

QM is an auditor that reports findings — it never creates Change Requests
directly. All QM output (regardless of trigger type) is a Findings Report
addressed to PM. PM decides what happens: fix now (→ CR to CM), defer, or
accept as-is. This simplifies the QM model to one output format and fully
aligns with the Merge Gate pattern established in qm-merge-gate.

---

## Change Request (from PM)

> **Mode:** user-guided
>
> **Scope:**
> As a syspilot user, I want the Quality Manager to always produce Findings
> Reports routed to PM — never create Change Requests directly. QM is an
> auditor that reports; PM decides what happens with findings.
>
> **Motivation:**
> QM Soul and Duties currently say "create Change Requests" for
> periodic/on-demand checks. This is wrong — QM should never autonomously
> trigger changes. Only PM has the authority to decide whether findings become
> CRs, get deferred, or are accepted. This simplifies the QM model (one
> output format: Findings Report → PM) and aligns with the Merge Gate pattern.
>
> **Acceptance Criteria:**
> 1. QM always produces Findings Reports addressed to PM — regardless of trigger type
> 2. QM never creates Change Requests directly
> 3. PM decides for each finding: fix now (→ CR to CM) / defer / accept

---

## Impact Analysis (CM)

**Performed**: 2026-05-01
**Method**: `get_need_links.py <id> --direction in --depth 1` from SYSP_US_QM, then depth 1 from each resulting REQ.

**From SYSP_US_QM (direct REQs):**
```
SYSP_REQ_QM_SOUL, SYSP_REQ_QM_DUTIES, SYSP_REQ_QM_WORKFLOW,
SYSP_REQ_QM_FRONTMATTER, SYSP_REQ_QM_PROMPT
```

**From QM REQs (direct SPECs):**
```
SYSP_REQ_QM_SOUL     → SYSP_SPEC_QM_SOUL
SYSP_REQ_QM_DUTIES   → SYSP_SPEC_QM_DUTIES
SYSP_REQ_QM_WORKFLOW → SYSP_SPEC_QM_WORKFLOW
```

**PM impact assessment:**
SYSP_US_PM → SYSP_REQ_PM_DUTIES/WORKFLOW already updated in qm-merge-gate
(Duty 7: QM Findings Review & Merge Decision). No additional PM changes
required — PM model already reflects the intended behavior.

**In-scope elements (behavioral/soul concern):**
- SYSP_US_QM
- SYSP_REQ_QM_SOUL, SYSP_REQ_QM_DUTIES, SYSP_REQ_QM_WORKFLOW
- SYSP_SPEC_QM_SOUL, SYSP_SPEC_QM_DUTIES, SYSP_SPEC_QM_WORKFLOW

**Out of scope:** FRONTMATTER and PROMPT elements (not behavioral concerns).
PM elements — already updated in qm-merge-gate.

**Agent file in scope:**
- `syspilot/agents/syspilot.qm.agent.md`

**Note:** Previous CR (qm-merge-gate) already forked QM workflow by trigger
type (targeted → PM, periodic → CRs to CM). This CR collapses that fork:
ALL trigger types → Findings Report → PM. The qm-merge-gate work for QM
Duty 7 + workflow fork is superseded/simplified by this CR.

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/qm-auditor-only |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | 59d7575 | US_QM context + AC-2 updated; AC-6 removed |
| Design (L1) | syspilot.design | ✅ | e20c0f6 | QM Soul/Duties/Workflow: CR creation removed |
| Design (L2) | syspilot.design | ✅ | facb417 | SPEC_QM Soul/Duties/Workflow: auditor-only model |
| Implement | syspilot.implement | ✅ | 3fbb0c9 | QM agent: auditor-only model, unified Findings Report → PM |
| Verify | syspilot.verify | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_QM` | Quality Manager Agent | modified | Single output type: Findings Report → PM |

### Designer Section

**Decision:** Collapse from dual-mode to single-mode output.

- **Context paragraph**: Removed "QM creates Change Requests for the Change Manager to fix" → replaced with "QM produces a Findings Report addressed to PM. PM decides: fix now (→ CR to CM), defer, or accept as-is."
- **AC-2**: Updated from "creates Change Requests with findings" to "produces a Findings Report addressed to PM."
- **AC-6**: Removed — now redundant; updated AC-2 covers all trigger types uniformly. AC-5 retained (describes the CM-completion trigger mechanism, not routing).

---

## Level 1: Requirements

**Status**: ✅ done

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_QM_SOUL` | `SYSP_US_QM` | modified | Remove CR-authoring from character; auditor identity |
| `SYSP_REQ_QM_DUTIES` | `SYSP_US_QM` | modified | Remove "create CRs" duty; single output = Findings Report |
| `SYSP_REQ_QM_WORKFLOW` | `SYSP_US_QM` | modified | Collapse fork; all triggers → Findings Report → PM |

### Designer Section

**Decision:** Remove the CR-creation responsibilities at the requirements level and collapse the trigger-based fork.

- **SYSP_REQ_QM_SOUL AC-3**: "findings that lead to Change Requests" → "findings as a Findings Report addressed to PM"
- **SYSP_REQ_QM_DUTIES**: Removed old AC-4 ("QM can create Change Requests"). Old AC-5 renumbered AC-4 (targeted check trigger). Old AC-6 generalized and renumbered AC-5: QM routes ALL findings to PM; NEVER creates CRs directly.
- **SYSP_REQ_QM_WORKFLOW**: Removed old AC-4 ("creates Change Requests for CM"). Old AC-5 renumbered AC-4 (targeted check trigger). Old AC-6 generalized and renumbered AC-5: all trigger types → Findings Report → PM; QM SHALL NOT create CRs autonomously.

---

## Level 2: Design

**Status**: ✅ done

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_QM_SOUL` | `SYSP_REQ_QM_SOUL` | modified | Auditor identity; no CR creation |
| `SYSP_SPEC_QM_DUTIES` | `SYSP_REQ_QM_DUTIES` | modified | Remove CR creation duty |
| `SYSP_SPEC_QM_WORKFLOW` | `SYSP_REQ_QM_WORKFLOW` | modified | Collapse trigger fork; uniform output |

### Designer Section

**Decision:** Collapse the trigger-based fork at the design level; single output format for all trigger types.

- **SYSP_SPEC_QM_SOUL**: Updated soul text from "you create Change Requests" to "you produce a Findings Report addressed to PM — you never fix things directly and never create CRs."
- **SYSP_SPEC_QM_DUTIES**: Duty 4 renamed from "Change Request Creation" to "Findings Report" with updated description (produce Findings Report to PM). Duty 7 "Merge Findings Report" removed — now folded into updated Duty 4.
- **SYSP_SPEC_QM_WORKFLOW**: Act step collapsed from a trigger-type fork to a uniform rule. Output updated to "Findings Report → PM". Process Flow diagram simplified: single terminal node replacing the conditional branches.

---

## Final Consistency Check

**Status**: ⏳ not started

### Traceability Verification

| Chain | Status |
|-------|--------|
| SYSP_US_QM → SYSP_REQ_QM_SOUL → SYSP_SPEC_QM_SOUL | ⏳ |
| SYSP_US_QM → SYSP_REQ_QM_DUTIES → SYSP_SPEC_QM_DUTIES | ⏳ |
| SYSP_US_QM → SYSP_REQ_QM_WORKFLOW → SYSP_SPEC_QM_WORKFLOW | ⏳ |

---

## Sign-off

- [ ] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] PM approval received
- [ ] Merged to development
