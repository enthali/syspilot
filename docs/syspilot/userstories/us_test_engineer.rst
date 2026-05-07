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
   Der Test Engineer ist verantwortlich für:

   * die Test-Coverage jedes Features — keine User Story bleibt ohne UAT-Chain
   * die Manuelle Ausführbarkeit der UAT-Szenarien — jedes Test-Szenario kann von einem Menschen ohne weitere Annahmen durchgespielt werden
   * die Sichtbarkeit von Untestbarkeit — wenn ein AC nicht meaningfully testbar ist, ist das im Output ausgewiesen, nicht verschwiegen
   * die Traceability zwischen Feature, Test-Story, Test-Daten und Expected Outcomes — keine offene Test-Spur, kein Test ohne Anker

   **Workflow (high-level):**
   Read Change Document → identify feature USes → generate UAT chain per US →
   validate with sphinx-build → report results.

   **Acceptance Criteria:**

   1. Given a Change Document, When the Test Engineer processes it, Then it generates one UAT chain per feature US
   2. Given acceptance criteria, When mapping to scenarios, Then every AC has at least one test scenario
   3. Given a UAT chain, When validating with sphinx-build, Then no warnings or errors
   4. Given untestable criteria, When detected, Then the Test Engineer reports testability concerns
   5. Given a generated UAT scenario, When read by a human tester, Then it contains all preconditions, steps, test data, and expected results sufficient to execute without consulting other artifacts
