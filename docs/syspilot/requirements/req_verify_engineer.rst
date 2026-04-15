Verify Engineer Requirements
============================


.. req:: Verify Engineer Soul
   :id: SYSP_REQ_VERIFY_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, verify, soul
   :links: SYSP_US_VERIFY

   **Description:**
   The Verify Engineer agent (syspilot.verify) SHALL have a Soul that defines it as
   thorough, skeptical, and evidence-based — embodying "Trust but verify." It never
   implements, only checks.

   **Acceptance Criteria:**

   * AC-1: Verify Engineer Soul defines a thorough, skeptical, evidence-based character
   * AC-2: Verify Engineer never modifies implementation code or spec content, except for writing validation reports and setting ``:status: implemented``
   * AC-3: Verify Engineer always provides evidence for every finding


.. req:: Verify Engineer Duties
   :id: SYSP_REQ_VERIFY_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, verify, duties
   :links: SYSP_US_VERIFY

   **Description:**
   The Verify Engineer agent SHALL have Duties covering Change Document reading,
   spec-to-implementation comparison, traceability link checking, sphinx-build
   validation, and validation report creation.

   **Acceptance Criteria:**

   * AC-1: Verify Engineer can read and parse a Change Document to identify all changed elements
   * AC-2: Verify Engineer can compare each spec change against its implementation
   * AC-3: Verify Engineer delegates traceability checking to the Trace Engineer subagent
   * AC-4: Verify Engineer can run sphinx-build and report warnings or errors


.. req:: Verify Engineer Workflow
   :id: SYSP_REQ_VERIFY_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, verify, workflow
   :links: SYSP_US_VERIFY

   **Description:**
   The Verify Engineer agent SHALL follow a workflow from receiving the Change
   Document through spec-to-code comparison to producing a validation report
   and updating spec statuses.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with receiving and reading the Change Document
   * AC-2: Verify Engineer compares specs against implementation for every changed element
   * AC-3: Verify Engineer checks traceability links across all levels
   * AC-4: Verify Engineer runs sphinx-build and writes a validation report at ``docs/changes/val-<name>.md``
   * AC-5: Verify Engineer sets ``:status: implemented`` on specs that pass verification


.. req:: Verify Engineer Frontmatter Configuration
   :id: SYSP_REQ_VERIFY_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, verify, frontmatter
   :links: SYSP_US_VERIFY; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Verify Engineer agent SHALL be configured with YAML frontmatter that
   declares it as a non-user-invocable subagent with read, search, and execution
   capabilities, delegating traceability checks to the Trace Engineer.

   **Rationale:**
   The Verify Engineer reads specs and implementation files, searches for
   references, and runs sphinx-build for validation. It needs ``read``, ``search``,
   and ``execute`` tools and delegates traceability link checking to the Trace Agent.

   **Acceptance Criteria:**

   * AC-1: Verify Engineer frontmatter declares ``user-invocable: false``
   * AC-2: Verify Engineer frontmatter lists ``agents: [syspilot.trace]``
   * AC-3: Verify Engineer frontmatter includes ``read``, ``search``, ``execute``, ``todo`` in tools
