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
   **I want** a defined orchestration pattern with generic verbs,
   **so that** engineer invocation is consistent, traceable, and
   independent of the underlying orchestration mechanism.

   **Context:**

   Manager agents (CM, QM, PM) orchestrate engineer agents as subagents.
   Without a defined pattern, each manager would invent its own invocation
   style, making the system inconsistent, hard to debug, and difficult to
   extend with new engineers.

   The orchestration pattern defines three generic verbs:

   * **INVOKE** — synchronous call to an engineer, block until result
   * **DELEGATE** — hand off work to an engineer (async variants add a
     Reply Contract; in the sync variant this collapses to INVOKE)
   * **REPLY** — engineer returns its result to the caller

   These verbs are tool-agnostic. The concrete mapping (e.g. INVOKE →
   ``runSubagent()``) is provided by the installed orchestration skill.

   The pattern also defines:

   * What the ``agents:`` frontmatter field means
   * How engineers report results back to managers

   **Acceptance Criteria:**

   1. Given any agent document that says "INVOKE", When interpreted by a manager, Then the installed orchestration skill maps it to a concrete call mechanism
   2. Given any agent document that says "DELEGATE", When interpreted by a manager, Then the installed orchestration skill maps it to the appropriate delegation mechanism
   3. Given an engineer that completes a task, When it executes REPLY, Then the installed orchestration skill delivers the result to the caller
   4. Given an agent's ``agents:`` frontmatter, When the manager operates, Then it can only invoke agents listed there
   5. Given an engineer completes a task, When reporting back, Then it uses a structured result format
   6. Given two engineers, When working on the same workflow, Then they are decoupled and unaware of each other
