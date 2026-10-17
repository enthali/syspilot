Installer Deterministic Runtime Expected Outcomes
=================================================

Expected outcomes for ``SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE``.

.. spec:: UAT Expected Outcomes: Installer Deterministic Runtime
  :id: SYSP_SPEC_UAT_INSTALLER_SPEC_REWRITE
  :status: approved
  :priority: mandatory
  :tags: uat, installer, spec-rewrite, expected-outcomes
  :links: SYSP_REQ_UAT_INSTALLER_SPEC_REWRITE, SYSP_SPEC_INSTALLER_DIRECT_OPS, SYSP_SPEC_INSTALLER_SUPPLIED_CHECKPOINT

   **TC-IDR-INITIAL - Remote-runtime clean installation**

  *Action:* Run the remote command against clean targets with ``--harness
  vscode``, ``--harness claude``, ``--harness opencode``, and ``--harness
  qoder`` separately.

   *Expected result:*

   * [ ] Every source request uses one resolved revision from the explicit
     repository and branch; no local product or installed harness tree is a source.
   * [ ] Each run writes only its explicit harness target or, for Qoder,
     exactly ``.syspilot/qoder/syspilot-qoder-plugin.zip`` with the validated
     manifest and package digest,
     ``.syspilot/installer.py``, shared ``.syspilot/{skills,templates}``
     resources, and missing-only documentation bootstrap files.
   * [ ] The stable runtime bytes equal the selected revision's runtime bytes.
   * [ ] Validation succeeds before one installation commit and success result.
   * [ ] Each harness has an independent result; a Claude Code or Qoder failure
     cannot be masked by another harness's pass.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-1

   ---

   **TC-IDR-UPDATE - Idempotent repeated command**

  *Action:* Repeat each successful command unchanged for all four harnesses,
  then invoke each installed Setup entry with the same inputs.

   *Expected result:*

   * [ ] The repeat reports zero content changes and creates no commit.
   * [ ] Setup records the stable local-runtime command and reaches the same state.
   * [ ] No Agent, Task, ``runSubagent``, SEND, or Installer-agent invocation
     appears in the command record.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-2, AC-7

   ---

   **TC-IDR-ADAPT - Deterministic native output**

   *Action:* Parse generated frontmatter, compare bodies with source, and scan
   every managed output for a BOM.

   *Expected result:*

   * [ ] VS Code files are byte-identical where adaptation is unnecessary.
   * [ ] OpenCode output matches adapter contracts; unsupported Skill
     ``group``, ``tools``, and ``triggers`` are omitted while source ``group``
     metadata still enforces mutual exclusion.
   * [ ] Every body and EOF-newline state matches source and no output begins
     with ``EF BB BF``.
   * [ ] Locally edited frontmatter is deterministically replaced, not preserved.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-3

   ---

   **TC-IDR-ARTIFACTS - No generated execution residue**

   *Action:* Recursively inspect the target and command record after both runs.

   *Expected result:*

   * [ ] No wrapper, helper, intermediary, ``.venv``, target dependency cache,
     ``__pycache__``, or ``docs/_build`` exists.
   * [ ] The only installed executable product artifact is the final stable runtime.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-4

   ---

   **TC-IDR-BOUNDARY - Read-only acquisition and protected mutation**

  *Action:* For each of the four harness values, inject source
  resolution/fetch/parse failures before the checkpoint, then inject every
  mutation and later failure after it.

   *Expected result:*

   * [ ] Source acquisition and in-memory transformation perform no target mutation.
   * [ ] Structured parsing, transformation, path containment, and the complete
     target plan finish before checkpoint creation.
   * [ ] Every pre-checkpoint failure leaves exact target and Git state and no residue.
   * [ ] A scoped checkpoint containing only declared mutable paths and exact
     Git metadata exists before every target mutation.
   * [ ] Every post-checkpoint failure, including after commit but before
     checkpoint deletion, restores exact HEAD, symbolic ref, index,
     tracked/untracked bytes, and path existence.
   * [ ] Rollback deletes the checkpoint and emits no retained commit or success;
     Git reset and manual recovery are not acceptance evidence.
   * [ ] After the Installer commit, an independently created concurrent commit
     advances the same ref; injected rollback reports a conflict, preserves the
     concurrent commit and ancestry, and restores only non-conflicting owned
     file/index state using compare-and-swap.
   * [ ] Clean installation, update, injected-failure restoration, and rollback
     are each reported separately for Claude Code production installation and
     Qoder experimental-tier package staging.
     The Qoder result is ``staged`` only; it never reports native import or a
     completed external Qoder UI lifecycle. Qoder Manager-to-Engineer
     orchestration is out of scope for this change and explicitly deferred to
     a future change, not a gate cleared or blocked here.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-5

   ---

   **TC-IDR-CONTAINMENT - Lexical and physical escape rejection**

   *Action:* Run each planned write, orphan deletion, and rollback case against
   lexical ``..``/absolute/drive/UNC escapes and against symlink, Windows
   junction, mount-point, and reparse-point ancestry fixtures.

   *Expected result:*

   * [ ] Every supported escape fixture fails before write, delete, or restore.
   * [ ] No external sentinel changes and no out-of-target link is followed.
   * [ ] Unsupported host fixture types are explicitly skipped, not passed.
   * [ ] Any post-checkpoint rejection restores non-conflicting planned paths
     and deletes checkpoint data without reporting success.
   * [ ] Deterministic race hooks replace each destination parent with a
     junction/reparse point after validation and before temporary-file create,
     replace, delete, and restore; every case fails closed and leaves the
     external sentinel byte-exact.
   * [ ] On POSIX, a second race hook swaps ancestry after the final identity
     validation for temporary-file creation, write/replace, delete, cleanup,
     and restore. Syscall evidence shows every operation remains relative to
     an opened target/parent directory descriptor, uses ``O_DIRECTORY`` and
     ``O_NOFOLLOW`` where available, never falls back to the mutable pathname,
     and leaves the external sentinel byte-exact.
   * [ ] Native POSIX execution is conditional on a capable POSIX host. On
     Windows these checks are recorded as unexecuted conditional UAT and are
     not reported as runtime proof.
   * [ ] On Windows, the existing handle identity and reparse-point checks are
     exercised unchanged as the platform-equivalent containment boundary.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-8

   ---

   **TC-IDR-SCOPED - Bounded checkpoint and concurrent preservation**

   *Action:* Install in a large repository containing unrelated files inside
   and outside mutable parents. Create unrelated files after checkpoint
   creation and inject external changes to both an unplanned path and a planned
   path before rollback.

   *Expected result:*

   * [ ] Checkpoint inventory contains only selected-harness planned entries,
     exact shared runtime/resources, planned missing-only docs, and exact Git
     metadata; its file count and bytes do not scale with the unrelated tree.
   * [ ] Unrelated and concurrently created unplanned files remain byte-exact.
   * [ ] A transaction-external change to a planned path is detected, preserved,
     and reported as an incomplete rollback conflict rather than overwritten.
   * [ ] Pre-existing mutable directories retain every unplanned child, and a
     transaction-created directory is removed only when empty.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-9

   ---

    **TC-IDR-SUPPLIED-CHECKPOINT - Coverage, identity, authenticity, and freshness**

    *Action:* Supply checkpoints to separate public attempts that fail during
    dependency resolution, source acquisition, source parsing, the
    plan-construction stage that formerly preceded lease acquisition, and
    malformed-input handling. After each failure, present the same identifier
    from a separate process. Also supply one checkpoint with the exact canonical
    mutable-path set and target-root identity, one omitting a planned OpenCode
    agent or shared runtime/resource path, one adding an undeclared target path,
    one recording a different resolved target root, one using mixed-case
    display paths on Windows, and stale same-plan checkpoints after changing an
    owned file, index, HEAD/ref, token, fingerprint, creation time, or expiry.
    Independently tamper with each bound field and recompute any caller-visible
    unkeyed hash; concurrently present one valid identifier; then replay it
    after successful and failed attempts. Repeat the token, tamper, expiry,
    lease, and replay cases for a direct internal checkpoint.

   *Expected result:*

   * [ ] The exact checkpoint is accepted only when its normalized path set is
     equal to the complete frozen plan.
   * [ ] The narrow, broad, and mismatched-root checkpoints are rejected before
     the first target or Git mutation.
   * [ ] Each rejection leaves the selected harness agent, stable runtime,
     ``.syspilot/skills/``, ``.syspilot/templates/``, documentation, HEAD,
     index, and worktree byte-exact to pre-run state.
   * [ ] Each rejection emits no commit or success result and leaves no
     checkpoint residue created by the rejected run.
   * [ ] On Windows, stored entries, expected-current identities, and restore
     lookup use one case-normalized canonical key while retaining original
     display spelling; the accepted mixed-case fixture restores every entry
     without lookup failure or transaction residue.
   * [ ] The caller-visible identifier is opaque; trusted token state is outside
     the target and authenticity binds target identity, canonical plan,
     owned-path/Git fingerprints, and creation/expiry times to a runtime-created
     secret or signed/HMAC token that the caller cannot recompute.
   * [ ] Atomic lease/consume permits exactly one attempt. Every concurrent,
     replayed, expired, missing, tampered, or stale supplied and direct internal
     checkpoint is rejected before target or Git mutation, including when a
     caller recomputes an unkeyed hash over altered fields.
   * [ ] Dependency, source-acquisition, parse, formerly pre-lease plan, and
     malformed-input failures each terminally consume or revoke the supplied
     capability; the separate-process retry rejects the identifier in every
     case and both attempts leave target bytes, Git state, and unrelated trusted
     state unchanged with no authorizing checkpoint residue.
   * [ ] Cleanup and forensic reporting may retain only non-authorizing records;
     malformed or unauthenticated input cannot delete, consume, or disclose a
     different transaction's trusted state.
   * [ ] The valid token and all owned-path/Git pre-state fingerprints are
     checked immediately before first mutation. Instrumentation proves unrelated
     paths were not read or hashed and no long-lived secret is persisted in the
     caller-controlled target.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-14

   ---

   **TC-IDR-WORKTREE - Linked Git worktree install and rollback**

   *Action:* Run changed installation and injected post-commit failure in
   linked worktrees with attached, detached, and unborn HEAD fixtures.

   *Expected result:*

   * [ ] Runtime discovery records command-derived Git directory, index path,
     symbolic full HEAD, and OID/unborn state without requiring a ``.git``
     directory.
   * [ ] Successful installation commits in the linked worktree without
     modifying unrelated common-worktree state.
   * [ ] Rollback restores the exact attached ref/OID, detached OID, or unborn
     symbolic ref plus exact index bytes and planned worktree paths.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-10

   ---

   **TC-IDR-GITHUB - Real GitHub API acquisition**

   *Action:* When network and rate-limit capacity are available, resolve a real
   public branch through the GitHub API, enumerate the selected immutable tree,
   and fetch representative product bytes through the production acquisition
   path.

   *Expected result:*

   * [ ] Branch resolution yields one commit SHA used by every tree and raw
     request; required product roots and representative bytes match that SHA.
   * [ ] No target mutation or checkpoint occurs during acquisition and plan
     validation.
   * [ ] Missing network, credentials, or rate-limit capacity yields an
     explicit conditional skip; fixture tests remain mandatory.
   * [ ] Public repository parsing accepts only ``owner/repository`` and the
     supported GitHub HTTPS form. A same-named local relative path, absolute
     path, ``file:`` URL, and non-GitHub URL are rejected before filesystem
     resolution; local fixture bytes enter only through the internal immutable
     ``SourceSnapshot.from_directory`` API.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-13

   ---

   **TC-IDR-SUCCESS - Validation-gated commit and structured summary**

   *Action:* Run a changed installation and inspect process order, Git history,
   checkpoint state, and structured result.

   *Expected result:*

   * [ ] Warning-as-error Sphinx validation completes before the final commit.
   * [ ] Checkpoint deletion completes before success becomes observable.
   * [ ] Non-negative counts identify actual selected-harness and shared paths;
     no fixed table or directory-row set is required.
   * [ ] No checkpoint residue remains after success.

   ---

   **TC-IDR-FULL-SUITE - Normal completion and bounded resources**

   *Action:* Run the complete Installer suite after all corrections in a clean
   process, including the large unrelated-tree fixture. Capture exit status,
   stderr, peak memory, open handles, worker count, and test totals. If a run
   terminates abruptly, preserve available diagnostics, investigate the cause,
   correct it, and rerun the complete suite from the beginning.

   *Expected result:*

   * [ ] The process exits normally with every mandatory test executed and no
     unexplained termination, timeout, or worker loss.
   * [ ] Worker count is explicitly bounded; checkpoint bytes, peak memory,
     handles, and path hashing scale with selected source plus declared mutable
     paths, not with unrelated target-tree size.
   * [ ] An interrupted run is never reported as passing or clearance evidence;
     only the subsequent complete normal run is recorded.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-6

   ---

   **TC-IDR-SPEC - Active workflow consistency**

   *Action:* Review active Installer and Setup specifications against these scenarios.

   *Expected result:*

   * [ ] Initial install is remote-runtime-owned and update is local-runtime-owned.
   * [ ] Read-only acquisition precedes the checkpoint, which precedes every mutation.
   * [ ] No active flow contains Setup-to-Installer delegation, local frontmatter
     preservation, customization prompts, double writes, or manual/Git-reset rollback.

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SPEC_REWRITE`` AC-7

   **Automation rule:** executable fixture evidence is required for runtime,
   adapter, transaction, and ordering outcomes. Prose matching and manual
   best-effort recovery are not acceptance evidence.

  **Exclusive ownership:** This design is the sole lifecycle acceptance owner
  for clean installation, update, injected failure, rollback, validation-gated
  commit, and checkpoint cleanup across ``vscode``, ``claude``, ``opencode``,
  and ``qoder``. For Qoder, this ownership ends at staged-package validity and
  reversible project state; it does not include external UI import. Native
  discovery/loading evidence belongs exclusively to
  SYSP_SPEC_UAT_HARNESS_TARGET_MATRIX.
