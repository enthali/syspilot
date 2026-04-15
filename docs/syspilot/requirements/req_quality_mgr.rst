Quality Manager Requirements
=============================


.. req:: Quality Manager Soul
   :id: SYSP_REQ_QM_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, qm, soul
   :links: SYSP_US_QM

   **Description:**
   The Quality Manager agent (syspilot.qm) SHALL have a Soul that defines it as
   independent, thorough, and uncompromising on quality. It operates outside the
   change workflow.

   **Acceptance Criteria:**

   * AC-1: QM Soul defines an independent, quality-focused character
   * AC-2: QM never modifies specifications directly
   * AC-3: QM always produces findings that lead to Change Requests


.. req:: Quality Manager Duties
   :id: SYSP_REQ_QM_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, qm, duties
   :links: SYSP_US_QM

   **Description:**
   The Quality Manager agent SHALL have Duties covering periodic MECE audits,
   trace checks, and quality reporting.

   **Acceptance Criteria:**

   * AC-1: QM can dispatch MECE Engineer to check specification levels
   * AC-2: QM can dispatch Trace Engineer for sample traceability checks
   * AC-3: QM can produce consolidated quality reports
   * AC-4: QM can create Change Requests when findings require fixes
   * AC-5: QM can perform targeted checks on specific elements identified by a CM-completion notification


.. req:: Quality Manager Workflow
   :id: SYSP_REQ_QM_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, qm, workflow
   :links: SYSP_US_QM

   **Description:**
   The Quality Manager agent SHALL follow a workflow from trigger through
   engineer dispatch to findings consolidation.

   **Acceptance Criteria:**

   * AC-1: QM workflow can be triggered periodically or on-demand
   * AC-2: QM dispatches Quality Engineers to perform checks
   * AC-3: QM collects and consolidates findings
   * AC-4: QM creates Change Requests for the Change Manager when fixes are needed
   * AC-5: QM workflow can be triggered by a CM-completion notification for targeted checks on changed elements


.. req:: Quality Manager Frontmatter Configuration
   :id: SYSP_REQ_QM_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, qm, frontmatter
   :links: SYSP_US_QM; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Quality Manager agent SHALL be configured with YAML frontmatter that
   declares it as a user-invocable quality dispatcher with access to the MECE
   and Trace engineer subagents.

   **Rationale:**
   The QM needs the ``agent`` tool to dispatch MECE and Trace engineers, and
   ``syspilot_jarvis_tools`` for creating Change Requests via Jarvis.

   **Acceptance Criteria:**

   * AC-1: QM frontmatter declares ``user-invocable: true``
   * AC-2: QM frontmatter lists ``syspilot.mece`` and ``syspilot.trace`` in ``agents``
   * AC-3: QM frontmatter includes ``agent`` and ``syspilot_jarvis_tools`` in tools
