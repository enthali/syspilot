# Change Document: skill-frontmatter-migration

**Status**: review
**Branch**: feature/skill-frontmatter-migration
**Created**: 2026-05-16
**Author**: CM

---

## Summary

Bring all four shipped syspilot skills into conformance with the Skill Architecture
established in v0.5.4. Group-member skills (`orchestration`, `impact-python`) gain
a `group` field and DEFINITIONS Dictionary reference. The orchestration skill is
rewritten to use the finalized three-verb model (INVOKE / DELEGATE / REPLY) instead
of hard-coding `runSubagent()`. Standalone skills (`ask-questions`, `branching`)
are verified as already conformant and require no structural changes.

---

## Intent Gate Decision

PM-AC-1 states "every shipped skill carries a `group` field." However,
`SYSP_US_SKILL_ARCH` AC-4 and the conventions document state that `group` is
**optional** — standalone skills with no exchangeable variants omit it.

**Resolved:** Only `orchestration` and `impact-python` receive `group` fields
(they have planned/released variants). `ask-questions` and `branching` remain
standalone — their current frontmatter (`name` + `description`, no `group`) is
already conformant with the spec. PM ACs 1-3 apply only to group-member skills.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| `SYSP_US_SKILL_ORCHESTRATION` | Consistent Agent Orchestration | modified | Update to reflect INVOKE/DELEGATE/REPLY verb model |

### New User Stories

None.

### Decisions

- **D-1:** `ask-questions` and `branching` skills are standalone — no group field needed, no US changes
- **D-2:** `impact-python` skill gets `group: impact` (future variant: `impact-ubcode`)
- **D-3:** `orchestration` skill gets `group: orchestration` and INVOKE/DELEGATE/REPLY verb model
- **D-4:** `SYSP_US_SKILL_ORCHESTRATION` AC-1 must be broadened to cover DELEGATE and REPLY, not just INVOKE

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
| `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` | `SYSP_US_SKILL_ORCHESTRATION` | modified | title + content expanded to 3-verb model (INVOKE/DELEGATE/REPLY) |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| `SYSP_REQ_SKILL_ORCHESTRATION_GROUP` | Orchestration Skill Group Membership | `SYSP_US_SKILL_ORCHESTRATION` | mandatory |
| `SYSP_REQ_SKILL_IMPACT_GROUP` | Impact Skill Group Membership | `SYSP_US_SKILL_IMPACT` | mandatory |

### Decisions

- **D-5:** `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` title and content must change; old "invoke = runSubagent" is now only one case of INVOKE
- **D-6:** New REQ covers INVOKE, DELEGATE, and REPLY semantics and their sync-variant implementation

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
| `SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN` | `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` | modified | Updated to 3-verb pattern; cross-link to VERB_MODEL added |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL` | Orchestration Verb Model Implementation (Sync Variant) | `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE`, `SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN` |
| `SYSP_SPEC_SKILL_ORCHESTRATION_GROUP` | Orchestration Skill Group Membership | `SYSP_REQ_SKILL_ORCHESTRATION_GROUP` |
| `SYSP_SPEC_SKILL_IMPACT_GROUP` | Impact Skill Group Membership | `SYSP_REQ_SKILL_IMPACT_GROUP` |

### Decisions

- **D-7:** SPEC must include verb-mapping table (INVOKE→runSubagent, DELEGATE→collapses to INVOKE in sync, REPLY→Prompt-Reminder)

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Implementation Scope

### Skill Files (product: `syspilot/skills/`)

| Skill | Change |
|-------|--------|
| `syspilot.orchestration` | Add `group: orchestration`; rewrite body with INVOKE/DELEGATE/REPLY model |
| `syspilot.impact-python` | Add `group: impact` |
| `syspilot.ask-questions` | No change — already conformant (standalone) |
| `syspilot.branching` | No change — already conformant (standalone) |

### Documentation

| File | Change |
|------|--------|
| `docs/syspilot/conventions.md` | Update implementation status — Phase 2 complete |

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| `SYSP_US_SKILL_ORCHESTRATION` | `SYSP_REQ_SKILL_ORCHESTRATION_INVOKE` (mod), `SYSP_REQ_SKILL_ORCHESTRATION_GROUP` (new) | `SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN` (mod), `SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL` (new), `SYSP_SPEC_SKILL_ORCHESTRATION_GROUP` (new) | ✅ |
| `SYSP_US_SKILL_IMPACT` | `SYSP_REQ_SKILL_IMPACT_GROUP` (new) | `SYSP_SPEC_SKILL_IMPACT_GROUP` (new) | ✅ |

### Artefakt-Removal-Check

No artefacts removed in this CR.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## Appendix: Impact Analysis Results

```json
SYSP_US_SKILL_ARCH (direction: in, depth 2)
  → SYSP_REQ_SKILL_ARCH_FRONTMATTER → SYSP_SPEC_SKILL_ARCH_FRONTMATTER
  → SYSP_REQ_SKILL_ARCH_INSTRUCTIONS → SYSP_SPEC_SKILL_ARCH_INSTRUCTIONS
  → SYSP_REQ_SKILL_ARCH_RULES → SYSP_SPEC_SKILL_ARCH_RULES
  → SYSP_REQ_SKILL_ARCH_SUBSTITUTABILITY → SYSP_SPEC_SKILL_ARCH_SUBSTITUTABILITY
  → SYSP_REQ_SKILL_DEFINITIONS → SYSP_SPEC_SKILL_DEFINITIONS
  → SYSP_US_SKILL_ORCHESTRATION → SYSP_REQ_SKILL_ORCHESTRATION_INVOKE
                                  SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER
                                  SYSP_REQ_SKILL_ORCHESTRATION_REPORTING
  → SYSP_US_SKILL_IMPACT → SYSP_REQ_SKILL_IMPACT_QUERY
                            SYSP_REQ_SKILL_IMPACT_EXCHANGE
  → SYSP_US_SKILL_ASK_QUESTIONS → SYSP_REQ_SKILL_ASK_QUESTIONS_USAGE
                                   SYSP_REQ_SKILL_ASK_QUESTIONS_FORMAT
  → SYSP_US_SKILL_BRANCHING → SYSP_REQ_SKILL_BRANCHING_CHAINED
                               SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION
                               SYSP_REQ_SKILL_BRANCHING_NAMING

SYSP_REQ_SKILL_ORCHESTRATION_INVOKE (direction: in, depth 1)
  → SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN

SYSP_REQ_SKILL_IMPACT_EXCHANGE (direction: in, depth 1)
  → SYSP_SPEC_SKILL_IMPACT_EXCHANGE
```
