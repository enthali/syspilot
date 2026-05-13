Skill: Orchestration
====================

Manager-to-engineer orchestration pattern.


.. story:: Consistent Agent Orchestration
   :id: SYSP_US_SKILL_ORCHESTRATION
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ARCH

   **As a** syspilot manager agent,
   **I want** a defined orchestration pattern,
   **so that** engineer invocation is consistent and traceable.

   **Context:**

   Manager agents (CM, QM, PM) orchestrate engineer agents as subagents.
   Without a defined pattern, each manager would invent its own invocation
   style, making the system inconsistent, hard to debug, and difficult to
   extend with new engineers.

   The orchestration pattern defines:

   * How managers invoke engineers (``runSubagent()``)
   * What the ``agents:`` frontmatter field means
   * How engineers report results back to managers

   **Acceptance Criteria:**

   1. Given any agent document that says "invoke", When interpreted by a manager, Then it means ``runSubagent()``
   2. Given an agent's ``agents:`` frontmatter, When the manager operates, Then it can only invoke agents listed there
   3. Given an engineer completes a task, When reporting back, Then it uses a structured result format
   4. Given two engineers, When working on the same workflow, Then they are decoupled and unaware of each other
