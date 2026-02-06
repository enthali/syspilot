Change Management User Stories
===============================

Stories covering the full change lifecycle: analyze, implement, verify, recover.

**Last Updated**: 2026-02-06


.. story:: Analyze Changes Before Implementation
   :id: US_CHG_ANALYZE
   :status: implemented
   :priority: mandatory
   :tags: agent, change
   :links: US_CORE_SPEC_AS_CODE

   **As a** developer,
   **I want to** have an agent analyze my change request against existing User Stories, Requirements, and Specs,
   **so that** I understand the full impact before coding.

   **Acceptance Scenarios:**

   1. Given I describe a feature, When I invoke change agent, Then I get a Change Proposal
   2. Given the proposal lists US/REQ/SPEC changes, When I review, Then I see affected areas
   3. Given conflicting requirements exist, When agent analyzes, Then it flags them and discusses resolution


.. story:: Implement with Full Traceability
   :id: US_CHG_IMPLEMENT
   :status: implemented
   :priority: mandatory
   :tags: agent, implementation
   :links: US_CHG_ANALYZE

   **As a** developer,
   **I want to** have an agent implement changes with automatic traceability,
   **so that** I don't have to manually link docs, code, and tests.

   **Acceptance Scenarios:**

   1. Given an approved Change Proposal, When implement agent runs, Then docs are updated first
   2. Given code is written, When I check, Then it references SPEC IDs
   3. Given tests are written, When I check, Then they reference REQ IDs


.. story:: Verify Implementation Completeness
   :id: US_CHG_VERIFY
   :status: implemented
   :priority: mandatory
   :tags: agent, verification
   :links: US_CHG_ANALYZE, US_CHG_IMPLEMENT

   **As a** developer,
   **I want to** verify that implementation matches the change proposal,
   **so that** I don't miss requirements or acceptance criteria.

   **Acceptance Scenarios:**

   1. Given implementation is done, When verify agent runs, Then it checks all ACs
   2. Given a requirement has no test, When agent verifies, Then it reports gap
   3. Given all checks pass, When agent finishes, Then I get PASS report


.. story:: Recover from Agent Failures
   :id: US_CHG_RECOVERY
   :status: implemented
   :priority: medium
   :tags: agent, recovery, error-handling

   **As a** developer,
   **I want to** recover gracefully when an agent fails mid-operation,
   **so that** I don't end up with inconsistent state between docs and code.

   **Acceptance Scenarios:**

   1. Given agent fails during doc update, When I check, Then partial changes are rolled back
   2. Given agent fails during code generation, When I retry, Then it picks up where it left off
   3. Given unrecoverable error, When agent stops, Then it reports what was completed


.. story:: Iterative Level-Based Change Analysis
   :id: US_CHG_ITERATIVE
   :status: implemented
   :priority: mandatory
   :tags: agent, change, iterative
   :links: US_CHG_ANALYZE

   **As a** developer,
   **I want to** have the change agent work iteratively through specification levels
   (User Story → Requirements → Design) with a persistent change document,
   **so that** large projects don't overflow context and I have a complete change history.

   **Acceptance Scenarios:**

   1. Given I start a change, When agent works on US level, Then it shows impacted User Stories
   2. Given US level complete, When I confirm, Then we proceed to REQ level
   3. Given I'm at REQ level, When links are followed, Then impacted REQs are found automatically
   4. Given I'm at DESIGN level, When implementation isn't feasible, Then I can go back to REQ
   5. Given all levels complete, When agent finishes, Then Change Document has full history
   6. Given Change is merged, When cleanup runs, Then Change Document is deleted (preserved in Git)


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('US_CHG')
