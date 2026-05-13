System Designer Requirements
=============================


.. req:: System Designer Soul
   :id: SYSP_REQ_DESIGN_SOUL
   :status: approved
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
   * AC-4: System Designer reads the Change Document created by CM — it does not create it


.. req:: System Designer Duties
   :id: SYSP_REQ_DESIGN_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, change, duties
   :links: SYSP_US_DESIGN

   **Description:**
   The System Designer agent SHALL have Duties that guarantee vertical integrity,
   MECE conformance, status discipline, design auditability, and user-approval
   discipline for every specification change.

   **Acceptance Criteria:**

   * AC-1: After every completed design pass, every new or changed spec element at every level is linked to its parent and children — no element exists without traceability context
   * AC-2: Before moving to the next level, the current level has no overlaps and no gaps — MECE violations are never inherited downward
   * AC-3: Every new element starts as ``draft`` and is only set to ``approved`` after successful validation — premature approval never occurs
   * AC-4: At every point during and after the design process, the Change Document reflects the decisions made and open points — including after interruption
   * AC-5: In user-guided mode, no level transition occurs without explicit user confirmation — the designer never proceeds silently


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
   * AC-4: System Designer frontmatter includes ``vscode/askQuestions`` in tools to enable user-guided level approval
