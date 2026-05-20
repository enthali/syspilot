Setup Manager Requirements
===========================


.. req:: Setup Bootloader Soul
   :id: SYSP_REQ_SETUP_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, soul, bootloader
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Bootloader agent (syspilot.setup) SHALL have a Soul that defines it as
   minimal, reliable, and transparent. It is the stable entry point — user-invocable —
   that fetches and places manifest files, then delegates orchestration to the Installer.

   **Acceptance Criteria:**

   * AC-1: Setup Bootloader Soul defines a minimal, reliable, transparent character
   * AC-2: Setup Bootloader is user-invocable


.. req:: Installer Duties
   :id: SYSP_REQ_INSTALLER_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer, duties
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer SHALL guarantee the following outcomes through its Duties.
   The Installer's scope is defined by SYSP_REQ_INSTALLER_SCOPE.

   **Acceptance Criteria:**

   * AC-1: After every successful run, all syspilot product components within
     the defined installation scope are complete and correctly placed in the
     target project
   * AC-2: After an update, all local user-anpassungen (``tools:`` and other
     customizations) are either preserved automatically or the user is
     explicitly informed what needs re-applying
   * AC-3: No installation run ends in a half-installed or unvalidated state —
     the result always passes sphinx-build before being reported as successful
   * AC-4: Every successful installation leaves a traceable Git commit
   * AC-5: If a Skill belonging to an exclusive group is being installed and
     a Skill of the same group already exists, the installation is rejected
     with a conflict report
   * AC-6: The file sync for every directory in scope is idempotent — re-running
     with unchanged source produces the same end-state with no side effects
   * AC-7: Files present in a target directory that no longer exist in the
     corresponding source directory are removed (orphan cleanup)
   * AC-8: The Installer run summary reports installed / updated / removed
     counts so the invoking agent can verify completeness


.. req:: Installer Workflow
   :id: SYSP_REQ_INSTALLER_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer, workflow
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer agent SHALL follow a workflow from source detection
   through installation to validation and commit. The installation scope
   is governed by SYSP_REQ_INSTALLER_SCOPE. Doc bootstrapping is governed
   by SYSP_REQ_INSTALLER_DOC_BOOTSTRAP.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with detecting install source and mode
   * AC-2: Installer checks dependencies (Python, Sphinx, sphinx-needs)
   * AC-3: Installer installs/updates files within the defined scope and configures the project
   * AC-4: Installer validates with sphinx-build and creates baseline commit
   * AC-5: When installed version equals source version, Installer asks user for reinstall confirmation; if declined, aborts gracefully
   * AC-6: Before overwriting files in update mode, Installer asks user whether customizations exist; if yes, records the list and reminds user to re-apply them after the update completes
   * AC-7: During update, Installer SHALL detect the existing ``tools:``
     value in each installed agent file before overwriting it, and re-inject
     the saved value after copying from product source
   * AC-8: During Configure step, Installer performs doc bootstrap per SYSP_REQ_INSTALLER_DOC_BOOTSTRAP
   * AC-9: During Install/Update, Installer detects orphan files in each
     target directory (files present in target but absent in source) and
     removes them
   * AC-10: After Install/Update, Installer outputs a run summary with
     per-directory counts of installed, updated, and removed files

.. req:: Installer Installation Scope
   :id: SYSP_REQ_INSTALLER_SCOPE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer, scope
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer SHALL have a positively defined installation scope: only the
   following product subdirectories from ``syspilot/`` are copied to the target
   project. syspilot-internal sources SHALL never be copied to user projects.

   **Installation scope (copied to target project):**

   * ``syspilot/agents/`` → ``.github/agents/``
   * ``syspilot/prompts/`` → ``.github/prompts/``
   * ``syspilot/skills/`` → ``.github/skills/``
   * ``syspilot/templates/`` → ``.github/templates/``

   **Explicitly excluded (NOT copied to user projects):**

   * ``docs/syspilot/`` (syspilot-internal specification sources)
   * ``docs/changes/`` (syspilot change documents)
   * ``syspilot/sphinx/`` (syspilot build scripts for its own docs — not user product)
   * ``syspilot/bootstrap.json`` (Bootloader manifest — consumed by Bootloader, not Installer)
   * Any other file or directory not listed in the installation scope above

   **Acceptance Criteria:**

   * AC-1: Only directories listed in the installation scope are copied to the target project
   * AC-2: ``docs/syspilot/`` is never copied to any user project
   * AC-3: ``docs/changes/`` is never copied to any user project
   * AC-4: No unlisted file or directory from the syspilot source is copied to the target project
   * AC-5: The sync for each directory in scope is idempotent — re-running
     the Installer with unchanged source yields the identical end-state
   * AC-6: Files present in a target directory that no longer exist in the
     corresponding source directory are removed (orphan cleanup)
   * AC-7: The Installer run summary reports the count of files installed,
     updated, and removed per scope directory


.. req:: Installer Doc Bootstrap
   :id: SYSP_REQ_INSTALLER_DOC_BOOTSTRAP
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer, doc-bootstrap
   :links: SYSP_US_INSTALLER

   **Description:**
   During the Configure step, the Installer SHALL check whether the target
   project already has a ``docs/index.rst``. If not, it SHALL create a minimal
   starter file. If yes, the existing file SHALL NOT be modified.

   **Acceptance Criteria:**

   * AC-1: If target project has no ``docs/index.rst``, Installer creates a minimal starter ``index.rst`` with a brief "documentation base" statement
   * AC-2: If target project already has a ``docs/index.rst``, it is not overwritten or modified
   * AC-3: The created starter ``index.rst`` is valid RST and does not cause sphinx-build warnings


.. req:: Bootloader Duties
   :id: SYSP_REQ_SETUP_BOOTLOADER_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader, duties
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Bootloader SHALL guarantee the following outcomes through its Duties.

   **Acceptance Criteria:**

   * AC-1: The user always has exactly one, stable entry point into syspilot —
     regardless of internal evolution
   * AC-2: Every invocation executes the upstream-current Installer logic —
     the locally installed version is never authoritative
   * AC-3: If the Bootloader detects version incompatibility with upstream,
     the user is protected from a faulty run (invocation is blocked with
     user-visible error)
   * AC-4: After every Bootloader run, exactly the files declared in
     bootstrap.json have been placed — no more, no less (Manifest Fidelity)


.. req:: Setup Manager Frontmatter Configuration
   :id: SYSP_REQ_SETUP_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, setup, frontmatter
   :links: SYSP_US_SETUP; SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   The Setup Manager agent SHALL be configured with YAML Agent Frontmatter that
   declares it as a user-invocable manager with editing and execution capabilities.

   **Acceptance Criteria:**

   * AC-1: Setup Manager frontmatter declares ``user-invocable: true``
   * AC-2: Setup Manager frontmatter lists ``agents: ["syspilot.installer"]``
   * AC-3: Setup Manager frontmatter includes ``read``, ``edit``, ``search``, ``execute``, ``todo``, ``agent``, ``vscode/askQuestions`` in tools
   * AC-4: The setup agent frontmatter SHALL include a ``version:`` field reflecting the installed syspilot version


.. req:: Setup Manager Prompt File
   :id: SYSP_REQ_SETUP_PROMPT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, prompt
   :links: SYSP_US_SETUP; SYSP_REQ_AGENT_ARCH_PROMPT

   **Description:**
   The Setup Manager SHALL have a prompt file ``syspilot.setup.prompt.md`` that
   enables direct user invocation via VS Code Copilot.

   **Acceptance Criteria:**

   * AC-1: File ``syspilot.setup.prompt.md`` exists in the prompts directory


.. req:: Bootloader Fetch and Place Manifest Files
   :id: SYSP_REQ_SETUP_BOOTLOADER_FETCH
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Bootloader SHALL fetch and place the files declared in the upstream
   bootstrap manifest (GitHub raw URL, ``main`` branch) on every run before
   invoking the Installer.

   **Acceptance Criteria:**

   * AC-1: Bootloader reads ``syspilot/bootstrap.json`` from upstream to resolve file list
   * AC-2: Bootloader fetches each file listed in the manifest ``files[]`` array and writes it to the specified destination
   * AC-3: Fetch happens on every Bootloader run (no local caching)


.. req:: Bootloader Invoke Installer
   :id: SYSP_REQ_SETUP_BOOTLOADER_INVOKE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Bootloader SHALL invoke the fetched Installer as a subagent,
   passing through the user's original request context.

   **Acceptance Criteria:**

   * AC-1: Bootloader invokes Installer via runSubagent()
   * AC-2: Bootloader passes user context to Installer subagent


.. req:: Bootloader Version Gate
   :id: SYSP_REQ_SETUP_BOOTLOADER_VERSION
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader
   :links: SYSP_US_SETUP

   **Description:**
   The Setup Bootloader SHALL validate the ``bootstrap_version`` field in the
   upstream manifest. If the manifest version exceeds the Bootloader's supported
   version, the Bootloader SHALL stop with a user-visible error message.

   **Acceptance Criteria:**

   * AC-1: Bootloader extracts ``bootstrap_version`` from the manifest already fetched by the Bootloader Fetch step — no additional upstream read
   * AC-2: If ``bootstrap_version`` > supported version, Bootloader displays a user-visible error and stops
   * AC-3: Error message instructs user to update their Bootloader


.. req:: Installer Not User-Invocable
   :id: SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, installer
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer agent SHALL NOT be directly user-invocable. It is an internal
   subagent invoked exclusively by the Bootloader.

   **Acceptance Criteria:**

   * AC-1: Installer frontmatter declares ``user-invocable: false``
   * AC-2: Installer agent documentation states it is invoked by Bootloader only


.. req:: Setup Agent Skill Mutual Exclusion
   :id: SYSP_REQ_SETUP_SKILL_MUTEX
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup, skill, mutex
   :links: SYSP_US_INSTALLER

   **Description:**
   The Setup Agent SHALL reject installation of a Skill that declares a ``group:``
   field when a Skill belonging to the same group is already installed, and SHALL
   report the conflict to the user.

   **Acceptance Criteria:**

   * AC-1: Before installing a Skill with a ``group:`` field, Setup Agent checks whether any installed Skill declares the same ``group:`` value
   * AC-2: If a conflicting Skill is found, Setup Agent aborts the installation and reports the conflict, naming the conflicting Skill
   * AC-3: If no conflicting Skill is found, installation proceeds normally
