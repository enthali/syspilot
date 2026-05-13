# Change Document: pm-duties-completeness

**Status**: in-progress
**Branch**: feature/pm-duties-completeness
**Created**: 2026-05-02
**Author**: syspilot.cm

---

## Summary

PM Duties are extended with Release-Trigger (PM decides when to release +
invokes Release Agent) and Setup-Trigger (PM triggers instance update via
Setup Agent after release). Additionally, SYSP_US_DESIGN AC1 is clarified:
Designer reads the Change Document created by CM — not creates it.

---

## Change Request (from PM)

> **Mode:** autonomous
>
> **WHAT:**
> 1. PM Duties: add Release-Trigger (PM decides when to release, invokes Release Agent)
> 2. PM Duties: add Setup-Trigger (PM triggers post-release instance update via Setup Agent)
> 3. C1-Fix: SYSP_US_DESIGN AC1 — clarify that CM creates the Change Document,
>    Designer reads/updates it
>
> **WHY:**
> PM has de facto Release and Setup responsibility that is not anchored in
> Duties anywhere. Without an explicit Duty it only exists in the `agents:`
> field — invisible to the agent at runtime. C1 is a contradiction at L0
> that confuses implementers.
>
> **ACs:**
> - PM Duties contain a Release-Duty (decision + invocation of Release Agent)
> - PM Duties contain a Setup-Duty (post-release instance update via Setup Agent)
> - SYSP_US_DESIGN AC1 says clearly: Designer reads the Change Document created by CM

---

## Impact Analysis (CM)

**Performed**: 2026-05-02
**Method**: `get_need_links.py <id> --direction in --depth 1` from SYSP_US_PM and SYSP_US_DESIGN, then depth 1 from relevant REQs.

**From SYSP_US_PM (relevant REQs):**
```
SYSP_REQ_PM_DUTIES, SYSP_REQ_PM_WORKFLOW
```

**From SYSP_US_DESIGN (relevant REQ for AC1 fix):**
```
SYSP_REQ_DESIGN_SOUL  → SYSP_SPEC_DESIGN_SOUL
```
*(AC1 is expressed at US level → REQ_SOUL → SPEC_SOUL)*

**From REQs (direct SPECs):**
```
SYSP_REQ_PM_DUTIES    → SYSP_SPEC_PM_DUTIES
SYSP_REQ_PM_WORKFLOW  → SYSP_SPEC_PM_WORKFLOW
SYSP_REQ_DESIGN_SOUL  → SYSP_SPEC_DESIGN_SOUL
```

**In-scope elements:**
- SYSP_US_PM, SYSP_US_DESIGN
- SYSP_REQ_PM_DUTIES, SYSP_REQ_PM_WORKFLOW
- SYSP_REQ_DESIGN_SOUL
- SYSP_SPEC_PM_DUTIES, SYSP_SPEC_PM_WORKFLOW
- SYSP_SPEC_DESIGN_SOUL

**Out of scope:** PM SOUL (character, not affected). FRONTMATTER/PROMPT.

**Agent files in scope:**
- `syspilot/agents/syspilot.pm.agent.md`
- `syspilot/agents/syspilot.design.agent.md` (AC1 fix)

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/pm-duties-completeness |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | — | SYSP_US_PM ACs 8–9; SYSP_US_DESIGN AC-1 fix |
| Design (L1) | syspilot.design | ✅ | — | SYSP_REQ_PM_DUTIES ACs 10–11; SYSP_REQ_PM_WORKFLOW ACs 8–9; SYSP_REQ_DESIGN_SOUL AC-4 |
| Design (L2) | syspilot.design | ✅ | — | SYSP_SPEC_PM_DUTIES Duties 8–9; SYSP_SPEC_PM_WORKFLOW Release Workflow; SYSP_SPEC_DESIGN_SOUL Guardrails |
| Implement | syspilot.implement | ✅ | cd6157e | PM Release+Setup duties, Designer reads Change Document |
| Verify | syspilot.verify | ⏳ | — | — |
| PM Approval | PM | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ done

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_PM` | Project Manager Agent | modified | Release + Setup duties as user-visible capabilities |
| `SYSP_US_DESIGN` | System Designer Agent | modified | AC1 clarification: Designer reads CM's Change Document |

### Designer Section

**Decisions:**
- `SYSP_US_PM`: Added AC-8 (Release-Trigger: PM decides release criteria met → invokes Release Agent) and AC-9 (Setup-Trigger: PM invokes Setup Agent after successful release) as user-visible behavioural commitments at the story level.
- `SYSP_US_DESIGN` AC-1: Changed "Then it creates a Change Document" → "Then it reads the Change Document created by CM". This removes the contradiction where both CM and Designer were implied to create the Change Document.

**Elements written:** `SYSP_US_PM` (ACs 8–9 added), `SYSP_US_DESIGN` (AC-1 corrected)

---

## Level 1: Requirements

**Status**: ✅ done

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_PM_DUTIES` | `SYSP_US_PM` | modified | Release-Duty (AC-10) + Setup-Duty (AC-11) added |
| `SYSP_REQ_PM_WORKFLOW` | `SYSP_US_PM` | modified | Release-Trigger step (AC-8) + Setup-Trigger step (AC-9) |
| `SYSP_REQ_DESIGN_SOUL` | `SYSP_US_DESIGN` | modified | AC-4: Designer reads Change Document created by CM |

### Designer Section

**Decisions:**
- `SYSP_REQ_PM_DUTIES`: Added AC-10 (PM SHALL decide when to release and invoke Release Agent) and AC-11 (PM SHALL invoke Setup Agent after successful release). Numbered sequentially after existing AC-9 to avoid renumbering.
- `SYSP_REQ_PM_WORKFLOW`: Added AC-8 (Release-Trigger step) and AC-9 (Setup-Trigger step) as workflow-level requirements capturing the sequencing of these new duties.
- `SYSP_REQ_DESIGN_SOUL`: Added AC-4 to the Soul requirement to anchor the AC-1 fix from US_DESIGN at the requirement level. The Soul requirement is the correct level for role-boundary constraints (what the Designer does/does not create).

**Elements written:** `SYSP_REQ_PM_DUTIES` (ACs 10–11), `SYSP_REQ_PM_WORKFLOW` (ACs 8–9), `SYSP_REQ_DESIGN_SOUL` (AC-4)

---

## Level 2: Design

**Status**: ✅ done

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_PM_DUTIES` | `SYSP_REQ_PM_DUTIES` | modified | Duty 8 (Release-Trigger) + Duty 9 (Setup-Trigger) added |
| `SYSP_SPEC_PM_WORKFLOW` | `SYSP_REQ_PM_WORKFLOW` | modified | Release Workflow sub-section added |
| `SYSP_SPEC_DESIGN_SOUL` | `SYSP_REQ_DESIGN_SOUL` | modified | Guardrails extended: reads Change Document, does not create it |

### Designer Section

**Decisions:**
- `SYSP_SPEC_PM_DUTIES`: Added Duty 8 **Release-Trigger** (evaluate release criteria → decide → invoke Release Agent) and Duty 9 **Setup-Trigger** (invoke Setup Agent after successful release). These are concrete design-level duties traceable to the new ACs in SYSP_REQ_PM_DUTIES.
- `SYSP_SPEC_PM_WORKFLOW`: Added a **Release Workflow** sub-section (5-step event-driven workflow: evaluate readiness → decide → invoke Release Agent → confirm → invoke Setup Agent). This mirrors the structure of the existing QM Findings Review Workflow and is traceable to the new ACs in SYSP_REQ_PM_WORKFLOW.
- `SYSP_SPEC_DESIGN_SOUL`: Extended Guardrails with "Never creates Change Documents — reads and updates the one created by CM." This is a guardrail (Soul-level constraint), appropriate in the Soul spec, and directly traces to SYSP_REQ_DESIGN_SOUL AC-4 and SYSP_US_DESIGN AC-1.

**Elements written:** `SYSP_SPEC_PM_DUTIES` (Duties 8–9), `SYSP_SPEC_PM_WORKFLOW` (Release Workflow), `SYSP_SPEC_DESIGN_SOUL` (Guardrails extended)

---

## Final Consistency Check

**Status**: ✅ done

### Traceability Verification

| Chain | Status |
|-------|--------|
| SYSP_US_PM (AC-8,9) → SYSP_REQ_PM_DUTIES (AC-10,11) → SYSP_SPEC_PM_DUTIES (Duties 8–9) | ✅ |
| SYSP_US_PM (AC-8,9) → SYSP_REQ_PM_WORKFLOW (AC-8,9) → SYSP_SPEC_PM_WORKFLOW (Release Workflow) | ✅ |
| SYSP_US_DESIGN (AC-1) → SYSP_REQ_DESIGN_SOUL (AC-4) → SYSP_SPEC_DESIGN_SOUL (Guardrails) | ✅ |

---

## Sign-off

- [ ] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] PM approval received
- [ ] Merged to development
