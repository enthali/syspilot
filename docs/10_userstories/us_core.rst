Core User Stories
=================

Foundation stories that define the syspilot methodology.

**Last Updated**: 2026-02-06


.. story:: Manage Specifications as Code
   :id: US_CORE_SPEC_AS_CODE
   :status: implemented
   :priority: mandatory
   :tags: core, sphinx-needs

   **As a** developer,
   **I want to** manage User Stories, Requirements, and Specs in version-controlled RST files,
   **so that** I can branch, merge, review, and track the full specification hierarchy like code.

   **Specification Hierarchy:**

   ::

      ┌─────────────────────────────────────────────────────────────┐
      │  Level 0: User Stories (WHY)                                │
      │  "As a user, I want X so that Y"                            │
      └──────────────────────┬──────────────────────────────────────┘
                             │ derives
                             ▼
      ┌─────────────────────────────────────────────────────────────┐
      │  Level 1: Requirements (WHAT)                               │
      │  "System SHALL do X" + Acceptance Criteria                  │
      └──────────────────────┬──────────────────────────────────────┘
                             │ implements
                             ▼
      ┌─────────────────────────────────────────────────────────────┐
      │  Level 2: Design/Specs (HOW)                                │
      │  Technical design, architecture, interfaces                 │
      └─────────────────────────────────────────────────────────────┘

   **Acceptance Scenarios:**

   1. Given I write a User Story, When I commit, Then it's in Git history
   2. Given I derive a Requirement from a US, When I link them, Then traceability is preserved
   3. Given I modify any spec level, When I diff, Then I see what changed
   4. Given I branch for a feature, When I merge, Then all spec levels merge together


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('US_CORE')
