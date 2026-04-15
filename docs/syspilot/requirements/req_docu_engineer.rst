Documentation Engineer Requirements
=====================================


.. req:: Documentation Engineer Soul
   :id: SYSP_REQ_DOCU_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, docu, soul
   :links: SYSP_US_DOCU

   **Description:**
   The Documentation Engineer agent (syspilot.docu) SHALL have a Soul that defines
   it as the documentation keeper — keeping docs in sync with reality, preferring
   brevity over verbosity, and removing stale information.

   **Acceptance Criteria:**

   * AC-1: Documentation Engineer Soul defines a sync-focused, concise character
   * AC-2: Documentation Engineer always removes redundant information
   * AC-3: Documentation Engineer links to sources instead of duplicating content


.. req:: Documentation Engineer Duties
   :id: SYSP_REQ_DOCU_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, docu, duties
   :links: SYSP_US_DOCU

   **Description:**
   The Documentation Engineer agent SHALL have Duties covering two areas:
   internal documentation (copilot-instructions.md, context.md, naming conventions)
   and external documentation (README, methodology, release notes, architecture).

   **Acceptance Criteria:**

   * AC-1: Documentation Engineer can update copilot-instructions.md
   * AC-2: Documentation Engineer can update manager context.md files
   * AC-3: Documentation Engineer can update README and methodology docs
   * AC-4: Documentation Engineer can update release notes and architecture docs
   * AC-5: Documentation Engineer can detect and remove stale documentation


.. req:: Documentation Engineer Workflow
   :id: SYSP_REQ_DOCU_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, docu, workflow
   :links: SYSP_US_DOCU

   **Description:**
   The Documentation Engineer agent SHALL follow a workflow from gathering
   recent changes through gap analysis to documentation updates.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with gathering recent changes (git log, changed files)
   * AC-2: Documentation Engineer compares documented state vs. reality
   * AC-3: Documentation Engineer updates internal docs first, then external
   * AC-4: Documentation Engineer verifies consistency after updates


.. req:: Documentation Engineer Frontmatter Configuration
   :id: SYSP_REQ_DOCU_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, docu, frontmatter
   :links: SYSP_US_DOCU; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Documentation Engineer agent SHALL be configured with YAML frontmatter
   that declares it as a non-user-invocable subagent with editing and execution
   capabilities but no subagents.

   **Rationale:**
   The Documentation Engineer updates multiple documentation files and needs
   ``edit`` and ``execute`` tools. It has no subagents — documentation is a
   self-contained task.

   **Acceptance Criteria:**

   * AC-1: Documentation Engineer frontmatter declares ``user-invocable: false``
   * AC-2: Documentation Engineer frontmatter lists an empty ``agents`` array
   * AC-3: Documentation Engineer frontmatter includes ``read``, ``edit``, ``search``, ``execute`` in tools
