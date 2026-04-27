System Designer Requirements
=============================


.. req:: System Designer Soul
   :id: SYSP_REQ_DESIGN_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, change, soul
   :links: SYSP_US_DESIGN

   **Description:**
   The System Designer agent (syspilot.design) SHALL have a Soul that defines it
   as analytical, systematic, and level-disciplined. It never skips specification
   levels and cares deeply about traceability.

   **Acceptance Criteria:**

   * AC-1: System Designer Soul defines an analytical, methodical character
   * AC-2: System Designer always processes levels in order (US → REQ → SPEC)
   * AC-3: System Designer never skips a level even when the answer seems obvious


.. req:: System Designer Duties
   :id: SYSP_REQ_DESIGN_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, change, duties
   :links: SYSP_US_DESIGN

   **Description:**
   The System Designer agent SHALL have Duties covering change request analysis,
   Change Document management, RST writing, and MECE advisory invocation.

   **Acceptance Criteria:**

   * AC-1: System Designer can analyze change requests and identify impacted elements
   * AC-2: System Designer can create and maintain Change Documents
   * AC-3: System Designer can write RST files with sphinx-needs directives
   * AC-4: System Designer can invoke MECE agent as advisory subagent
   * AC-5: System Designer can perform horizontal MECE checks per level
   * AC-6: System Designer can use the impact analysis skill to discover affected elements before each level


.. req:: System Designer Workflow
   :id: SYSP_REQ_DESIGN_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, change, workflow
   :links: SYSP_US_DESIGN

   **Description:**
   The System Designer agent SHALL follow an iterative level-by-level workflow
   with user discussion at each level.

   **Acceptance Criteria:**

   * AC-1: Workflow processes Level 0 (US), then Level 1 (REQ), then Level 2 (SPEC)
   * AC-2: Each level includes: identify (via impact analysis) → propose → discuss → write RST → MECE advisory
   * AC-3: User can navigate back to previous levels at any time
   * AC-4: Final consistency check across all levels before setting status to approved
   * AC-5: Impact Analysis SHALL be executed before spec changes at each level — CR file lists are hints, not the complete scope


.. req:: System Designer Frontmatter Configuration
   :id: SYSP_REQ_DESIGN_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, change, frontmatter
   :links: SYSP_US_DESIGN; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The System Designer agent SHALL be configured with YAML frontmatter that
   declares it as a non-user-invocable subagent with RST editing capabilities
   and the MECE engineer as its only subagent.

   **Rationale:**
   The System Designer writes RST files and invokes MECE as advisory subagent
   per level. It is invoked only by the CM, not directly by users.

   **Acceptance Criteria:**

   * AC-1: System Designer frontmatter declares ``user-invocable: false``
   * AC-2: System Designer frontmatter lists ``syspilot.mece`` in ``agents``
   * AC-3: System Designer frontmatter includes ``read``, ``edit``, ``search``, ``execute`` in tools
