Skill: Orchestration Design
===========================

Design specifications for the agent orchestration skill.


.. spec:: Communication Pattern
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_VERBS; SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL

   **Definition:**

   Agent communication is peer-to-peer and follows a three-verb model:

   **Initiating work (SEND):**

   The initiator uses SEND to pass work to another agent:

   * Input context (file paths, scope description, expected output format)
   * Instruction to work autonomously without asking questions

   The installed variant decides whether SEND is asynchronous message
   delivery or a synchronous call.

   **Obtaining the assignment (RECEIVE):**

   The agent uses RECEIVE at workflow start to obtain the instructions that
   triggered the run — a pending inbox message or the task it was started
   with, depending on the installed variant.

   **Returning a result (RESPOND):**

   The agent executes RESPOND to return a structured result:

   * Created / modified files
   * Specification IDs (new or changed)
   * Build status
   * Decisions made during execution

   RESPOND is the only mode-dependent verb: the installed variant routes
   the result back to the initiator (active send-back or plain output).

   **Callee isolation:**

   * Each callee receives all needed context from its initiator
   * Callees have no knowledge of other callees in the same workflow
   * The initiator alone holds the full sequence

   **Verbs (abstract):**

   ::

      SEND <work> to <agent>  → installed skill maps to work dispatch
      RECEIVE                 → installed skill provides the triggering instructions
      RESPOND                 → installed skill delivers result to the initiator (mode-detected)


.. spec:: Orchestration Constraints
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_VERBS

   **Definition:**

   The following constraints govern orchestration verb usage:

   **Rules:**

   * An agent may SEND work to another agent
   * An agent RESPONDs to its initiator regardless of any frontmatter field —
     RESPOND is always permitted

   **Prohibited:**

   * Agent names SHALL NOT appear in the orchestration skill content
   * Orchestration matrices listing specific agent→agent mappings belong
     in agent frontmatter declarations, not in the skill


.. spec:: Reporting Format
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_REPORTING
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_REPORTING

   **Definition:**

   Agents completing a delegated task SHALL report back with a structured
   result using RESPOND. The report SHALL include the following fields:

   **Report Fields:**

   * **Status** — One of: ``completed``, ``blocked``, ``failed``
   * **Commits** — List of commit hashes with messages (if applicable)
   * **Summary** — Brief description of what was done
   * **Issues** — List of problems or follow-up items found (empty if none)

   **Delivery mechanism:** RESPOND. The installed variant routes the result
   to the initiator (active send-back or plain output).


.. spec:: Orchestration Group Contract
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_VERBS; SYSP_REQ_SKILL_ORCHESTRATION_GROUP

   **Definition:**

   This is the Group Contract Spec for the ``orchestration`` skill group.
   It defines the DEFINITIONS section that all variants in the group must
   implement.

   **DEFINITIONS:**

   .. list-table:: Orchestration Group Vocabulary
      :header-rows: 1
      :widths: 20 80

      * - Term
        - Semantics
      * - ``SEND``
        - Pass work to another agent. The installed variant decides whether
          this is asynchronous message delivery or a synchronous call.
      * - ``RECEIVE``
        - Obtain the instructions that triggered this run — a pending inbox
          message or the task the agent was started with.
      * - ``RESPOND``
        - Deliver result to the initiator. The only mode-dependent verb: the
          installed variant routes the result back (active send-back or plain
          output). Terminal workflow step.

   **Constraints:**

   * The DEFINITIONS section declares exactly these three terms — no more, no less
   * No agent names appear in the group contract
   * No orchestration matrix (who-calls-whom) appears in the group contract
   * Each definition is tool-agnostic — no runtime API names (e.g.
     ``runSubagent``, ``jarvis_sendMessage``) appear in DEFINITIONS

   **Acceptance Criteria:**

   * AC-1: DEFINITIONS section exists with exactly SEND, RECEIVE, RESPOND
   * AC-2: No agent names or orchestration matrix in the group contract
   * AC-3: Each definition is tool-agnostic (no runtime API references)


.. spec:: Orchestration Verb Model Implementation (Jarvis Variant)
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_VERBS; SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN; SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT

   **Definition:**

   The Jarvis variant (``syspilot.orchestration-jarvis``) is the asynchronous,
   session-messaging variant. It maps the three generic verbs to concrete
   runtime mechanisms:

   .. list-table:: Verb Mapping — Jarvis Variant
      :header-rows: 1
      :widths: 20 30 50

      * - Verb
        - Syntax
        - Mapping
      * - ``SEND``
        - ``SEND <work> to <agent>``
        - ``jarvis_sendMessage("<session>", "<message>", "<senderSession>")``
      * - ``RECEIVE``
        - ``RECEIVE``
        - ``jarvis_receiveMessage("<destination>")`` — returns the triggering message or empty
      * - ``RESPOND``
        - ``RESPOND``
        - Deliver result to the initiator: SEND result back to the
          originating sender via ``jarvis_sendMessage``

   **Mutual Exclusion:** Only one skill with ``group: orchestration`` may
   be installed at a time.


.. spec:: Orchestration Verb Model Implementation (Subagent Variant)
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL_SUBAGENT
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture, graceful-degradation
   :links: SYSP_REQ_SKILL_ORCHESTRATION_VERBS; SYSP_REQ_SKILL_ORCHESTRATION_GROUP; SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT

   **Definition:**

   The Subagent variant (``syspilot.orchestration-subagent``) is the
   synchronous, in-process variant. It requires no session-messaging
   infrastructure and maps the three generic verbs to ``runSubagent``:

   .. list-table:: Verb Mapping — Subagent Variant
      :header-rows: 1
      :widths: 20 30 50

      * - Verb
        - Syntax
        - Mapping
      * - ``SEND``
        - ``SEND <work> to <agent>``
        - ``runSubagent("syspilot.<agent>", "<task>")`` — blocks until the
          callee returns
      * - ``RECEIVE``
        - ``RECEIVE``
        - The task/prompt the agent was started with (the ``runSubagent``
          argument) — no inbox poll
      * - ``RESPOND``
        - ``RESPOND``
        - The agent's normal output, captured as the ``runSubagent`` return
          value

   **RESPOND mode (subagent):**

   In the synchronous variant RESPOND is always plain output: the agent emits
   its structured result as its final message, which the calling
   ``runSubagent`` captures as the return value. There is no active send-back
   and no inbox.

   **Mutual Exclusion:** Only one skill with ``group: orchestration`` may
   be installed at a time. The Subagent variant is the graceful-degradation
   path for workspaces without session-messaging infrastructure.


.. spec:: Orchestration Skill Group Membership
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_GROUP
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_GROUP; SYSP_SPEC_SKILL_ARCH_FRONTMATTER

   **Definition:**

   Each orchestration variant SHALL carry the following frontmatter field:

   .. code-block:: yaml

      group: orchestration

   **Mutual Exclusion:** The Setup Agent enforces that at most one skill
   with ``group: orchestration`` is installed. If a new variant is installed,
   the previous one is removed.

   **Variants:** Two interchangeable variants implement the group contract:

   * ``syspilot.orchestration-jarvis`` — asynchronous, session-messaging
   * ``syspilot.orchestration-subagent`` — synchronous, in-process

   The Setup Agent installs exactly one, selected by workspace context. No
   default assumption is made in agent documents — the group mechanism handles
   substitutability.

   **DEFINITIONS:** The ``orchestration`` group uses a DEFINITIONS section
   in the Group Contract Spec (``SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT``)
   to declare the three vocabulary terms: SEND, RECEIVE, RESPOND.


.. spec:: Agent Workflow Vocabulary Rules
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_AGENT_VOCAB
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_AGENT_VOCAB; SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL

   **Definition:**

   Agent workflow step prose SHALL use the following routing table to
   determine which verb to use:

   .. list-table:: Agent Vocabulary Routing
      :header-rows: 1
      :widths: 50 20 30

      * - Situation
        - Verb
        - Semantics
      * - Passing work to another agent
        - ``SEND``
        - Work dispatch (async or sync, per installed variant)
      * - Obtaining the triggering instructions at workflow start
        - ``RECEIVE`` (first step)
        - Returns the message or task that triggered the run
      * - Returning a result to the initiator
        - ``RESPOND`` (terminal)
        - Final workflow step; mode-detected delivery

   **Prohibited patterns in workflow step prose:**

   * ``runSubagent()`` — platform-specific invocation mechanism
   * ``jarvis_sendMessage`` — platform-specific messaging tool
   * ``jarvis_receiveMessage`` — platform-specific inbox mechanism
   * ``INVOKE`` — retired verb; synchronous dispatch is SEND under the
     synchronous variant
   * Any other concrete runtime tool name used as an invocation verb

   These tool names belong to the orchestration skill implementation
   (``SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL``), not to agent documents.

   **Bootstrap exception:** The Setup Bootloader's synchronous call to the
   Installer is explicitly outside the orchestration contract — it does not
   use these verbs (see ``SYSP_SPEC_SETUP_WORKFLOW``).

   **Binding:** SEND in agent workflow prose binds to the installed
   orchestration skill for runtime resolution. The skill translates the verb
   to concrete tool calls at execution time.

   **Scope:** All agent files in ``syspilot/agents/`` (product). Instance
   files in ``.github/agents/`` are updated by the Setup Agent post-release.

   **Acceptance Criteria:**

   * AC-1: All agent workflow steps use SEND to pass work to another agent
   * AC-2: Agents obtaining their assignment include RECEIVE as first step
   * AC-3: All callee agents have RESPOND as terminal workflow step
   * AC-4: No agent file in ``syspilot/agents/`` contains
     ``runSubagent()``, ``jarvis_sendMessage``, ``jarvis_receiveMessage``, or
     ``INVOKE`` in workflow step prose
