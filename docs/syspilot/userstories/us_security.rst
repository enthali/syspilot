Security Agent
===============


.. story:: Project Security Agent
   :id: SYSP_US_SEC
   :status: draft
   :priority: mandatory
   :tags: agent, engineer, security, security-plan, threat-model
   :links: SYSP_US_AGENT_ARCH, SYSP_US_TAIL

   **As a** syspilot user on a project where security is in scope,
   **I want** a Security Agent (syspilot.security) that creates and maintains
   a project Security Plan and reviews each security-relevant change,
   **so that** security goals, threats, countermeasures, update strategy and
   monitoring concerns are tracked alongside the specifications and not
   forgotten between releases.

   **Context:**

   The Security Agent is activated via the Tailoring Profile flag
   ``security_required: true``. It owns the project's **Security Plan**
   stored under ``docs/inst/syspilot/security/`` in a hybrid form:

   * **RST (sphinx-needs):** security goals, threats / threat scenarios,
     failure criticality, and countermeasures — all linkable to REQ, SPEC
     and tests so countermeasures are traceable.
   * **Markdown:** narrative chapters for the Update Strategy (CVE
     observation, deployment of fixes — easy in cloud, harder in embedded)
     and the Monitoring & Operations Strategy.

   The Security Agent is invoked as a subagent of the Quality Manager
   (``syspilot.qm``) during the change workflow. It can also be invoked
   directly by the user (``@syspilot.security``) for plan maintenance,
   threat model reviews, or after a CVE disclosure.

   **Acceptance Criteria:**

   1. Given a project where the Tailoring Profile flags
      ``security_required: true`` and no Security Plan exists yet, When
      ``@syspilot.security`` is invoked, Then it interviews the user and
      writes the Security Plan under ``docs/inst/syspilot/security/``
   2. The Security Plan covers all six elements: security goals, threat
      scenarios / vulnerable features, failure criticality, countermeasures,
      update strategy, monitoring & operations strategy
   3. Given a Change Request whose Change Document touches security-relevant
      elements, When QM dispatches ``syspilot.security``, Then it produces a
      Security Findings Report at ``docs/changes/sec-<name>.md`` with severity
      and recommendations for PM
   4. Every countermeasure recorded by the Security Agent SHALL link to at
      least one requirement (``SYSP_REQ_*`` or instance ``INST_*_REQ_*``) and
      SHOULD reference at least one tracked test
   5. The Security Agent never writes production code; it writes plan content,
      findings and traceable countermeasure specs only
