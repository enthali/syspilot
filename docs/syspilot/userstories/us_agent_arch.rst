Agent Architecture
==================

Meta-level definition of the Soul/Duties/Workflow agent structure.


.. story:: Clean Agent Architecture
   :id: SYSP_US_AGENT_ARCH
   :status: draft
   :priority: mandatory
   :tags: agent-v2, meta, architecture

   **As a** syspilot user,
   **I want to** have a clean, consistent agent structure where every agent
   is defined through Soul (identity), Duties (tasks), and Workflow (process),
   **so that** agents are predictable, customizable, and composable across projects.

   **Context:**

   The agent architecture distinguishes two tiers:

   * **Managers** (user-invocable) — orchestrate workflows, delegate to engineers
   * **Engineers** (subagents) — execute specialized tasks, decoupled from each other

   Every agent — manager or engineer — follows the same three-section structure:

   * **Soul** — immutable identity, character, and perspective
   * **Duties** — customer-customizable task list
   * **Workflow** — customer-customizable process steps

   **Acceptance Criteria:**

   1. Given any agent, When I read its definition, Then it has exactly three sections: Soul, Duties, Workflow
   2. Given I customize an agent, When I modify Duties or Workflow, Then the Soul remains unchanged
   3. Given a Manager agent, When invoked by a user, Then it orchestrates Engineers without exposing them
   4. Given an Engineer agent, When invoked as subagent, Then it works independently without knowledge of other Engineers
