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
   The Setup Manager is responsible for:

   - the identity and discoverability of the single, stable entry point into syspilot — the user never needs to know how syspilot evolves internally
   - the currency of the executed installation logic against the upstream state — what is locally installed is not authoritative
   - the version compatibility between itself and upstream — on incompatibility, it protects the user from a faulty run
   - the manifest fidelity of the placed files — exactly the files from bootstrap.json are placed, no more and no less

   **Workflow (high-level):**
   Fetch upstream manifest → validate manifest version → fetch and install each
   file listed in manifest → invoke Installer as subagent with user context.

   **Additional Acceptance Criteria:**

   1. Given I invoke the Setup agent, When it completes successfully, Then my project has a working syspilot installation that passes sphinx-build
   2. Given any locally installed version, When I invoke Setup, Then I always get the behavior of the current upstream Installer — not the behavior of the version that was previously installed
   3. Given the upstream manifest signals an incompatible version, When Setup runs, Then it stops with a user-visible error rather than proceeding with an outdated Bootloader
   4. Given the Setup agent exists in my workspace, When I need to install or update syspilot, Then I can find and invoke exactly one entry point — without knowing any internal structure


.. story:: Installer Agent
   :id: SYSP_US_INSTALLER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer
   :links: SYSP_US_AGENT_ARCH, SYSP_US_SETUP

   **As a** syspilot user,
   **I want** an Installer agent that is invoked by the Setup Bootloader and
   performs all installation and update work for non-manifest files,
   **so that** I get a functioning, validated syspilot environment that always
   reflects the current upstream product state.

   **Soul:**
   The Installer SHALL be a thorough, methodical engineer — diligent and
   reliable. It never leaves a broken state. It validates every installation
   before reporting success. It is user-friendly in its reporting even though
   it is not directly invoked by the user.

   **Duties:**
   The Installer is responsible for:

   - the completeness and correctness of the installed syspilot components in the target project
   - the working state of the installation at the end of a run — nothing remains half-installed or unvalidated
   - the traceability of every installation — every run leaves a verifiable trace (Git commit)
   - the enforcement of mutual exclusion for skill groups — exactly one skill of each exclusive group is installed at a time

   **Workflow (high-level):**
   Determine install source and mode → verify dependencies → install or
   update all files from upstream → configure Sphinx →
   validate with sphinx-build → create baseline Git commit.

   **Additional Acceptance Criteria:**

   1. Given a fresh project, When the Installer runs, Then all syspilot product files are correctly placed and the project builds cleanly
   2. Given any installation, When the Installer completes, Then a Git commit documents exactly what was changed
   3. Given a Skill that belongs to an exclusive group is being installed, When a Skill from the same exclusive group is already installed, Then the Installer SHALL remove the previously installed Skill and install the new one — enforcing mutual exclusion through replacement, not rejection
   4. Given any installation, When the Installer copies product files, Then only ``agents/``, ``prompts/``, ``skills/``, ``templates/`` from ``syspilot/`` are copied — syspilot-internal sources (``docs/syspilot/``, ``docs/changes/``) are never copied to user projects
   5. Given a fresh project with no ``docs/index.rst``, When the Installer runs, Then a minimal starter ``index.rst`` is created; given a project that already has a ``docs/index.rst``, it is never overwritten
   6. Given a file exists in ``.github/templates/`` but no longer exists in ``syspilot/templates/``, When the Installer runs, Then the orphan file is removed from ``.github/templates/``
   7. Given any install or update, When the Installer completes the template sync, Then the run summary reports the count of templates installed, updated, and removed
   8. Given a session-messaging infrastructure is present in the workspace, When the Installer runs, Then it defaults to installing the session-based orchestration variant; otherwise it defaults to the synchronous fallback variant — and the user may override the default via an explicit prompt
   9. Given the session-based orchestration variant is selected, When the Installer completes, Then every installed agent (except the bootstrap layer) is reachable as a named session without any manual configuration
   10. Given a session scaffold already exists for an agent, When the Installer runs an update, Then the existing scaffold and the agent's accumulated context are left untouched; missing scaffolds are created
   11. Given a file in ``.github/agents/``, ``.github/prompts/``, or ``.github/skills/`` that does NOT have the ``syspilot.`` filename prefix, OR that has the ``syspilot.`` prefix but ends with ``.tailoring.md``, When the Installer runs orphan cleanup, Then that file is left untouched and remains unmodified — only files that start with ``syspilot.`` and do not end with ``.tailoring.md`` are eligible for orphan removal
