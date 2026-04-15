Quality Engineer Trace Agent
==============================


.. story:: Quality Engineer Trace Agent
   :id: SYSP_US_TRACE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, trace, quality-engineer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a Quality Engineer Trace agent (syspilot.trace) that traces
   one item vertically through all specification levels,
   **so that** I can verify that a User Story flows correctly through Requirements
   to Design Specs to Code to Tests with semantic consistency.

   **Context:**

   The Trace agent performs vertical analysis — following one item's links from
   User Story through Requirements to Design Specs (and optionally to code and
   tests). It checks that semantic intent is preserved across levels and that
   no links are broken. It does not check horizontal consistency (that's the
   MECE agent's job).

   **Acceptance Criteria:**

   1. Given a spec element ID, When Trace runs, Then it follows all links up and down
   2. Given a broken link, When detected, Then Trace reports the gap with context
   3. Given semantic drift, When intent changes between levels, Then Trace flags the inconsistency
   4. Given a complete chain, When all links valid, Then Trace confirms full traceability
