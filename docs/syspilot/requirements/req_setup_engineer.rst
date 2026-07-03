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
   * AC-2: No installation run ends in a half-installed or unvalidated state —
     the result always passes sphinx-build before being reported as successful
   * AC-3: Every successful installation leaves a traceable Git commit
   * AC-4: If a Skill belonging to an exclusive group is being installed and
     a Skill of the same group already exists, the existing Skill is removed
     before the new one is written — mutual exclusion is enforced through
     replacement, and the run summary names the replaced Skill
   * AC-5: The file sync for every directory in scope is idempotent — re-running
     with unchanged source produces the same end-state with no side effects
   * AC-6: A file is eligible for orphan removal only if its name starts with
     the ``syspilot.`` filename prefix **and** does not end with
     ``.tailoring.md``; an eligible file present in a target directory but no
     longer existing in the corresponding source directory is removed (orphan
     cleanup). Files without the ``syspilot.`` prefix, and ``syspilot.*``
     files ending in ``.tailoring.md``, are never removed
   * AC-7: The Installer run summary reports installed / updated / removed
     counts so the invoking agent can verify completeness
   * AC-8: All files written by the Installer are encoded as UTF-8 without BOM
   * AC-9: The Installer performs file operations directly per file — it
     SHALL NOT generate wrapper scripts or helper files
   * AC-10: On any failure between install start and final commit, the
     Installer restores the workspace to the pre-install state via
     transactional rollback


.. req:: Installer Workflow
   :id: SYSP_REQ_INSTALLER_WORKFLOW
   :status: draft
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
   SYSP_REQ_INSTALLER_ROLLBACK. Orchestration variant selection is governed by
   SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT. Session scaffold creation is
   governed by SYSP_REQ_INSTALLER_SESSION_SCAFFOLD.

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
   * AC-5: During install/update, for each file in scope, all frontmatter
     fields come from upstream — no local field is preserved; every file is
     written verbatim from upstream
   * AC-6: During Configure step, Installer performs doc bootstrap per
     SYSP_REQ_INSTALLER_DOC_BOOTSTRAP
   * AC-7: During Configure step, Installer selects and installs exactly one
     orchestration-group Skill per SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT
   * AC-8: During Orphan Cleanup, Installer detects orphan files in each
     target directory (files that start with ``syspilot.`` and do not end
     with ``.tailoring.md``, present in target but absent in source) and
     removes them; files without the ``syspilot.`` prefix and
     ``syspilot.*.tailoring.md`` files are left untouched
   * AC-9: After Install/Update, Installer outputs a run summary with
     per-directory counts of installed, updated, and removed files
   * AC-10: Installer validates with sphinx-build; on failure, executes
     transactional rollback per SYSP_REQ_INSTALLER_ROLLBACK
   * AC-11: When the asynchronous orchestration variant was selected, as the
     final step before commit, Installer creates session scaffolds per
     SYSP_REQ_INSTALLER_SESSION_SCAFFOLD
   * AC-12: On success, Installer creates final Git commit documenting
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
   * AC-6: A file is eligible for orphan removal only if its name starts with
     the ``syspilot.`` filename prefix **and** does not end with
     ``.tailoring.md``; an eligible file present in a target directory but no
     longer existing in the corresponding source directory is removed (orphan
     cleanup). Files without the ``syspilot.`` prefix, and ``syspilot.*``
     files ending in ``.tailoring.md``, are never removed
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
   * AC-3: Setup Manager frontmatter includes ``read``, ``edit``, ``search``, ``execute``, ``todo``, ``agent/runSubagent``, ``vscode/askQuestions`` in tools
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
   The Setup Bootloader SHALL call the fetched Installer as a synchronous
   in-process subagent, passing through the user's original request context.
   This call is a deliberate exception **outside the orchestration contract**:
   it does not use the orchestration skill and does not use the SEND/RECEIVE/
   RESPOND verbs, because the Bootloader runs before any orchestration skill or
   session infrastructure is available.

   **Acceptance Criteria:**

   * AC-1: Bootloader calls the Installer as a synchronous in-process subagent
   * AC-2: Bootloader passes user context to the Installer
   * AC-3: The Bootloader → Installer call is explicitly outside the orchestration contract — it does not use the orchestration skill or its verbs


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
   :status: approved
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
   The Setup Agent SHALL enforce mutual exclusion for Skills that declare a
   ``group:`` field: at most one Skill per group is installed at any time. When
   a Skill of a group is installed and a Skill of the same group already exists,
   the Setup Agent SHALL remove the existing Skill before writing the new one,
   and SHALL report the replacement to the user.

   **Acceptance Criteria:**

   * AC-1: Before installing a Skill with a ``group:`` field, Setup Agent checks whether any installed Skill declares the same ``group:`` value
   * AC-2: If a Skill of the same group is found, Setup Agent removes the existing Skill before writing the new one — installation proceeds through replacement, not rejection
   * AC-3: After installation, exactly one Skill of the group is present and the run summary names the replaced Skill (if any)


.. req:: Installer Orchestration Variant Selection
   :id: SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer, orchestration, skill
   :links: SYSP_US_INSTALLER, SYSP_US_SKILL_ORCHESTRATION

   **Description:**
   The Installer SHALL install exactly one orchestration-group Skill, chosen
   between the asynchronous (session-messaging) variant and the synchronous
   (in-process) variant. The Installer SHALL ask the user which variant to use
   and SHALL infer the default answer from the workspace: if a session-messaging
   infrastructure is detected, the asynchronous variant is the default;
   otherwise the synchronous variant is the default. The selected variant is
   installed under the mutual-exclusion rule (SYSP_REQ_SETUP_SKILL_MUTEX).

   **Rationale:**
   syspilot must run with or without session-messaging infrastructure. Letting
   the Installer pick a sensible default while still asking keeps installation
   automatic in the common case and explicit when the user wants the other
   variant.

   **Acceptance Criteria:**

   * AC-1: Given an install or update, When the Installer runs, Then it asks the user which orchestration variant to install
   * AC-2: Given a workspace with session-messaging infrastructure present, When the Installer determines the default, Then the asynchronous variant is the default
   * AC-3: Given a workspace without session-messaging infrastructure, When the Installer determines the default, Then the synchronous variant is the default
   * AC-4: Given the variant is chosen, When the Installer writes it, Then exactly one orchestration-group Skill is present afterward (mutual exclusion via replacement)


.. req:: Installer Session Scaffold Creation
   :id: SYSP_REQ_INSTALLER_SESSION_SCAFFOLD
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer, session, scaffold
   :links: SYSP_US_INSTALLER

   **Description:**
   When the asynchronous orchestration variant is selected, the Installer SHALL,
   as the final installation step, create a session scaffold for every installed
   agent except the Setup Bootloader and the Installer. Each scaffold declares
   the agent's session identity, derived from the agent file's frontmatter. The
   Installer SHALL preserve any existing scaffold and its agent-owned context on
   update — only missing scaffolds are created.

   **Rationale:**
   The asynchronous variant runs each orchestrating agent as its own persistent
   session. Pre-declaring a scaffold per agent gives every agent a stable session
   identity and a place to accumulate its own context across changes, without the
   Installer ever overwriting accumulated context.

   **Acceptance Criteria:**

   * AC-1: Given the asynchronous variant is selected, When the Installer finishes, Then a session scaffold exists for every installed agent except the Setup Bootloader and the Installer
   * AC-2: Given an agent file with session-identity frontmatter, When the Installer creates that agent's scaffold, Then the scaffold's identity is taken from the agent file's frontmatter
   * AC-3: Given an update where a scaffold already exists, When the Installer runs, Then the existing scaffold and its agent-owned context are left untouched
   * AC-4: Given an update where a scaffold is missing, When the Installer runs, Then the missing scaffold is created
   * AC-5: Given the synchronous variant is selected, When the Installer finishes, Then no session scaffolds are created

