Installation & Setup User Stories
==================================

Stories covering bootstrap, portability, installation, adoption, and updates.

**Last Updated**: 2026-02-06


.. story:: Automatic Environment Bootstrap
   :id: US_INST_BOOTSTRAP
   :status: implemented
   :priority: high
   :tags: init, automation

   **As a** developer (or cloud agent),
   **I want to** have the sphinx-needs environment auto-initialize,
   **so that** I can start working without manual setup.

   **Acceptance Scenarios:**

   1. Given fresh checkout, When I run init script, Then dependencies are installed
   2. Given agent runs in cloud, When it needs sphinx, Then init runs automatically
   3. Given init completes, When I build docs, Then sphinx-build works


.. story:: Use syspilot Across Projects
   :id: US_INST_CROSS_PROJECT
   :status: implemented
   :priority: medium
   :tags: portability, sync
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING

   **As a** developer,
   **I want to** use syspilot in multiple projects,
   **so that** I have consistent requirements engineering everywhere.

   **Acceptance Scenarios:**

   1. Given syspilot is released, When I sync to new project, Then agents work
   2. Given syspilot is updated, When I sync again, Then I get new version
   3. Given project-specific config, When I sync, Then my config is preserved


.. story:: Install syspilot in New Project
   :id: US_INST_NEW_PROJECT
   :status: implemented
   :priority: mandatory
   :tags: install, distribution
   :links: US_INST_BOOTSTRAP

   **As a** developer starting a new project,
   **I want to** install syspilot from the beginning,
   **so that** I have requirements engineering built-in from day one.

   **Acceptance Scenarios:**

   1. Given the setup agent is available in .github/agents/, When I invoke @syspilot.setup, Then syspilot structure is created without requiring manual path configuration
   2. Given syspilot is not found in the project directory, When I invoke @syspilot.setup, Then the agent offers to download the latest version from GitHub
   3. Given installation completes, When I check, Then I'm ready to run bootstrap
   4. Given I need a specific version, When I install, Then I can obtain that version


.. story:: Adopt syspilot in Existing Project
   :id: US_INST_ADOPT_EXISTING
   :status: implemented
   :priority: mandatory
   :tags: install, adoption, distribution
   :links: US_INST_BOOTSTRAP

   **As a** developer with an existing project,
   **I want to** adopt syspilot without disrupting my current work,
   **so that** I can add requirements engineering to a project already in progress.

   **Acceptance Scenarios:**

   1. Given I have an existing project with code, When I follow the adoption process, Then syspilot is added alongside existing files
   2. Given I have existing documentation, When I adopt syspilot, Then my existing docs are not overwritten
   3. Given adoption completes, When I check, Then I can start creating User Stories
   4. Given syspilot is not found in the project directory, When I start adoption, Then the agent offers to download the latest version from GitHub


.. story:: Update syspilot to Latest Version
   :id: US_INST_UPDATE
   :status: implemented
   :priority: mandatory
   :tags: update, migration, distribution
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING

   **As a** developer using syspilot,
   **I want to** update to the latest version,
   **so that** I benefit from new features, fixes, and improvements.

   **Acceptance Scenarios:**

   1. Given syspilot is installed, When a new version is available, Then I can update by following the update process
   2. Given I update syspilot, When the update completes, Then my project-specific customizations are preserved
   3. Given a breaking change exists, When I update, Then I receive migration guidance
   4. Given I update, When I check, Then I can see which version I now have


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('US_INST')
