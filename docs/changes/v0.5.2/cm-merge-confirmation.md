# Change Document: cm-merge-confirmation

**Status**: in-progress
**Branch**: feature/cm-merge-confirmation
**Created**: 2026-05-01
**Author**: syspilot.cm

---

## Summary

After merging to development, CM sends a confirmation message to PM via
Jarvis with the merge commit hash and branch name. The existing pre-merge
notification (post-engineer, pre-merge) remains unchanged — this adds a
separate post-merge confirmation step.

---

## Change Request (from PM)

> **Intent (WHAT):**
> After merging to development, the Change Manager shall send a merge
> confirmation to PM with the commit hash.
>
> **Motivation (WHY):**
> Currently the CM workflow ends silently after merging. PM has no
> confirmation that the merge happened or which commit hash it produced.
>
> **Acceptance Criteria:**
> 1. After a successful merge, CM SHALL send a confirmation message to PM
>    via Jarvis with the merge commit hash and branch name
> 2. The existing "Upon completion" notification (pre-merge) SHALL remain
>    unchanged — the new confirmation is an additional post-merge step

---

## Impact Analysis (CM)

**Performed**: 2026-05-01
**Method**: `get_need_links.py <id> --direction in --depth 1` from SYSP_US_CM, then depth 1 from relevant REQs.

**From SYSP_US_CM (relevant REQs):**
```
SYSP_REQ_CM_DUTIES, SYSP_REQ_CM_WORKFLOW
```

**From CM REQs (direct SPECs):**
```
SYSP_REQ_CM_DUTIES   → SYSP_SPEC_CM_DUTIES
SYSP_REQ_CM_WORKFLOW → SYSP_SPEC_CM_WORKFLOW
```

**In-scope elements:**
- SYSP_US_CM
- SYSP_REQ_CM_DUTIES, SYSP_REQ_CM_WORKFLOW
- SYSP_SPEC_CM_DUTIES, SYSP_SPEC_CM_WORKFLOW

**Out of scope:** Soul (character trait, not affected). PM/QM elements (receiver, not sender).

**Agent file in scope:**
- `syspilot/agents/syspilot.cm.agent.md`

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/cm-merge-confirmation |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | — | AC-9 added to SYSP_US_CM |
| Design (L1) | syspilot.design | ✅ | — | AC-9 to SYSP_REQ_CM_DUTIES; AC-11 to SYSP_REQ_CM_WORKFLOW |
| Design (L2) | syspilot.design | ✅ | — | Duty 8 to SYSP_SPEC_CM_DUTIES; Step 10 to SYSP_SPEC_CM_WORKFLOW |
| Implement | syspilot.implement | ✅ | 4dc84ac | — |
| Verify | syspilot.verify | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_CM` | Change Manager Agent | modified | Post-merge confirmation step |

### Designer Section

**Decision:** Add AC-9 to `SYSP_US_CM`. The existing 8 ACs cover intake, orchestration, quality gates, pre-merge notification (AC-5), and PM merge approval gate (AC-8). None captured the post-merge confirmation. AC-9 closes this gap at the user story level.

**AC-9 text:**
> Given a successful merge to development, When the merge completes, Then CM SHALL send a post-merge confirmation message to PM via Jarvis containing the merge commit hash and branch name

**Status change:** None — `SYSP_US_CM` remains `draft` (it was already draft from prior changes).

---

## Level 1: Requirements

**Status**: ✅ done

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_CM_DUTIES` | `SYSP_US_CM` | modified | AC-9 added: post-merge confirmation duty |
| `SYSP_REQ_CM_WORKFLOW` | `SYSP_US_CM` | modified | AC-11 added: post-merge confirmation workflow step |

### Designer Section

**SYSP_REQ_CM_DUTIES — AC-9 (new):**
> After a successful merge, CM SHALL send a post-merge confirmation message to PM via Jarvis containing the merge commit hash and branch name

Rationale: Duties is the behavioural capability inventory. The confirmation is a new duty CM gains; existing AC-8 (no merge without approval) is the pre-condition, AC-9 is the post-condition.

**SYSP_REQ_CM_WORKFLOW — AC-11 (new):**
> After merging to development, CM SHALL send a post-merge confirmation message to PM via Jarvis containing the merge commit hash and branch name

Rationale: Workflow is the sequence model. AC-10 is the merge gate; AC-11 is the explicit step that follows it. Numbering is sequential to avoid renumbering existing ACs.

---

## Level 2: Design

**Status**: ✅ done

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_CM_DUTIES` | `SYSP_REQ_CM_DUTIES` | modified | Duty 8 added: Post-Merge Confirmation |
| `SYSP_SPEC_CM_WORKFLOW` | `SYSP_REQ_CM_WORKFLOW` | modified | Step 10 added + process flow updated |

### Designer Section

**SYSP_SPEC_CM_DUTIES — Duty 8 (new):**
> **Post-Merge Confirmation** — After a successful merge to development, send a post-merge confirmation message to PM via Jarvis containing the merge commit hash and branch name

Rationale: Duties enumerates what CM does. Duty 7 is the merge gate (pre-merge); Duty 8 is the post-merge act. The separation is deliberate — Duty 8 fires only after the merge succeeds.

**SYSP_SPEC_CM_WORKFLOW — Step 10 (new):**
> **Post-Merge Confirmation** — After merging to development, send a confirmation message to PM via Jarvis containing the merge commit hash and branch name.

Also updated the Process Flow diagram to append: `→ Post-Merge Confirmation (Jarvis to PM: commit hash + branch name)` as the final step.

Rationale: Step 9 ends with the merge decision and the actual merge. Step 10 is a distinct follow-up act, explicitly separated so implementers know it happens after the merge completes.

---

## Final Consistency Check

**Status**: ⏳ not started

### Traceability Verification

| Chain | Status |
|-------|--------|
| SYSP_US_CM → SYSP_REQ_CM_DUTIES → SYSP_SPEC_CM_DUTIES | ⏳ |
| SYSP_US_CM → SYSP_REQ_CM_WORKFLOW → SYSP_SPEC_CM_WORKFLOW | ⏳ |

---

## Sign-off

- [ ] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] PM approval received
- [ ] Merged to development
