# Change Document: qm-merge-gate

**Status**: in-progress
**Branch**: feature/qm-merge-gate
**Created**: 2026-05-01
**Author**: syspilot.cm

---

## Summary

Changes must not be merged to development until QM has reviewed and PM has
approved the merge. QM results are always routed to PM, who decides whether
findings are fixed immediately, deferred, or accepted as-is. This introduces
a formal merge gate between QM review and development merge.

---

## Change Request (from PM)

> **Mode:** user-guided
>
> **Scope:**
> As a syspilot user, I want changes to be merged to development only after
> QM approval — and the PM decides whether QM findings are fixed immediately,
> deferred to a later release, or accepted as-is.
>
> **Motivation:**
> CM merged to development before QM could review. Findings had to be fixed
> retroactively on development (messy). PM needs decision authority over
> merge timing based on QM results.
>
> **Acceptance Criteria:**
> 1. CM does not merge to development without PM approval
> 2. QM results are always routed to PM
> 3. PM decides: fix now / fix later / accept as-is

---

## Impact Analysis (CM)

**Performed**: 2026-05-01
**Method**: `get_need_links.py <id> --direction in --depth 1` from US nodes, then depth 1 from each resulting REQ.

**From SYSP_US_CM (direct REQs):**
```
SYSP_REQ_CM_SOUL, SYSP_REQ_CM_DUTIES, SYSP_REQ_CM_WORKFLOW,
SYSP_REQ_CM_FRONTMATTER, SYSP_REQ_CM_PROMPT
```

**From SYSP_US_PM (direct REQs):**
```
SYSP_REQ_PM_SOUL, SYSP_REQ_PM_DUTIES, SYSP_REQ_PM_WORKFLOW,
SYSP_REQ_PM_FRONTMATTER, SYSP_REQ_PM_PROMPT
```

**From SYSP_US_QM (direct REQs):**
```
SYSP_REQ_QM_SOUL, SYSP_REQ_QM_DUTIES, SYSP_REQ_QM_WORKFLOW,
SYSP_REQ_QM_FRONTMATTER, SYSP_REQ_QM_PROMPT
```

**From CM REQs (direct SPECs):**
```
SYSP_REQ_CM_WORKFLOW  → SYSP_SPEC_CM_WORKFLOW
SYSP_REQ_CM_DUTIES    → SYSP_SPEC_CM_DUTIES
```

**From PM REQs (direct SPECs):**
```
SYSP_REQ_PM_WORKFLOW  → SYSP_SPEC_PM_WORKFLOW
SYSP_REQ_PM_DUTIES    → SYSP_SPEC_PM_DUTIES
```

**From QM REQs (direct SPECs):**
```
SYSP_REQ_QM_WORKFLOW  → SYSP_SPEC_QM_WORKFLOW
SYSP_REQ_QM_DUTIES    → SYSP_SPEC_QM_DUTIES
```

**Cross-reference (aggregator):**
```
SYSP_SPEC_DOC_WORKFLOWS  links to SYSP_SPEC_CM_WORKFLOW + SYSP_SPEC_PM_WORKFLOW
→ docs/workflows.md may need updating (Docu Agent scope)
```

**In-scope elements (behavioral/workflow concern):**
- SYSP_US_CM, SYSP_US_PM, SYSP_US_QM
- SYSP_REQ_CM_DUTIES, SYSP_REQ_CM_WORKFLOW
- SYSP_REQ_PM_DUTIES, SYSP_REQ_PM_WORKFLOW
- SYSP_REQ_QM_DUTIES, SYSP_REQ_QM_WORKFLOW
- SYSP_SPEC_CM_DUTIES, SYSP_SPEC_CM_WORKFLOW
- SYSP_SPEC_PM_DUTIES, SYSP_SPEC_PM_WORKFLOW
- SYSP_SPEC_QM_DUTIES, SYSP_SPEC_QM_WORKFLOW
- SYSP_SPEC_DOC_WORKFLOWS (aggregator — monitor for sync)

**Out of scope:** FRONTMATTER and PROMPT elements (not behavioral concerns).
SOUL elements — merge gate is a workflow/duties concern, not a character trait.

**Agent files in scope:**
- `syspilot/agents/syspilot.cm.agent.md`
- `syspilot/agents/syspilot.pm.agent.md`
- `syspilot/agents/syspilot.qm.agent.md`

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/qm-merge-gate |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | 8f2416d | US_CM AC-8; US_PM AC-6/7; US_QM AC-6 |
| Design (L1) | syspilot.design | ✅ | 20a567b | REQ_CM/PM/QM Duties+Workflow ACs |
| Design (L2) | syspilot.design | ✅ | d83d01e | SPEC_CM/PM/QM Duties+Workflow updated |
| Implement | syspilot.implement | ✅ | 2c14277 | agent files updated from approved specs |
| Verify | syspilot.verify | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_CM` | Change Manager Agent | modified | Merge gate + PM approval step |
| `SYSP_US_PM` | Project Manager Agent | modified | QM result routing + merge decision authority |
| `SYSP_US_QM` | Quality Manager Agent | modified | Results routed to PM, not only CM |

### Designer Section

**Decision:** All three user stories require new ACs to encode the merge gate concept at the user-visible level.

- **SYSP_US_CM** — Added AC-8: CM must explicitly request PM approval and wait before merging to development. Status: `approved` → `draft`.
- **SYSP_US_PM** — Added AC-6 (PM receives QM findings and decides fix/defer/accept) and AC-7 (PM communicates merge approval to CM). Status: `approved` → `draft`.
- **SYSP_US_QM** — Added AC-6: QM routes targeted-check findings to PM (not directly to CM) for merge decision. Status remains `draft`.

**Rationale:** The merge gate is a user-visible behavioral change — it directly affects how the user perceives the workflow end (wait for PM approval). Encoding it at L0 anchors all lower-level requirements and design specs to an explicit user story.

---

## Level 1: Requirements

**Status**: ✅ done

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_CM_DUTIES` | `SYSP_US_CM` | likely modified | Merge gate duty |
| `SYSP_REQ_CM_WORKFLOW` | `SYSP_US_CM` | likely modified | PM approval step before merge |
| `SYSP_REQ_PM_DUTIES` | `SYSP_US_PM` | likely modified | QM result reception + merge decision |
| `SYSP_REQ_PM_WORKFLOW` | `SYSP_US_PM` | likely modified | Merge approval workflow step |
| `SYSP_REQ_QM_DUTIES` | `SYSP_US_QM` | likely modified | Route findings to PM |
| `SYSP_REQ_QM_WORKFLOW` | `SYSP_US_QM` | likely modified | Findings delivery to PM |

### Designer Section

**Decision:** Six requirements updated to encode the merge gate at requirement level.

- **SYSP_REQ_CM_DUTIES** — Added AC-8: CM SHALL NOT merge without explicit PM approval. Status → `draft`.
- **SYSP_REQ_CM_WORKFLOW** — Added AC-10: CM requests PM approval before merge; proceeds only after explicit PM approval. Status → `draft`.
- **SYSP_REQ_PM_DUTIES** — Added AC-7 (receive QM findings), AC-8 (decide fix/defer/accept), AC-9 (communicate merge decision to CM). Status → `draft`.
- **SYSP_REQ_PM_WORKFLOW** — Added AC-7: PM evaluates QM findings and communicates merge decision to CM before CM can merge. Status → `draft`.
- **SYSP_REQ_QM_DUTIES** — Added AC-6: for CM-completion triggered checks, route findings to PM; do not create CRs autonomously. Already `draft`.
- **SYSP_REQ_QM_WORKFLOW** — Added AC-6: distinguishes periodic checks (AC-4, CRs to CM) from targeted checks (AC-6, findings to PM). Already `draft`.

**Rationale:** The merge gate is a behavioral contract across three agents. Requirements must be explicit about who holds decision authority (PM), who executes (CM), and who supplies input (QM). The periodic vs. targeted check distinction preserves QM's independent auditing function.

---

## Level 2: Design

**Status**: ✅ done

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_CM_DUTIES` | `SYSP_REQ_CM_DUTIES` | likely modified | — |
| `SYSP_SPEC_CM_WORKFLOW` | `SYSP_REQ_CM_WORKFLOW` | likely modified | — |
| `SYSP_SPEC_PM_DUTIES` | `SYSP_REQ_PM_DUTIES` | likely modified | — |
| `SYSP_SPEC_PM_WORKFLOW` | `SYSP_REQ_PM_WORKFLOW` | likely modified | — |
| `SYSP_SPEC_QM_DUTIES` | `SYSP_REQ_QM_DUTIES` | likely modified | — |
| `SYSP_SPEC_QM_WORKFLOW` | `SYSP_REQ_QM_WORKFLOW` | likely modified | — |
| `SYSP_SPEC_DOC_WORKFLOWS` | `SYSP_REQ_DOC_WORKFLOWS` | monitor | Aggregator — keep in sync |

### Designer Section

**Decision:** Six design specs updated. Status → `draft` for all six.

- **SYSP_SPEC_CM_DUTIES** — Added Duty 7: Merge Approval Gate — CM waits for PM's explicit approval after QM delivers findings; does not merge autonomously.
- **SYSP_SPEC_CM_WORKFLOW** — Added Step 9 (Await PM Merge Approval) and updated Process Flow with the merge gate step.
- **SYSP_SPEC_PM_DUTIES** — Added Duty 7: QM Findings Review & Merge Decision — PM receives QM report, evaluates, decides fix/defer/accept, communicates to CM.
- **SYSP_SPEC_PM_WORKFLOW** — Added QM Findings Review sub-workflow (4 steps: Receive → Evaluate → Decide → Communicate). Placed after the existing planning workflow.
- **SYSP_SPEC_QM_DUTIES** — Added Duty 7: Merge Findings Report — for CM-completion targeted checks, QM produces a report to PM (not a CR to CM).
- **SYSP_SPEC_QM_WORKFLOW** — Updated Act step and Process Flow to fork on trigger type: periodic/on-demand → CRs to CM; CM-completion → Findings Report to PM.

**SYSP_SPEC_DOC_WORKFLOWS** (aggregator): no change required — workflows.md describes the overall flow at a high level; Docu Agent will update it during the Implement phase.

**Traceability note:** All changes trace cleanly up the hierarchy:
- CM AC-8 ← SYSP_REQ_CM_DUTIES AC-8 ← SYSP_US_CM AC-8
- PM Duty 7 ← SYSP_REQ_PM_DUTIES AC-7/8/9 ← SYSP_US_PM AC-6/7
- QM Duty 7 ← SYSP_REQ_QM_DUTIES AC-6 ← SYSP_US_QM AC-6

---

## Final Consistency Check

**Status**: ✅ done

### Traceability Verification

| Chain | Status |
|-------|--------|
| SYSP_US_CM AC-8 → SYSP_REQ_CM_DUTIES AC-8 / SYSP_REQ_CM_WORKFLOW AC-10 → SYSP_SPEC_CM_DUTIES Duty-7 / SYSP_SPEC_CM_WORKFLOW Step-9 | ✅ |
| SYSP_US_PM AC-6/7 → SYSP_REQ_PM_DUTIES AC-7/8/9 / SYSP_REQ_PM_WORKFLOW AC-7 → SYSP_SPEC_PM_DUTIES Duty-7 / SYSP_SPEC_PM_WORKFLOW QM-sub-flow | ✅ |
| SYSP_US_QM AC-6 → SYSP_REQ_QM_DUTIES AC-6 / SYSP_REQ_QM_WORKFLOW AC-6 → SYSP_SPEC_QM_DUTIES Duty-7 / SYSP_SPEC_QM_WORKFLOW Act-fork | ✅ |

---

## Sign-off

- [ ] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] PM approval received
- [ ] Merged to development
