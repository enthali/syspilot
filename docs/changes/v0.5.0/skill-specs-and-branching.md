# Change Document: skill-specs-and-branching

**Status**: approved
**Branch**: feature/agent-architecture-v2
**Created**: 2026-04-12
**Author**: System Designer (@syspilot.change)

---

## Summary

Create RST specification files for three skills (ask-questions, orchestration, branching) across all three specification levels (User Stories, Requirements, Design). The ask-questions and orchestration skills already have SKILL.md implementations; the branching skill is new and codifies existing rules from workflows.md and copilot-instructions.md. All toctree indexes are updated to include the new files.

---

## Level 0: User Stories

**Status**: ✅ completed

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_SKILL_ASK_QUESTIONS | As a syspilot user, I want agents to present choices via selection menus so that workflow transitions are clear and consistent | mandatory |
| SYSP_US_SKILL_ORCHESTRATION | As a syspilot manager agent, I want a defined orchestration pattern so that engineer invocation is consistent and traceable | mandatory |
| SYSP_US_SKILL_BRANCHING | As a syspilot agent, I want clear branching rules so that I know where to commit and what branches to create | mandatory |

### Decisions

- Decision 1: All three skills are independent User Stories (not sub-stories of an existing US)
- Decision 2: Status set to `approved` per CR constraint (not `draft`)

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies (skill US are distinct from agent-architecture US)
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_SKILL_ASK_QUESTIONS_USAGE | Selection Menu Usage Criteria | SYSP_US_SKILL_ASK_QUESTIONS | mandatory |
| SYSP_REQ_SKILL_ASK_QUESTIONS_FORMAT | Selection Menu Format Constraints | SYSP_US_SKILL_ASK_QUESTIONS | mandatory |
| SYSP_REQ_SKILL_ORCHESTRATION_INVOKE | Invoke Means runSubagent | SYSP_US_SKILL_ORCHESTRATION | mandatory |
| SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER | Agents Frontmatter Semantics | SYSP_US_SKILL_ORCHESTRATION | mandatory |
| SYSP_REQ_SKILL_ORCHESTRATION_REPORTING | Orchestration Completion Reporting | SYSP_US_SKILL_ORCHESTRATION | mandatory |
| SYSP_REQ_SKILL_BRANCHING_CHAINED | Chained Feature Branches | SYSP_US_SKILL_BRANCHING | mandatory |
| SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION | Main Branch Protection | SYSP_US_SKILL_BRANCHING | mandatory |
| SYSP_REQ_SKILL_BRANCHING_NAMING | Branch Naming Conventions | SYSP_US_SKILL_BRANCHING | mandatory |

### Decisions

- Decision 1: ask-questions has 2 REQs (usage criteria + format constraints) matching the two key skill sections
- Decision 2: orchestration has 3 REQs (invoke semantics + frontmatter + reporting) matching the skill's three core topics
- Decision 3: branching has 3 REQs (strategy + protection + naming) covering the three rule categories

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_SKILL_ASK_QUESTIONS_API | ask_questions Tool API | SYSP_REQ_SKILL_ASK_QUESTIONS_USAGE, SYSP_REQ_SKILL_ASK_QUESTIONS_FORMAT |
| SYSP_SPEC_SKILL_ASK_QUESTIONS_RULES | ask_questions Usage Rules | SYSP_REQ_SKILL_ASK_QUESTIONS_USAGE, SYSP_REQ_SKILL_ASK_QUESTIONS_FORMAT |
| SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN | Communication Pattern | SYSP_REQ_SKILL_ORCHESTRATION_INVOKE, SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER |
| SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX | Orchestration Matrix | SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER |
| SYSP_SPEC_SKILL_ORCHESTRATION_REPORTING | Reporting Format | SYSP_REQ_SKILL_ORCHESTRATION_REPORTING |
| SYSP_SPEC_SKILL_BRANCHING_STRATEGY | Chained Branching Strategy | SYSP_REQ_SKILL_BRANCHING_CHAINED |
| SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS | Branch Permissions | SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION, SYSP_REQ_SKILL_BRANCHING_NAMING |
| SYSP_SPEC_SKILL_BRANCHING_COMMIT_CONVENTIONS | Commit Message Conventions | SYSP_REQ_SKILL_BRANCHING_NAMING |

### Decisions

- Decision 1: ask-questions design splits into API (structure) and Rules (behavioral) specs
- Decision 2: orchestration design covers pattern, matrix, and reporting as three independent specs
- Decision 3: branching design splits into strategy, permissions, and commit conventions

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_SKILL_ASK_QUESTIONS | SYSP_REQ_SKILL_ASK_QUESTIONS_USAGE, SYSP_REQ_SKILL_ASK_QUESTIONS_FORMAT | SYSP_SPEC_SKILL_ASK_QUESTIONS_API, SYSP_SPEC_SKILL_ASK_QUESTIONS_RULES | ✅ |
| SYSP_US_SKILL_ORCHESTRATION | SYSP_REQ_SKILL_ORCHESTRATION_INVOKE, SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER, SYSP_REQ_SKILL_ORCHESTRATION_REPORTING | SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN, SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX, SYSP_SPEC_SKILL_ORCHESTRATION_REPORTING | ✅ |
| SYSP_US_SKILL_BRANCHING | SYSP_REQ_SKILL_BRANCHING_CHAINED, SYSP_REQ_SKILL_BRANCHING_MAIN_PROTECTION, SYSP_REQ_SKILL_BRANCHING_NAMING | SYSP_SPEC_SKILL_BRANCHING_STRATEGY, SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS, SYSP_SPEC_SKILL_BRANCHING_COMMIT_CONVENTIONS | ✅ |

### Issues Found

(none)

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

*Generated by syspilot System Designer*
