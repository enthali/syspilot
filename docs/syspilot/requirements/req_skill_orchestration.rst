Skill: Orchestration Requirements
=================================

Requirements for agent orchestration patterns.


.. req:: Invoke Means runSubagent
   :id: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   Whenever an agent document says "invoke", "dispatch", or "run" another
   agent, this SHALL mean calling ``runSubagent("syspilot.<name>", ...)``.

   **Rationale:**
   A single, unambiguous invocation mechanism prevents confusion between
   different ways to call agents. Every orchestration action maps to exactly
   one runtime operation.

   **Acceptance Criteria:**

   * AC-1: "invoke" in any agent document means ``runSubagent()``
   * AC-2: "dispatch" in any agent document means ``runSubagent()``
   * AC-3: "run" (in agent context) means ``runSubagent()``
   * AC-4: No alternative invocation mechanisms exist


.. req:: Agents Frontmatter Semantics
   :id: SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   The ``agents:`` list in YAML frontmatter SHALL declare which agents this
   agent may call as subagents. Only agents listed in the ``agents:`` field
   can be invoked via ``runSubagent()``.

   **Rationale:**
   Explicit declaration of callable subagents creates a static, auditable
   dependency graph. It prevents agents from invoking arbitrary other agents
   and makes the orchestration topology visible in the frontmatter.

   **Acceptance Criteria:**

   * AC-1: ``agents:`` is a list of strings in YAML frontmatter
   * AC-2: Each entry follows the format ``syspilot.<name>``
   * AC-3: Only listed agents can be invoked by this agent
   * AC-4: An empty ``agents: []`` means no subagent invocation permitted


.. req:: Orchestration Completion Reporting
   :id: SYSP_REQ_SKILL_ORCHESTRATION_REPORTING
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   When an orchestrator completes a delegated task, it SHALL report back to
   the sender with a structured result. The report SHALL include status,
   commit hashes (if applicable), summary, and issues found.

   **Rationale:**
   Structured reporting enables reliable handoff between workflow stages.
   The sender can verify completion and route follow-up work based on
   reported status and issues.

   **Acceptance Criteria:**

   * AC-1: Completion reports include status (completed / blocked / failed)
   * AC-2: Completion reports include commit hashes when commits were made
   * AC-3: Completion reports include a summary of what was done
   * AC-4: Completion reports include any issues or follow-up items found
   * AC-5: Reports are sent via ``jarvis_sendToSession``
