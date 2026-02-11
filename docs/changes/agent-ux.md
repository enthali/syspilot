# Change Document: agent-ux

**Status**: approved
**Branch**: feature/agent-ux
**Created**: 2026-02-06
**Author**: Change Agent

---

## Summary

Two UX improvements for agent interaction:

1. **Cross-cutting**: All agents should use VS Code's `ask_questions` tool (quick-pick selection menus) instead of plain-text choices when presenting options to the user. This provides a consistent, efficient interaction pattern.
2. **Change Agent specific**: Level transition communication should explicitly confirm that the current level has been saved to the Change Document before asking the user where to continue.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_CHG_ITERATIVE | Iterative Level-Based Change Analysis | no change | AC-2 covers "When I confirm" — the confirmation UX is a design detail |

### New User Stories

#### US_DX_AGENT_INTERACTION: Consistent Agent Interaction via Selection Menus

```rst
.. story:: Consistent Agent Interaction via Selection Menus
   :id: US_DX_AGENT_INTERACTION
   :status: draft
   :priority: high
   :tags: agent, ux, developer-experience

   **As a** developer,
   **I want to** have agents present choices using VS Code's native selection menus
   (quick-pick UI) instead of plain-text questions,
   **so that** I can respond efficiently with a single click and have a consistent
   interaction experience across all agents.

   **Acceptance Scenarios:**

   1. Given an agent needs my decision, When it presents choices, Then I see a VS Code selection menu (not plain text)
   2. Given I'm at a workflow transition, When the agent asks what to do next, Then I can click an option instead of typing
   3. Given any syspilot agent presents choices, When I compare interactions, Then all agents use the same selection mechanism
```

### Decisions

- D-1: Finding 2 (level transition clarity) is a design-level concern, not a US-level concern. Addressed via SPEC_CHG_LEVEL_PROCESSING step 6, not via US modification.
- D-2: US_DX_AGENT_INTERACTION placed in `us_developer_experience.rst`.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies — no existing US covers agent interaction style
- [x] Gaps identified and addressed — Finding 2 covered at design level

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_CHG_WORKFLOW_STEPS | US_WF_CHANGE | no change | Inter-agent handoffs (YAML), not intra-agent choices — complementary |
| REQ_CHG_CHANGE_DOC | US_CHG_ITERATIVE | no change | Finding 2 kept at design level per D-1 |

### New Requirements

#### REQ_DX_AGENT_SELECTION_MENUS: Agent Selection Menus for User Choices

```rst
.. req:: Agent Selection Menus for User Choices
   :id: REQ_DX_AGENT_SELECTION_MENUS
   :status: draft
   :priority: high
   :tags: agent, ux, developer-experience
   :links: US_DX_AGENT_INTERACTION

   **Description:**
   syspilot agents SHALL use VS Code's ``ask_questions`` tool (quick-pick
   selection menus) when presenting choices to the user during a session.

   **Rationale:**
   Free-text choices require users to type or copy responses, and the
   presentation varies between agents. Using the native selection menu
   provides a consistent, single-click interaction pattern across all agents.

   **Acceptance Criteria:**

   * AC-1: Agents SHALL use the ``ask_questions`` tool when presenting 2 or
     more options to the user
   * AC-2: Each option SHALL include a label and a brief description
   * AC-3: All syspilot agents SHALL follow the same interaction pattern for
     presenting choices
   * AC-4: Free-form input SHALL be enabled (``allowFreeformInput``) when the
     user may want to provide a custom response beyond the listed options
```

### Decisions

- D-3: Finding 2 remains at design level only (SPEC_CHG_LEVEL_PROCESSING step 6), no REQ-level AC added.
- D-4: REQ_DX_AGENT_SELECTION_MENUS placed in `req_developer_experience.rst`.
- D-5: Distinction: REQ_CHG_WORKFLOW_STEPS = inter-agent handoffs (YAML), REQ_DX_AGENT_SELECTION_MENUS = intra-agent choices (ask_questions).
- D-9: Added REQ_DX_AGENT_SKILL_FILES for consolidating reusable patterns into skill files.
- D-10: REQ_DX_AGENT_SKILL_FILES links to US_DX_AGENT_INTERACTION (AC-3 consistency goal).

### New Requirements (added in revision)

#### REQ_DX_AGENT_SKILL_FILES: Shared Skill Files for Agent Patterns

```rst
.. req:: Shared Skill Files for Agent Patterns
   :id: REQ_DX_AGENT_SKILL_FILES
   :status: draft
   :priority: high
   :tags: agent, ux, developer-experience, skills
   :links: US_DX_AGENT_INTERACTION

   **Description:**
   syspilot SHALL provide a mechanism for consolidating reusable interaction
   patterns into shared skill files that are available to all agents.

   **Rationale:**
   Without consolidation, reusable patterns (like how to present choices)
   must be duplicated across agent files. Skill files define the pattern
   once and make it available to all agents through a single reference.

   **Acceptance Criteria:**

   * AC-1: Reusable agent patterns SHALL be defined in dedicated skill files
   * AC-2: Skill files SHALL be accessible to all agents without duplication
   * AC-3: Adding a new skill SHALL require minimal configuration
     (single reference point)
```

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies — no overlap with REQ_CHG_WORKFLOW_STEPS (different mechanism, different scope)
- [x] All new REQs link to User Stories — REQ_DX_AGENT_SELECTION_MENUS → US_DX_AGENT_INTERACTION

---

## Level 2: Design

**Status**: ✅ completed (revised)

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_CHG_LEVEL_PROCESSING | REQ_CHG_ANALYSIS_AGENT | modified | Step 6: add save confirmation + ask_questions reference. Add link to REQ_DX_AGENT_SELECTION_MENUS. |
| SPEC_INST_SETUP_AGENT | REQ_INST_NEW_PROJECT | modified | Section 3: add skill files copy |
| SPEC_INST_FILE_OWNERSHIP | REQ_INST_CUSTOM_PRESERVE | modified | Add .github/skills/ to ownership categories |
| SPEC_INST_RELEASE_STRUCTURE | REQ_INST_GITHUB_RELEASES | modified | Add .github/skills/ to release archive |
| SPEC_INST_UPDATE_PROCESS | REQ_INST_VERSION_UPDATE | modified | Step 2e: add skills to merge |

### New Design Elements

#### SPEC_AGENT_INTERACTION: Agent Interaction via Selection Menus

```rst
.. spec:: Agent Interaction via Selection Menus
   :id: SPEC_AGENT_INTERACTION
   :status: draft
   :links: REQ_DX_AGENT_SELECTION_MENUS, REQ_DX_AGENT_SKILL_FILES
   :tags: architecture, agents, ux

   **Design:**
   All syspilot agents use the ``ask_questions`` tool for presenting choices
   to the user. This replaces free-text menus with VS Code's native
   quick-pick selection UI for a consistent, efficient interaction.

   **When to Use ``ask_questions``:**

   * Workflow transitions (level navigation, agent handoffs within session)
   * Decisions with 2–6 discrete options
   * Confirmations where alternatives exist (approve / revise / pause)

   **When NOT to Use:**

   * Free-form questions requiring typed answers (use normal conversation)
   * Single yes/no confirmations with no meaningful alternatives

   **Format Reference:**

   ::

      ask_questions({
        questions: [{
          header: "≤12 chars",        // Quick-pick title, unique ID
          question: "Full context",    // Explains what is being decided
          options: [
            { label: "Option A", description: "Brief detail" },
            { label: "Option B", description: "Brief detail", recommended: true }
          ],
          allowFreeformInput: false    // true when custom response is expected
        }]
      })

   **Rules:**

   * ``recommended`` marks the agent's suggested default — user sees it pre-selected
   * ``allowFreeformInput: true`` when the user's custom input would be valuable
   * Max 4 questions per call, 2–6 options each
   * Batch related questions into a single call

   **Implementation via Skill File:**

   The interaction pattern is consolidated in a skill file instead of
   being duplicated across agent files:

   * **Skill file:** ``.github/skills/ask-questions.skill.md``
     Contains the full pattern description, format reference, rules,
     and examples.

   * **Activation:** A single reference in ``.github/copilot-instructions.md``:

     ::

        When presenting choices to the user during agent sessions,
        read and follow .github/skills/ask-questions.skill.md.

   * **Effect:** All agents (change, implement, verify, memory, mece,
     trace, setup) automatically pick up the skill without needing
     individual instructions in each agent file.

   **Example — Level Transition (Change Agent):**

   ::

      ask_questions({
        questions: [{
          header: "Continue?",
          question: "Level 1 is saved to the Change Document. Where do you want to continue?",
          options: [
            { label: "Proceed to Level 2 (Design)", description: "Analyze design specs", recommended: true },
            { label: "Revise Level 1", description: "Go back and revise requirements" },
            { label: "Pause here", description: "Save progress and continue later" }
          ]
        }]
      })
```

### Modified Design Elements

#### SPEC_CHG_LEVEL_PROCESSING — Step 6

**Before:**
```
6. **Ask Navigation** — "Proceed to Level N+1 / Revise Level N-1 / Pause?"
```

**After:**
```
6. **Ask Navigation** — Confirm that the current level is saved to the
   Change Document, then present navigation using ``ask_questions``:
   "Level N is saved to the Change Document. Where do you want to continue?"
   Options: Proceed to Level N+1 / Revise Level N-1 / Pause
   (see SPEC_AGENT_INTERACTION for format)
```

Also: add `REQ_DX_AGENT_SELECTION_MENUS` to `:links:`.

#### SPEC_INST_SETUP_AGENT — Section 3

**Before:**
```
* Copy agents: ``$syspilotRoot/.github/agents/*.agent.md`` → ``.github/agents/``
* Copy prompts: ``$syspilotRoot/.github/prompts/*.prompt.md`` → ``.github/prompts/``
* Apply intelligent merge (SPEC_INST_FILE_OWNERSHIP)
```

**After:**
```
* Copy agents: ``$syspilotRoot/.github/agents/*.agent.md`` → ``.github/agents/``
* Copy prompts: ``$syspilotRoot/.github/prompts/*.prompt.md`` → ``.github/prompts/``
* Copy skills: ``$syspilotRoot/.github/skills/*.skill.md`` → ``.github/skills/``
* Apply intelligent merge (SPEC_INST_FILE_OWNERSHIP)
```

#### SPEC_INST_FILE_OWNERSHIP — Syspilot Core

**Add to "Syspilot Core (with intelligent merge)":**
```
* ``.github/skills/syspilot.*.skill.md`` - merge if modified
```

#### SPEC_INST_RELEASE_STRUCTURE — Archive Layout

**Add `.github/skills/` to the directory structure:**
```
├── .github/
│   ├── agents/       # Agent definitions (*.agent.md)
│   ├── prompts/      # Prompt files (*.prompt.md)
│   ├── skills/       # Skill files (*.skill.md)
│   └── copilot-instructions.md
```

#### SPEC_INST_UPDATE_PROCESS — Step 2e

**Before:**
```
e. **Merge**: Copy agents/prompts with intelligent merge (see SPEC_INST_FILE_OWNERSHIP)
```

**After:**
```
e. **Merge**: Copy agents/prompts/skills with intelligent merge (see SPEC_INST_FILE_OWNERSHIP)
```

### Decisions

- D-6: SPEC_AGENT_INTERACTION placed in `spec_agent_framework.rst` (shared patterns).
- D-7: SPEC_CHG_LEVEL_PROCESSING step 6 explicitly confirms save status before navigation (Finding 2).
- D-8: SPEC_CHG_LEVEL_PROCESSING gets additional link to REQ_DX_AGENT_SELECTION_MENUS.
- D-11: SPEC_AGENT_INTERACTION links to both REQ_DX_AGENT_SELECTION_MENUS and REQ_DX_AGENT_SKILL_FILES.
- D-12: Skill file at `.github/skills/ask-questions.skill.md`, activated via one-liner in `copilot-instructions.md`.
- D-13: Setup agent copies skill files alongside agents/prompts (Section 3, Update Step 2e).
- D-14: Skill files added to file ownership (syspilot core, intelligent merge) and release structure.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements — SPEC_AGENT_INTERACTION → REQ_DX_AGENT_SELECTION_MENUS, REQ_DX_AGENT_SKILL_FILES

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_DX_AGENT_INTERACTION (new) | REQ_DX_AGENT_SELECTION_MENUS (new) | SPEC_AGENT_INTERACTION (new) | ✅ |
| US_DX_AGENT_INTERACTION (new) | REQ_DX_AGENT_SKILL_FILES (new) | SPEC_AGENT_INTERACTION (new) | ✅ |
| — | — | SPEC_CHG_LEVEL_PROCESSING (modified) | ✅ |
| — | — | SPEC_INST_SETUP_AGENT (modified) | ✅ |
| — | — | SPEC_INST_FILE_OWNERSHIP (modified) | ✅ |
| — | — | SPEC_INST_RELEASE_STRUCTURE (modified) | ✅ |
| — | — | SPEC_INST_UPDATE_PROCESS (modified) | ✅ |

### Sign-off

- [x] All levels completed (no DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified — no orphaned elements
- [x] Ready for implementation

---

## Post-Implementation: Memory Agent Compactness

**Status**: ✅ completed

During the memory agent step, copilot-instructions.md was trimmed from 325 → 177 lines
by removing sections that agents can discover from existing files (directive formats,
status lists, dependency lists, key files table, installation/release workflow details,
element counts, per-file directory listings).

To enforce this compactness going forward:

### Modified Files

- **syspilot.memory.agent.md**: Added core principle ("if agents can discover it, don't document it"), explicit exclusion list, size target (~150–180 lines)
- **SPEC_MEM_UPDATE_PROCESS**: 4→3 steps, added discoverability principle
- **SPEC_MEM_CONTENT_CATEGORIES**: Replaced 6 generic categories with include/exclude based on discoverability
- **SPEC_MEM_INSTRUCTIONS_STRUCTURE**: Replaced generic template with syspilot-specific 10-section list + size target
- **copilot-instructions.md**: Trimmed to target structure

### Decisions

- D-15: Compactness is a memory agent concern, not a separate change — applied directly during memory step.
- D-16: Skill file renamed to `syspilot.ask-questions.skill.md` to follow `syspilot.*` prefix convention (found during verify).

---

*Generated by syspilot Change Agent*
