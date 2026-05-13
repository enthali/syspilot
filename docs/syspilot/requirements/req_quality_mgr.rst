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
   * AC-3: QM always produces findings as a Findings Report addressed to PM


.. req:: Quality Manager Duties
   :id: SYSP_REQ_QM_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, qm, duties
   :links: SYSP_US_QM

   **Description:**
   The Quality Manager agent SHALL have Duties that guarantee independent
   assessment, per-level separation, findings visibility, clear quality
   statements, targeted check precision, and complete check coverage.

   **Acceptance Criteria:**

   * AC-1: Every quality assessment is performed independently from the active change flow — QM never participates in or influences the change pipeline
   * AC-2: After every quality check, L0, L1, and L2 findings are clearly separated — findings for different levels are never mixed into a single undifferentiated list
   * AC-3: After every quality check, all findings are routed to PM as a Findings Report — no finding remains internal to QM without an addressee
   * AC-4: After every quality check, the output is either a clean bill of health OR a structured Findings Report — never an ambiguous intermediate state
   * AC-5: When triggered by a CM-completion notification, QM focuses exclusively on the elements declared in the Change Document — no scope creep beyond the declared change
   * AC-6: During every audit run, MECE, Trace, and Schema checks are all executed — no check type is omitted


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

   * AC-1: QM workflow can be triggered periodically, on-demand, or by a CM-completion notification
   * AC-2: QM dispatches the MECE Engineer in separate invocations — one per specification level (L0, L1, L2) in the current scope
   * AC-3: QM collects per-level findings and the Findings Report clearly indicates pass/fail status for each specification level
   * AC-4: QM workflow supports targeted checks on changed elements when triggered by a CM-completion notification
   * AC-5: QM SHALL report findings to PM as a Findings Report for all trigger types; PM makes the fix/defer/accept decision; QM SHALL NEVER create CRs


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
   ``syspilot_jarvis_tools`` for sending Findings Reports to PM via Jarvis.

   **Acceptance Criteria:**

   * AC-1: QM frontmatter declares ``user-invocable: true``
   * AC-2: QM frontmatter lists ``syspilot.mece`` and ``syspilot.trace`` in ``agents``
   * AC-3: QM frontmatter includes ``agent`` and ``syspilot_jarvis_tools`` in tools


.. req:: Quality Manager Prompt File
   :id: SYSP_REQ_QM_PROMPT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, qm, prompt
   :links: SYSP_US_QM; SYSP_REQ_AGENT_ARCH_PROMPT

   **Description:**
   The Quality Manager SHALL have a prompt file ``syspilot.qm.prompt.md`` that
   enables direct user invocation via VS Code Copilot.

   **Acceptance Criteria:**

   * AC-1: File ``syspilot.qm.prompt.md`` exists in the prompts directory
   * AC-2: Prompt file references agent ``syspilot.qm``
   * AC-3: User can invoke the QM via the prompt mechanism
