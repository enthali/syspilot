Setup Manager Agent
===================


.. story:: Setup Manager Agent
   :id: SYSP_US_SETUP
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** a Setup Manager agent (syspilot.setup) that installs
   and updates syspilot in my project,
   **so that** I can bootstrap a new syspilot project or update an existing
   one with minimal manual effort.

   **Context:**

   The Setup Manager is user-invocable and manages installation infrastructure.
   It detects the install source (local or GitHub), determines the mode
   (fresh install or update), copies files, configures the project, validates
   the setup with sphinx-build, and creates a baseline commit.

   **Acceptance Criteria:**

   1. Given a new project, When Setup runs, Then it installs all syspilot files and validates with sphinx-build
   2. Given an existing project, When Setup detects it, Then it offers update mode
   3. Given a local syspilot directory, When detected, Then Setup offers local vs. GitHub install source
   4. Given successful setup, When complete, Then Setup creates a baseline Git commit
