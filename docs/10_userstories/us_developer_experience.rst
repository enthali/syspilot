Developer Experience User Stories
==================================

Stories covering developer experience, onboarding, and process ergonomics.

**Last Updated**: 2026-02-06


.. story:: Maintain Project Memory
   :id: US_DX_PROJECT_MEMORY
   :status: implemented
   :priority: high
   :tags: agent, memory

   **As a** developer,
   **I want to** have project knowledge automatically maintained,
   **so that** new Copilot sessions have full context.

   **Acceptance Scenarios:**

   1. Given I add a new pattern, When memory agent runs, Then copilot-instructions.md is updated
   2. Given structure changes, When agent analyzes, Then outdated info is removed
   3. Given a new session starts, When Copilot reads instructions, Then it has context


.. story:: Consistent Agent Interaction via Selection Menus
   :id: US_DX_AGENT_INTERACTION
   :status: implemented
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


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('US_DX')
