Skill: Orchestration Design
===========================

Design specifications for the manager-engineer orchestration pattern.


.. spec:: Communication Pattern
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN
   :status: approved
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE; SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER; SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL

   **Definition:**

   Agent orchestration follows a strict three-phase communication pattern
   expressed through the generic verb model:

   **1. Manager → Engineer (INVOKE) / Manager → Manager (SEND):**

   The manager uses INVOKE or SEND to assign work:

   * Input paths (Change Document, file paths, scope description)
   * Instruction to work autonomously without asking questions
   * Expected output format

   The choice of verb determines the calling semantics:

   * **INVOKE** — synchronous, caller blocks until result
   * **SEND** — cross-session message delivery (non-blocking)

   **2. Callee → Caller (RESPOND):**

   The callee executes RESPOND to return a structured result:

   * Created / modified files
   * Specification IDs (new or changed)
   * Build status
   * Decisions made during execution

   RESPOND auto-detects invocation mode: if a pending message triggered
   this run (detected via RECEIVE), RESPOND routes the result back to the
   sender via SEND; otherwise the result is returned directly.

   **3. Engineers are decoupled:**

   * Engineers do not know about each other
   * Only the manager knows the full sequence
   * Engineers receive all needed context from the manager, not from sibling engineers

   **Invocation (abstract):**

   ::

      INVOKE <agent>               → installed skill maps to synchronous call
      SEND <message> to <session>  → installed skill maps to message delivery
      RECEIVE                      → installed skill checks inbox for pending messages
      RESPOND                      → installed skill delivers result (mode-detected)


.. spec:: Orchestration Constraints
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX
   :status: approved
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER

   **Definition:**

   The following constraints govern orchestration topology:

   **Rules:**

   * Managers may INVOKE engineers (same-session synchronous call)
   * Managers may SEND messages to other managers (cross-session)
   * Engineers generally do not invoke other engineers
   * Special-case engineers (e.g. those with advisory capabilities) may
     INVOKE specific utility agents if declared in their ``agents:`` frontmatter
   * The ``agents:`` frontmatter is the single source of truth for permitted
     INVOKE targets

   **Prohibited:**

   * Agent names SHALL NOT appear in the orchestration skill content
   * Orchestration matrices listing specific agent→agent mappings belong
     in agent frontmatter declarations, not in the skill


.. spec:: Reporting Format
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_REPORTING
   :status: approved
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_REPORTING

   **Definition:**

   Engineer-to-manager reports and manager-to-sender reports SHALL use the
   following structured format:

   **Report Fields:**

   * **Status** — One of: ``completed``, ``blocked``, ``failed``
   * **Commits** — List of commit hashes with messages (if applicable)
   * **Summary** — Brief description of what was done
   * **Issues** — List of problems or follow-up items found (empty if none)

   **Applies to:**

   * CM → PM: After completing a Change Request
   * QM → PM: After completing a Quality Audit
   * Any engineer → orchestrating manager: After completing a delegated task

   **Delivery mechanism:** ``jarvis_sendToSession`` for inter-manager communication.
   Direct return value for engineer → manager within the same workflow.


.. spec:: Orchestration Group Contract
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT
   :status: approved
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE; SYSP_REQ_SKILL_ORCHESTRATION_GROUP

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
      * - ``INVOKE``
        - Synchronous call. The caller blocks until the callee returns a
          structured result. Used for same-session manager-to-engineer calls.
      * - ``SEND``
        - Deliver a message to another session. Non-blocking cross-session
          communication. Used for manager-to-manager handoff.
      * - ``RECEIVE``
        - Check inbox for pending messages. Returns the next pending message
          or indicates no messages are available. Used by agents waiting for
          async work assignments.
      * - ``RESPOND``
        - Deliver result to caller. Auto-detects invocation mode: if a
          pending message triggered this run (detected via RECEIVE), routes
          the result back to the sender via SEND; otherwise returns the
          result directly as structured output. Terminal workflow step.

   **Constraints:**

   * The DEFINITIONS section declares exactly these four terms — no more, no less
   * No agent names appear in the group contract
   * No orchestration matrix (who-calls-whom) appears in the group contract
   * Each definition is tool-agnostic — no runtime API names (e.g.
     ``runSubagent``, ``jarvis_sendToSession``) appear in DEFINITIONS

   **Acceptance Criteria:**

   * AC-1: DEFINITIONS section exists with exactly INVOKE, SEND, RECEIVE, RESPOND
   * AC-2: No agent names or orchestration matrix in the group contract
   * AC-3: Each definition is tool-agnostic (no runtime API references)


.. spec:: Orchestration Verb Model Implementation (Jarvis Variant)
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE; SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN; SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT

   **Definition:**

   The Jarvis variant (``syspilot.orchestration-jarvis``) maps the four
   generic verbs to concrete runtime mechanisms:

   .. list-table:: Verb Mapping — Jarvis Variant
      :header-rows: 1
      :widths: 20 30 50

      * - Verb
        - Syntax
        - Mapping
      * - ``INVOKE``
        - ``INVOKE <agent>``
        - ``runSubagent("syspilot.<agent>", "<prompt>")``
      * - ``SEND``
        - ``SEND <message> to <session>``
        - ``jarvis_sendToSession("<session>", "<message>")``
      * - ``RECEIVE``
        - ``RECEIVE``
        - ``jarvis_readMessage()`` — returns next pending message or empty
      * - ``RESPOND``
        - ``RESPOND``
        - Mode-detection logic (see below)

   **RESPOND mode-detection:**

   1. Call RECEIVE (``jarvis_readMessage()``) to check if a pending
      message triggered this run
   2. If yes (message found with sender context): route the result back
      to the sender via SEND (``jarvis_sendToSession``)
   3. If no (no triggering message): output the result directly as
      structured final message (captured by ``runSubagent()`` return value)

   **Mutual Exclusion:** Only one skill with ``group: orchestration`` may
   be installed at a time. The Jarvis variant is delivered in this CR.


.. spec:: Orchestration Skill Group Membership
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_GROUP
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_GROUP; SYSP_SPEC_SKILL_ARCH_FRONTMATTER

   **Definition:**

   The orchestration skill SHALL carry the following frontmatter field:

   .. code-block:: yaml

      group: orchestration

   **Mutual Exclusion:** The Setup Agent enforces that at most one skill
   with ``group: orchestration`` is installed. If a new variant is installed,
   the previous one is removed.

   **Delivered Variant:** ``syspilot.orchestration-jarvis`` is the variant
   delivered in this CR. No default assumption is made about which variant
   is installed — the group mechanism handles substitutability.

   **DEFINITIONS:** The ``orchestration`` group uses a DEFINITIONS section
   in the Group Contract Spec (``SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT``)
   to declare the four vocabulary terms: INVOKE, SEND, RECEIVE, RESPOND.


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
      :widths: 40 30 30

      * - Caller → Callee
        - Verb
        - Semantics
      * - Manager → Engineer subagent
        - ``INVOKE``
        - Same-session synchronous call
      * - Manager → Manager (cross-session)
        - ``SEND``
        - Cross-session message delivery
      * - Agent waiting for async work
        - ``RECEIVE`` (first step)
        - Check inbox for pending messages
      * - Any callee returning result
        - ``RESPOND`` (terminal)
        - Final workflow step; mode-detected delivery

   **Prohibited patterns in workflow step prose:**

   * ``runSubagent()`` — platform-specific invocation mechanism
   * ``jarvis_sendToSession`` — platform-specific messaging tool
   * ``jarvis_readMessage`` — platform-specific inbox mechanism
   * Any other concrete runtime tool name used as an invocation verb

   These tool names belong to the orchestration skill implementation
   (``SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL``), not to agent documents.

   **Binding:** INVOKE and SEND in agent workflow prose bind to the
   installed orchestration skill for runtime resolution. The skill
   translates these verbs to concrete tool calls at execution time.

   **Scope:** All agent files in ``syspilot/agents/`` (product). Instance
   files in ``.github/agents/`` are updated by the Setup Agent post-release.

   **Acceptance Criteria:**

   * AC-1: All manager agents workflow steps use INVOKE for engineer calls
   * AC-2: All manager agents use SEND for cross-session message delivery
   * AC-3: Agents waiting for async work include RECEIVE as first step
   * AC-4: All callee agents have RESPOND as terminal workflow step
   * AC-5: No agent file in ``syspilot/agents/`` contains
     ``runSubagent()``, ``jarvis_sendToSession``, or ``jarvis_readMessage``
     in workflow step prose
