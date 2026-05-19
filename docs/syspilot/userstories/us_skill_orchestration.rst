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

   The orchestration pattern defines four generic verbs:

   * **INVOKE** — synchronous call to an engineer; caller blocks until
     the callee returns a structured result
   * **SEND** — deliver a message to another session (cross-session,
     non-blocking communication)
   * **RECEIVE** — check inbox for pending messages; used by agents
     waiting for async work assignments
   * **RESPOND** — deliver result to caller; the skill auto-detects
     invocation mode: if a pending message triggered this run (detected
     via RECEIVE), RESPOND routes the result back to the sender via SEND;
     otherwise the result is returned directly

   These verbs are tool-agnostic. The concrete mapping (e.g. INVOKE →
   ``runSubagent()``) is provided by the installed orchestration skill
   variant.

   The pattern also defines:

   * What the ``agents:`` frontmatter field means
   * How engineers report results back to managers

   **Acceptance Criteria:**

   1. Given any agent document that says "INVOKE", When interpreted by a manager, Then the installed orchestration skill maps it to a concrete synchronous call mechanism
   2. Given any agent document that says "SEND", When interpreted by a manager, Then the installed orchestration skill maps it to a cross-session message delivery mechanism
   3. Given an agent that needs to check for incoming work, When it executes RECEIVE, Then the installed orchestration skill checks the inbox for pending messages
   4. Given an engineer that completes a task, When it executes RESPOND, Then the installed orchestration skill auto-detects invocation mode and delivers the result appropriately
   5. Given an agent's ``agents:`` frontmatter, When the manager operates, Then it can only invoke agents listed there
   6. Given an engineer completes a task, When reporting back, Then it uses a structured result format
   7. Given two engineers, When working on the same workflow, Then they are decoupled and unaware of each other
