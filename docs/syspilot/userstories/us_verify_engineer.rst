Verify Engineer Agent
=====================


.. story:: Verify Engineer Agent
   :id: SYSP_US_VERIFY
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, verify
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a Verify Engineer agent (syspilot.verify) that validates
   implementation against the Change Document and checks traceability completeness,
   **so that** I can be confident that what was specified is what was actually built,
   with full spec-to-code and spec-to-file comparison.

   **Context:**

   The Verify Engineer answers "Did we build it right?" It reads the Change
   Document, compares each spec change against the actual implementation, delegates
   traceability checking to the Trace Engineer, runs sphinx-build, and produces a
   validation report. It is complementary to MECE (horizontal consistency) and
   Trace (vertical traceability). Scope: only elements declared in the Change Document.

   **Acceptance Criteria:**

   1. Given a Change Document, When the Verify Engineer processes it, Then it compares every spec change against the implementation
   2. Given traceability links, When checking completeness, Then every link chain is validated end-to-end
   3. Given a verification run, When completed, Then a validation report is created at ``docs/changes/val-<name>.md``
   4. Given discrepancies, When detected, Then the Verify Engineer reports gaps without attempting to fix them
