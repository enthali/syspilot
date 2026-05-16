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

   **1. Manager → Engineer (INVOKE / DELEGATE):**

   The manager uses INVOKE or DELEGATE to assign work to an engineer:

   * Input paths (Change Document, file paths, scope description)
   * Instruction to work autonomously without asking questions
   * Expected output format

   The choice of verb determines the calling semantics:

   * **INVOKE** — synchronous, caller blocks until result
   * **DELEGATE** — hand-off (async variants add Reply Contract;
     sync variant collapses to INVOKE)

   **2. Engineer → Manager (REPLY):**

   The engineer executes REPLY to return a structured result:

   * Created / modified files
   * Specification IDs (new or changed)
   * Build status
   * Decisions made during execution

   **3. Engineers are decoupled:**

   * Engineers do not know about each other
   * Only the manager knows the full sequence
   * Engineers receive all needed context from the manager, not from sibling engineers

   **Invocation (abstract):**

   ::

      INVOKE <agent>        → installed skill maps to runtime call
      DELEGATE <task> to <agent> → installed skill maps to delegation
      REPLY                 → installed skill delivers result to caller


.. spec:: Orchestration Matrix
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX
   :status: approved
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER

   **Definition:**

   The following table defines who may orchestrate whom:

   .. list-table:: Orchestration Matrix
      :header-rows: 1
      :widths: 20 40 40

      * - Agent
        - Invokes
        - Purpose
      * - ``syspilot.cm``
        - change, implement, uat, verify, mece, trace, release, docu
        - Full change workflow orchestration
      * - ``syspilot.qm``
        - mece, trace
        - Quality audits (MECE + Trace checks)
      * - ``syspilot.design``
        - mece
        - Advisory MECE check per specification level

   **Constraints:**

   * Managers (CM, QM, PM) may invoke engineers
   * Engineers generally do not invoke other engineers
   * The ``syspilot.design`` agent is a special case: it is an engineer
     that may invoke ``syspilot.mece`` for advisory checks


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


.. spec:: Orchestration Verb Model Implementation (Sync Variant)
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL
   :status: draft
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE; SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN

   **Definition:**

   The default sync variant (``syspilot.orchestration``) maps the three
   generic verbs to concrete runtime mechanisms:

   .. list-table:: Verb Mapping — Sync Variant
      :header-rows: 1
      :widths: 25 35 40

      * - Verb
        - Syntax
        - Mapping
      * - ``INVOKE``
        - ``INVOKE <agent>``
        - ``runSubagent("syspilot.<agent>", "<prompt>")``
      * - ``DELEGATE``
        - ``DELEGATE <task> to <agent>``
        - Collapses to INVOKE (no async in sync variant)
      * - ``REPLY``
        - ``REPLY``
        - Prompt-Reminder: "Summarize findings as your final message"

   **REPLY is runtime-conditional:** The callee checks how it was called.
   In the sync variant, REPLY is implemented as a prompt reminder injected
   at the end of the engineer's workflow — the engineer summarizes its
   findings as its final message, which ``runSubagent()`` captures as the
   return value.

   **Mutual Exclusion:** Only one skill with ``group: orchestration`` may
   be installed at a time. The sync variant is the default.


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

   **Default Variant:** ``syspilot.orchestration`` (sync variant) is the
   default. It is installed by the Setup Agent unless an alternative is
   explicitly configured.

   **DEFINITIONS:** The ``orchestration`` group does not use DEFINITIONS.
   Verbs (INVOKE/DELEGATE/REPLY) map directly to runtime tools via the installed
   skill variant. No project-specific configuration is required.


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
        - ``DELEGATE``
        - Cross-session handoff
      * - Any callee returning result
        - ``REPLY`` (terminal)
        - Final workflow step

   **Prohibited patterns in workflow step prose:**

   * ``runSubagent()`` — platform-specific invocation mechanism
   * ``jarvis_sendToSession`` — platform-specific messaging tool
   * Any other concrete runtime tool name used as an invocation verb

   These tool names belong to the orchestration skill implementation
   (``SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL``), not to agent documents.

   **Binding:** INVOKE and DELEGATE in agent workflow prose bind to the
   installed orchestration skill for runtime resolution. The skill
   translates these verbs to concrete tool calls at execution time.

   **Scope:** All agent files in ``syspilot/agents/`` (product). Instance
   files in ``.github/agents/`` are updated by the Setup Agent post-release.

   **Acceptance Criteria:**

   * AC-1: All 3 manager agents (CM, PM, QM) workflow steps use INVOKE
     for engineer calls
   * AC-2: All 3 manager agents use DELEGATE for Manager-to-Manager
     handoffs
   * AC-3: All engineer agents called by another agent have REPLY as
     terminal step
   * AC-4: No agent file in ``syspilot/agents/`` contains
     ``runSubagent()`` or ``jarvis_sendToSession`` in workflow step prose
