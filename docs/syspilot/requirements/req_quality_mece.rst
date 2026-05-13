Quality Engineer MECE Requirements
====================================


.. req:: Quality Engineer MECE Soul
   :id: SYSP_REQ_MECE_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, mece, soul
   :links: SYSP_US_MECE

   **Description:**
   The Quality Engineer MECE agent (syspilot.mece) SHALL have a Soul that defines
   it as a horizontal consistency expert — systematic, analytical, and focused on
   the MECE principle.

   **Acceptance Criteria:**

   * AC-1: MECE Soul defines a systematic, analytical character
   * AC-2: MECE agent focuses exclusively on horizontal analysis (one level at a time)
   * AC-3: MECE agent never modifies specifications — it only reports findings


.. req:: Quality Engineer MECE Duties
   :id: SYSP_REQ_MECE_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, mece, duties
   :links: SYSP_US_MECE

   **Description:**
   The Quality Engineer MECE agent SHALL have Duties that guarantee complete
   item coverage, overlap visibility, gap visibility, and strict level isolation.

   **Acceptance Criteria:**

   * AC-1: After every MECE run, every item at the checked level has been examined — no item remains unexamined
   * AC-2: After every MECE run, all detected overlaps are reported with specific details — no overlap remains implicit
   * AC-3: After every MECE run, all detected gaps in coverage are explicitly named — no gap is silently passed over
   * AC-4: During every MECE run, exactly one level (L0, L1, or L2) is checked — levels are never mixed in a single run


.. req:: Quality Engineer MECE Workflow
   :id: SYSP_REQ_MECE_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, mece, workflow
   :links: SYSP_US_MECE

   **Description:**
   The Quality Engineer MECE agent SHALL follow a workflow from reading items
   through analysis to report generation.

   **Acceptance Criteria:**

   * AC-1: Workflow accepts a specification level as input (US, REQ, or SPEC)
   * AC-2: MECE agent reads all items at the specified level
   * AC-3: MECE agent applies MECE and consistency checks
   * AC-4: MECE agent produces a structured findings report


.. req:: Quality Engineer MECE Frontmatter Configuration
   :id: SYSP_REQ_MECE_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, mece, frontmatter
   :links: SYSP_US_MECE; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Quality Engineer MECE agent SHALL be configured with YAML frontmatter
   that declares it as a non-user-invocable, read-only subagent with no
   editing tools and no subagents.

   **Rationale:**
   The MECE agent is strictly read-only — it analyzes but never modifies.
   Its minimal toolset (``read``, ``search``, ``todo``) enforces the guardrail
   that it can only report findings.

   **Acceptance Criteria:**

   * AC-1: MECE frontmatter declares ``user-invocable: false``
   * AC-2: MECE frontmatter lists an empty ``agents`` array
   * AC-3: MECE frontmatter includes only ``read``, ``search``, ``todo`` in tools
   * AC-4: MECE frontmatter does NOT include ``edit`` or ``execute`` in tools
