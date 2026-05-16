Skill: Orchestration Requirements
=================================

Requirements for agent orchestration patterns.


.. req:: Orchestration Verb Model
   :id: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   The orchestration skill SHALL define three generic verbs for
   inter-agent communication:

   * **INVOKE <agent>** — Synchronous call. The caller blocks until the
     callee returns a result. Whenever an agent document says "invoke",
     "dispatch", or "run" another agent, this SHALL mean INVOKE.
   * **DELEGATE <task> to <agent>** — Hand off work. In async variants
     this is non-blocking with a Reply Contract. In the default sync
     variant, DELEGATE collapses to INVOKE.
   * **REPLY** — Return result to the caller. The callee executes REPLY
     at the end of its workflow to deliver findings back. The concrete
     mechanism is resolved by the installed orchestration skill variant.

   These verbs are **tool-agnostic**. The concrete mapping (e.g.
   INVOKE → ``runSubagent()``) is provided by the installed skill variant,
   not defined here.

   **Rationale:**
   A fixed set of generic verbs decouples agent workflows from the
   orchestration mechanism. Agents use INVOKE/DELEGATE/REPLY in their
   documents; the installed skill translates these to runtime calls.
   This enables exchangeability — a different orchestration backend can
   be installed without rewriting agent documents.

   **Acceptance Criteria:**

   * AC-1: "invoke", "dispatch", or "run" in any agent document means INVOKE
   * AC-2: DELEGATE is defined as a work hand-off verb; in sync variant it collapses to INVOKE
   * AC-3: REPLY is defined as the callee's mechanism to return results
   * AC-4: The verb definitions are tool-agnostic — no runtime API is prescribed at this level
   * AC-5: No alternative invocation verbs exist beyond INVOKE, DELEGATE, REPLY


.. req:: Agents Frontmatter Semantics
   :id: SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   The ``agents:`` list in YAML frontmatter SHALL declare which agents this
   agent may call as subagents. Only agents listed in the ``agents:`` field
   can be INVOKED by this agent.

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


.. req:: Orchestration Skill Group Membership
   :id: SYSP_REQ_SKILL_ORCHESTRATION_GROUP
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   The orchestration skill SHALL declare ``group: orchestration`` in its
   YAML frontmatter. Only one skill with ``group: orchestration`` may be
   installed at a time (mutual exclusion). The sync variant
   ``syspilot.orchestration`` is the default installed variant.

   **Rationale:**
   Group membership enables the Skill Architecture's substitutability
   mechanism. By declaring a group, the orchestration skill advertises
   that it can be replaced by another skill in the same group (e.g. an
   async variant) while agents continue to use the same verbs.

   **Acceptance Criteria:**

   * AC-1: The orchestration skill frontmatter contains ``group: orchestration``
   * AC-2: At most one skill with ``group: orchestration`` is installed at any time
   * AC-3: ``syspilot.orchestration`` (sync variant) is the default when no alternative is configured
   * AC-4: The orchestration group does not require DEFINITIONS entries — verbs map
     directly to installed tools, not to project-specific configuration
