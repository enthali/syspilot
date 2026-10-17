Installer Deterministic Runtime Test Data
=========================================

Test data for ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE``.

.. req:: UAT Test Data: Installer Deterministic Runtime
  :id: SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE
  :status: approved
  :links: SYSP_US_UAT_INSTALLER_SPEC_REWRITE

   **Required Artifacts:**

   * The selected revision's ``syspilot/installer.py`` and product
     ``syspilot/{agents,prompts,skills,templates}`` roots.
   * ``SYSP_SPEC_INSTALLER_ADAPTER_ENGINE``,
     ``SYSP_SPEC_INSTALLER_WORKFLOW``, and
     ``SYSP_SPEC_INSTALLER_ROLLBACK``.
   * Isolated upstream and target Git fixtures for ``vscode``, ``claude``,
     ``opencode``, and ``qoder``.
   * Source files with structured YAML, source-only Skill ``group``/``tools``/
     ``triggers`` fields, and bodies with and without terminal newlines.
   * Pre-existing HEAD, staged/unstaged changes, untracked files, harness
     orphans, customer-owned files, and tailoring files for state comparison.
   * Failure hooks for dependencies, source resolution/fetch/parse, first
     target mutation, runtime and harness writes, docs bootstrap, cleanup,
     validation, summary, commit, and checkpoint deletion.
   * Supplied checkpoint fixtures with the correct target root and exact frozen
     mutable-path set, with one required path removed, with one undeclared path
     added, and with a different resolved target-root identity.
   * A command recorder, byte comparator, YAML parser, BOM scanner, Git state
     inspector, and checkpoint-directory inspector.
   * Lexical ``..`` escape, file/directory symlink, Windows junction, and other
     reparse-point fixtures in every mutable-path ancestry position supported
     by the host; unsupported fixture types are reported as skipped, not passed.
   * Pre-existing mutable files/directories, transaction-external concurrent
     writers, unrelated files inside and outside top-level mutable parents, and
     a large repository whose unrelated tree is measurably larger than the
     declared mutable set.
   * Main and linked-worktree fixtures in attached, detached, and unborn states,
     with recorded ``--git-dir``, ``--git-path index``, and symbolic HEAD data.
   * Isolated VS Code GitHub Copilot, Claude Code, OpenCode, and Qoder lifecycle
     fixtures that record selected-target installation, update, failure, and
     rollback state, plus installed shared templates used by change-launcher.
   * A network-conditional GitHub API fixture using a real public revision;
     absent network or rate-limit capacity produces an explicit skip.
   * Repository-input fixtures for ``owner/repository``, supported GitHub HTTPS,
     a target-local same-named relative directory, absolute/UNC/drive paths,
     ``file:`` URLs, and non-GitHub URLs, plus an internal immutable directory
     snapshot fixture unavailable through the public CLI.
   * Supplied and direct internal checkpoint fixtures with opaque identifiers,
     runtime-created secrets or signed/HMAC tokens, trusted state outside the
     target, short creation/expiry windows, exact target/plan/path/Git binding,
     concurrent lease attempts, copied consumed identifiers, and independently
     tampered fields with caller-recomputed unkeyed hashes.
   * Separate supplied-checkpoint failure fixtures for dependency resolution,
     source acquisition, source parsing, the plan-construction stage that
     formerly preceded lease acquisition, and malformed public inputs. Each
     fixture retains the identifier for a second-process replay attempt.
   * Deterministic mutation-boundary hooks that replace a verified parent with
     a symlink on POSIX after final validation and before descriptor-relative
     temp creation, replace, delete, cleanup, and restore; Windows fixtures use
     junction/reparse swaps against the existing handle/reparse contract.
   * A post-install concurrent-commit fixture and full-suite process/resource
     recorder for exit status, stderr, peak memory, handles, worker count, and
     enumerated/hashed paths.

   **Commands:**

   Initial installation SHALL use::

      uv run --no-project "https://raw.githubusercontent.com/<owner>/<repository>/<branch>/syspilot/installer.py" install --repository <repository> --branch <branch> --target <target-root> --harness <vscode|claude|opencode|qoder>

   Setup update SHALL invoke::

      uv run --no-project .syspilot/installer.py install --repository <repository> --branch <branch> --target <target-root> --harness <vscode|claude|opencode|qoder>

   **Captured Evidence:**

   * Resolved revision and complete source-request log.
   * Mutation log showing checkpoint existence before each target mutation.
   * Checkpoint inventory and byte count proving only declared mutable paths
     and exact Git metadata were captured.
   * Before/after HEAD, symbolic-ref, index bytes, path existence, and file
     bytes for every success and failure case.
   * Structured installed/updated/removed counts keyed by actual selected
     target and shared paths; no table rendering is required.
   * Child-process order proving validation precedes commit and success.
   * Before/after mutation and Git-state logs proving every invalid supplied
     checkpoint is rejected before the first mutation.
   * Ref compare-and-swap log and commit graph proving concurrent history is
     preserved, plus path-access logs proving freshness and resource checks do
     not read unrelated target content.
   * POSIX syscall instrumentation proving mutations use opened directory
     descriptors and no mutable destination is reopened by pathname, with an
     external sentinel comparison for every late ancestry-swap fixture.
   * Trusted token-state and lease logs proving exactly one consumer can acquire
     an identifier and every tampered, expired, concurrent, or replay attempt
     fails before the first target or Git mutation.
   * For every supplied-checkpoint failure fixture, first-attempt and
     second-process replay logs plus before/after target, Git, and trusted-state
     inventories proving terminal capability revocation, zero mutation, and no
     authorizing checkpoint residue.

   **Lifecycle Acceptance Ownership:**

    This requirement is the exclusive normative UAT owner for clean installation, update, injected-failure, and rollback acceptance. For each of ``vscode``, ``claude``, ``opencode``, and ``qoder``, evidence SHALL independently prove a clean installation, an update from an earlier revision, an injected post-checkpoint failure, and exact rollback of target and Git state.

    Live native discovery and loading acceptance is owned exclusively by ``SYSP_REQ_UAT_HARNESS_TARGET_MATRIX`` and SHALL NOT be inferred from this requirement's deterministic lifecycle evidence.

   **Preconditions:**

   * Git and ``uv`` are the only ambient installation prerequisites.
   * No product tree or Setup agent is pre-placed for initial installation.
   * Read-only acquisition hooks fire before checkpoint creation; mutation and
     later hooks fire only after checkpoint creation.
   * Parsing, transformation, containment, and complete target-plan validation
     hooks all fire before checkpoint creation.
   * Fixtures run separately for each explicit harness and never infer another
     target from directory presence.
   * Native POSIX descriptor-relative fixtures execute only on a capable POSIX
     host. On Windows they are recorded as conditional and unexecuted, never as
     runtime proof; platform-independent static or implementation evidence does
     not convert those skipped checks into passing UAT.
