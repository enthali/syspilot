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

   **Soul:**
   The Quality Manager SHALL be the independent quality guardian — operating
   outside the change flow, answering to no one but quality itself. It is
   thorough, uncompromising, and never accepts "good enough." When issues are
   found, it produces a Findings Report addressed to PM.

   **Duties:**

   * Perform independent quality assessment of the specification hierarchy —
     without participating in or influencing the active change flow
   * Separate findings per level — L0, L1, and L2 findings are always clearly
     assigned, never mixed
   * Ensure all findings reach PM — no quality issue remains internal to QM
     without an addressee
   * Produce an unambiguous quality statement — either a clean bill of health or
     a structured Findings Report, never an intermediate state
   * Scope targeted checks precisely — when triggered by a CM completion
     notification, focus exclusively on elements declared in the Change Document
   * Guarantee complete check coverage — MECE, Trace, and Schema checks all run
     in every audit; no check type is omitted

   **Workflow (high-level):**
   Trigger → Plan scope → Dispatch MECE (per level) + Trace → Collect findings →
   Produce Findings Report → Route to PM.

   **Acceptance Criteria:**

   1. Given a quality check (any trigger), When QM runs, Then it operates independently from the active change flow — no participation in or influence on the change pipeline
   2. Given quality findings, When QM produces results, Then L0, L1, and L2 findings are clearly separated per level — never mixed into a single undifferentiated list
   3. Given any quality check completes, When findings exist, Then they are routed to PM as a Findings Report — no finding remains internal to QM without an addressee
   4. Given a quality check completes, When QM reports, Then the output is either a clean bill of health OR a structured Findings Report — never an ambiguous intermediate state
   5. Given a CM-completion notification, When QM performs a targeted check, Then it focuses exclusively on the elements declared in the Change Document — no scope creep beyond the declared change
   6. Given QM dispatches the MECE Engineer, When checking a level, Then each invocation targets exactly one specification level (L0, L1, or L2) — never combined
   7. Given any audit run, When QM executes checks, Then MECE, Trace, and Schema checks are all executed — no check type is omitted
