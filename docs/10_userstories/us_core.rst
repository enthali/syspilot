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


.. story:: Consistent File Organization Across Specification Levels
   :id: US_CORE_FILE_ORG
   :status: implemented
   :priority: high
   :tags: core, methodology, organization
   :links: US_CORE_SPEC_AS_CODE

   **As a** developer (or AI agent),
   **I want to** have a well-defined methodology for organizing specification files
   across levels (User Stories, Requirements, Design),
   **so that** I can find, navigate, maintain, and scale specifications consistently
   as the project grows.

   **Acceptance Scenarios:**

   1. Given I need to add a new user story, When I check the methodology, Then I know
      which file to put it in (or when to create a new one)
   2. Given I create a new requirement, When I follow the conventions, Then I know it
      belongs in the file that mirrors the corresponding US file
   3. Given I write a design spec, When I organize by component, Then it can link to
      REQs from multiple US themes without artificial file splits
   4. Given the project grows beyond 50 user stories, When I follow the scaling guidelines,
      Then the file structure remains navigable and reviewable


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('US_CORE')
