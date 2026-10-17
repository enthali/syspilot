Installed Setup Update Entry Point
==================================


.. story:: Installed Setup Update Entry Point
   :id: SYSP_US_SETUP
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, setup
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** an installed Setup entry point (syspilot.setup) that updates
   syspilot in my project,
   **so that** I can refresh an existing installation with minimal manual
   effort after the remote runtime performs initial installation.

   **Soul:**
   The Setup agent SHALL be the stable, reliable entry point for syspilot
   updates after the remote deterministic runtime performs initial
   installation. It is transparent about what it does and directly invokes
   the installed deterministic runtime; it does not bootstrap or delegate
   installation through another agent.

   **Duties:**
   The Setup Manager is responsible for:

   - the identity and discoverability of the primary user-facing update entry point
   - direct invocation of ``.syspilot/installer.py`` through ``uv run --no-project``
   - propagation of the selected repository, branch, target root, and harness
   - preservation of the deterministic runtime's validation and rollback outcome

   **Workflow (high-level):**
   Resolve repository/branch/harness → invoke the installed deterministic
   runtime directly → report its validated result.

   **Additional Acceptance Criteria:**

   1. Given I invoke the Setup agent, When it completes successfully, Then my project has a working syspilot installation that passes sphinx-build
   2. Given any locally installed version, When I invoke Setup, Then the
      runtime refreshes itself and all selected-harness content from the
      selected upstream revision
   3. Given Setup invokes an install or update, When it transfers control,
      Then it executes the deterministic runtime command directly and never
      uses Agent, Task, ``runSubagent``, or another nested-agent mechanism
   4. Given the Setup agent exists in my workspace, When I need to install or update syspilot, Then I can find and invoke exactly one entry point — without knowing any internal structure
   5. Given I invoke Setup from a supported non-VS Code harness (see ``SYSP_US_HARNESS_INSTALL``), When it completes, Then it uses that harness's own native entry-point mechanism to expose itself — I never need to hand-edit personal or global configuration to discover or run Setup
   6. Given syspilot is absent from a project, When initial installation is
      required, Then the remote deterministic runtime owns that operation and
      no Setup, bootstrap, Installer-agent, or Jarvis actor flow is required


.. story:: Installer Agent
   :id: SYSP_US_INSTALLER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, installer
   :links: SYSP_US_AGENT_ARCH, SYSP_US_SETUP

   **As a** syspilot user,
   **I want** a deterministic Installer runtime that performs all installation
   and update work, with an optional internal Installer agent as documentation,
   **so that** I get a functioning, validated syspilot environment that always
   reflects the current upstream product state.

   **Soul:**
   The Installer SHALL be a thorough, methodical engineer — diligent and
   reliable. It never leaves a broken state. It validates every installation
   before reporting success. The runtime, not an agent delegation chain, owns
   installation control flow.

   **Duties:**
   The Installer is responsible for:

   - the completeness and correctness of the installed syspilot components in the target project
   - the working state of the installation at the end of a run — nothing remains half-installed or unvalidated
   - the traceability of every installation — every run leaves a verifiable trace (Git commit)
   - the enforcement of mutual exclusion for skill groups — exactly one skill of each exclusive group is installed at a time

   **Workflow (high-level):**
   Determine install source and mode → verify dependencies → install or
   update the selected harness plus shared runtime and documentation from
   upstream → configure Sphinx →
   validate with sphinx-build → create baseline Git commit.

   **Additional Acceptance Criteria:**

   1. Given a fresh project, When the Installer runs, Then all syspilot product files are correctly placed and the project builds cleanly
   2. Given any installation, When the Installer completes, Then a Git commit documents exactly what was changed
   3. Given a Skill that belongs to an exclusive group is being installed, When a Skill from the same exclusive group is already installed, Then the Installer SHALL remove the previously installed Skill and install the new one — enforcing mutual exclusion through replacement, not rejection
   4. Given any installation, When the Installer copies product files, Then only ``agents/``, ``prompts/``, ``skills/``, ``templates/`` from ``syspilot/`` are copied — syspilot-internal sources (``docs/syspilot/``, ``docs/changes/``) are never copied to user projects
   5. Given a fresh project with no ``docs/index.rst``, When the Installer runs, Then a minimal starter ``index.rst`` is created; given a project that already has a ``docs/index.rst``, it is never overwritten
   6. Given a legacy template exists in the explicitly selected harness tree,
      or an obsolete shared template exists in ``.syspilot/templates/``, When
      the Installer migrates templates, Then it removes only eligible legacy
      artifacts covered by the frozen selected-harness/shared-resource plan,
      installs the current shared template under ``.syspilot/templates/``, and
      leaves every unselected harness tree unchanged
   7. Given any install or update, When the Installer completes the template sync, Then the run summary reports the count of templates installed, updated, and removed
   8. Given any harness installation, When orchestration support is installed,
      Then the deterministic runtime selects the synchronous orchestration
      variant without Jarvis detection or user choice
   9. Given any install or update, When the runtime executes, Then it does not
      create actors or session scaffolds and does not invoke Setup or an
      Installer agent as part of installation control flow
   10. Given pre-existing user-owned session or actor state, When the runtime
       installs or updates syspilot, Then that state remains untouched
   11. Given a file in ``.github/agents/``, ``.github/prompts/``, or ``.github/skills/`` that does NOT have the ``syspilot.`` filename prefix, OR that has the ``syspilot.`` prefix but ends with ``.tailoring.md``, When the Installer runs orphan cleanup, Then that file is left untouched and remains unmodified — only files that start with ``syspilot.`` and do not end with ``.tailoring.md`` are eligible for orphan removal
   12. Given the selected harness is not VS Code (see ``SYSP_US_HARNESS_INSTALL``), When the Installer places methodology files, Then it writes each available native invocation surface (agents, skills, and commands where the harness supports them) into only that harness's project directories and never asks the user to hand-edit personal or global configuration files
   13. Given a harness's own extension mechanism cannot fully support an installation requirement of this list, When the Installer completes on that harness, Then the gap is reported in the run summary as a documented limitation rather than silently dropped, and installation on other supported harnesses is not blocked
