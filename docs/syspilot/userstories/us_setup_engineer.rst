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

   **Soul:**
   The Setup agent SHALL be the stable, reliable entry point for syspilot
   installation — minimal by design, never changing on the customer system.
   It is transparent about what it does. It fetches and places exactly the files
   declared in the upstream bootstrap manifest, then delegates orchestration to
   the Installer.

   **Duties:**

   - Maintain the identity and discoverability of the single, stable syspilot
     entry point — users never need to know how syspilot evolves internally
   - Always execute current upstream installation logic — the locally installed
     version is never authoritative
   - Enforce version compatibility — protect the user from a faulty run when the
     upstream manifest signals incompatibility
   - Guarantee manifest fidelity — exactly the files declared in bootstrap.json
     are placed, no more and no less

   **Workflow (high-level):**
   Fetch upstream manifest → validate manifest version → fetch and install each
   file listed in manifest → invoke Installer as subagent with user context.

   **Additional Acceptance Criteria:**

   1. Given I invoke the Setup agent, When it completes successfully, Then my project has a working syspilot installation that passes sphinx-build
   2. Given any locally installed version, When I invoke Setup, Then I always get the behavior of the current upstream Installer — not the behavior of the version that was previously installed
   3. Given the upstream manifest signals an incompatible version, When Setup runs, Then it stops with a user-visible error rather than proceeding with an outdated Bootloader
   4. Given the Setup agent exists in my workspace, When I need to install or update syspilot, Then I can find and invoke exactly one entry point — without knowing any internal structure


.. note::

   The Installer Agent user story has been moved to its own file: :doc:`us_installer`.
   See ``SYSP_US_INSTALLER`` in that file.
