# Change Document: agent-vocabulary-migration

**Status**: review
**Branch**: feature/agent-vocabulary-migration
**Created**: 2026-05-16
**Author**: Change Manager

---

## Summary

Phase 3 of the Skill Architecture rollout: All syspilot agent documents shall
use the finalized verb vocabulary (INVOKE, DELEGATE, REPLY) instead of
referencing concrete tools or mechanisms directly in their workflow descriptions.
Manager agents (PM, CM, QM) use INVOKE for engineer subagent calls and DELEGATE
for cross-session handoffs. Engineer agents add REPLY as their terminal workflow
step. No agent document prescribes a specific runtime tool (e.g. `runSubagent()`,
`jarvis_sendToSession`) in workflow steps — tool mapping is left to the installed
orchestration skill.

---

## CR Acceptance Criteria (from PM)

1. Every manager agent (PM, CM, QM) uses INVOKE for subagent calls and DELEGATE for
   cross-session handoffs in its workflow descriptions — no concrete tool names appear
   in workflow steps.
2. The distinction between INVOKE (same session, sync) and DELEGATE (cross-session
   handoff) is applied consistently: Manager-to-Manager = DELEGATE; Manager-to-Engineer
   subagent = INVOKE.
3. REPLY appears as the terminal workflow step in every agent that is called by
   another agent and must return a result.
4. No agent document prescribes a specific runtime tool (e.g. `runSubagent()`,
   `jarvis_sendToSession`) in its workflow steps — tool mapping is left to the
   installed orchestration skill.
5. The conventions document reflects Phase 3 as complete.
6. Traceability is complete and QM-verified.

**Sensitive token:** `agent/runSubagent` in frontmatter `agents:` or `tools:` fields
is an agent path declaration — NOT a tool reference to be refactored. Only workflow
step prose is in scope.

---

## Scope: Agent Files

Product agents in `syspilot/agents/` (instance `.github/agents/` updated by Setup post-release).

| Agent File | Role | Changes Needed |
|---|---|---|
| `syspilot.cm.agent.md` | Manager | Remove "via Jarvis message queue" / "via Jarvis" from steps 9+11; use DELEGATE |
| `syspilot.pm.agent.md` | Manager | Step 7: DELEGATE explicit; QM-Findings step 4: DELEGATE |
| `syspilot.qm.agent.md` | Manager | Step 3: INVOKE explicit; Step 6: DELEGATE |
| `syspilot.design.agent.md` | Engineer | MECE advisory steps → INVOKE; add REPLY terminal step |
| `syspilot.uat.agent.md` | Engineer | Step 5: rename to REPLY |
| `syspilot.implement.agent.md` | Engineer | Add REPLY terminal step |
| `syspilot.mece.agent.md` | Engineer | Step 4: rename Report → REPLY |
| `syspilot.trace.agent.md` | Engineer | Step 5: rename Report → REPLY |
| `syspilot.docu.agent.md` | Engineer | Add REPLY terminal step |
| `syspilot.verify.agent.md` | Engineer | Add REPLY after step 7 |
| `syspilot.release.agent.md` | Engineer | Add REPLY terminal step |
| `syspilot.setup.agent.md` | Bootloader | Step 4: INVOKE; remove `runSubagent()` tool reference |
| `syspilot.installer.agent.md` | Engineer | Add REPLY terminal step |

---

## Impact Analysis

**Queried elements:**
- `SYSP_US_SKILL_ORCHESTRATION` (L0) — covers 3-verb model, ACs imply agents use verbs
- `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` (L1) — defines verbs in skill, not in agent docs
- `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL` (L2) — defines skill implementation

**Gap identified:** No existing spec says "agent workflow step prose SHALL use
INVOKE/DELEGATE/REPLY". New specs needed at L1 and L2.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_SKILL_ORCHESTRATION` | Consistent Agent Orchestration | unchanged | ACs 1-3 presuppose (not mandate) verb usage in agent docs; new REQ closes the mandating gap |

### New User Stories

None. `SYSP_US_SKILL_ORCHESTRATION` ACs 1-3 use language like "Given any agent
document that says INVOKE..." — they presuppose the vocabulary is already used,
but do not mandate it. `SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB` closes this
mandating gap at L1. This is a genuine new requirement, not a restatement.

### Decisions

- No L0 changes: `SYSP_US_SKILL_ORCHESTRATION` ACs 1-3 presuppose verb usage
  ("Given any agent document that says INVOKE...") but do not mandate it.
  The mandating happens at L1 via `SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] No gaps at L0 — existing US covers vocabulary usage

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` | Orchestration Verb Model | unchanged | Defines verb semantics in skill; not about agent doc format |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| `SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB` | Agent Workflow Vocabulary | `SYSP_US_SKILL_ORCHESTRATION` | mandatory |

**`SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`** — Agent workflow step descriptions
SHALL use INVOKE/DELEGATE/REPLY vocabulary:
- Manager agents use INVOKE for engineer subagent calls (same-session)
- Manager agents use DELEGATE for cross-session handoffs (Manager-to-Manager)
- Every callee agent (called by another agent) SHALL include REPLY as terminal step
- No agent workflow step SHALL prescribe a specific runtime tool name

### Decisions

- AC-5 in `SYSP_REQ_SKILL_ORCHESTRATION_REPORTING` says "Reports are sent via
  `jarvis_sendToSession`" — this is a tool reference in a REQ, not in an agent doc.
  Out of scope for this CR (AC-4 scopes to "agent document", not specs). Defer to
  a separate cleanup CR.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies — new REQ is agent-doc format, existing INVOKE REQ is skill semantics
- [x] New REQ links to existing US

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL` | Verb Model (Sync Variant) | unchanged | Covers skill mapping, not agent doc format |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| `SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB` | Agent Workflow Vocabulary Rules | `SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB; SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL` |

**`SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB`** — Defines:
- Routing table: Manager-to-Engineer → INVOKE; Manager-to-Manager → DELEGATE
- REPLY: terminal step in all callee agents
- Prohibited patterns: `runSubagent()`, `jarvis_sendToSession`, or similar in step prose
- INVOKE and DELEGATE in agent workflow prose refer to the installed orchestration skill

### Decisions

- `SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB` links to `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL`
  because the vocabulary is defined there; the new SPEC governs how agents USE it in docs

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] New SPEC links to new REQ and existing VERB_MODEL SPEC

---

## Final Consistency Check

**Status**: ⏳ not started

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| `SYSP_US_SKILL_ORCHESTRATION` | `SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB` (new) | `SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB` (new) | ✅ |

### Artefakt-Removal-Check

No artefacts removed in this CR.

### Issues Found

None yet.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [ ] QM-verified (in progress)
