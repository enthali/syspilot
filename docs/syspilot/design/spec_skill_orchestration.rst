Skill: Orchestration Design
===========================

Design specifications for the manager-engineer orchestration pattern.


.. spec:: Communication Pattern
   :id: SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN
   :status: approved
   :tags: agent-v2, skill, orchestration, architecture
   :links: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE; SYSP_REQ_SKILL_ORCHESTRATION_FRONTMATTER

   **Definition:**

   Agent orchestration follows a strict three-phase communication pattern:

   **1. Manager → Engineer (Assignment):**

   The manager provides a clear assignment with:

   * Input paths (Change Document, file paths, scope description)
   * Instruction to work autonomously without asking questions
   * Expected output format

   **2. Engineer → Manager (Result):**

   The engineer returns a structured result report with:

   * Created / modified files
   * Specification IDs (new or changed)
   * Build status
   * Decisions made during execution

   **3. Engineers are decoupled:**

   * Engineers do not know about each other
   * Only the manager knows the full sequence
   * Engineers receive all needed context from the manager, not from sibling engineers

   **Invocation:**

   ::

      runSubagent("syspilot.<name>", {
        // assignment with input paths and instructions
      })


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
