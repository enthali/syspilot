Installer Design
=================


.. spec:: Installer Agent Soul
   :id: SYSP_SPEC_INSTALLER_SOUL
   :status: implemented
   :tags: agent-v2, installer, soul
   :links: SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE, SYSP_REQ_INSTALLER_ENCODING, SYSP_REQ_INSTALLER_DIRECT_OPS, SYSP_REQ_INSTALLER_ROLLBACK

   **Soul:**

   You are the **Installer** documentation and diagnostic surface for the
   deterministic syspilot installation runtime. Setup is the primary installed
   user entry point, but installation correctness does not depend on invoking
   this agent.

   **Character:** Thorough, methodical, user-friendly (in reporting).
   **Perspective:** Is the installation correct? Does everything work?
   **Guardrails:**

   * Always validates Sphinx through the specified ``uv run`` command. Never leaves a broken state.
   * Performs file operations through the shipped deterministic adapter engine; does not generate wrappers, temporary helpers, or intermediary target artifacts.
   * All files are written as UTF-8 without BOM — regardless of platform.
   * Implements transactional rollback across every Setup and Installer target; any post-checkpoint failure restores exact pre-state, and only successful validation permits final commit/report.

   **Care:** Correct installation, preserved customizations, working environment.


.. spec:: Installer Frontmatter
   :id: SYSP_SPEC_INSTALLER_FRONTMATTER
   :status: implemented
   :tags: agent-v2, installer, frontmatter
   :links: SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE

   **Frontmatter Configuration:**

   * **description:** ``"Internal documentation and diagnostic surface for the deterministic syspilot installer runtime; not a control-plane dependency."``
   * **user-invocable:** ``false``
   * **agents:** ``[]``

   **File:** ``syspilot.installer.agent.md``


.. spec:: Installer Duties
   :id: SYSP_SPEC_INSTALLER_DUTIES
   :status: implemented
   :tags: agent-v2, installer, duties
   :links: SYSP_REQ_INSTALLER_DUTIES, SYSP_SPEC_SKILL_ASK_QUESTIONS_API, SYSP_SPEC_INSTALLER_SCOPE

   **Duties:**

   * **Completeness and Correctness** — After every successful run, all
     syspilot product components within the defined installation scope
     are complete and correctly placed in the target project
   * **Operability** — No run ends in a half-installed or unvalidated
       state; the result always passes the uv-managed Sphinx validation command
       before being reported as successful
   * **Traceability** — Every successful installation leaves a
     traceable Git commit documenting exactly what was changed
   * **Skill Conflict Prevention** — If a Skill belonging to an exclusive group
     is being installed and a Skill of the same group already exists, the
     existing Skill is replaced by the new one, and the run summary names
     the replaced Skill
   * **Idempotent Sync** — Re-running the Installer with unchanged source
     yields the identical end-state; no files are needlessly rewritten and
     no side effects occur
   * **Orphan Cleanup** — A file is eligible for orphan removal only if its
     name starts with the ``syspilot.`` filename prefix **and** does not end
     with ``.tailoring.md``. An eligible file present in a target directory but
     no longer existing in the corresponding source directory is removed during
     every run; files without the ``syspilot.`` prefix (customer-owned or
     project-specific) and ``syspilot.*.tailoring.md`` instance tailoring files
     are never removed
   * **Observable Summary** — Every run outputs a per-directory summary of
     installed / updated / removed file counts so the invoking agent can
     verify completeness
   * **UTF-8 Without BOM** — All files are written as UTF-8 without BOM,
     regardless of platform. Detailed behaviour: SYSP_SPEC_INSTALLER_ENCODING.
   * **Direct File Operations** — Use the shipped deterministic implementation; do not generate wrappers, helpers, temporary files, or intermediary target artifacts. Detailed behaviour: SYSP_SPEC_INSTALLER_DIRECT_OPS.
   * **Transaction Model** — Snapshot only the validated mutable-path plan and
     exact Git metadata; preserve unrelated paths, detect conflicting writes,
     and permit final commit/report only after successful validation.


.. spec:: Installer Scope Definition
   :id: SYSP_SPEC_INSTALLER_SCOPE
   :status: approved
   :tags: agent-v2, installer, scope
   :links: SYSP_REQ_INSTALLER_SCOPE

   **Installation Scope:**

   The Installer enumerates product content from the selected branch's
   upstream ``syspilot/`` tree and writes it to exactly one explicit harness
   target per invocation. The source content is adapted per
   SYSP_SPEC_HARNESS_AGENT_ADAPTER and SYSP_SPEC_HARNESS_SKILL_ADAPTER:

    .. csv-table::
         :header: "Harness", "Source", "Destination"
         :widths: 25, 35, 40

         "``vscode``", "``agents/``, ``prompts/``, ``skills/``", "``.github/{agents,prompts,skills}/``"
         "``opencode``", "``agents/``, ``prompts/``, ``skills/``", "``.opencode/{agents,commands,skills}/``"
         "``claude``", "``agents/``, ``skills/``", "``.claude/{agents,skills}/``"
         "``qoder``", "``agents/``, ``skills/``", "``.syspilot/qoder/syspilot-qoder-plugin.zip``"

   Every invocation also manages shared ``.syspilot/installer.py``, product
   templates under ``.syspilot/templates/``, non-``SKILL.md`` Skill resources
   under ``.syspilot/skills/<name>/``, and missing-only ``docs/index.rst`` /
   ``docs/conf.py`` files. Native ``SKILL.md`` files remain only in the
   selected harness tree; another harness's methodology directories are never
   written. ``vscode``, ``opencode``, and ``claude`` are the production-parity
   targets. ``qoder`` is the experimental, installable target: it writes only
   the final archive defined by the Qoder Staging Contract in
   SYSP_SPEC_HARNESS_TARGET_MATRIX. It is an Installer-owned final
   project artifact, not a direct live-load path or an executable helper. The
   Installer verifies archive format, manifest inventory, and digest, and
   this deterministic staging is Qoder's complete, accepted installability
   evidence for this change. The Installer has no documented non-interactive
   Qoder import/install operation. It therefore never performs or claims
   native import, never hand-edits user-global configuration, and reports
   Qoder staging separately from external Qoder UI acceptance; native import
   and Manager-to-Engineer orchestration parity for Qoder are explicitly
   deferred to a future change, not silently dropped.

   **Explicitly excluded (NEVER copied to user projects):**

   * ``docs/syspilot/`` — syspilot-internal specification sources
   * ``docs/changes/`` — syspilot change documents
   * ``syspilot/sphinx/`` — syspilot build scripts for its own docs (not user product)
   * ``syspilot/bootstrap.json`` — deprecated bootstrap manifest
   * Any other path not listed above

   The Installer SHALL NOT copy any file or directory not listed in this scope,
   regardless of what exists in the product source. In particular, upstream
   ``.github/`` is an installed instance and SHALL NOT be read as source or
   used to derive inventory. The shipped adapter engine declared by
   SYSP_SPEC_INSTALLER_ADAPTER_ENGINE is executed from its remote raw URL for
   initial installation and refreshes its stable local copy from the selected
   revision; it is not part of source-directory enumeration.


.. spec:: Installer Doc Bootstrap
   :id: SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP
   :status: implemented
   :tags: agent-v2, installer, doc-bootstrap
   :links: SYSP_REQ_INSTALLER_DOC_BOOTSTRAP

   **Behavior:**

   During the Configure step (Workflow Step 6), the Installer SHALL:

   1. Check whether ``docs/index.rst`` exists in the target project.
   2. If **not present**: create ``docs/index.rst`` with the following minimal content:

      .. code-block:: rst

         Welcome to Project Documentation
         =================================

         This is the documentation base for this project.

         .. toctree::
            :maxdepth: 2
            :caption: Contents:

   3. If **already present**: do nothing — the existing file is never modified.
   4. Check whether ``docs/conf.py`` exists in the target project.
   5. If **not present**: create ``docs/conf.py`` with the following minimal
      validation-ready content:

      .. code-block:: python

         project = "Project Documentation"
         extensions = ["sphinx_needs"]

   6. If **already present**: do nothing — the existing file is never modified.

   **Input:** Target project directory
   **Output:** Non-overwritten ``docs/index.rst`` and ``docs/conf.py`` files
   sufficient for a fresh Sphinx project to load ``sphinx_needs``


.. spec:: Installer Deterministic Adapter Engine
   :id: SYSP_SPEC_INSTALLER_ADAPTER_ENGINE
   :status: approved
   :tags: agent-v2, installer, adapter, implementation, deterministic
   :links: SYSP_REQ_HARNESS_CONTENT_SINGLE_SOURCE, SYSP_REQ_HARNESS_NATIVE_INSTALL, SYSP_REQ_INSTALLER_DUTIES, SYSP_REQ_INSTALLER_WORKFLOW, SYSP_REQ_INSTALLER_GITHUB_SOURCE, SYSP_REQ_INSTALLER_DIRECT_OPS, SYSP_REQ_INSTALLER_ENCODING

   **Ownership:**

   The deterministic installation implementation SHALL be the
   version-controlled product module ``syspilot/installer.py``. Initial
   installation executes that module directly from the selected repository and
   branch's raw URL; during the same transaction it writes those exact bytes to
   the stable installed runtime path ``.syspilot/installer.py``. This module is a final shipped
   product artifact, not a run-generated wrapper, helper, temporary file, or
   intermediary target artifact.

   The module SHALL contain PEP 723 inline script metadata with an exact
   Python compatibility requirement and exact dependency versions for the
   release series, including YAML, Sphinx, and sphinx-needs. ``uv`` resolves
   that metadata into its external user cache. The engine SHALL NOT require or
   create a target-repository ``.venv``, dependency directory, or package
   cache, and SHALL NOT depend on globally installed Python packages.

   **Invocation contract:**

   Initial installation is invoked from the target Git repository root through
   this externally observable command contract::

      uv run --no-project "https://raw.githubusercontent.com/<owner>/<repository>/<branch>/syspilot/installer.py" install --repository <repository> --branch <branch> --target <target-root> --harness <harness>

   Installed Setup performs updates through the stable local runtime::

      uv run --no-project .syspilot/installer.py install --repository <repository> --branch <branch> --target <target-root> --harness <harness>

   ``uv`` is the sole Python runtime, environment, and package entry point.
   Setup, Installer, tests, and shipped Python tools exercised by this feature
   SHALL use ``uv run`` and SHALL NOT invoke bare ``python``, ``python3``,
   ``pip``, ``pip3``, or ``sphinx-build``. Package install or update guidance,
   when needed outside automatic PEP 723 resolution, SHALL use ``uv`` only.
   The module returns a structured per-target summary and a success/failure
   result. It SHALL NOT select a branch independently or fall back after an
   explicit branch value has been supplied.

   Repository-input grammar and the fixture-only local snapshot boundary are
   owned by SYSP_SPEC_INSTALLER_GITHUB_SOURCE; the engine invokes that source
   contract without adding filesystem fallback semantics.

   **Required implementation delta:** The current baseline supports only
   ``vscode`` and ``opencode``. Implementation SHALL extend the public
   ``--harness`` selector and every public install/checkpoint validation path
   in ``syspilot/installer.py`` to accept exactly ``vscode``, ``claude``,
   ``opencode``, and ``qoder``. It SHALL map ``claude`` to the established
   ``.claude/{agents,skills}`` output and ``qoder`` to only
   ``.syspilot/qoder/syspilot-qoder-plugin.zip``; it SHALL not map Qoder to a
   live ``.qoder/`` tree. The implementation SHALL add deterministic package
   construction, manifest/inventory/digest validation, summary status
   ``staged``, target-plan/checkpoint inclusion, update replacement, and
   rollback restoration for that final archive. These are implementation
   requirements, not claims about current code.

   The installed Setup source/template and each harness adaptation mapping
   SHALL forward the selected value unchanged to this public selector. Their
   shipped invocation text SHALL name Claude Code canonically and shall not
   classify Claude Code or Qoder as unsupported or experimental. No component
   may synthesize a Qoder native-import result because no documented
   programmable Qoder import/delegation/result API exists. The Dev Engineer
   owns these source, selector, Setup-forwarding, harness-mapping, archive,
   transaction, and invocation-artifact changes; this design owns the required
   contract only.

   **Deterministic data flow:**

   1. Resolve the selected branch to one upstream revision and enumerate only
      ``syspilot/agents``, ``syspilot/prompts``, ``syspilot/skills``, and
      ``syspilot/templates`` at that revision. Reject inventory entries outside
      those roots; never enumerate upstream ``.github``. This and the next
      three steps are read-only with respect to the target repository.
   2. Fetch every selected source as bytes from that same revision. Parse the
      first YAML frontmatter block with a YAML parser after UTF-8 decoding;
      ad-hoc regular-expression or line-fragment YAML parsing is prohibited.
   3. Define the methodology body as every byte after the closing frontmatter
      delimiter line and its line ending. Preserve those bytes unchanged,
      including empty bodies and the presence or absence of the terminal
      newline at EOF.
   4. Apply the target matrix and harness transformations to structured
      frontmatter and filenames in memory. Preserve source ``group`` metadata
      for Installer mutual-exclusion decisions even when the selected harness
      omits that unsupported field. Serialize generated frontmatter as UTF-8
      without BOM, then append the unchanged source body bytes except for the
      designated orchestration binding defined by
      SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER. Files whose content requires no
      adaptation are copied byte-for-byte.
   5. For ``qoder``, build the final archive defined by the Qoder Staging
      Contract entirely in memory, validate its ZIP structure, ``plugin.json``
      manifest, normalized member inventory, and digest, and include only the
      final archive in the target plan. Do not invoke a Qoder CLI/API or infer
      native acceptance from this validation.
   6. Build and freeze one complete target plan in memory. The plan names every
      write, orphan deletion, shared resource, missing-only docs creation, and
      Git index entry and includes expected pre-state identities. It rejects
      collisions and validates every path through
      SYSP_SPEC_INSTALLER_DIRECT_OPS immediately before checkpoint creation.
      No source parse, transformation, path derivation, or plan validation
      occurs after this step.
   7. Write each planned final target atomically without creating a persistent helper
      or intermediary target file only after the complete transaction
      checkpoint exists, enforce Skill mutual exclusion from source metadata,
      remove only eligible syspilot orphans, and accumulate
      installed/updated/removed counts per target directory.
   8. Return the summary directly to the invoking command or Setup; commit and
      success reporting remain gated by SYSP_SPEC_INSTALLER_WORKFLOW and
      SYSP_SPEC_INSTALLER_ROLLBACK. No Installer-agent invocation is required.

   **Sphinx subprocess contract:**

   The install command SHALL launch warning-as-error Sphinx validation by
   re-entering the same PEP 723 script through ``uv``::

      uv run --no-project .syspilot/installer.py validate-sphinx --target <target-root> --output <os-temp>/html --doctrees <os-temp>/doctrees

   The validation subcommand imports and runs Sphinx from the uv-managed
   script environment. The parent SHALL NOT launch ``sys.executable -m
   sphinx`` or bare ``sphinx-build``. Build output, doctrees, uv environments,
   and dependency caches remain outside the target repository.

   **Test surface:**

   Source enumeration, YAML mapping, filename conversion, exact body/EOF
   preservation, UTF-8-no-BOM output, orphan cleanup, and summary calculation
   SHALL be exposed as deterministic functions callable by fixture-based tests
   without invoking an LLM or a harness. Fixtures SHALL include upstream
   ``syspilot/`` and misleading upstream ``.github/`` trees, YAML values that
   require real parsing, bodies both with and without a terminal newline,
   nested Skill files, orphan candidates and protected customer/tailoring
   files, and every supported harness. Assertions compare output bytes and
   structured summaries, not prose fragments in Installer instructions.


.. spec:: Installer Skill Mutual Exclusion
   :id: SYSP_SPEC_INSTALLER_SKILL_MUTEX
   :status: implemented
   :tags: agent-v2, installer, skill, mutex
   :links: SYSP_REQ_SETUP_SKILL_MUTEX

   **Behavior:**

   Before writing a Skill that declares a ``group:`` field, the Installer SHALL
   enforce mutual exclusion through replacement:

   1. **Detect group** — Read the ``group:`` field from the incoming Skill's
      YAML frontmatter. If no ``group:`` field is present, skip the Mutual
      Exclusion step and proceed.
   2. **Scan installed Skills** — Enumerate all ``SKILL.md`` files in the
      ``.github/skills/`` directory (or the configured skills directory) and
      read their ``group:`` frontmatter field.
   3. **Replace** — If any installed Skill declares the same ``group:`` value as
      the Skill being installed, remove that existing Skill before writing the
      new one, and record the replacement for the run summary:

      .. code-block:: text

         Replacing Skill of group '<group>':
         removed '<installed-skill-name>' → installing '<incoming-skill-name>'.

   4. **Proceed** — Write the new Skill. After this step exactly one Skill of
      the group is present.

   **Input:** Skill to be installed (path to ``SKILL.md``)
   **Output:** Exactly one Skill of the group installed; replacement (if any) reported


.. spec:: Installer Workflow
   :id: SYSP_SPEC_INSTALLER_WORKFLOW
   :status: approved
   :tags: agent-v2, installer, workflow
   :links: SYSP_REQ_INSTALLER_WORKFLOW, SYSP_SPEC_INSTALLER_SCOPE, SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP, SYSP_REQ_INSTALLER_GITHUB_SOURCE, SYSP_REQ_INSTALLER_ROLLBACK, SYSP_REQ_INSTALLER_ENCODING, SYSP_REQ_INSTALLER_DIRECT_OPS, SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER

   **Workflow:**

   1. **Select Source and Harness** — Receive repository, branch, target-root,
      and one explicit harness from the CLI or Setup. Default branch is
      ``main``. The public harness values are exactly ``vscode``, ``claude``,
      ``opencode``, and ``qoder``. No local product tree or installed harness
      directory is offered as source, and no additional harness is inferred
      from directory presence.

   2. **Check Dependencies** — Before Setup or Installer mutates an
      installation target, execute ``uv --version`` and ``git --version``.
      Never probe bare ``python``, ``python3``, ``pip``, ``pip3``, or
      ``sphinx-build``. Use the PEP 723 ``uv run --no-project`` contracts in
      SYSP_SPEC_INSTALLER_ADAPTER_ENGINE to resolve and verify Python, Sphinx,
      sphinx-needs, and YAML dependencies before checkpoint creation. A missing
      executable or failed uv resolution stops without a final commit, success
      report, or checkpoint residue.

   3. **Acquire, Adapt, and Plan Read-Only** — Resolve one upstream revision;
      enumerate, fetch, parse, and transform all selected product sources in
      memory; derive every write/delete; validate every lexical and physical
      target path; and freeze the complete immutable target plan. These
      operations SHALL finish before checkpoint creation and SHALL NOT mutate
      the target repository. Any failure stops with zero target mutation and no
      checkpoint residue.

   4. **Pre-Install Snapshot** — After read-only source acquisition and before
      the runtime performs any target mutation, it
      creates the rollback checkpoint described by
      SYSP_SPEC_INSTALLER_ROLLBACK. It captures only planned entries in the
      explicitly selected harness tree, ``.syspilot/installer.py``, shared
      ``.syspilot/{templates,skills}`` resources, missing-only documentation
      files, and exact Git metadata/index entries required by the transaction.
      It never snapshots the whole project or an entire mutable parent merely
      because one child is planned. Supplied-checkpoint validation is governed
      by SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT.

   5. **Install/Update** — Continue within
      SYSP_SPEC_INSTALLER_ADAPTER_ENGINE after the remote or local command has
      entered the ``install`` subcommand. Using the read-only source snapshot
      from Step 3, it refreshes ``.syspilot/installer.py`` from that same
      revision and executes only the frozen plan for the explicit harness per
      SYSP_SPEC_INSTALLER_HARNESS_TARGETS. It does not parse, transform,
      discover, or add targets after checkpoint creation.

      Every methodology body is written byte-for-byte from upstream. Parsed
      frontmatter fields come from upstream and are transformed only as
      required by the selected harness; no local field is preserved. The
      product source is the single source of truth for every file's behavior.

      All files are written as UTF-8 without BOM. Methodology body bytes and
      EOF-newline state are preserved exactly. No wrapper scripts, temporary
      helpers, or intermediary target artifacts are generated.

      For ``qoder``, this step guarantees only a valid staged archive and its
      reversible project state, which is Qoder's complete, accepted
      installability evidence at the experimental tier for this change.
      Native import acceptance is external Qoder UI work, and
      Manager-to-Engineer orchestration parity for Qoder is deferred future
      scope; neither is reported as completed installation or production
      parity.

   6. **Configure** — Set up Sphinx. Perform doc bootstrap per
      SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP: create missing ``docs/index.rst`` and
      ``docs/conf.py`` only; never overwrite either. Deterministically install
      ``syspilot.orchestration-subagent``; do not inspect Jarvis state or ask
      the user to choose an orchestration variant.

   7. **Orphan Cleanup** — For each directory in installation scope,
      enumerate the eligible files in the target directory — those whose name
      starts with ``syspilot.`` and does not end with ``.tailoring.md`` — and
      compare against the source directory before checkpoint creation. Remove
      only an eligible file already present in the frozen plan. Files whose
      name does not start with ``syspilot.`` (customer-owned, project-specific)
      and ``syspilot.*.tailoring.md`` instance tailoring files are never
      removed, nor are user-created files outside the installation scope
      directories.

   8. **Summary** — Output a per-directory run summary table with counts of:
      installed (new files), updated (overwritten files), removed (orphans).
      Example format:

      .. code-block:: text

         | Directory       | Installed | Updated | Removed |
         |-----------------|-----------|---------|---------|
         | agents/         |         0 |       3 |       0 |
         | prompts/        |         0 |       2 |       0 |
         | skills/         |         1 |       0 |       0 |
         | templates/      |         0 |       1 |       1 |

   9. **Validate** — Require the engine to execute the exact
      ``uv run --no-project .syspilot/installer.py validate-sphinx`` subprocess
      contract from SYSP_SPEC_INSTALLER_ADAPTER_ENGINE. On failure, restore the
      checkpoint from Step 4 and report the failure to the invoking agent.

   10. **Commit, Clean, and Report** — Only after successful validation,
         create the final post-install commit documenting the installation,
         delete the checkpoint artifact, then emit the success report and
         summary. A failure after commit creation but before checkpoint deletion
         restores pre-install HEAD, index, and worktree state. No earlier step
         may report success.

   **Failure Handling:**

   On any failure after Step 4 and before checkpoint deletion in Step 10, the
   Installer SHALL restore transaction-owned paths and exact Git state from
   Step 4, preserve paths outside the plan, delete the checkpoint artifact,
   and report the failure without a retained installation commit or success
   result. A detected concurrent conflict inside a planned path is reported
   without silently overwriting the conflicting bytes. A dependency failure
   before script execution occurs before mutation and creates no checkpoint.
   See
   SYSP_SPEC_INSTALLER_ROLLBACK for the full transactional model.

   **Reliability gate:** The complete Installer suite is rerun after every
   correction pass. Normal process completion is required; an abrupt exit,
   worker loss, timeout, or operating-system termination is recorded with exit
   status and available stderr/system diagnostics, investigated, and rerun
   after the cause is addressed. Fixture generation, checkpointing, and state
   comparison enumerate only selected source entries and declared mutable
   paths. They do not recursively copy, hash, or retain unrelated repository
   content, and parallelism is explicitly bounded so memory and handle use do
   not scale with an unrelated target tree.

   **Input:** User request to install or update syspilot (forwarded by Bootloader)
   **Output:** Working syspilot installation + baseline commit


.. spec:: Installer Orchestration Variant Selection
   :id: SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT
   :status: deprecated
   :tags: agent-v2, installer, orchestration, skill
   :links: SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT

   **Behavior:**

   This design is deprecated. The replacement behavior is
   SYSP_SPEC_HARNESS_ORCHESTRATION_ADAPTER: every installation selects the
   synchronous variant deterministically without inference or user choice.


.. spec:: Installer Actor Creation
   :id: SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD
   :status: deprecated
   :tags: agent-v2, installer, session, scaffold
   :links: SYSP_REQ_INSTALLER_SESSION_SCAFFOLD

   **Behavior:**

   This design is deprecated. Installation creates no actors or session
   scaffolds. The replacement behavior is SYSP_SPEC_INSTALLER_WORKFLOW, which
   leaves all pre-existing user-owned actor and session state untouched.


.. spec:: Installer GitHub-Only Source
   :id: SYSP_SPEC_INSTALLER_GITHUB_SOURCE
   :status: approved
   :tags: agent-v2, installer, source
   :links: SYSP_REQ_INSTALLER_GITHUB_SOURCE

   **Behavior:**

   The Installer SHALL always acquire product files from the upstream GitHub
   repository using raw content URLs. The base URL pattern is:

   .. code-block:: text

      https://raw.githubusercontent.com/<org>/<repo>/<branch>/syspilot/<path>

   **Rules:**

   1. Default branch is ``main``.
   2. Branch override is accepted only when explicitly provided by the user
      at runtime and is passed through unchanged by Setup. The same branch
      governs the remote script URL, source enumeration, and every product-file
      fetch. No branch-selection dialog is offered by the Installer itself.
   3. Inventory is enumerated only below the selected revision's
      ``syspilot/{agents,prompts,skills,templates}`` roots. No local
      ``syspilot/`` directory, upstream ``.github/`` installed instance, or
      target harness directory is ever read or offered as source.
   4. All enumeration and content fetches are pinned to the same resolved
      upstream revision so a branch movement cannot mix source versions.
   5. No Mode-Detect step exists — the Installer does not compare installed
      vs. source versions. It always installs the latest upstream content.
   6. Resolve a branch through the GitHub API to one commit SHA before tree
      enumeration. Every API tree request and raw-content request uses that
      immutable SHA; reject truncated/incomplete inventories, missing roots,
      duplicate destinations, and entries outside the approved product roots
      before checkpoint creation.
   7. Parse public repository input before any filesystem lookup. Accept only
      two path components in ``owner/repository`` form or a supported HTTPS URL
      whose host is exactly ``github.com`` and whose path identifies those two
      components, optionally ending in ``.git``. Reject dot segments, local
      relative/absolute paths, UNC/drive forms, ``file:`` URLs, credentials,
      query/fragment data, and all other hosts. Existence of a same-named path
      below the target or current directory never changes this decision.
   8. Local source is test infrastructure only. An internal immutable
      ``SourceSnapshot.from_directory`` fixture constructor may create the same
      already-resolved byte inventory for unit tests, but public CLI and
      production ``acquire_source`` semantics never accept a directory.

   **Input:** Branch name (default ``main``)
   **Output:** Files fetched from upstream GitHub


.. spec:: Installer File Encoding
   :id: SYSP_SPEC_INSTALLER_ENCODING
   :status: implemented
   :tags: agent-v2, installer, encoding
   :links: SYSP_REQ_INSTALLER_ENCODING

   **Behavior:**

   Every file written by the Installer — whether fetched from upstream or
   generated (e.g. ``docs/index.rst``) — SHALL be encoded as UTF-8 without BOM.

   **Implementation constraint (PowerShell):**

   On PowerShell, the Installer SHALL use an encoding method that produces
   UTF-8 without BOM. The default ``Out-File`` encoding (which adds BOM on
   Windows PowerShell 5.x) SHALL NOT be used without explicit UTF-8-no-BOM
   override.

   **Verification:** No output file SHALL contain the byte sequence
   ``EF BB BF`` at position 0.


.. spec:: Installer Direct File Operations
   :id: SYSP_SPEC_INSTALLER_DIRECT_OPS
   :status: implemented
   :tags: agent-v2, installer, file-ops
   :links: SYSP_REQ_INSTALLER_DIRECT_OPS

   **Behavior:**

    The Installer SHALL fetch, transform, and write each final file through the
    version-controlled ``syspilot/installer.py`` implementation defined by
    SYSP_SPEC_INSTALLER_ADAPTER_ENGINE. The implementation uses structured HTTP,
    YAML, and byte-oriented file APIs directly; it is product logic rather than
    a generated installation helper.

   **Prohibitions:**

   * SHALL NOT generate wrapper scripts (e.g. ``install.ps1``, ``install.sh``,
     ``update.ps1``)
   * SHALL NOT write helper files to ``temp/``, ``$env:TEMP``, or any other
     temporary or intermediate location
   * SHALL NOT produce batch files, shell scripts, or any executable artifact
     as part of the installation process
   * SHALL NOT accept an absolute, drive-relative, UNC, or ``..``-escaping
     target path
   * SHALL NOT follow a symlink, junction, mount point, or other reparse point
     in mutable path ancestry during write, delete, cleanup, or restore

   The stable ``.syspilot/installer.py`` copy installed by the remote entry
   command is a final installed product runtime and is therefore not an
   intermediary artifact. No other executable file is emitted by a run.

   **Containment and mutation algorithm:** Resolve and retain the existing
   target-root identity without following a caller-supplied child path. For
   each frozen relative destination, reject non-relative and lexically escaping
   forms. At the mutation boundary, reopen the root and each existing parent
   with no-follow semantics, reject symbolic links and platform link-like
   objects, and compare every reopened identity with the frozen ancestry.
   Recheck after creating a parent and immediately before the final write,
   replace, delete, or restore. Create an atomic temporary file with exclusive
   creation only inside the verified real final parent; retain that parent
   identity and revalidate it before replacing the destination. Delete and
   restore use the same reopened-parent and final-component no-follow checks.
   Any mismatch or unsupported primitive fails closed before the final
   operation and never retries through a path that could escape the target.

   On POSIX, every write, temporary-file creation, replace/rename, unlink,
   directory creation/removal, cleanup, and restore SHALL operate relative to
   opened target-root or parent directory descriptors. Each ancestry component
   is opened relative to the preceding descriptor with ``O_DIRECTORY`` and
   ``O_NOFOLLOW`` where the host exposes them; final operations use
   ``dir_fd``/``*at`` equivalents and never resolve the mutable destination
   again from a pathname. A host/runtime lacking the descriptor-relative or
   no-follow primitive required for a planned mutation fails closed before
   mutation; pathname revalidation immediately before a path-based operation
   is not a permitted POSIX fallback. This preserves the opened directory
   object even if an attacker renames or replaces its pathname after validation.

   On Windows, ``pathlib.resolve``, ``lstat``, and ``os.replace`` alone are not a
   sufficient boundary. A narrow ``ctypes`` Win32 layer opens each component
   with ``CreateFileW`` using ``FILE_FLAG_OPEN_REPARSE_POINT`` and
   ``FILE_FLAG_BACKUP_SEMANTICS``, rejects reparse tags, records volume/file
   identity, and uses handle-relative rename/disposition APIs where supported.
   Where Windows cannot complete an operation relative to the verified handle,
   it reopens and compares the full parent identity immediately before the
   single final path-based call and fails on any change. Deterministic test
   hooks swap a parent for a junction/reparse point between plan validation,
   temporary-file creation, identity revalidation, and each final operation;
   every injected race must fail without changing an external sentinel. These
   handle/reparse checks and the documented last-moment identity fallback are
   the Windows equivalent and are unchanged by the POSIX descriptor rule.

   Git metadata outside the worktree is mutable only when returned by the exact
   Git discovery commands in SYSP_SPEC_INSTALLER_ROLLBACK; it is never reached
   by traversing a target path.


.. spec:: Installer Transactional Rollback
   :id: SYSP_SPEC_INSTALLER_ROLLBACK
   :status: implemented
   :tags: agent-v2, installer, rollback, transaction
   :links: SYSP_REQ_INSTALLER_ROLLBACK

   **Behavior:**

   **Public supplied-checkpoint attempt gate** — Before dependency resolution,
   source acquisition or parsing, plan construction, target-root or plan
   comparison, and freshness validation, a public invocation that supplies a
   checkpoint identifier atomically consumes its capability or acquires a
   one-time lease. That lease is terminally revoked on every return or failure
   path. The runtime may retain non-authorizing records required for bounded
   cleanup and forensic reporting, but no retained record can authorize replay.

   1. **Dependency gate** — ``uv`` resolves the remote or local PEP 723 runtime
      before any target mutation. Failure leaves the workspace untouched,
      creates no direct-run checkpoint, terminally revokes any supplied
      capability, and prohibits a final commit or success report.

   2. **Read-only acquisition** — Source resolution, enumeration, fetch, parse,
      and transformation may complete before checkpoint creation because they
      do not mutate the target. Failure in this phase leaves the workspace
      untouched and creates no checkpoint residue. A supplied capability was
      already consumed by the public attempt gate and cannot be retried.

   3. **Pre-Mutation Checkpoint (Workflow Step 4)** — After the complete target
      plan passes validation, a direct run creates an atomic checkpoint below
      the operating system temporary directory. A supplied run uses the
      already-consumed trusted checkpoint state and cannot reactivate its
      public capability. The manifest contains only
      exact planned files and directories in the selected harness tree,
      ``.syspilot/installer.py``, shared ``.syspilot/{templates,skills}``
      resources, missing-only docs files, and exact Git metadata/index entries.
      Existing directories are represented by existence/type plus planned
      children, never recursive whole-tree copies. Unrelated project files are
      neither read into the checkpoint nor listed for restoration.

      Git state is discovered with ``git rev-parse --git-dir``, ``git
      rev-parse --git-path index``, and ``git rev-parse --symbolic-full-name
      HEAD`` together with an OID query that may fail for an unborn branch.
      The checkpoint records attached full ref plus OID, detached HEAD OID, or
      unborn full ref, and index bytes/existence. A ``.git`` directory is never
      assumed; linked-worktree Git paths may reside outside the target root and
      are accepted only as exact command results.

      Every manifest entry is stored in a map keyed only by one canonical
      target-relative representation: ``/`` separators, normalized components,
      and host case normalization. The case-preserving source spelling is a
      separate ``display_path`` value. The frozen expected-current map and all
      restore lookups use the same canonical-key function; no code indexes one
      map with display spelling or a differently normalized value.

      Every supplied or direct internal checkpoint is represented to callers by
      an opaque transaction identifier. Checkpoint creation records, outside
      the caller-controlled target, an expiring runtime-owned token bound by a
      process/runtime-created secret or equivalent signed/HMAC authentication
      to the target identity, canonical frozen plan, exact mutable-path and Git
      pre-state fingerprints, and creation/expiry times. The secret is neither
      derivable from checkpoint fields nor persisted in the target.

      For supplied checkpoints, the public attempt gate has already atomically
      consumed the token or acquired its one-time lease. Before the first
      mutation, verify authenticity, expiry, target/plan binding, and exactly
      this owned state without restoring public usability. A token already
      leased or consumed, expired, missing from trusted state, or failing
      authentication is rejected before mutation. Every terminal path revokes
      the lease and removes authorizing state. Unrelated paths are neither
      opened nor hashed.

   4. **Rollback trigger** — If any write, cleanup, summary, validation,
      commit, or checkpoint-deletion operation after the
      checkpoint and before final success fails, the runtime executes:

      .. code-block:: text

         restore <checkpoint-id>, pre-install HEAD, and Git index

   5. **Post-rollback state** — Restore only manifest entries. Remove a
      transaction-created directory only after its transaction-owned children
      are removed and only if it is empty. Preserve every unrelated child of a
      pre-existing mutable directory. The runtime records both pre-install Git
      state and, if it creates the installation commit, the exact post-commit
      ref or detached-HEAD OID it owns. Restore an attached ref with ``git
      update-ref <ref> <pre-oid> <created-oid>`` semantics, or the corresponding
      delete-with-expected-OID form for an unborn pre-state. Restore detached
      HEAD only if its current OID still equals the transaction-created OID.
      These are compare-and-swap operations: if the ref or HEAD advanced
      independently, preserve that history, report a rollback conflict, and do
      not force-reset or check out the old commit. Restore index and planned
      worktree entries only where their current identities still match the
      transaction's last recorded identities; otherwise preserve them and
      report the conflict.

      Before each write/delete, compare the current identity with the plan's
      expected identity. Before rollback, restore a path only if its current
      identity matches the transaction's last recorded identity. A mismatch is
      a concurrent-change conflict: preserve the conflicting bytes, restore all
      non-conflicting entries, remove checkpoint data, report incomplete
      rollback, and never report success. The Installer never silently discards
      external changes inside a mutable path.

   6. **Terminal cleanup** — On successful validation and final commit, delete
      the checkpoint before reporting success. After a handled failure, delete
      it after restoration. Neither path leaves checkpoint residue.

   **Input:** Runtime-owned checkpoint identifier (created in Workflow Step 4)
   **Output:** Either a clean post-install commit or a rolled-back workspace

   **Executable transaction tests:**

   Fixture-based tests SHALL run the real shipped adapter engine in isolated
   Git repositories and compare path existence, file bytes, HEAD, and reported
   status against a captured pre-state. At minimum they inject failure at the
   dependency gate, source fetch, YAML parse, runtime write, target write,
   orphan cleanup, documentation bootstrap, Sphinx validation, post-validation
   summary, commit, and post-commit checkpoint deletion. Dependency failure
   and read-only source-acquisition failures must cause zero mutation and no
   checkpoint residue. Separate supplied-checkpoint fixtures SHALL fail during
   dependency resolution, source acquisition, source parsing, the
   plan-construction stage that formerly preceded lease acquisition, and
   malformed-input handling; each then retries the same identifier from a
   separate process and proves replay rejection, zero target/Git mutation, and
   no authorizing residue. Every post-checkpoint failure must restore the exact
   pre-state and emit neither a retained installation commit nor success report.
   The suite SHALL additionally cover lexical escape, symlink/junction/reparse
   ancestry and deterministic parent-swap races at each mutation boundary,
   unrelated and concurrent files, checkpoint size independent of a large
   unrelated tree, Windows mixed-case supplied-checkpoint restore, authenticated
   token tampering, expiry, concurrent lease, replay rejection for supplied and
   direct internal checkpoints, independently advanced refs after the Installer
   commit, and attached/detached/unborn linked worktrees. POSIX race fixtures
   SHALL swap ancestry after the final validation and prove every write,
   replace, delete, cleanup, and restore remains anchored to opened descriptors
   and leaves an external sentinel byte-exact. The full suite must
   finish normally with bounded workers and no recursive processing of the
   unrelated tree. The success case must prove that validation ran successfully
   before the final commit and report became observable.


.. spec:: Installer Supplied Checkpoint Validation
   :id: SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT
   :status: implemented
   :tags: agent-v2, installer, rollback, checkpoint, validation
   :links: SYSP_REQ_INSTALLER_ROLLBACK, SYSP_SPEC_INSTALLER_WORKFLOW, SYSP_SPEC_INSTALLER_ROLLBACK

   **Behavior:**

   A caller-supplied checkpoint is accepted only before mutation and only when
   both of these comparisons succeed:

   * its recorded physically resolved target-root identity equals the current
     physically resolved target root; and
   * its mutable-path set equals the complete frozen plan's mutable-path set
     exactly, including the selected harness tree,
     ``.syspilot/installer.py``, every planned entry below
     ``.syspilot/skills/`` and ``.syspilot/templates/``, and planned
     missing-only documentation paths.

   **Canonical comparison and lookup:** Each entry is converted to a contained
   target-relative path, separators are normalized to ``/``, ``.`` components
   are removed, absolute, drive/UNC, empty, and ``..``-escaping forms are
   rejected, host filesystem case normalization is applied, and duplicate
   normalized entries are rejected before forming the set. That canonical string is the
   sole map key for stored entries, frozen expected-current identities, and
   restoration; original spelling is retained separately as ``display_path``.
   Exact set equality is required; neither a subset nor a superset is accepted.

   **Authenticated single-use binding:** The caller receives only an opaque,
   unforgeable transaction identifier. Trusted checkpoint state is stored
   outside the caller-controlled target and binds, using a process/runtime-
   created secret or equivalent signed/HMAC transaction token, the resolved
   target identity, canonical frozen plan, exact pre-state fingerprint of each
   mutable path, exact handoff Git state, and creation and expiry times. No
   long-lived authentication secret is persisted in the target, and callers
   cannot recompute a valid binding after editing checkpoint fields.

   At public-attempt entry, before dependency resolution, source acquisition or
   parsing, frozen-plan construction, target-root or plan comparison, and
   freshness validation, the runtime atomically consumes the supplied
   capability or acquires a one-time lease. Every success, rejection,
   exception, cancellation, and other terminal path irreversibly revokes that
   lease. A trusted registry operation may retain non-authorizing metadata for
   bounded cleanup and forensic reporting; malformed or attacker-chosen input
   cannot nominate another transaction's paths or erase its trusted state.

   Before the first mutation, the runtime verifies the consumed checkpoint's
   authenticator and expiry and recomputes only the declared path and Git
   fingerprints. The same identifier cannot be accepted concurrently or after
   any prior attempt, including dependency, source-acquisition, parse,
   plan-construction, root-mismatch, plan-mismatch, and freshness failures. A
   copied, replayed, expired, missing, tampered, stale same-plan,
   changed-owned-path, changed-index/ref/HEAD, or incomplete checkpoint is
   rejected without mutation. Direct internal checkpoints use the same
   authenticated, single-use state machine; they do not bypass validation
   because their identifier originated inside the runtime. Validation does not
   enumerate, read, or hash unrelated paths.

   A narrow, broad, mismatched-root, malformed, or duplicate-ambiguous
   checkpoint fails before the first target or Git mutation with zero target
   or Git-state change, no final commit, no success report, no authorizing
   checkpoint residue, and no reusable identifier.

   **Input:** Supplied checkpoint and complete frozen installation plan
   **Output:** Validated checkpoint identity or pre-mutation rejection


.. spec:: Installer Harness Targets
   :id: SYSP_SPEC_INSTALLER_HARNESS_TARGETS
   :status: approved
   :tags: agent-v2, installer, harness, targets
   :links: SYSP_REQ_HARNESS_NATIVE_INSTALL, SYSP_REQ_HARNESS_INSTALL_NO_REGRESSION, SYSP_REQ_HARNESS_PORTABILITY_NO_REGRESSION, SYSP_SPEC_HARNESS_TARGET_MATRIX, SYSP_SPEC_HARNESS_AGENT_ADAPTER, SYSP_SPEC_HARNESS_SKILL_ADAPTER, SYSP_SPEC_HARNESS_PROMPT_ADAPTER, SYSP_SPEC_INSTALLER_ADAPTER_ENGINE, SYSP_SPEC_INSTALLER_SCOPE, SYSP_SPEC_INSTALLER_WORKFLOW

   **Behavior:**

   1. **Select** — At the start of Workflow Step 5 (Install/Update), the
      Installer accepts exactly one explicit ``--harness`` value:

      Production-parity values are ``vscode`` for VS Code GitHub Copilot,
      ``claude`` for Claude Code, and ``opencode`` for OpenCode. ``qoder``
      for Qoder is the experimental, installable value: its accepted
      installability evidence is deterministic package staging: native
      import and Manager-to-Engineer orchestration parity are deferred to a
      future change. The Installer rejects every other value and never
      infers or adds targets from existing directories, installed
      applications, configuration, or environment-specific launcher names.

   2. **Adapt** — For the selected harness, invoke
      SYSP_SPEC_INSTALLER_ADAPTER_ENGINE to generate frontmatter per
      SYSP_SPEC_HARNESS_AGENT_ADAPTER (agents) and
      SYSP_SPEC_HARNESS_SKILL_ADAPTER (skills), and commands per
      SYSP_SPEC_HARNESS_PROMPT_ADAPTER. Reuse the exact source methodology
      body bytes, including terminal-newline state.

   3. **Write** — The adapted final files are written to the harness's native
      directory from SYSP_SPEC_HARNESS_TARGET_MATRIX (project scope, e.g.
      ``.claude/agents/`` or ``.opencode/skills/<name>/``), following the same UTF-8-no-BOM, direct-file-
      operation, and orphan-cleanup rules defined for the VS Code target
      (SYSP_SPEC_INSTALLER_ENCODING, SYSP_SPEC_INSTALLER_DIRECT_OPS). No
      generated wrapper, temporary helper, or intermediary target is written.
      Product templates and non-native Skill resources are written only to
      shared ``.syspilot/{templates,skills}`` paths; no unselected harness tree
      is created.

   4. **Report** — The per-directory run summary (Workflow Step 7) contains
      rows only for the explicit selected harness and shared runtime/docs paths.

   Clean installation, update, injected-failure restoration, rollback, and
   validation-gated commit behavior are identical for all four values and are
   owned by SYSP_SPEC_INSTALLER_ADAPTER_ENGINE, SYSP_SPEC_INSTALLER_WORKFLOW,
   and SYSP_SPEC_INSTALLER_ROLLBACK. Native discovery and loading are owned by
   SYSP_SPEC_HARNESS_TARGET_MATRIX and its UAT counterpart for the
   production-parity values; for ``qoder``, that ownership is limited to
   deterministic package-staging discovery, since native in-app loading is
   deferred future scope for this change.

   **Input:** Target project directory and explicit production harness
   **Output:** Native files for exactly the selected harness
