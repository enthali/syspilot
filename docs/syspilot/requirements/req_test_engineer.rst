Test Engineer Requirements
==========================


.. req:: Test Engineer Soul
   :id: SYSP_REQ_UAT_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, uat, soul
   :links: SYSP_US_UAT

   **Description:**
   The Test Engineer agent (syspilot.uat) SHALL have a Soul that defines it as
   the quality conscience of the change workflow — precise, systematic, and
   focused on testability.

   **Acceptance Criteria:**

   * AC-1: Test Engineer Soul defines a quality-conscious, precise character
   * AC-2: Test Engineer always checks for testability concerns
   * AC-3: Test Engineer never skips edge cases


.. req:: Test Engineer Duties
   :id: SYSP_REQ_UAT_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, uat, duties
   :links: SYSP_US_UAT

   **Description:**
   The Test Engineer agent SHALL have Duties covering UAT chain generation,
   testability validation, and sphinx-build verification.

   **Acceptance Criteria:**

   * AC-1: Test Engineer can generate UAT user stories from feature acceptance criteria
   * AC-2: Test Engineer can generate UAT requirements (test data specifications)
   * AC-3: Test Engineer can generate UAT design specs (expected outcomes tables)
   * AC-4: Test Engineer can validate testability and report untestable criteria


.. req:: Test Engineer Workflow
   :id: SYSP_REQ_UAT_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, uat, workflow
   :links: SYSP_US_UAT

   **Description:**
   The Test Engineer agent SHALL follow a workflow from reading the Change
   Document through UAT chain generation to validation and reporting.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with reading the Change Document and identifying feature US
   * AC-2: Test Engineer reads existing RST patterns before generating
   * AC-3: Test Engineer generates one UAT chain per feature user story
   * AC-4: Test Engineer validates with sphinx-build and reports results


.. req:: Test Engineer Frontmatter Configuration
   :id: SYSP_REQ_UAT_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, uat, frontmatter
   :links: SYSP_US_UAT; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Test Engineer agent SHALL be configured with YAML frontmatter that
   declares it as a non-user-invocable subagent with editing and execution
   capabilities but no subagents.

   **Rationale:**
   The Test Engineer generates UAT RST files and runs sphinx-build for
   validation. It needs ``edit`` and ``execute`` tools but has no subagents.

   **Acceptance Criteria:**

   * AC-1: Test Engineer frontmatter declares ``user-invocable: false``
   * AC-2: Test Engineer frontmatter lists an empty ``agents`` array
   * AC-3: Test Engineer frontmatter includes ``read``, ``edit``, ``search``, ``execute`` in tools
