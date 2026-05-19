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
   The orchestration skill SHALL define four generic verbs for
   inter-agent communication:

   * **INVOKE <agent>** — Synchronous call. The caller blocks until the
     callee returns a result. Whenever an agent document says "invoke",
     "dispatch", or "run" another agent, this SHALL mean INVOKE.
   * **SEND <message> to <session>** — Deliver a message to another
     session. Non-blocking cross-session communication. Replaces the
     former DELEGATE verb for async handoff scenarios.
   * **RECEIVE** — Check inbox for pending messages. Used by agents
     waiting for async work assignments. Returns the next pending
     message or indicates no messages are available.
   * **RESPOND** — Return result to the caller. The callee executes
     RESPOND at the end of its workflow. The skill auto-detects
     invocation mode: if a pending message triggered this run (detected
     via RECEIVE), RESPOND routes the result back to the sender via
     SEND; otherwise the result is returned directly as structured output.

   These verbs are **tool-agnostic**. The concrete mapping (e.g.
   INVOKE → ``runSubagent()``) is provided by the installed skill variant,
   not defined here.

   **Rationale:**
   A fixed set of generic verbs decouples agent workflows from the
   orchestration mechanism. Agents use INVOKE/SEND/RECEIVE/RESPOND in their
   documents; the installed skill translates these to runtime calls.
   This enables exchangeability — a different orchestration backend can
   be installed without rewriting agent documents.

   **Acceptance Criteria:**

   * AC-1: Given any agent document that uses "invoke", "dispatch", or "run" for another agent, When interpreted at runtime, Then this SHALL mean INVOKE
   * AC-2: Given a caller that needs to deliver a message to another session, When it acts, Then it uses SEND — a non-blocking cross-session verb
   * AC-3: Given an agent that checks for pending work, When it starts, Then it uses RECEIVE to inspect its inbox
   * AC-4: Given a callee that completes a task, When it finishes, Then it executes RESPOND — which auto-detects invocation mode and delivers the result appropriately
   * AC-5: Given the verb definitions, When inspected, Then they are tool-agnostic — no runtime API is prescribed at this level
   * AC-6: Given the verb vocabulary, When inspected, Then no alternative invocation verbs exist beyond INVOKE, SEND, RECEIVE, RESPOND


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

   * AC-1: Given an agent that declares ``agents:`` in YAML frontmatter, When it operates, Then only the agents listed there can be invoked via INVOKE
   * AC-2: Given an ``agents:`` list entry, When inspected, Then each entry follows the format ``syspilot.<name>``
   * AC-3: Given an agent with an empty ``agents: []``, When it attempts to invoke a subagent, Then no subagent invocation is permitted
   * AC-4: Given the ``agents:`` frontmatter field, When used, Then it is a list of strings in YAML syntax
   * AC-5: Given any agent that attempts to call another agent via INVOKE, When the call is resolved, Then only agents listed in the calling agent's own ``agents:`` frontmatter field can be invoked — cross-agent references outside that list are structurally prevented


.. req:: Orchestration Completion Reporting
   :id: SYSP_REQ_SKILL_ORCHESTRATION_REPORTING
   :status: approved
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   When an agent completes a delegated task, it SHALL report back to
   the caller with a structured result. The report SHALL include status,
   commit hashes (if applicable), summary, and issues found.

   **Rationale:**
   Structured reporting enables reliable handoff between workflow stages.
   The caller can verify completion and route follow-up work based on
   reported status and issues.

   **Note:** AC-5 of this requirement still references ``jarvis_sendToSession`` directly.
   Cleanup to align with ``SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB`` is deferred
   per the CR-Defer list of ``agent-vocabulary-migration``.

   **Acceptance Criteria:**

   * AC-1: Given an agent that completes a delegated task, When it reports back, Then the report includes status (completed / blocked / failed)
   * AC-2: Given an agent that made commits, When it reports back, Then the report includes commit hashes with messages
   * AC-3: Given an agent that completes work, When it reports back, Then the report includes a summary of what was done
   * AC-4: Given an agent that encountered issues, When it reports back, Then the report includes any issues or follow-up items found
   * AC-5: Given cross-session reporting, When a result is delivered, Then it is sent via ``jarvis_sendToSession``


.. req:: Orchestration Skill Group Membership
   :id: SYSP_REQ_SKILL_ORCHESTRATION_GROUP
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   The orchestration skill SHALL declare ``group: orchestration`` in its
   YAML frontmatter. Only one skill with ``group: orchestration`` may be
   installed at a time (mutual exclusion). The variant delivered in this
   CR is ``syspilot.orchestration-jarvis``.

   **Rationale:**
   Group membership enables the Skill Architecture's substitutability
   mechanism. By declaring a group, the orchestration skill advertises
   that it can be replaced by another skill in the same group (e.g. a
   sync-only variant) while agents continue to use the same verbs.

   **Acceptance Criteria:**

   * AC-1: Given an orchestration skill, When its frontmatter is inspected, Then it contains ``group: orchestration``
   * AC-2: Given a target project, When skills are installed, Then at most one skill with ``group: orchestration`` is installed at any time
   * AC-3: Given the orchestration group contract, When inspected, Then it contains a DEFINITIONS section declaring INVOKE, SEND, RECEIVE, RESPOND
   * AC-4: Given this CR, When delivered, Then ``syspilot.orchestration-jarvis`` is the orchestration variant present


.. req:: Agent Workflow Vocabulary
   :id: SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   Agent workflow step descriptions SHALL use the orchestration verb
   vocabulary (INVOKE, SEND, RECEIVE, RESPOND) instead of referencing
   concrete runtime tools or mechanisms.

   * An agent SHALL use **INVOKE** in workflow step prose when calling
     another agent synchronously in the same session (caller waits for result).
   * An agent SHALL use **SEND** in workflow step prose when delivering
     a message to another session (non-blocking cross-session communication).
   * An agent that checks for pending work SHALL use **RECEIVE** as
     its first workflow step.
   * Every agent that is called by another agent
     SHALL include **RESPOND** as the terminal step in its workflow.
   * No agent workflow step description SHALL contain a specific runtime
     tool name (e.g. ``runSubagent()``, ``jarvis_sendToSession``) — tool
     mapping is delegated to the installed orchestration skill.

   **Routing rule:** Synchronous same-session call = INVOKE;
   Cross-session delivery = SEND; Callee returning = RESPOND (terminal).

   **Rationale:**
   While ``SYSP_REQ_SKILL_ORCHESTRATION_INVOKE`` defines the verb
   semantics within the skill, this requirement governs how agent
   documents USE those verbs. Consistent vocabulary in agent workflow
   prose ensures that the orchestration skill can resolve verbs to
   runtime calls without ambiguity.

   **Acceptance Criteria:**

   * AC-1: Given an agent that calls another agent synchronously, When the workflow step is written, Then "INVOKE" appears — no alternative verbs permitted
   * AC-2: Given an agent that delivers a message to another session, When the workflow step is written, Then "SEND" appears — no "delegate to" or tool-referencing language
   * AC-3: Given an agent that checks for pending work, When its workflow is written, Then RECEIVE appears as the first step
   * AC-4: Given a callee agent that is called by another agent, When its workflow is written, Then RESPOND appears as the terminal step
   * AC-5: Given any agent file in ``syspilot/agents/``, When its workflow step prose is inspected, Then it contains no concrete runtime tool names (``runSubagent()``, ``jarvis_sendToSession``, ``jarvis_readMessage``)
   * AC-6: Given all agent documents, When the routing rule is verified, Then synchronous same-session calls use INVOKE and cross-session deliveries use SEND
