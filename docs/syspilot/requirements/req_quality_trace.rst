Quality Engineer Trace Requirements
=====================================


.. req:: Quality Engineer Trace Soul
   :id: SYSP_REQ_TRACE_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, trace, soul
   :links: SYSP_US_TRACE

   **Description:**
   The Quality Engineer Trace agent (syspilot.trace) SHALL have a Soul that defines
   it as a vertical traceability expert — detail-oriented, chain-following, and
   focused on semantic consistency across levels.

   **Acceptance Criteria:**

   * AC-1: Trace Soul defines a detail-oriented, methodical character
   * AC-2: Trace agent focuses exclusively on vertical analysis (one item through all levels)
   * AC-3: Trace agent never modifies specifications — it only reports findings


.. req:: Quality Engineer Trace Duties
   :id: SYSP_REQ_TRACE_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, trace, duties
   :links: SYSP_US_TRACE

   **Description:**
   The Quality Engineer Trace agent SHALL have Duties covering link traversal,
   chain completeness verification, and semantic consistency checking.

   **Acceptance Criteria:**

   * AC-1: Trace agent can follow links upward (SPEC → REQ → US)
   * AC-2: Trace agent can follow links downward (US → REQ → SPEC → Code → Tests)
   * AC-3: Trace agent can detect broken links and orphaned elements
   * AC-4: Trace agent can verify semantic consistency across levels


.. req:: Quality Engineer Trace Workflow
   :id: SYSP_REQ_TRACE_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, trace, workflow
   :links: SYSP_US_TRACE

   **Description:**
   The Quality Engineer Trace agent SHALL follow a workflow from receiving an
   item ID through link traversal to gap analysis and reporting.

   **Acceptance Criteria:**

   * AC-1: Workflow accepts a specification element ID as input
   * AC-2: Trace agent uses link discovery script to find all connected elements
   * AC-3: Trace agent analyzes chain completeness and semantic validity
   * AC-4: Trace agent produces a structured trace report


.. req:: Quality Engineer Trace Frontmatter Configuration
   :id: SYSP_REQ_TRACE_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, trace, frontmatter
   :links: SYSP_US_TRACE; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Quality Engineer Trace agent SHALL be configured with YAML frontmatter
   that declares it as a non-user-invocable, read-only subagent with execution
   access (for the link discovery script) but no subagents.

   **Rationale:**
   The Trace agent needs ``execute`` to run ``get_need_links.py`` for link
   discovery. It is read-only otherwise and has no subagents.

   **Acceptance Criteria:**

   * AC-1: Trace frontmatter declares ``user-invocable: false``
   * AC-2: Trace frontmatter lists an empty ``agents`` array
   * AC-3: Trace frontmatter includes ``read``, ``search``, ``execute`` in tools
   * AC-4: Trace frontmatter does NOT include ``edit`` in tools
