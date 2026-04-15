Quality Manager Agent
=====================


.. story:: Quality Manager Agent
   :id: SYSP_US_QM
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, qm
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a Quality Manager agent (syspilot.qm) that independently
   checks quality across the specification hierarchy,
   **so that** quality issues are found proactively — not just during changes —
   through periodic MECE audits, trace checks, and schema validations.

   **Context:**

   The Quality Manager operates independently from the change flow. It can be
   triggered periodically or on-demand. It dispatches Quality Engineers (MECE,
   Trace) and collects findings. When issues are found, QM creates Change
   Requests for the Change Manager to fix.

   **Acceptance Criteria:**

   1. Given a periodic check, When QM runs, Then it dispatches MECE and Trace engineers
   2. Given quality findings, When issues are found, Then QM creates Change Requests with findings
   3. Given no issues, When all checks pass, Then QM reports a clean bill of health
   4. Given I ask for a quality report, When QM produces it, Then it covers all specification levels
   5. Given a CM-completion notification, When QM receives it, Then it performs a targeted check on the changed elements
