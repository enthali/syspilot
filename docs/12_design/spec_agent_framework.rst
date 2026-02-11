Agent Framework Design
======================

Shared architectural patterns across all syspilot agents.

**Document Version**: 0.2
**Last Updated**: 2026-02-06


Agent Workflow
--------------

.. spec:: Four-Agent Workflow
   :id: SPEC_AGENT_WORKFLOW
   :status: implemented
   :links: REQ_WF_CHANGE_SEQUENCE, REQ_CHG_ANALYSIS_AGENT, REQ_CHG_IMPL_AGENT, REQ_CHG_VERIFY_AGENT, REQ_DX_MEMORY_AGENT, REQ_CHG_WORKFLOW_STEPS
   :tags: architecture, agents

   **Design:**
   syspilot implements a four-agent workflow for structured change management.

   **Agent Responsibilities:**

   1. **change agent**: Analyze request + current implementation → Change Document + US/REQ/SPEC updates
   2. **implement agent**: Read Change Document → Code + Scripts + Tests (no spec changes)
   3. **verify agent**: Implementation → Verification Report
   4. **memory agent**: Project → Updated copilot-instructions.md

   **Workflow:**

   ::

      User Request
           │
           ▼
      ┌─────────────┐
      │   change    │ ──→ Change Document + US/REQ/SPEC RST updates
      └─────────────┘
           │
           ▼ (approved)
      ┌─────────────┐
      │  implement  │ ──→ Code + Scripts + Tests (reads SPECs from Change Doc)
      └─────────────┘
           │
           ▼
      ┌─────────────┐
      │   verify    │ ──→ Verification Report
      └─────────────┘
           │
           ▼ (passed)
      ┌─────────────┐
      │   memory    │ ──→ Updated copilot-instructions.md
      └─────────────┘
           │
           ▼
      ┌──────────┬──────────┐
      │  change  │ release  │  (user decides)
      └──────────┴──────────┘

   **Files:**

   * ``.github/agents/syspilot.change.agent.md``
   * ``.github/agents/syspilot.implement.agent.md``
   * ``.github/agents/syspilot.verify.agent.md``
   * ``.github/agents/syspilot.memory.agent.md``

   **VS Code Handoffs:**

   Each agent file includes YAML frontmatter with ``handoffs:`` that enable
   VS Code to suggest the next agent in the workflow.

   **Main Chain:**

   ::

      change → implement → verify → memory
          ↑                            │
          ├────────────────────────────┘ (next change)
          │
          └── or ──→ release (bundle changes)

   **Analysis Agents (bidirectional):**

   ::

      mece ↔ trace
        │       │
        └───────┴──→ change (to fix issues)

   **Memory Agent:**

   Invoked after verify. Hands off to change (for next change) or
   release (to bundle changes into a versioned release).

   **Handoff Format:**

   ::

      ---
      description: Short agent purpose for UI display
      handoffs:
        - label: Display name
          agent: syspilot.targetagent
          prompt: Default prompt text
      ---

   **Initial Prompt Recommendations:**

   To show syspilot agents as suggestions when opening a new chat,
   configure VS Code workspace settings:

   **File:** ``.vscode/settings.json``

   ::

      {
        "chat.promptFilesRecommendations": {
          "syspilot.change": true,
          "syspilot.implement": true,
          "syspilot.verify": true,
          "syspilot.mece": true,
          "syspilot.trace": true,
          "syspilot.memory": true
        }
      }

   This ensures users see syspilot workflow options immediately.


Prompt Architecture
-------------------

.. spec:: Prompt-Agent Separation
   :id: SPEC_AGENT_PROMPT_SEPARATION
   :status: implemented
   :links: REQ_CORE_SPHINX_NEEDS
   :tags: architecture, prompts

   **Design:**
   Strict separation between prompt files and agent files.

   **Prompt Files** (``.github/prompts/*.prompt.md``):
   
   - Minimal frontmatter only
   - Reference the agent, nothing else
   - User-facing entry point

   **Format:**

   ::

      ---
      agent: syspilot.change
      ---

   **Agent Files** (``.github/agents/*.agent.md``):
   
   - Full instructions
   - Workflow descriptions
   - Examples
   - All the logic

   **Rationale:**

   - Prompts are stable entry points
   - Agents can be updated without changing invocation
   - Separation of concerns: WHAT to invoke vs HOW to execute
   - Consistent with speckit design pattern


Agent Interaction
-----------------

.. spec:: Agent Interaction via Selection Menus
   :id: SPEC_AGENT_INTERACTION
   :status: implemented
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

   * **Skill file:** ``.github/skills/syspilot.ask-questions.skill.md``
     Contains the full pattern description, format reference, rules,
     and examples.

   * **Activation:** A single reference in ``.github/copilot-instructions.md``:

     ::

        When presenting choices to the user during agent sessions,
        read and follow .github/skills/syspilot.ask-questions.skill.md.

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


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_AGENT')

.. needflow:: SPEC_AGENT_WORKFLOW
