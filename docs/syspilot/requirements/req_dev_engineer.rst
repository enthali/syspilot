Dev Engineer Requirements
=========================


.. req:: Dev Engineer Soul
   :id: SYSP_REQ_IMPLEMENT_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, implement, soul
   :links: SYSP_US_IMPLEMENT

   **Description:**
   The Dev Engineer agent (syspilot.implement) SHALL have a Soul that defines it
   as pragmatic, focused, and implementation-oriented. It implements exactly what
   specs say — no over-engineering, no under-engineering.

   **Acceptance Criteria:**

   * AC-1: Dev Engineer Soul defines a pragmatic, code-focused character
   * AC-2: Dev Engineer never modifies specifications
   * AC-3: Dev Engineer implements exactly what the Design Specs prescribe


.. req:: Dev Engineer Duties
   :id: SYSP_REQ_IMPLEMENT_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, implement, duties
   :links: SYSP_US_IMPLEMENT

   **Description:**
   The Dev Engineer agent SHALL have Duties covering Change Document reading,
   spec querying, code implementation, testing, and documentation updates.

   **Acceptance Criteria:**

   * AC-1: Dev Engineer can read and understand Change Documents
   * AC-2: Dev Engineer can query sphinx-needs to find relevant specifications
   * AC-3: Dev Engineer can write code matching Design Spec acceptance criteria
   * AC-4: Dev Engineer can write and run tests
   * AC-5: Dev Engineer can update user documentation (README, agent.md files)


.. req:: Dev Engineer Workflow
   :id: SYSP_REQ_IMPLEMENT_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, implement, workflow
   :links: SYSP_US_IMPLEMENT

   **Description:**
   The Dev Engineer agent SHALL follow a workflow from reading specs through
   implementation to testing and committing.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with reading the Change Document
   * AC-2: Dev Engineer queries and reads all impacted SPEC elements
   * AC-3: Dev Engineer implements code, then writes tests
   * AC-4: Dev Engineer runs tests and ensures they pass
   * AC-5: Dev Engineer commits with traceability to the Change Document


.. req:: Dev Engineer Frontmatter Configuration
   :id: SYSP_REQ_IMPLEMENT_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, implement, frontmatter
   :links: SYSP_US_IMPLEMENT; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Dev Engineer agent SHALL be configured with YAML frontmatter that
   declares it as a non-user-invocable subagent with editing and execution
   capabilities but no subagents.

   **Rationale:**
   The Dev Engineer writes code and runs tests. It needs ``edit`` and
   ``execute`` tools but has no subagents — it is a leaf node in the
   orchestration tree.

   **Acceptance Criteria:**

   * AC-1: Dev Engineer frontmatter declares ``user-invocable: false``
   * AC-2: Dev Engineer frontmatter lists an empty ``agents`` array
   * AC-3: Dev Engineer frontmatter includes ``read``, ``edit``, ``search``, ``execute`` in tools
