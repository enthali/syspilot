# Change Document: pm-cm-role-boundary

**Status**: in-progress
**Branch**: feature/pm-cm-role-boundary
**Created**: 2026-04-30
**Author**: syspilot.cm

---

## Summary

PM writes CRs from user perspective only — intent + user-visible ACs, no
implementation details. CM always follows the complete change process and
documents its progress in the Change Document. The Design Agent must be able
to interact with the user directly (user-guided mode), requiring `vscode/askQuestions`
in its frontmatter.

---

## Change Request (from PM)

> **Scope:**
> As a syspilot user, I want the PM to describe only WHAT should be changed
> (from the user's perspective), and the CM to independently run the defined
> process (Branch → Change Doc → Impact → Design → Implement) — without the
> PM prescribing HOW.
>
> **Motivation:**
> The PM included too many implementation details in past CRs.
> The CM subsequently skipped process steps (Impact Analysis, Design).
> The role boundary must be anchored in the agent specs.

---

## Impact Analysis (CM)

**Performed**: 2026-04-30
**Method**: `get_need_links.py --direction in --depth 1` from SYSP_US_PM and SYSP_US_CM, then depth 1 from each resulting REQ.
**Note**: Script invoked directly from product path (`syspilot/skills/...`) — correct path per installed skill is `.github/skills/syspilot.impact-python/scripts/get_need_links.py`. This is a process gap addressed by this CR.

**From SYSP_US_PM (direct REQs):**
```
SYSP_REQ_PM_DUTIES, SYSP_REQ_PM_SOUL, SYSP_REQ_PM_WORKFLOW,
SYSP_REQ_PM_FRONTMATTER, SYSP_REQ_PM_PROMPT
```

**From SYSP_US_CM (direct REQs):**
```
SYSP_REQ_CM_DUTIES, SYSP_REQ_CM_SOUL, SYSP_REQ_CM_WORKFLOW,
SYSP_REQ_CM_FRONTMATTER, SYSP_REQ_CM_PROMPT
```

**From PM REQs (direct SPECs):**
```
SYSP_REQ_PM_SOUL     → SYSP_SPEC_PM_SOUL
SYSP_REQ_PM_DUTIES   → SYSP_SPEC_PM_DUTIES
SYSP_REQ_PM_WORKFLOW → SYSP_SPEC_PM_WORKFLOW
```

**From CM REQs (direct SPECs):**
```
SYSP_REQ_CM_SOUL     → SYSP_SPEC_CM_SOUL
SYSP_REQ_CM_DUTIES   → SYSP_SPEC_CM_DUTIES
SYSP_REQ_CM_WORKFLOW → SYSP_SPEC_CM_WORKFLOW
```

**Cross-reference (aggregator):**
```
SYSP_SPEC_DOC_WORKFLOWS  links to SYSP_SPEC_CM_WORKFLOW + SYSP_SPEC_PM_WORKFLOW
→ docs/workflows.md must be updated by Docu Agent
```

**Note:** FRONTMATTER and PROMPT REQs/SPECs are in the impact tree but initially considered out of scope — however SYSP_REQ_DESIGN_FRONTMATTER is in scope (see addendum below).

**Addendum — Design Agent frontmatter (found during design discussion):**
```
SYSP_US_DESIGN  →  SYSP_REQ_DESIGN_FRONTMATTER  →  SYSP_SPEC_DESIGN_FRONTMATTER
```
The Design Agent needs `vscode/askQuestions` in its `tools:` frontmatter to support
user-guided mode. Without it, the agent cannot ask the user for level approvals.
Impact queried via installed skill (`.github/skills/syspilot.impact-python/scripts/get_need_links.py`).

**Agent files in scope:**
- `syspilot/agents/syspilot.pm.agent.md`
- `syspilot/agents/syspilot.change.agent.md`
- `syspilot/agents/syspilot.change.agent.md` (Design Agent — frontmatter tools list)

**Open question 1 for Designer:** The Change Document template (`syspilot/templates/change-document.md`) has no sphinx-needs ID and is not referenced in any SPEC. Designer to assess whether a new SPEC is needed or a reference in `SYSP_SPEC_CM_WORKFLOW` suffices.

**Open question 2 for Designer:** CM must load and use the installed skill instance before executing skill-dependent process steps (e.g., impact analysis). Currently no REQ or SPEC mandates this — the skill to load is referenced by name (e.g., `syspilot.impact-python`) not by path, keeping it implementation-agnostic. Designer to assess: does this require a new REQ (`SYSP_REQ_CM_SKILL_USAGE`) or does it fit into `SYSP_REQ_CM_WORKFLOW`?

---

## Desired Behavior (CM — documented from design discussion)

This section captures the agreed design intent before the Designer starts.
It is input context for the Designer — NOT implementation instructions.

### For the PM role

- CRs must be intent-based: WHAT the user wants + WHY + user-visible ACs
- CRs must NOT contain: file paths, code snippets, implementation steps, agent instructions
- If a CR is too technical, CM raises an alarm and asks the user whether this is intentional — regardless of whether the PM requested autonomous or user-guided mode

### For the CM role

**CM is a process controller, not a detail worker:**

- CM's context must stay focused on the process — it must not get lost in implementation details
- CM creates the Change Document (this document) as the first act after receiving a CR
- CM fills the Impact Analysis section itself
- CM delegates to the Designer with: CR intent + impact IDs + mode — nothing else
- CM does NOT prescribe solutions to the Designer
- CM checks quality gates: is the Change Document complete? Did each agent fill their section?
- CM's prompts to engineers are brief: "Here is the CR, here is the Change Doc, mode=X"

**Change Document as process log and recovery point:**

- The Change Document is created by CM at the start (this file)
- Each agent appends what it did to its dedicated section
- The process state is always readable from the Change Document
- If the session crashes, any CM can resume from the Change Document

**CM uses installed skills, not product skills:**

- Before executing any process step that depends on a skill (e.g., impact analysis),
  CM loads the skill from `.github/skills/` (the installed instance)
- CM does NOT call product skill files directly (e.g., `syspilot/skills/...`)
- The installed skill defines which tools to use — this keeps the process
  independent of the specific implementation (Python script today, MCP tomorrow)

**Designer interaction model (user-guided by default):**

- Designer uses `vscode_askQuestions` to get user approval level by level
- Designer is NOT instructed on what to write — it reads the specs and decides
- CM only enables autonomous mode if PM explicitly requests it
- **Prerequisite:** Designer agent frontmatter must include `vscode/askQuestions` in `tools:` — without it, user-guided mode is impossible

---

## Process Log

| Step | Agent | Status | Commit | Notes |
|------|-------|--------|--------|-------|
| Branch created | CM | ✅ | — | feature/pm-cm-role-boundary |
| Impact Analysis | CM | ✅ | — | See section above |
| Change Document | CM | ✅ | — | This file |
| Design (L0) | syspilot.design | ✅ | dd41914 | US_PM AC-5 added; US_CM context + AC-6, AC-7 added |
| Design (L1) | syspilot.design | ✅ | 224c65a | PM: AC-4/6/6; CM: Soul AC-4, Duties AC-6/7, Workflow AC-8/9; Design Frontmatter AC-4 |
| Design (L2) | syspilot.design | ✅ | 222afc8 | PM Soul/Duties/Workflow; CM Soul/Duties/Workflow; DOC_WORKFLOWS; Design Frontmatter |
| Implement | syspilot.implement | ✅ | df45e74 | PM Soul/Duties/Workflow; CM Soul/Duties/Workflow; Design Frontmatter tools |
| Verify | syspilot.verify | ⏳ | — | — |
| Merged | CM | ⏳ | — | — |

---

## Level 0: User Stories

**Status**: ✅ complete

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_PM` | Project Manager Agent | modified | Added AC-5: CR must be intent-based only |
| `SYSP_US_CM` | Change Manager Agent | modified | Context + AC-6 (CR quality gate) + AC-7 (Change Document) |

### Designer Section

**Decisions made:**

- **SYSP_US_PM AC-5 added:** The CR content constraint is anchored at the user story level as a user-visible outcome. Users benefit from PM producing clean, intent-only CRs that downstream agents can act on without ambiguity.

- **SYSP_US_CM context updated:** Added explicit statement that CM is a process controller that owns its workflow independently — CRs provide intent only, CM decides execution.

- **SYSP_US_CM AC-6 added:** CR quality gate — CM returns non-conforming CRs (those containing implementation instructions) to the submitter, regardless of requested execution mode. This is user-visible: the user sees consistent behavior.

- **SYSP_US_CM AC-7 added:** Change Document creation as first act — user-visible because it creates an auditable, recoverable process log.

**Open questions resolved (for L1/L2):**

- OQ1 (Change Document template): No new SPEC needed. Template is an implementation artifact referenced by SYSP_SPEC_CM_WORKFLOW. Will add a reference at L2.

- OQ2 (installed skill usage): No new `SYSP_REQ_CM_SKILL_USAGE`. The constraint fits as an AC within `SYSP_REQ_CM_WORKFLOW` at L1 — it is a workflow constraint, not a separate capability.

**FRONTMATTER and PROMPT elements:** Confirmed not affected by this CR — role boundary is a behavioral/process concern, not a configuration concern.

---

## Level 1: Requirements

**Status**: ✅ complete

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_REQ_PM_SOUL` | `SYSP_US_PM` | likely modified | Guardrail AC |
| `SYSP_REQ_PM_DUTIES` | `SYSP_US_PM` | likely modified | CR authoring constraint |
| `SYSP_REQ_PM_WORKFLOW` | `SYSP_US_PM` | likely modified | CR validation step |
| `SYSP_REQ_CM_SOUL` | `SYSP_US_CM` | likely modified | Process discipline AC |
| `SYSP_REQ_CM_DUTIES` | `SYSP_US_CM` | likely modified | CR intake + process enforcement |
| `SYSP_REQ_CM_WORKFLOW` | `SYSP_US_CM` | likely modified | Change Document + quality gates |
| `SYSP_REQ_DESIGN_FRONTMATTER` | `SYSP_US_DESIGN` | modified | Add vscode/askQuestions to tools list |

### Designer Section

**Decisions made:**

- **SYSP_REQ_PM_SOUL AC-4 added:** Content guardrail encoded as a character trait — PM always frames outputs in terms of user value and intent; file paths, code, or agent instructions are out of character.

- **SYSP_REQ_PM_DUTIES AC-6 added:** Explicit CR content restriction as a duty: only WHAT, WHY, and user-visible ACs are permitted; no implementation details.

- **SYSP_REQ_PM_WORKFLOW AC-6 added:** Workflow self-check step before delegation — PM reviews the CR for implementation details and revises before submitting to CM.

- **SYSP_REQ_CM_SOUL AC-4 added:** Positive framing of the intent-gateway role — CM treats implementation details in a CR as imprecise intent and works to extract and clarify the true intent before proceeding.

- **SYSP_REQ_CM_DUTIES AC-6 added:** When a CR contains implementation instructions, CM reasons about underlying intent and consults the user to clarify — regardless of operation mode.

- **SYSP_REQ_CM_DUTIES AC-7 added:** CM creates a Change Document as the first act after CR acceptance.

- **SYSP_REQ_CM_WORKFLOW AC-8 added:** CR conformance assessment step — if CR contains implementation instructions, CM reasons about intent, consults the user, agrees on a well-formulated CR, then proceeds.

- **SYSP_REQ_CM_WORKFLOW AC-9 added:** Change Document creation step in workflow — before invoking any engineer.

- **SYSP_REQ_DESIGN_FRONTMATTER AC-4 added:** `vscode/askQuestions` added to tools list — prerequisite for user-guided level approval.

**OQ2 resolution (L1 implementation):** Installed skill usage is not modelled at the requirements level — GitHub Copilot handles skill loading natively; this does not need to be specified as a system requirement.

**MECE check:** PM and CM requirement sets are each complete and non-overlapping. Soul (character), Duties (capabilities), Workflow (process steps) operate at distinct abstraction levels — no duplication.

---

## Level 2: Design

**Status**: ✅ complete

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| `SYSP_SPEC_PM_SOUL` | `SYSP_REQ_PM_SOUL` | likely modified | — |
| `SYSP_SPEC_PM_DUTIES` | `SYSP_REQ_PM_DUTIES` | likely modified | — |
| `SYSP_SPEC_PM_WORKFLOW` | `SYSP_REQ_PM_WORKFLOW` | likely modified | CR validation step in workflow |
| `SYSP_SPEC_CM_SOUL` | `SYSP_REQ_CM_SOUL` | likely modified | — |
| `SYSP_SPEC_CM_DUTIES` | `SYSP_REQ_CM_DUTIES` | likely modified | — |
| `SYSP_SPEC_CM_WORKFLOW` | `SYSP_REQ_CM_WORKFLOW` | likely modified | Change Document step + quality gates |
| `SYSP_SPEC_DOC_WORKFLOWS` | `SYSP_REQ_DOC_WORKFLOWS` | likely modified | Aggregates CM+PM workflow — must stay in sync |
| `SYSP_SPEC_DESIGN_FRONTMATTER` | `SYSP_REQ_DESIGN_FRONTMATTER` | modified | Add vscode/askQuestions to tools list |

### Designer Section

**Decisions made:**

- **SYSP_SPEC_PM_SOUL**: Guardrails extended — "CRs contain only user intent (WHAT), motivation (WHY), and user-visible ACs — no implementation details."

- **SYSP_SPEC_PM_DUTIES**: Duty 4 updated — intent-only CR authoring + self-check before submitting to CM.

- **SYSP_SPEC_PM_WORKFLOW**: New step 6 "CR Content Check" inserted between Plan and Delegate; Delegate → 7, Track → 8.

- **SYSP_SPEC_CM_SOUL**: Intent-gateway sentence added to soul text; Guardrails extended: implementation details in CRs are treated as imprecise intent to clarify, not instructions to follow.

- **SYSP_SPEC_CM_DUTIES**: Duty 1 updated to include intent reasoning + user consultation; new Duty 6 "Change Document Creation" as first act after CR acceptance.

- **SYSP_SPEC_CM_WORKFLOW**: Step 1 renamed to "Receive + Intent Gate" with intent-reasoning and user-consultation text; new Step 1a "Change Document"; new "CR Intent Gate" constraint section; process flow diagram updated.

- **SYSP_SPEC_DOC_WORKFLOWS**: Status Notes updated — workflows.md must reflect CM Intent Gate step, Change Document creation step, and PM CR Content Check step.

- **SYSP_SPEC_DESIGN_FRONTMATTER**: `vscode/askQuestions` added to tools list to enable user-guided level approval.

**OQ1 resolution (L2 implementation):** No new SPEC created for the Change Document template. `SYSP_SPEC_CM_WORKFLOW` Step 1a and `SYSP_SPEC_CM_DUTIES` Duty 6 reference `docs/changes/<name>.md` — this is sufficient without a standalone template SPEC.

**MECE check:** PM spec set (Soul/Duties/Workflow) covers character, capability, and process at distinct abstraction levels — no overlap. CM spec set same. SYSP_SPEC_DESIGN_FRONTMATTER covers only tool configuration — no overlap with workflow or soul specs.

---

## Final Consistency Check

**Status**: ✅ complete

### Traceability Verification

| Chain | Status | Notes |
|-------|--------|-------|
| SYSP_US_PM → SYSP_REQ_PM_SOUL → SYSP_SPEC_PM_SOUL | ✅ | Content guardrail at all three levels |
| SYSP_US_PM → SYSP_REQ_PM_DUTIES → SYSP_SPEC_PM_DUTIES | ✅ | CR content restriction at all three levels |
| SYSP_US_PM → SYSP_REQ_PM_WORKFLOW → SYSP_SPEC_PM_WORKFLOW | ✅ | CR self-check step at all three levels |
| SYSP_US_CM → SYSP_REQ_CM_SOUL → SYSP_SPEC_CM_SOUL | ✅ | Intent-gateway at all three levels |
| SYSP_US_CM → SYSP_REQ_CM_DUTIES → SYSP_SPEC_CM_DUTIES | ✅ | Intent clarification + Change Document at all three levels |
| SYSP_US_CM → SYSP_REQ_CM_WORKFLOW → SYSP_SPEC_CM_WORKFLOW | ✅ | Intent Gate step + Change Document step at all three levels |
| SYSP_US_DESIGN → SYSP_REQ_DESIGN_FRONTMATTER → SYSP_SPEC_DESIGN_FRONTMATTER | ✅ | vscode/askQuestions at all three levels |
| SYSP_SPEC_DOC_WORKFLOWS → SYSP_SPEC_CM_WORKFLOW + SYSP_SPEC_PM_WORKFLOW | ✅ | Aggregator spec updated, existing links intact |

**Status changes:** All modified draft elements set to approved (15 elements across L0/L1/L2).

---

## Sign-off

- [x] Design approved by user
- [ ] Implementation complete
- [ ] Verify passed
- [ ] Merged to development
