Installer Deterministic Runtime UAT
===================================

Acceptance coverage for the current deterministic Installer runtime.

.. story:: UAT: Installer Deterministic Runtime
   :id: SYSP_US_UAT_INSTALLER_SPEC_REWRITE
   :status: approved
   :priority: mandatory
   :tags: uat, installer, spec-rewrite
   :links: SYSP_US_INSTALLER, SYSP_US_HARNESS_INSTALL, SYSP_US_HARNESS_PORTABILITY

   **As a** syspilot Test Designer,
   **I want** to verify initial installation and update through the shipped
   deterministic runtime,
   **so that** every explicit harness installation is complete, repeatable,
   validated, and transactionally recoverable.

   **Scope:**

   This chain validates the active remote-runtime initial-install and stable
   local-runtime update model. It does not use Setup for initial installation,
   assume VS Code-only output, preserve local frontmatter, require a particular
   summary rendering, or accept Git reset/manual best-effort rollback.

   **Acceptance Criteria:**

   1. A clean installation executes the selected branch's remote PEP 723
      runtime with one explicit production harness and creates only that
      harness target plus shared runtime and missing-only documentation files.
   2. Repeating the identical command is idempotent: output remains correct,
      unchanged files are not rewritten, and no empty installation commit is
      created.
   3. Harness-required frontmatter is adapted deterministically, unsupported
      native fields are omitted, methodology body bytes and EOF state match
      source, and all written files are UTF-8 without BOM.
   4. Installation creates no wrapper, helper, intermediary target, target
      virtual environment, dependency cache, or documentation build output.
   5. Source resolution, enumeration, fetch, parse, and transformation are
      read-only and may precede checkpoint creation; a complete checkpoint
      exists before every target mutation, and every later injected failure
      restores exact HEAD, index, worktree, and path state.
   6. Warning-as-error Sphinx validation succeeds before the installation
      commit, checkpoint deletion, structured summary, and success result.
   7. Installed Setup updates by directly invoking the stable local runtime;
      no Installer-agent delegation or other agent mechanism participates.
   8. Filesystem containment rejects lexical escapes and symlink, junction, or
      other reparse-point ancestry before write, delete, or restore; rollback
      never follows an out-of-target link.
   9. Checkpoint and restore cover only declared mutable paths and exact Git
      metadata, preserve unrelated and concurrent files, bound work to that
      path set in large repositories, and fail safely on conflicting changes
      within a mutable path.
   10. Linked attached, detached, and unborn Git worktrees install and roll
       back exactly without assuming that ``.git`` is a directory.
   11. OpenCode executes SEND through its native Task binding while VS Code
       executes SEND through ``runSubagent``; both preserve one shared
       SEND/RECEIVE/RESPOND semantic contract.
   12. Harness-adapted Skills resolve stable shared resources, including the
       installed change-document template, without depending on ``.github``
       paths when another harness is selected.
   13. A network-conditional test acquires an actual revision and product
       inventory through the GitHub API and validates the same immutable
       revision and containment rules as fixture acquisition.
   14. A supplied checkpoint is rejected before mutation when its target root
       differs or its canonical mutable-path set is narrower or broader than
       the exact frozen plan; each rejection leaves target and Git state
       byte-exact and emits no success result.
   15. Supplied checkpoints use one platform-canonical lookup key and prove
       freshness with a nonce plus exact owned-path and Git fingerprints before
       mutation, without reading unrelated paths.
   16. Rollback uses compare-and-swap for Installer-created Git state and
       preserves independently advanced commits while reporting conflicts.
   17. Every mutation revalidates parent identity with no-follow primitives;
       deterministic parent-swap races fail closed without touching an escaped
       target.
   18. Public source selection remains GitHub-only even when a target-local
       relative path has the repository name; local directories are available
       only through an internal fixture snapshot API.
   19. The complete corrected suite terminates normally with bounded resource
       use; an abrupt run is investigated and rerun, never accepted as evidence.
   20. On POSIX, every mutation and restore remains anchored to opened target
       or parent directory descriptors after a deterministic ancestry swap;
       no pathname-only revalidation is accepted and no external path changes.
   21. Supplied and direct internal checkpoint identifiers are opaque,
       authenticity-protected, expiring, and single-use; tampering, concurrent
       use, expiry, or replay fails before target or Git mutation.
