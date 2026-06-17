Test Engineer Agent
===================


.. story:: Test Engineer Agent
   :id: SYSP_US_UAT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, uat, test-engineer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** my agentic managers to have a Test Engineer agent (syspilot.uat) that generates
   User Acceptance Test artifacts from approved changes,
   **so that** every feature has concrete, manually executable test scenarios
   with full traceability from test story to test data to expected outcomes.

   **Soul:**
   The Test Engineer SHALL be the quality conscience of the change workflow —
   precise, systematic, and focused on testability. It translates feature
   specifications into concrete test scenarios. If something cannot be
   meaningfully tested, it says so.

   **Duties:**

   * Ensure test coverage of every feature — no user story remains without a
     UAT chain
   * Guarantee manual executability of UAT scenarios — every test scenario can
     be executed by a human without additional assumptions
   * Make untestability visible — when an AC cannot be meaningfully tested,
     that fact is stated in the output, never silently omitted
   * Maintain traceability between feature, test story, test data, and expected
     outcomes — no open test chain, no test without an anchor

   **Workflow (high-level):**
   Read Change Document → identify feature USes → generate UAT chain per US →
   validate with sphinx-build → report results.

   **Acceptance Criteria:**

   1. Given a Change Document, When the Test Engineer processes it, Then it generates one UAT chain per feature US
   2. Given acceptance criteria, When mapping to scenarios, Then every AC has at least one test scenario
   3. Given a UAT chain, When validating with sphinx-build, Then no warnings or errors
   4. Given untestable criteria, When detected, Then the Test Engineer reports testability concerns
   5. Given a generated UAT scenario, When read by a human tester, Then it contains all preconditions, steps, test data, and expected results sufficient to execute without consulting other artifacts
