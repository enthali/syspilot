Test Engineer Agent
===================


.. story:: Test Engineer Agent
   :id: SYSP_US_UAT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, uat, test-engineer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a Test Engineer agent (syspilot.uat) that generates
   User Acceptance Test artifacts from approved changes,
   **so that** every feature has concrete, manually executable test scenarios
   with full traceability from test story to test data to expected outcomes.

   **Context:**

   The Test Engineer translates feature specifications into UAT traceability
   chains. For each feature user story, it generates a test story (scenarios),
   a test data requirement, and an expected outcomes spec. It cares about
   testability — if something cannot be meaningfully tested, it says so.

   **Acceptance Criteria:**

   1. Given a Change Document, When the Test Engineer processes it, Then it generates one UAT chain per feature US
   2. Given acceptance criteria, When mapping to scenarios, Then every AC has at least one test scenario
   3. Given a UAT chain, When validating with sphinx-build, Then no warnings or errors
   4. Given untestable criteria, When detected, Then the Test Engineer reports testability concerns
