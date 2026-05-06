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

   ``syspilot.setup`` is the user-invocable entry point (Bootloader) that always
   fetches the current Installer from upstream and delegates all installation work
   to it. The Installer performs environment detection, file copy, configuration,
   sphinx-build validation, and baseline commit.

   **Acceptance Criteria:**

   1. Given a new project, When Setup runs, Then it installs all syspilot files and validates with sphinx-build
   2. Given an existing project, When Setup detects it, Then it offers update mode
   3. Given a local syspilot directory, When detected, Then Setup offers local vs. GitHub install source
   4. Given successful setup, When complete, Then Setup creates a baseline Git commit
   5. Given an update is about to overwrite installed files, When Setup runs, Then it asks the user whether they have made customizations and, if yes, gathers what was customized and reminds the user to re-apply their customizations after the update
   6. Given the installed version equals the source version, When Setup runs, Then it asks the user whether to reinstall anyway before proceeding, and aborts gracefully if the user declines
   7. Given an update overwrites agent files, When Setup completes, Then it SHALL automatically preserve the existing ``tools:`` frontmatter in each updated agent, copy new agents completely (including ``tools:``), and inform the user which agents were updated and that their ``tools:`` were preserved
   8. Given a Skill with a ``group:`` field is being installed, When a Skill of the same group is already installed, Then the Setup Agent SHALL reject the installation and report the conflict (Mutual Exclusion enforcement)


.. story:: Bootstrap Always-Current Installer
   :id: SYSP_US_INST_BOOTSTRAP
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootstrap
   :links: SYSP_US_SETUP

   **As a** syspilot developer,
   **I want** the Setup Agent to always use the current Installer from upstream,
   **so that** every installation run benefits from the latest installer version
   regardless of which version was previously installed locally.

   **Context:**

   Today the old version installs the new version of itself — every improvement
   inherits the risk and bugs of the predecessor version. The Bootloader breaks
   this cycle by always fetching the latest Installer from the upstream repository
   before executing it.

   **Acceptance Criteria:**

   1. Given any installed version, When Setup runs, Then Bootloader fetches the Installer from the upstream main branch
   2. Given a fetched Installer, When bootstrap_version in manifest exceeds supported version, Then Bootloader stops with a user-visible error
   3. Given a valid Installer, When fetched, Then Bootloader invokes it as a subagent
