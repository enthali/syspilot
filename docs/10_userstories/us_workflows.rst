Workflow User Stories
=====================

Stories describing the end-to-end workflows that orchestrate syspilot agents.

**Last Updated**: 2026-02-06


.. story:: End-to-End Change Workflow
   :id: US_WF_CHANGE
   :status: implemented
   :priority: mandatory
   :tags: core, workflow, agents
   :links: US_CORE_SPEC_AS_CODE, US_CHG_ANALYZE, US_CHG_IMPLEMENT, US_CHG_VERIFY, US_CHG_ITERATIVE, US_DX_PROJECT_MEMORY

   **As a** developer,
   **I want to** follow a defined workflow (Change → Implement → Verify → Memory)
   to evolve my specifications and code,
   **so that** every change is analyzed, implemented with traceability, verified,
   and captured in project memory.

   **Acceptance Scenarios:**

   1. Given I have a change request, When I start the workflow, Then I know to
      invoke @change first
   2. Given @change produces an approved Change Document, When I proceed, Then
      I invoke @implement with the Change Document as input
   3. Given @implement completes, When I proceed, Then I invoke @verify to check
      completeness
   4. Given @verify passes, When I proceed, Then I invoke @memory to update
      project context
   5. Given any step fails, When I check the workflow, Then I know which step
      to revisit
   6. Given @memory completes, When I decide next steps, Then I can either
      start a new change workflow (@change) or proceed to release (@release)


.. story:: Independent Quality Checks
   :id: US_WF_QUALITY
   :status: implemented
   :priority: high
   :tags: core, workflow, quality
   :links: US_CORE_SPEC_AS_CODE, US_TRACE_MECE, US_TRACE_VERTICAL

   **As a** developer,
   **I want to** run independent consistency checks on my specifications
   at any time (horizontal MECE review, vertical traceability),
   **so that** I can validate specification quality outside of a change workflow.

   **Acceptance Scenarios:**

   1. Given I want to check one level for consistency, When I invoke @mece,
      Then I get a horizontal MECE report without needing a Change Document
   2. Given I want to trace one element through all levels, When I invoke @trace,
      Then I get a vertical coverage report
   3. Given I find issues in a quality check, When I want to fix them, Then I can
      start a change workflow to address the findings


.. story:: Release Workflow
   :id: US_WF_RELEASE
   :status: implemented
   :priority: mandatory
   :tags: core, workflow, release
   :links: US_CORE_SPEC_AS_CODE, US_REL_CREATE, US_REL_VALIDATE

   **As a** syspilot maintainer,
   **I want to** follow a defined release workflow that bundles multiple changes
   into a versioned release (Version → Validate → Publish),
   **so that** I can release stable, tested versions covering multiple changes.

   **Acceptance Scenarios:**

   1. Given multiple changes are merged, When I start a release, Then all changes
      are bundled into one versioned release
   2. Given I follow the release workflow, When validation passes, Then the release
      is ready for distribution
   3. Given a release is published, When users update, Then they get all bundled
      changes together
   4. Given a release is complete, When I want to continue development, Then I
      can start a new change workflow (@change)


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('US_WF')
