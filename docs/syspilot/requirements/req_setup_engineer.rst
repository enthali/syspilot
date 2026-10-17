Setup Manager Requirements
===========================


.. req:: Setup Bootloader Soul
   :id: SYSP_REQ_SETUP_SOUL
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, setup, soul, bootloader
   :links: SYSP_US_SETUP

   **Description:**
    The Setup Bootloader agent (syspilot.setup) SHALL have a Soul that defines it as
    minimal, reliable, and transparent. It is the installed, user-invocable
    update entry point that directly executes the deterministic Installer runtime.

   **Acceptance Criteria:**

   * AC-1: Setup Bootloader Soul defines a minimal, reliable, transparent character
   * AC-2: Setup Bootloader is user-invocable
   * AC-3: Setup invokes installation through the deterministic runtime and
     never delegates it to an Installer agent


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
   * AC-2: No installation run ends in a half-installed or unvalidated state —
     the result always passes Sphinx validation through the ``uv`` command
     contract before a final commit is created or the run is reported as
     successful
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
   * AC-9: Installer file operations conform to
     SYSP_REQ_INSTALLER_DIRECT_OPS
   * AC-10: Transaction boundaries and restoration behavior are owned
     exclusively by SYSP_REQ_INSTALLER_ROLLBACK


.. req:: Installer Workflow
  :id: SYSP_REQ_INSTALLER_WORKFLOW
  :status: approved
  :links: SYSP_US_INSTALLER; SYSP_REQ_AGENT_ARCH_WORKFLOW

    The deterministic Installer runtime owns source fetch, installation,
    validation, and commit. Scope, documentation bootstrap, source
    acquisition, encoding, direct file operations, and rollback are governed
    by their dedicated Installer requirements. Installation has no nested
    Setup, Installer-agent, bootstrap-manifest, Jarvis, or actor flow.

   **Acceptance Criteria:**

   * AC-1: Workflow entry and direct runtime invocation conform to
     SYSP_REQ_HARNESS_NATIVE_INSTALL for initial installation and
     SYSP_REQ_HARNESS_NATIVE_UPDATE for installed updates; repository and
     branch propagation conform to SYSP_REQ_INSTALLER_GITHUB_SOURCE
   * AC-2: Every Python-related execution and dependency operation conforms to
     the uv-only policy owned by SYSP_REQ_HARNESS_NATIVE_INSTALL; a failed gate
     stops before mutation, final commit, or success reporting
   * AC-3: Source resolution, enumeration, fetch, structured parse,
     transformation, mutable-path derivation, containment checks, and complete
     target-plan validation are read-only and SHALL finish before checkpoint
     creation; only after that validated plan is frozen does the runtime create
     a scoped checkpoint outside the target and begin mutation
   * AC-4: Installer installs/updates files within the defined scope by
     fetching each file from upstream and writing it to the target location
   * AC-5: During install/update, each methodology body is written byte-for-byte
     from upstream while frontmatter is deterministically transformed only as
     required by the selected harness; no local source field is preserved
   * AC-6: During Configure step, Installer performs doc bootstrap per
     SYSP_REQ_INSTALLER_DOC_BOOTSTRAP
   * AC-7: During Configure step, Installer deterministically installs the
     synchronous orchestration-group Skill; no infrastructure inference or
     user selection occurs
   * AC-8: During Orphan Cleanup, Installer detects orphan files in each
     target directory (files that start with ``syspilot.`` and do not end
     with ``.tailoring.md``, present in target but absent in source) and
     removes them; files without the ``syspilot.`` prefix and
     ``syspilot.*.tailoring.md`` files are left untouched
   * AC-9: After Install/Update, Installer outputs a run summary with
     per-directory counts of installed, updated, and removed files
   * AC-10: Installer validates Sphinx through the externally observable
     ``uv run`` engine command defined by SYSP_SPEC_INSTALLER_ADAPTER_ENGINE;
     on failure, it executes transactional rollback per
     SYSP_REQ_INSTALLER_ROLLBACK and does not create a final commit or report
     success
   * AC-11: Installer does not create sessions, actors, or scaffolds and does
     not invoke another agent as part of installation
   * AC-12: On success, Installer creates final Git commit documenting
     the installation
   * AC-13: A final commit is created only after every dependency and
     validation gate has passed, but success is not final until checkpoint
     deletion completes; any failure through that deletion restores the exact
     pre-install HEAD, index, and worktree state
   * AC-14: On both success and handled failure, the runtime removes its
     checkpoint artifact; no checkpoint residue remains in or outside the
     target repository
   * AC-15: The complete Installer test suite SHALL finish normally after each
     correction pass. An abrupt termination is a failed run that SHALL be
     investigated and rerun; test and runtime resource use SHALL remain bounded
     by selected source content and declared mutable paths rather than by the
     size of unrelated target content


.. req:: Installer GitHub-Only Source
  :id: SYSP_REQ_INSTALLER_GITHUB_SOURCE
  :status: approved
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
   * AC-4: Default repository and branch are the published syspilot repository
     and ``main``; explicit CLI or Setup inputs may override either
   * AC-5: Given a branch selected explicitly through Setup, When the
     Installer fetches or enumerates product files, Then it uses that same
     branch for every operation
   * AC-6: Installer enumerates product files from the upstream ``syspilot/``
     tree on the selected branch; an installed ``.github/`` or other
     harness-native target tree is never used as the source inventory
   * AC-7: Source resolution, enumeration, fetch, parse, and transformation do
     not mutate the target repository and may complete before the transaction
     checkpoint is created
   * AC-8: GitHub API inventory and raw-content acquisition resolve and use one
     immutable revision; malformed, missing, or out-of-root inventory entries
     fail before checkpoint creation
   * AC-9: The public ``--repository`` input accepts only ``owner/repository``
     or a supported GitHub HTTPS repository URL. It rejects relative and
     absolute filesystem paths, ``file:`` URLs, non-GitHub hosts, and malformed
     values before any working-directory or target-path resolution. Local
     directory snapshots may be supplied only through an internal fixture API
     that is unavailable from the production CLI and source-acquisition API


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
  :links: SYSP_US_INSTALLER

   **Description:**
    The Installer SHALL perform file operations through the deterministic,
    version-controlled implementation shipped in the product
    ``syspilot/`` tree. During installation it SHALL NOT generate wrapper
    scripts, temporary helper files, or intermediary target artifacts.

   **Acceptance Criteria:**

   * AC-1: Each final target file is fetched, adapted when required, and
     written by the shipped deterministic product implementation
   * AC-2: The Installer never generates target-side wrapper scripts (e.g.
     ``install.ps1``, ``install.sh``) during a run
   * AC-3: The Installer never generates helper files in ``temp/`` or any
     other temporary or target location during a run
   * AC-4: No intermediary target artifacts are produced — only final files
     within the installation scope and the transaction state required by
     SYSP_REQ_INSTALLER_ROLLBACK
   * AC-5: Version-controlled implementation present in the upstream product
     ``syspilot/`` tree is permitted and is not classified as a generated
     helper or intermediary artifact
   * AC-6: Before write, delete, or restore, every target path passes lexical
     containment and physical no-follow ancestry validation against the
     resolved target root
   * AC-7: A symlink, junction, mount point, or other reparse point in mutable
     path ancestry is rejected before mutation; the Installer never follows
     such a link outside the target during install or rollback
   * AC-8: Every write, atomic replace, delete, and restore uses a no-follow
     mutation primitive that reopens and verifies each parent immediately
     before the final operation. Atomic temporary files are created only in
     the verified real parent, whose identity is revalidated before replace;
     a detected ancestry or identity race fails closed without touching an
     escaped target


.. req:: Installer Transactional Rollback
  :id: SYSP_REQ_INSTALLER_ROLLBACK
  :status: approved
  :links: SYSP_US_INSTALLER

   **Description:**
    The Installer SHALL implement a checkpoint-based transactional model. A
    scoped pre-mutation checkpoint is stored outside the target repository;
    on any failure after checkpoint creation and before checkpoint deletion,
    including after the installation commit, only declared mutable paths and
    exact Git metadata are restored to their pre-install state. Unrelated
    project paths are never snapshotted, deleted, or reconstructed.

   **Acceptance Criteria:**

   * AC-1: After all read-only acquisition, parsing, transformation, and target
     plan validation and before every mutation, a checkpoint is created outside
     the target repository capturing only the selected harness tree,
     ``.syspilot/installer.py``, ``.syspilot/skills/``,
     ``.syspilot/templates/``, exact missing-only documentation bootstrap files,
     and exact Git metadata and index entries required by the frozen plan
   * AC-2: On any failure after checkpoint creation and before checkpoint
     deletion, including after commit creation, the Installer restores
     pre-install HEAD, index, and worktree state, including removal of newly
     created files
   * AC-3: After rollback, every declared mutable path and transaction-owned Git
     state is exactly as it was before mutation; unrelated or concurrently
     created files outside that path set remain unchanged
   * AC-4: Only after every dependency and validation gate passes does the
     Installer create the post-install commit; the transaction becomes
     successful only after its checkpoint is deleted
   * AC-5: On dependency or validation failure, the Installer does not create
     a final commit and does not report the run as successful
   * AC-6: Successful completion and completed rollback both delete the
     checkpoint artifact
   * AC-7: If a pre-existing mutable directory or file changes after checkpoint
     creation in a way not caused by the transaction, the Installer detects the
     conflict before destructive overwrite or restore, fails safely, and does
     not silently discard the concurrent change
   * AC-8: Git discovery uses ``git rev-parse --git-dir``, ``git rev-parse
     --git-path index``, and ``git rev-parse --symbolic-full-name HEAD`` plus
     explicit OID/unborn detection; attached, detached, and unborn
     linked-worktree states restore exactly without a ``.git`` directory
     assumption
   * AC-9: Before any mutation, a supplied checkpoint is accepted only when its
     recorded resolved target-root identity equals the current resolved target
     root and its declared mutable-path set equals the frozen plan's mutable-
     path set exactly. Both sets are canonicalized as contained target-relative
     paths by normalizing separators, removing ``.`` components, rejecting
     absolute, drive/UNC, empty, and ``..``-escaping forms, applying the host
     filesystem's case normalization, and deduplicating. A narrower, broader,
     mismatched-root, malformed, or duplicate-ambiguous checkpoint is rejected
     before mutation, final commit, or success reporting and leaves no target
     or Git-state change
   * AC-10: The checkpoint records pre-install Git state and, after commit,
     the exact transaction-created ref/OID state. Rollback changes a ref or
     detached HEAD only by compare-and-swap against that expected created
     state. If HEAD or the ref advanced independently, rollback preserves the
     concurrent history, reports a rollback conflict, and restores only owned
     file/index changes whose current identities still match transaction state
   * AC-11: Checkpoint entries, the frozen plan's expected-current map, and
     restore lookup use one canonical target-relative key representation.
     Original path spelling is retained separately for display and filesystem
     operations. Case-insensitive hosts normalize case before every map access;
     mixed canonical and display representations are never used as keys
   * AC-12: A supplied checkpoint carries an immutable, unguessable nonce plus
     exact pre-state fingerprints for every declared mutable path and the Git
     state captured at handoff. At the start of every public attempt that
     supplies an identifier, the runtime atomically consumes its capability,
     or acquires a lease that is terminally revoked on every failure path,
     before dependency resolution, source acquisition or parsing, frozen-plan
     construction, target-root or plan-binding validation, and freshness
     validation. No dependency, source, parse, plan, root-mismatch, freshness,
     or later failure leaves the identifier reusable. Immediately before the
     first mutation, the runtime recomputes only the declared owned-path and Git
     fingerprints and requires an exact match. A reused, stale, or altered
     checkpoint is rejected without target or Git mutation and without reading
     or hashing unrelated paths; trusted-state cleanup and forensic reporting
     preserve no capability that can authorize replay


.. req:: Installer Installation Scope
   :id: SYSP_REQ_INSTALLER_SCOPE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, installer, scope
   :links: SYSP_US_INSTALLER, SYSP_US_HARNESS_INSTALL

   **Description:**
   The Installer SHALL have a positively defined installation scope: one
   explicitly selected harness target plus shared runtime and documentation.
   syspilot-internal specification sources SHALL never be copied to user
   projects.

   **Selected-harness scope (exactly one per invocation):**

   * ``vscode`` → ``.github/{agents,prompts,skills,templates}/``
   * ``opencode`` → ``.opencode/{agents,commands,skills}/``
   * production ``claude`` → ``.claude/{agents,skills}/``
   * experimental, installable ``qoder`` → the checksummed package archive
     ``.syspilot/qoder/syspilot-qoder-plugin.zip`` (Qoder Staging Contract,
     SYSP_SPEC_HARNESS_TARGET_MATRIX); no project-native ``.qoder/`` tree is
     written by this change

   **Shared scope (every invocation):**

   * ``.syspilot/installer.py``
   * ``.syspilot/skills/<name>/`` containing non-``SKILL.md`` runtime
     resources required by installed Skills
   * ``.syspilot/templates/`` containing product templates required by
     installed Skills, including ``change-document.md``
   * missing-only ``docs/index.rst`` and ``docs/conf.py`` bootstrap files

   **Explicitly excluded (NOT copied to user projects):**

   * ``docs/syspilot/`` (syspilot-internal specification sources)
   * ``docs/changes/`` (syspilot change documents)
   * ``syspilot/sphinx/`` (syspilot build scripts for its own docs — not user product)
   * ``syspilot/bootstrap.json`` (deprecated bootstrap manifest)
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
   * AC-8: Given any explicit harness, When the Installer targets it, Then
     methodology files are written only to that harness's native directories
     and format; another harness's methodology directories are not written
   * AC-9: Harness limitation disclosure is owned exclusively by
     SYSP_REQ_HARNESS_LIMITATION_DISCLOSURE
   * AC-10: Each invocation targets exactly the explicitly selected harness;
     the Installer does not infer additional targets from directory presence
   * AC-11: Every selected production harness installs required shared
     templates at stable ``.syspilot/templates/`` paths while native agents,
     Skills, and commands remain selected-harness-only
   * AC-12: Non-native Skill runtime resources are installed at stable
     ``.syspilot/skills/<name>/`` paths; native ``SKILL.md`` files remain only
     in the explicitly selected harness tree


   * AC-13: Given the public harness selection surface, When a user selects
         Claude Code, Then that value is an explicit production target and
         installation remains isolated to its native tree. When a user
         selects Qoder, Then that value is an explicit experimental,
         installable target and installation is isolated to its declared
         package-staging path, not a native project tree.
.. req:: Installer Doc Bootstrap
   :id: SYSP_REQ_INSTALLER_DOC_BOOTSTRAP
   :status: approved
   :priority: mandatory
   :tags: agent-v2, installer, doc-bootstrap
   :links: SYSP_US_INSTALLER

   **Description:**
    During the Configure step, the Installer SHALL ensure a fresh target
    project has the minimal documentation source and Sphinx configuration
    needed to run the mandatory Sphinx + sphinx-needs validation. Existing
    documentation files SHALL NOT be overwritten or modified.

   **Acceptance Criteria:**

   * AC-1: If the target project has no ``docs/index.rst``, Installer creates
     a minimal valid RST starter source
   * AC-2: If the target project has no ``docs/conf.py``, Installer creates a
     minimal Sphinx configuration that enables ``sphinx_needs``
   * AC-3: Any existing ``docs/index.rst`` or ``docs/conf.py`` is not
     overwritten or modified
   * AC-4: Given a fresh project with the required dependencies available,
     When bootstrap completes, Then the Installer's mandatory Sphinx +
     sphinx-needs validation can run successfully through ``uv run`` using the
     created documentation configuration


.. req:: Setup Update Duties
   :id: SYSP_REQ_SETUP_BOOTLOADER_DUTIES
   :status: approved
   :priority: mandatory
   :tags: agent-v2, manager, setup, bootloader, duties
   :links: SYSP_US_SETUP, SYSP_US_HARNESS_INSTALL

   **Description:**
   Installed Setup SHALL guarantee the following update outcomes through its Duties.

   **Acceptance Criteria:**

   * AC-1: The user always has exactly one, stable entry point into syspilot —
     regardless of internal evolution
   * AC-2: Every invocation conforms to the installed direct-runtime contract
     owned by SYSP_REQ_HARNESS_NATIVE_UPDATE
   * AC-3: If the local runtime cannot resolve or validate the requested
     upstream revision, the operation stops with a user-visible error before
     target mutation
   * AC-4: After every Setup run, the selected harness contains exactly the
     deterministic runtime's selected-revision output
   * AC-5: Given a non-VS Code harness, When the user installs or updates
     syspilot, Then the entry point is that harness's own native install
     mechanism — never a hand-edited personal or global configuration file
   * AC-6: Setup update execution does not require a discoverable native
     Installer agent, as governed by SYSP_REQ_HARNESS_NATIVE_UPDATE
   * AC-7: Setup passes repository and branch inputs according to the normative
     propagation and source-fidelity rules in SYSP_REQ_INSTALLER_GITHUB_SOURCE
   * AC-8: Setup execution conforms to the uv-only policy owned by
     SYSP_REQ_HARNESS_NATIVE_INSTALL
   * AC-9: Given Claude Code or Qoder is explicitly selected, When installed Setup updates or rolls back, Then the selected harness lifecycle works without hand-edited personal or global configuration, with independent Claude Code and Qoder evidence.

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
   * AC-2: Setup Manager frontmatter does not grant or list an Installer
     subagent target
   * AC-3: Setup Manager frontmatter provides execution capability without
     ``agent/runSubagent`` or an equivalent nested-agent tool
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
   :status: deprecated
   :priority: mandatory
   :tags: agent-v2, installer, orchestration, skill
   :links: SYSP_US_INSTALLER, SYSP_US_SKILL_ORCHESTRATION; SYSP_REQ_SKILL_ORCHESTRATION_GROUP

   **Description:**
   This requirement is deprecated. Installation deterministically selects the
   synchronous orchestration-group Skill and performs no Jarvis detection,
   infrastructure inference, or user choice.

   **Rationale:**
   syspilot must run with or without session-messaging infrastructure. Letting
   the Installer pick a sensible default while still asking keeps installation
   automatic in the common case and explicit when the user wants the other
   variant.

   **Replacement:** ``SYSP_REQ_SKILL_ORCHESTRATION_GROUP``.


.. req:: Installer Actor Creation
   :id: SYSP_REQ_INSTALLER_SESSION_SCAFFOLD
   :status: deprecated
   :priority: mandatory
   :tags: agent-v2, installer, session, scaffold
   :links: SYSP_US_INSTALLER; SYSP_REQ_INSTALLER_WORKFLOW

   **Description:**
   This requirement is deprecated. The deterministic runtime creates no
   Jarvis actors or session scaffolds and leaves existing user-owned actor or
   session state untouched.

   **Rationale:**
   The asynchronous variant runs each orchestrating agent as its own persistent
   session. Pre-declaring an actor per agent gives every agent a stable session
   identity and a place to accumulate its own context across changes, without the
   Installer ever overwriting accumulated context. The three-way check handles
   both fresh installs and workspaces migrating from the legacy session format.

   **Replacement:** ``SYSP_REQ_INSTALLER_WORKFLOW``.

