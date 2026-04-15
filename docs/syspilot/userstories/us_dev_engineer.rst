Dev Engineer Agent
==================


.. story:: Dev Engineer Agent
   :id: SYSP_US_IMPLEMENT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, implement, dev-engineer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a Dev Engineer agent (syspilot.implement) that implements
   code and configuration changes based on approved specifications,
   **so that** approved Design Specs are turned into working code with tests
   and documentation updates.

   **Context:**

   The Dev Engineer takes approved Change Documents and implements them. It reads
   the specifications, writes code, creates tests, updates user documentation, and
   commits with traceability. It does not modify specifications — that is the System
   Designer's job. It does not change spec statuses or versions.

   **Acceptance Criteria:**

   1. Given a Change Document, When the Dev Engineer reads it, Then it identifies all SPEC elements to implement
   2. Given a Design Spec, When implementing, Then the code matches the spec's acceptance criteria
   3. Given implementation is complete, When tests run, Then all tests pass
   4. Given code changes, When committing, Then the commit references the Change Document
