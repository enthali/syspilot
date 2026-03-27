Release User Stories
====================

Stories covering release creation, validation, and automation.

**Last Updated**: 2026-02-06


.. story:: Create syspilot Release
   :id: SYSPILOT_US_REL_CREATE
   :status: implemented
   :priority: mandatory
   :tags: release, distribution
   :links: SYSPILOT_US_INST_NEW_PROJECT, SYSPILOT_US_INST_ADOPT_EXISTING, SYSPILOT_US_INST_UPDATE

   **As a** syspilot maintainer,
   **I want to** create official releases with version numbers,
   **so that** users can install stable, tested versions of syspilot.

   **Acceptance Scenarios:**

   1. Given I'm ready to release, When I follow the release process, Then a versioned release is created
   2. Given release is created, When users check for updates, Then they can see the new version
   3. Given version is released, When I check Git, Then I see a version tag
   4. Given release artifacts exist, When users download, Then they get complete syspilot installation


.. story:: Validate Release Quality
   :id: SYSPILOT_US_REL_VALIDATE
   :status: implemented
   :priority: mandatory
   :tags: release, quality, testing
   :links: SYSPILOT_US_REL_CREATE

   **As a** syspilot maintainer,
   **I want to** validate release quality before distribution,
   **so that** users receive stable, working releases.

   **Acceptance Scenarios:**

   1. Given I prepare a release, When I run validation, Then all agents are tested
   2. Given validation passes, When I check docs, Then self-documentation builds successfully
   3. Given validation fails, When I review, Then I see which tests failed
   4. Given all checks pass, When I approve, Then release is ready for distribution


.. story:: Release Agent for Consumer Projects
   :id: SYSPILOT_US_REL_AGENT_TEMPLATE
   :status: implemented
   :priority: medium
   :tags: release, agent, template
   :links: SYSPILOT_US_REL_CREATE, SYSPILOT_US_REL_VALIDATE

   **As a** syspilot user,
   **I want** a release agent that knows how to release and only documents
   my project-specific decisions (version file, change doc policy, validations),
   **so that** I get a short, maintainable agent instead of a verbose playbook.

   **Acceptance Scenarios:**

   1. Given I install syspilot, When I first invoke @syspilot.release, Then it bootstraps release decisions by asking me project-specific questions and saves them in the agent file
   2. Given release decisions exist in the agent file, When I invoke @syspilot.release, Then it performs a standard release using those decisions without prescribing every step
   3. Given the agent encounters a project without archived change docs, When releasing, Then change documents are archived (not deleted)
   4. Given I want to customize my release process, When I edit the agent file decisions section, Then the agent respects my overrides


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('SYSPILOT_US_REL')
