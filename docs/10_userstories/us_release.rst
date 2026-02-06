Release User Stories
====================

Stories covering release creation, validation, and automation.

**Last Updated**: 2026-02-06


.. story:: Create syspilot Release
   :id: US_REL_CREATE
   :status: implemented
   :priority: mandatory
   :tags: release, distribution
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING, US_INST_UPDATE

   **As a** syspilot maintainer,
   **I want to** create official releases with version numbers,
   **so that** users can install stable, tested versions of syspilot.

   **Acceptance Scenarios:**

   1. Given I'm ready to release, When I follow the release process, Then a versioned release is created
   2. Given release is created, When users check for updates, Then they can see the new version
   3. Given version is released, When I check Git, Then I see a version tag
   4. Given release artifacts exist, When users download, Then they get complete syspilot installation


.. story:: Validate Release Quality
   :id: US_REL_VALIDATE
   :status: implemented
   :priority: mandatory
   :tags: release, quality, testing
   :links: US_REL_CREATE

   **As a** syspilot maintainer,
   **I want to** validate release quality before distribution,
   **so that** users receive stable, working releases.

   **Acceptance Scenarios:**

   1. Given I prepare a release, When I run validation, Then all agents are tested
   2. Given validation passes, When I check docs, Then self-documentation builds successfully
   3. Given validation fails, When I review, Then I see which tests failed
   4. Given all checks pass, When I approve, Then release is ready for distribution


.. story:: Release Agent Template
   :id: US_REL_AGENT_TEMPLATE
   :status: implemented
   :priority: medium
   :tags: release, agent, template
   :links: US_REL_CREATE, US_REL_VALIDATE

   **As a** syspilot user,
   **I want to** see how a release agent could work,
   **so that** I can create my own release automation for my projects.

   **Acceptance Scenarios:**

   1. Given I read release documentation, When I see the release agent concept, Then I understand how it could automate releases
   2. Given I want my own release process, When I check syspilot, Then I can use it as a template
   3. Given installation/update agent handles modified agents, When I create custom release agent, Then update process respects my changes


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('US_REL')
