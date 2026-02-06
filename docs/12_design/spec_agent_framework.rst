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

      change → implement → verify
          ↑                   │
          └───────────────────┘ (if issues found)

   **Analysis Agents (bidirectional):**

   ::

      mece ↔ trace
        │       │
        └───────┴──→ change (to fix issues)

   **Memory Agent:**

   Standalone - invoked after verify or on-demand. Has description but no handoffs.

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


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_AGENT')

.. needflow:: SPEC_AGENT_WORKFLOW
