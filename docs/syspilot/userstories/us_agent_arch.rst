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
   is defined through Soul (identity), Duties (accountability), and Workflow
   (execution sequence),
   **so that** agents are predictable, customizable, and composable across projects.

   **Context:**

   The agent architecture distinguishes two tiers:

   * **Managers** (user-invocable) — orchestrate workflows, delegate to engineers
   * **Engineers** (subagents) — execute specialized tasks, decoupled from each other

   Agents can be specialized by **Skills** — exchangeable implementations that
   bind generic Agent verbs to concrete tools. Swapping a Skill changes the tool
   without changing the Agent's workflow.

   Every agent — manager or engineer — shares the same three behavioural
   sections:

   * **Soul** — immutable identity, character, and perspective
   * **Duties** — customer-customizable list of responsibilities and outcomes
     (unordered; *what the agent is accountable for*)
   * **Workflow** — customer-customizable ordered execution steps
     (*how the agent executes its work*)

   A single behavioural item belongs in exactly one of Duties or Workflow,
   never both. In addition to these three behavioural sections, every agent
   has a YAML Frontmatter block, and every Manager additionally has a Prompt
   File — see the dedicated requirements for those.

   **Acceptance Criteria:**

   1. Given any agent, When I read its definition, Then it contains the three behavioural sections Soul, Duties, and Workflow (additional structural elements such as Frontmatter and Prompt File are governed by their own requirements)
   2. Given I customize an agent, When I modify Duties or Workflow, Then the Soul remains unchanged
   3. Given a Manager agent, When invoked by a user, Then it orchestrates Engineers without exposing them
   4. Given an Engineer agent, When invoked as subagent, Then it works independently without knowledge of other Engineers
   5. Given any behavioural item describing the agent's work, When placed in the agent definition, Then it appears in exactly one of Duties or Workflow — never both
