Installer Agent
===============


.. story:: Installer Agent
   :id: SYSP_US_INSTALLER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer
   :links: SYSP_US_AGENT_ARCH, SYSP_US_SETUP

   **As a** syspilot user,
   **I want** an Installer agent that is invoked by the Setup Bootloader and
   performs all installation and update work for non-manifest files,
   **so that** I get a functioning, validated syspilot environment without
   losing my local customizations during updates.

   **Soul:**
   The Installer SHALL be a thorough, methodical engineer — diligent and
   reliable. It never leaves a broken state. It validates every installation
   before reporting success. It is user-friendly in its reporting even though
   it is not directly invoked by the user.

   **Duties:**

   - Keep all syspilot product components in the target project complete and
     correct after every successful run
   - Preserve local user customizations across updates
   - Ensure the installation is functional (passes sphinx-build) before
     reporting success — never leave a half-installed state
   - Leave a traceable Git commit after every successful installation
   - Reject installation of mutually exclusive Skills and report the conflict

   **Workflow (high-level):**
   Determine install source and mode → verify dependencies → install or
   update all files (preserving user customizations) → configure Sphinx →
   validate with sphinx-build → create baseline Git commit.

   **Acceptance Criteria:**

   1. Given a fresh project, When the Installer runs, Then all syspilot product
      files are correctly placed and the project builds cleanly
   2. Given an update, When the Installer runs, Then my ``tools:`` customizations
      in agent files survive the update
   3. Given any installation, When the Installer completes, Then a Git commit
      documents exactly what was changed
   4. Given a Skill that belongs to an exclusive group is being installed, When
      a Skill from the same exclusive group is already installed, Then the
      Installer SHALL reject the installation and report the conflict
