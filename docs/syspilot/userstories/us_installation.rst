Installation & Setup User Stories
==================================

Stories covering bootstrap, portability, installation, adoption, and updates.

**Last Updated**: 2026-03-16


.. story:: Automatic Environment Bootstrap
   :id: SYSPILOT_US_INST_BOOTSTRAP
   :status: implemented
   :priority: high
   :tags: init, automation
   :links: SYSPILOT_US_CORE_SPEC_AS_CODE

   **As a** developer (or cloud agent),
   **I want to** have the sphinx-needs environment auto-initialize,
   **so that** I can start working without manual setup.

   **Acceptance Scenarios:**

   1. Given fresh checkout with no sphinx-needs, When I curl the setup agent and invoke it, Then the agent detects the absence and asks whether to install or use a custom mechanism
   2. Given agent runs in cloud, When it needs sphinx, Then setup runs automatically
   3. Given setup completes, When I build docs, Then sphinx-build works
   4. Given sphinx-needs is already available (e.g. via virtual env or custom scripts), When I invoke the setup agent, Then the agent detects this and skips the installation step


.. story:: Use syspilot Across Projects
   :id: SYSPILOT_US_INST_CROSS_PROJECT
   :status: implemented
   :priority: medium
   :tags: portability, sync
   :links: SYSPILOT_US_INST_NEW_PROJECT, SYSPILOT_US_INST_ADOPT_EXISTING

   **As a** developer,
   **I want to** use syspilot in multiple projects,
   **so that** I have consistent requirements engineering everywhere.

   **Acceptance Scenarios:**

   1. Given syspilot is released, When I sync to new project, Then agents work
   2. Given syspilot is updated, When I sync again, Then I get new version
   3. Given project-specific config, When I sync, Then my config is preserved


.. story:: Install syspilot in New Project
   :id: SYSPILOT_US_INST_NEW_PROJECT
   :status: implemented
   :priority: mandatory
   :tags: install, distribution
   :links: SYSPILOT_US_INST_BOOTSTRAP, SYSPILOT_US_DOC_MAINTAIN

   **As a** developer starting a new project,
   **I want to** install syspilot from the beginning,
   **so that** I have requirements engineering built-in from day one.

   **Acceptance Scenarios:**

   1. Given the setup agent is available in .github/agents/, When I invoke @syspilot.setup, Then syspilot structure is created without requiring manual path configuration
   2. Given the setup agent is available, When I invoke @syspilot.setup, Then the agent fetches all files from GitHub main
   3. Given installation completes, When I check, Then I'm ready to run bootstrap
   4. Given I need a specific version, When I install, Then I can obtain that version
   5. Given the syspilot/ directory exists locally, When I invoke @syspilot.setup, Then the agent offers me a choice between local copy and GitHub fetch
   6. Given installation completes successfully, When the Setup Agent finishes,
      Then it stages all newly created files and commits them with a descriptive
      message (e.g. "chore: initial syspilot setup v{version}") so I have a
      clean git baseline


.. story:: Adopt syspilot in Existing Project
   :id: SYSPILOT_US_INST_ADOPT_EXISTING
   :status: implemented
   :priority: mandatory
   :tags: install, adoption, distribution
   :links: SYSPILOT_US_INST_BOOTSTRAP, SYSPILOT_US_DOC_MAINTAIN

   **As a** developer with an existing project,
   **I want to** adopt syspilot without disrupting my current work,
   **so that** I can add requirements engineering to a project already in progress.

   **Acceptance Scenarios:**

   1. Given I have an existing project with code, When I follow the adoption process, Then syspilot is added alongside existing files
   2. Given I have existing documentation, When I adopt syspilot, Then my existing docs are not overwritten
   3. Given adoption completes, When I check, Then I can start creating User Stories
   4. Given the setup agent is available, When I start adoption, Then the agent fetches files from GitHub main and merges with existing content
   5. Given the syspilot/ directory exists locally, When I invoke @syspilot.setup, Then the agent offers me a choice between local copy and GitHub fetch
   6. Given adoption completes successfully, When the Setup Agent finishes,
      Then it stages and commits all added syspilot files with a descriptive
      message, handling any pre-existing uncommitted changes gracefully


.. story:: Update syspilot to Latest Version
   :id: SYSPILOT_US_INST_UPDATE
   :status: implemented
   :priority: mandatory
   :tags: update, migration, distribution
   :links: SYSPILOT_US_INST_NEW_PROJECT, SYSPILOT_US_INST_ADOPT_EXISTING

   **As a** developer using syspilot,
   **I want to** update to the latest version,
   **so that** I benefit from new features, fixes, and improvements.

   **Acceptance Scenarios:**

   1. Given syspilot is installed, When a new version is available, Then I can update
      by invoking @syspilot.setup
   2. Given I update syspilot, When the update completes, Then methodology agents
      (change, verify, mece, trace, memory) are replaced with the latest version
   3. Given the syspilot/ directory exists locally, When I update, Then the agent
      offers me a choice between local copy and GitHub fetch
      and project-specific agents (release, implement) are never modified
   4. Given a breaking change exists, When I update, Then I receive migration guidance
   5. Given I update, When I check, Then I can see which version I now have
   6. Given the setup agent is outdated, When I invoke @syspilot.setup, Then the setup
      agent updates itself first before updating other files
   7. Given I update syspilot, When a methodology-owned file I modified contained
      content not present in the new version, Then I am warned and can review
      the differences before deciding to accept or merge back my additions
   8. Given I update syspilot, When the update starts, Then the setup agent
      creates a dedicated branch and a change document summarizing what was
      updated, so that changes are reviewable and traceable


.. story:: Language-Agnostic Implementation Agent
   :id: SYSPILOT_US_INST_AGNOSTIC
   :status: implemented
   :priority: mandatory
   :tags: install, portability, distribution
   :links: SYSPILOT_US_INST_CROSS_PROJECT, SYSPILOT_US_CHG_IMPLEMENT

   **As a** developer using any programming language or build system,
   **I want to** receive a language-agnostic implement agent when installing syspilot,
   **so that** I can customize it for my tech stack instead of having to strip out
   Python-specific examples that don't apply to my project.

   **Acceptance Scenarios:**

   1. Given I install syspilot into any project, When setup completes, Then the
      implement agent contains no language-specific build/test commands
   2. Given I read the installed implement agent, When I look for customization
      points, Then I see clear TODO placeholders for build command, test command,
      and language-specific patterns
   3. Given I customize the implement agent for my stack, When syspilot updates,
      Then the implement agent is never modified by the update process
   4. Given the implement agent is a skeleton, When I follow the workflow structure,
      Then Change → Implement → Verify still works end-to-end
   5. Given I install syspilot, When I see the implement and release agents,
      Then they contain a reminder to customize via @syspilot.change


Traceability
------------

.. needtable::
   :columns: id, title, status, priority
   :filter: id.startswith('SYSPILOT_US_INST')
