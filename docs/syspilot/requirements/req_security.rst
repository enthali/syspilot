Security Agent Requirements
============================


.. req:: Security Agent Soul
   :id: SYSP_REQ_SEC_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent, security, soul
   :links: SYSP_US_SEC

   **Description:**
   The Security Agent (syspilot.security) SHALL have a Soul that defines it
   as an adversarial-minded, evidence-based plan owner — every countermeasure
   it records SHALL be linkable to a requirement and a tracked test.

   **Acceptance Criteria:**

   * AC-1: Security Soul defines an adversarial, evidence-based character
   * AC-2: Security Agent treats undocumented threats as plan defects, not
     features
   * AC-3: Security Agent never writes production code; it writes plan
     content, threat / countermeasure specs, and findings reports only


.. req:: Security Agent Duties
   :id: SYSP_REQ_SEC_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent, security, duties
   :links: SYSP_US_SEC

   **Description:**
   The Security Agent SHALL have Duties covering Security Plan creation,
   Security Plan maintenance, per-CR security review, CVE / dependency
   awareness guidance, and traceability of countermeasures.

   **Acceptance Criteria:**

   * AC-1: Security Agent can create the Security Plan from scratch when
     ``docs/inst/syspilot/security/`` is empty
   * AC-2: Security Agent can update the Security Plan when threats,
     countermeasures or scope change
   * AC-3: Security Agent can perform a per-CR security review and produce a
     ``docs/changes/sec-<name>.md`` Security Findings Report
   * AC-4: Security Agent SHALL ensure every countermeasure links to at
     least one requirement and SHOULD link to a tracked test
   * AC-5: Security Agent's Update Strategy chapter SHALL describe how new
     CVEs in dependencies are observed and how patches reach the field
     (cloud vs. embedded)


.. req:: Security Plan Structure
   :id: SYSP_REQ_SEC_PLAN_STRUCTURE
   :status: draft
   :priority: mandatory
   :tags: security, plan, structure
   :links: SYSP_US_SEC

   **Description:**
   The Security Plan SHALL be a hybrid artifact stored under
   ``docs/inst/syspilot/security/``. The structured content SHALL be
   sphinx-needs RST items; the strategy chapters SHALL be Markdown.

   **Acceptance Criteria:**

   * AC-1: Security Goals — RST items ``INST_SYSP_SPEC_SEC_GOAL_*`` covering
     the system and, where applicable, individual subsystems
   * AC-2: Threat Scenarios — RST items ``INST_SYSP_SPEC_SEC_THREAT_*``
     describing plausible attacks or vulnerable features
   * AC-3: Failure Criticality — each threat carries a severity field
     (``critical``, ``high``, ``medium``, ``low``) prioritized by user and
     Security Agent together
   * AC-4: Countermeasures — RST items ``INST_SYSP_SPEC_SEC_CM_*`` linked to
     the threat(s) they mitigate and to at least one requirement; SHOULD
     link to a tracked test
   * AC-5: Update Strategy — Markdown chapter
     ``docs/inst/syspilot/security/update-strategy.md`` covering CVE
     observation in dependencies and patch deployment for the project's
     deployment model
   * AC-6: Monitoring & Operations Strategy — Markdown chapter
     ``docs/inst/syspilot/security/monitoring-and-ops.md`` covering runtime
     detection, logging, incident response and ops-side controls


.. req:: Security Agent Workflow
   :id: SYSP_REQ_SEC_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent, security, workflow
   :links: SYSP_US_SEC

   **Description:**
   The Security Agent SHALL follow a workflow that selects between bootstrap
   mode (no plan exists) and per-change mode (invoked by QM with a Change
   Document).

   **Acceptance Criteria:**

   * AC-1: Workflow detects whether ``docs/inst/syspilot/security/`` is
     empty (bootstrap) or populated (maintenance / per-change)
   * AC-2: Bootstrap mode interviews the user with the
     ``syspilot.ask-questions`` skill for each of the six plan elements
   * AC-3: Per-change mode reads the Change Document, identifies
     security-relevant changes, re-evaluates affected threats and
     countermeasures, and writes ``docs/changes/sec-<name>.md``
   * AC-4: After writing or updating threat / countermeasure specs, workflow
     invokes ``syspilot.mece`` advisory on the security spec set
   * AC-5: Workflow ends by reporting back to its invoker (QM in per-change
     mode, the user otherwise) via the standard structured report


.. req:: Security Agent Activation
   :id: SYSP_REQ_SEC_ACTIVATION
   :status: draft
   :priority: mandatory
   :tags: agent, security, activation, tailoring
   :links: SYSP_US_SEC, SYSP_REQ_TAIL_PROFILE_SCHEMA

   **Description:**
   The Security Agent's involvement in the change workflow SHALL be
   activated by the Tailoring Profile flag ``security_required: true``.
   Other agents SHALL NOT hardcode security activation.

   **Acceptance Criteria:**

   * AC-1: When the Tailoring Profile sets ``security_required: true``, QM
     dispatches ``syspilot.security`` alongside MECE and Trace for every
     CR's quality check
   * AC-2: When the Tailoring Profile sets ``security_required: false`` or
     no profile exists, QM does NOT dispatch ``syspilot.security``
     automatically; the user may still invoke it directly
   * AC-3: The Security Agent itself does not depend on the profile flag —
     it can always be user-invoked


.. req:: Security Frontmatter Configuration
   :id: SYSP_REQ_SEC_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: agent, security, frontmatter
   :links: SYSP_US_SEC, SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Security Agent SHALL be configured with YAML frontmatter that
   declares it as a user-invocable engineer-style agent that may invoke
   ``syspilot.mece`` as a subagent.

   **Acceptance Criteria:**

   * AC-1: Security frontmatter declares ``user-invocable: true``
   * AC-2: Security frontmatter ``agents`` list contains exactly
     ``syspilot.mece``
   * AC-3: Security frontmatter ``tools`` includes ``read``, ``edit``,
     ``search``, ``todo``, and the ``vscode/askQuestions`` (ask-questions)
     tooling
   * AC-4: Security frontmatter does NOT include any tool that allows
     modifying ``.github/agents/`` files
