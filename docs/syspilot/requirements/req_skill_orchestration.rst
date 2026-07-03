Skill: Orchestration Requirements
=================================

Requirements for agent orchestration patterns.


.. req:: Orchestration Verb Model
   :id: SYSP_REQ_SKILL_ORCHESTRATION_VERBS
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   The orchestration skill SHALL define three generic verbs for
   peer-to-peer inter-agent communication:

   * **SEND** — Pass work to another agent. The installed variant decides
     whether this is asynchronous message delivery or a synchronous call.
   * **RECEIVE** — Obtain the instructions that triggered this run. This
     is either a pending inbox message or the task the agent was started
     with, depending on the installed variant.
   * **RESPOND** — Deliver the result back to the agent that initiated the
     work. RESPOND is the only verb whose behaviour differs by variant: the
     installed variant routes the result appropriately (active send-back or
     plain output).

   These verbs are **tool-agnostic**. The concrete mapping is provided by the
   installed skill variant, not defined here.

   **Rationale:**
   A fixed set of generic verbs decouples agent workflows from the
   communication mechanism. Agents use SEND/RECEIVE/RESPOND in their
   documents; the installed skill translates these to runtime calls.
   This enables exchangeability — a different communication backend can
   be installed without rewriting agent documents.

   **Acceptance Criteria:**

   * AC-1: Given an agent that passes work to another agent, When it acts, Then it uses SEND
   * AC-2: Given an agent that starts a run, When it obtains its triggering instructions, Then it uses RECEIVE
   * AC-3: Given an agent that completes a task, When it returns the result to the initiator, Then it uses RESPOND
   * AC-4: Given the verb definitions, When inspected, Then they are tool-agnostic — no runtime API is prescribed at this level
   * AC-5: Given the verb vocabulary, When inspected, Then no verbs exist beyond SEND, RECEIVE, RESPOND — there is no separate synchronous-call verb
   * AC-6: Given the three verbs, When inspected, Then only RESPOND is mode-dependent; SEND and RECEIVE map identically across variants


.. req:: Orchestration Completion Reporting
   :id: SYSP_REQ_SKILL_ORCHESTRATION_REPORTING
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   When an agent completes a delegated task, it SHALL report back to
   the initiator with a structured result via RESPOND. The report SHALL
   include status, commit hashes (if applicable), summary, and issues found.

   **Rationale:**
   Structured reporting enables reliable handoff between workflow stages.
   The initiator can verify completion and route follow-up work based on
   reported status and issues.

   **Acceptance Criteria:**

   * AC-1: Given an agent that completes a delegated task, When it reports back, Then the report includes status (completed / blocked / failed)
   * AC-2: Given an agent that made commits, When it reports back, Then the report includes commit hashes with messages
   * AC-3: Given an agent that completes work, When it reports back, Then the report includes a summary of what was done
   * AC-4: Given an agent that encountered issues, When it reports back, Then the report includes any issues or follow-up items found
   * AC-5: Given an agent that finished its work, When it returns the result, Then it does so via RESPOND — no concrete runtime tool is named at this level


.. req:: Orchestration Skill Group Membership
   :id: SYSP_REQ_SKILL_ORCHESTRATION_GROUP
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   The orchestration skill SHALL declare ``group: orchestration`` in its
   YAML frontmatter. Only one skill with ``group: orchestration`` may be
   installed at a time (mutual exclusion). Two interchangeable variants
   SHALL exist: an asynchronous, session-messaging variant and a
   synchronous, in-process variant. Both implement the same group contract.

   **Rationale:**
   Group membership enables the Skill Architecture's substitutability
   mechanism. By declaring a group, the orchestration skill advertises
   that it can be replaced by another skill in the same group while agents
   continue to use the same verbs. The two variants let syspilot run with or
   without session-messaging infrastructure.

   **Acceptance Criteria:**

   * AC-1: Given an orchestration skill, When its frontmatter is inspected, Then it contains ``group: orchestration``
   * AC-2: Given a target project, When skills are installed, Then at most one skill with ``group: orchestration`` is installed at any time
   * AC-3: Given the orchestration group contract, When inspected, Then it contains a DEFINITIONS section declaring SEND, RECEIVE, RESPOND
   * AC-4: Given the orchestration group, When inspected, Then exactly two variants exist — one asynchronous (session messaging) and one synchronous (in-process)
   * AC-5: Given either variant is installed, When any agent uses the verbs, Then the agent documents require no modification to switch variants


.. req:: Agent Workflow Vocabulary
   :id: SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   Agent workflow step descriptions SHALL use the orchestration verb
   vocabulary (SEND, RECEIVE, RESPOND) instead of referencing concrete
   runtime tools or mechanisms.

   * An agent SHALL use **SEND** in workflow step prose when passing work
     to another agent.
   * An agent that obtains its triggering instructions SHALL use
     **RECEIVE** as its first workflow step.
   * Every agent that is given work by another agent SHALL include
     **RESPOND** as the terminal step in its workflow.
   * No agent workflow step description SHALL contain a specific runtime
     tool name — tool mapping is delegated to the installed orchestration
     skill.

   **Routing rule:** Passing work to another agent = SEND; obtaining
   triggering instructions = RECEIVE (first step); returning a result =
   RESPOND (terminal).

   **Rationale:**
   While ``SYSP_REQ_SKILL_ORCHESTRATION_VERBS`` defines the verb
   semantics within the skill, this requirement governs how agent
   documents USE those verbs. Consistent vocabulary in agent workflow
   prose ensures that the orchestration skill can resolve verbs to
   runtime calls without ambiguity.

   **Acceptance Criteria:**

   * AC-1: Given an agent that passes work to another agent, When the workflow step is written, Then "SEND" appears — no "invoke", "dispatch", "delegate to", or tool-referencing language
   * AC-2: Given an agent that obtains its triggering instructions, When its workflow is written, Then RECEIVE appears as the first step
   * AC-3: Given an agent that is given work by another agent, When its workflow is written, Then RESPOND appears as the terminal step
   * AC-4: Given any agent file in ``syspilot/agents/``, When its workflow step prose is inspected, Then it contains no concrete runtime tool names
   * AC-5: Given all agent documents, When the routing rule is verified, Then work dispatch uses SEND, instruction intake uses RECEIVE, and result return uses RESPOND
