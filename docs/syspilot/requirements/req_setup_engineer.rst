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
   :status: approved
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
   * AC-9: All files written by the Installer are encoded as UTF-8 without BOM
   * AC-10: The Installer performs file operations directly per file — it
     SHALL NOT generate wrapper scripts or helper files
   * AC-11: On any failure between install start and final commit, the
     Installer restores the workspace to the pre-install state via
     transactional rollback


.. req:: Installer Workflow
   :id: SYSP_REQ_INSTALLER_WORKFLOW
   :status: approved
   :priority: mandatory
   :tags: agent-v2, installer, workflow
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer agent SHALL follow a workflow from source fetch through
   installation to validation and commit. The installation scope is governed
   by SYSP_REQ_INSTALLER_SCOPE. Doc bootstrapping is governed by
   SYSP_REQ_INSTALLER_DOC_BOOTSTRAP. Source acquisition is governed by
   SYSP_REQ_INSTALLER_GITHUB_SOURCE. Encoding is governed by
   SYSP_REQ_INSTALLER_ENCODING. File operations discipline is governed by
   SYSP_REQ_INSTALLER_DIRECT_OPS. Rollback is governed by
   SYSP_REQ_INSTALLER_ROLLBACK.

   **Acceptance Criteria:**

   * AC-1: Workflow starts with fetching from upstream GitHub repository
     (default branch ``main``); branch override only via explicit user prompt
     at runtime
   * AC-2: Installer checks dependencies (Python, Sphinx, sphinx-needs);
     if any dependency is missing, prints install instructions and stops —
     does NOT auto-install
   * AC-3: Before file operations, Installer creates a pre-install Git commit
     of the current ``.github/`` state as a rollback point
   * AC-4: Installer installs/updates files within the defined scope by
     fetching each file from upstream and writing it to the target location
   * AC-5: During install/update, for each existing file that is NOT the
     Bootloader (``syspilot.setup.agent.md``): read the current ``tools:``
     frontmatter value, fetch file from upstream, replace the upstream
     ``tools:`` line with the saved value, write the result. All other
     frontmatter fields come from upstream — no preservation
   * AC-6: The Bootloader file (``syspilot.setup.agent.md``) is overwritten
     verbatim from upstream with no field preservation
   * AC-7: During Configure step, Installer performs doc bootstrap per
     SYSP_REQ_INSTALLER_DOC_BOOTSTRAP
   * AC-8: During Orphan Cleanup, Installer detects orphan files in each
     target directory (files present in target but absent in source) and
     removes them
   * AC-9: After Install/Update, Installer outputs a run summary with
     per-directory counts of installed, updated, and removed files
   * AC-10: Installer validates with sphinx-build; on failure, executes
     transactional rollback per SYSP_REQ_INSTALLER_ROLLBACK
   * AC-11: On success, Installer creates final Git commit documenting
     the installation


.. req:: Installer GitHub-Only Source
   :id: SYSP_REQ_INSTALLER_GITHUB_SOURCE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, installer, source
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer SHALL always fetch product files from the upstream GitHub
   repository. There is no local-source path, no source-choice dialog, and
   no mode-detection step. The Installer always installs the latest version
   from the specified branch.

   **Acceptance Criteria:**

   * AC-1: Installer always fetches files from upstream GitHub — no local
     ``syspilot/`` directory is ever used as install source
   * AC-2: There is no source-choice dialog presented to the user
   * AC-3: There is no Mode-Detect step — the Installer always installs
     the latest upstream version without comparing against an installed version
   * AC-4: Default fetch branch is ``main``; branch override is only possible
     via explicit user prompt at runtime


.. req:: Installer File Encoding
   :id: SYSP_REQ_INSTALLER_ENCODING
   :status: approved
   :priority: mandatory
   :tags: agent-v2, installer, encoding
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer SHALL write all output files using UTF-8 encoding without
   Byte Order Mark (BOM). This applies to every file written during
   installation, update, or configuration.

   **Acceptance Criteria:**

   * AC-1: All files written by the Installer are encoded as UTF-8
   * AC-2: No file written by the Installer contains a BOM (byte sequence
     ``EF BB BF``)
   * AC-3: The encoding rule applies regardless of platform (Windows,
     macOS, Linux)


.. req:: Installer Direct File Operations
   :id: SYSP_REQ_INSTALLER_DIRECT_OPS
   :status: approved
   :priority: mandatory
   :tags: agent-v2, installer, file-ops
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer SHALL perform all file operations directly per file using
   platform-native commands (e.g. ``Invoke-WebRequest`` + ``Out-File`` on
   PowerShell, or equivalent). It SHALL NOT generate wrapper scripts, helper
   files, or intermediary artifacts.

   **Acceptance Criteria:**

   * AC-1: Each file is fetched and written individually via direct platform
     commands
   * AC-2: The Installer never generates wrapper scripts (e.g.
     ``install.ps1``, ``install.sh``)
   * AC-3: The Installer never writes helper files to ``temp/`` or any other
     temporary location
   * AC-4: No intermediary artifacts are produced — only the final target
     files within the installation scope


.. req:: Installer Transactional Rollback
   :id: SYSP_REQ_INSTALLER_ROLLBACK
   :status: approved
   :priority: mandatory
   :tags: agent-v2, installer, rollback, transaction
   :links: SYSP_US_INSTALLER

   **Description:**
   The Installer SHALL implement a git-based transactional model: a
   pre-install commit is created before file operations begin, and on any
   failure between install start and final commit, the workspace is restored
   to the pre-install state via ``git reset --hard``.

   **Acceptance Criteria:**

   * AC-1: Before file operations begin, a pre-install Git commit is created
     capturing the current state of ``.github/``
   * AC-2: On any failure between the pre-install commit and the final
     success commit, the Installer executes ``git reset --hard`` to the
     pre-install commit SHA
   * AC-3: After rollback, the workspace is in exactly the state it was
     before the Installer started — no partial installation remains
   * AC-4: On successful completion, the pre-install commit is replaced by
     the final post-install commit


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
