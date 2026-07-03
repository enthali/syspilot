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
   * AC-7: After every CM-triggered quality check, QM writes all findings directly into the ``## QM Findings`` section of the Change Document — the findings live durably in the contract, not only in a transient message


.. req:: Quality Manager Workflow
   :id: SYSP_REQ_QM_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, qm, workflow
   :links: SYSP_US_QM

   **Description:**
   The Quality Manager is the final quality gate for a completed change. CM
   triggers QM after implementation and validation. QM scopes the check to the
   change. For the specification it SENDs work to the MECE Engineer once per
   specification level and to the Trace Engineer; the implementation and
   validation it assesses itself, as no specialist engineers exist for those.
   QM consolidates all findings and records them in the change's Change
   Document. The concrete orchestration flow is specified in
   ``SYSP_SPEC_QM_WORKFLOW``.

   **Acceptance Criteria:**

   * AC-1: QM is triggered by CM as the final quality gate of a completed change, after implementation and validation
   * AC-2: QM scopes the check to the elements declared in the Change Document
   * AC-3: For each specification level in scope, QM SENDs one MECE check; traceability is covered via the Trace Engineer
   * AC-4: QM assesses the implementation and the validation of the change itself
   * AC-5: The findings state pass/fail per specification level, kept separate
   * AC-6: QM records the consolidated findings in the Change Document's ``## QM Findings`` section, one sub-section per review round
   * AC-7: The fix / defer / accept decision on the findings rests with PM


.. req:: Quality Manager Frontmatter Configuration
   :id: SYSP_REQ_QM_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, qm, frontmatter
   :links: SYSP_US_QM; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Quality Manager agent SHALL be configured with YAML frontmatter that
   declares it as a user-invocable quality dispatcher. It declares no
   ``tools:`` field.

   **Rationale:**
   The QM SENDs work to the MECE and Trace engineer sessions and reports Findings
   to PM using whatever tools are enabled on the user's default VS Code agent,
   including session-messaging (``enthali.jarvis-core/*``). The QM does not invoke
   subagents; it omits ``agents:`` and carries no ``agent/runSubagent``.

   **Acceptance Criteria:**

   * AC-1: QM frontmatter declares ``user-invocable: true``
   * AC-2: QM frontmatter omits ``agents:`` — it SENDs to engineer sessions
   * AC-3: QM frontmatter declares no ``tools:`` field — it inherits the user's default agent tool selection


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
