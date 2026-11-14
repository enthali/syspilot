Release Contract
================

.. req:: Release Contract Process
   :id: SYSP_REQ_RELEASE_CONTRACT
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_CONTRACT_HANDLING
   :realized_by: docs/Syspilot Contracts/release.md

   Every publication shall use a Release Contract initialized by Project Manager
   from the canonical template at ``docs/releases/v{version}.md`` and committed
   before first handoff to Release. Release shall own the process and closure.
   The process shall be listed in the registry.

   Its template shall offer only ``autonomous | user-guided`` with their complete
   rules, agreed with the User; publication shall require the User reachable.
   Only the User-owned ``Release start`` gate's ``approved`` state shall
   authorize work. The gate request shall open the Contract in the User's editor.

   The template shall carry the inherited shared rules, including the Handover
   log with its short note, and one artifact-table ownership/evidence row for
   objective/scope, inventory, version, preflight, notes, documentation,
   infrastructure, verification, publication and closure. Release shall be the
   sole notes writer; Technical Writer's terminal documentation row shall be
   checked by Release, not written by it.

.. vc:: Release initialization establishes an authorized Contract
   :id: SYSP_VC_RELEASE_CONTRACT_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_CONTRACT

   The registered process initializes the record at the stated path with
   Release as first receiver and closure owner.

.. vc:: Release mode requires a reachable User
   :id: SYSP_VC_RELEASE_CONTRACT_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_CONTRACT

   The template offers complete autonomous/user-guided rules and no unattended
   mode; publication evidence shows the User reachable.

.. vc:: Release start request opens the governing Contract
   :id: SYSP_VC_RELEASE_CONTRACT_4
   :status: approved
   :verifies: SYSP_REQ_RELEASE_CONTRACT

   Project Manager opens the Contract in the User's editor in the same step
   that requests the User-owned Release start gate.

.. vc:: Release work starts only with the User release gate
   :id: SYSP_VC_RELEASE_CONTRACT_5
   :status: approved
   :verifies: SYSP_REQ_RELEASE_CONTRACT

   Every release start path requires the sole User-owned Release start gate
   to be approved.

.. vc:: Release artifact ownership has a single statement
   :id: SYSP_VC_RELEASE_CONTRACT_3
   :status: approved
   :verifies: SYSP_REQ_RELEASE_CONTRACT

   All declared artifacts have one owner/evidence row and inherited shared rules;
   notes belong to Release, other documentation to Technical Writer.

.. req:: Release Change Inventory And Archive
   :id: SYSP_REQ_RELEASE_INVENTORY
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: docs/Syspilot Contracts/release.md

   Release shall require each included Change closed or a recorded User decision
   for its inclusion while open. Its required inventory check verifies the ``Example sync`` row of each
   included Change that carries one as ``complete`` or reasoned ``not applicable``.
   Example updates shall not be deferred to release-time merging.

   Before preflight, Release shall commit content-unchanged moves of all included
   Change Contracts to ``docs/changes/v{version}/`` on ``development``.
   Internal relative links shall not be rewritten. No shipped Contract shall
   remain directly in ``docs/changes/``.

.. vc:: Release inventory has a disposition for every included Change
   :id: SYSP_VC_RELEASE_INVENTORY_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_INVENTORY

   Each included Change is closed or explicitly User-approved while open;
   its existing Example sync row is complete or reasoned not applicable.

.. vc:: Release archives Change records before verification
   :id: SYSP_VC_RELEASE_INVENTORY_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_INVENTORY

   Git history shows content-unchanged moves into the version archive before P;
   no included record remains flat, and a move after P fails the record rule.

.. req:: Release Local Preflight
   :id: SYSP_REQ_RELEASE_PREFLIGHT
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: docs/Syspilot Contracts/release.md

   Preflight shall run on the intended ``development`` commit P after notes,
   version heading, documentation and archived Changes are committed.
   It shall record commands, commit and results for exactly four local checks:
   build-runner tests, strict clean documentation build, release QA suites and
   the shared automated version check of ``SYSP_REQ_RELEASE_VERSION``.

   The Contract shall state the build's external-inventory network requirement
   and that local evidence proves neither runner-platform execution nor
   publication; path case, line endings and runner-only tools may fail after tagging.
   Unavailable inventory shall be recorded as environment failure, not content failure.
   It shall state that a failure of the validation or of the documentation build
   after the tag publishes nothing, while a later failure leaves a partial
   publication if documentation was already deployed.

.. vc:: Preflight evidence covers the exact committed candidate
   :id: SYSP_VC_RELEASE_PREFLIGHT_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_PREFLIGHT

   Four local check records identify P, commands and results after all release
   content and archive moves are final.

.. vc:: Preflight evidence states its platform and publication limits
   :id: SYSP_VC_RELEASE_PREFLIGHT_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_PREFLIGHT

   The Contract distinguishes network/build failure, untested runner behavior
   and partial publication; only failed validation/build prerequisites guarantee
   no publication.

.. req:: Release Revalidation Triggers
   :id: SYSP_REQ_RELEASE_REVALIDATION
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: docs/Syspilot Contracts/release.md

   A validation-only workflow run on a pushed branch of P shall be required
   only when an input path differs from the last successful tag run, Admin
   records an environment change since that run, or the immediately preceding
   release has no successful tag run. Before pushing the branch, the Contract
   shall record the User's explicit authorization naming that run.

   The trigger list shall include workflow definition, version checker,
   dependency/lock files, installed Python/Sphinx versions and all documentation
   configuration inputs except release notes. The notes exception shall hold
   only while heading parsing stays in the checker and configuration; a new
   parser file shall join the list.

   At release start, Release shall assess the sufficiency of Admin's workflow
   facts, path list and environment-change statement as mandatory consultee,
   and record which triggers fired. Every successful tag run shall record
   run, commit, runner image and resolved build-tool versions in the release
   record as the next environment-comparison baseline.

.. vc:: Revalidation is conditional on observable staleness
   :id: SYSP_VC_RELEASE_REVALIDATION_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_REVALIDATION

   Trigger dispositions reference the last successful run and explicit
   path/environment/no-run conditions; no unconditional extra run is required.

.. vc:: Revalidation paths preserve the notes exception boundary
   :id: SYSP_VC_RELEASE_REVALIDATION_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_REVALIDATION

   The recorded list contains the required inputs; release notes are excepted
   only under the two-parser condition, with new parser paths included.

.. vc:: Release assesses revalidation evidence at release start
   :id: SYSP_VC_RELEASE_REVALIDATION_3
   :status: approved
   :verifies: SYSP_REQ_RELEASE_REVALIDATION

   At release start, Release records whether Admin's workflow facts, path list
   and environment-change statement suffice to determine the triggers.

.. vc:: Revalidation branch push has explicit User authorization
   :id: SYSP_VC_RELEASE_REVALIDATION_4
   :status: approved
   :verifies: SYSP_REQ_RELEASE_REVALIDATION

   Before a validation-only branch push, the record contains the User's explicit
   authorization naming that run.

.. vc:: Successful tag runs establish the next comparison baseline
   :id: SYSP_VC_RELEASE_REVALIDATION_5
   :status: approved
   :verifies: SYSP_REQ_RELEASE_REVALIDATION

   Each successful tag run records run, commit, runner image and resolved
   build-tool versions for the next release's environment comparison.

.. req:: Release Record Commit Boundary
   :id: SYSP_REQ_RELEASE_RECORD
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: scripts/check_release_record.py

   At publication, Release shall run ``scripts/check_release_record.py`` with
   P, release commit R and tag. It shall read committed Git state, not the
   working tree, and write nothing.
   The check shall require P as ancestor of R and exactly one changed path,
   ``docs/releases/v{version}.md``, with no rename, mode change or deletion.
   The record shall exist at P and R, contain P's full SHA in an evidence cell
   at R, and have a ``Version:`` line equal to the tag without ``v`` and the
   newest notes heading, obtained through the shared version checker.
   Success shall exit ``0``; failure shall exit ``1`` with the failing condition
   first on stderr. No publication shall proceed on failure.

.. vc:: Record checking accepts only the permitted committed path
   :id: SYSP_VC_RELEASE_RECORD_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_RECORD

   An evidence-only record change passes; unrelated ancestry, a second path,
   rename, mode change or deletion fails without writing files.

.. vc:: Record checking validates both records and version evidence
   :id: SYSP_VC_RELEASE_RECORD_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_RECORD

   Absent P/R records, missing full P SHA and mismatched Version/tag/newest
   heading each fail with exit 1 and a condition-first diagnostic.

.. req:: Release Record Protected Content
   :id: SYSP_REQ_RELEASE_RECORD_CONTENT
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_RECORD
   :realized_by: scripts/check_release_record.py

   Record comparison shall reject a P-to-R change in:

   - Operation Mode;
   - ``Objective And Scope``, ``Version`` or ``Change Inventory`` sections;
   - ``Artifact or gate``, ``Included`` or ``Owner`` cells of any artifact row;
   - any cell of ``Objective and scope``, ``Release start`` or ``Version`` rows;
   - the preflight command list; or
   - Release Verification's version/tag text.

   The check shall require every second-level template heading at R, checking
   presence only, and fail on an unreadable expected heading/table row.
   Diagnostics shall name the missing heading or changed protected block.
   Remaining fields, results, log, publication/closure evidence and unprotected
   narrative may differ; automation shall not claim to enforce evidence-only changes.

.. vc:: Protected-content mutations cannot inherit preflight
   :id: SYSP_VC_RELEASE_RECORD_CONTENT_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_RECORD_CONTENT

   One-at-a-time mutations of each protected block fail and identify that block.
   Allowed evidence/status/log changes pass.

.. vc:: Missing record structure fails explicitly
   :id: SYSP_VC_RELEASE_RECORD_CONTENT_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_RECORD_CONTENT

   Removing any second-level heading or an expected parsed heading/row fails;
   heading presence alone makes no claim about order or narrative content.

.. req:: Release Record Review And Isolation
   :id: SYSP_REQ_RELEASE_RECORD_REVIEW
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: docs/Syspilot Contracts/release.md

   Quality and Release shall review the complete P-to-R record diff before
   publication, including authorization and unprotected content. Changed
   release content, procedures or failure rules shall be rejected or require
   new preflight; every other changed path shall also require new preflight.

   The record-only exception shall hold only while the build excludes
   ``docs/releases/`` and the record checker is its only reader.
   The introducing Change and any later Change adding a reader shall evidence
   this with the configuration exclusion and a build/QA run using an altered
   record, not a reference scan alone.

.. vc:: Manual record review covers what automation does not
   :id: SYSP_VC_RELEASE_RECORD_REVIEW_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_RECORD_REVIEW

   Quality and Release's full-diff dispositions reject non-evidence content
   changes or require fresh preflight; bounded automation is not treated as proof.

.. vc:: Record isolation supports reuse of preflight evidence
   :id: SYSP_VC_RELEASE_RECORD_REVIEW_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_RECORD_REVIEW

   Configuration excludes release and archived Change records. Evidence for
   the introducing/reader-adding Change includes altered-record build and QA,
   with no additional reader of the release record.

.. req:: Release Push Authorization
   :id: SYSP_REQ_RELEASE_AUTHORIZATION
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: docs/Syspilot Contracts/release.md

   Publication shall require the User's explicit authorization to push ``main``
   and the tag, distinct from Release start.
   The authorization shall acknowledge local-only tests, runner execution first
   proven by the tag run, a new-version fix without moving the tag after failure,
   and any triggered validation-only run before push.
   It shall be committed in the record on ``development`` after P and before
   the merge to R, and reviewed by Quality; no append-only mechanism shall be claimed.

.. vc:: Tagged state already contains the reviewed push authorization
   :id: SYSP_VC_RELEASE_AUTHORIZATION_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_AUTHORIZATION

   Git history places the record-only authorization commit between P and R;
   R contains all acknowledgements and Quality's review covers them.

.. req:: Release Publication Evidence And Failure
   :id: SYSP_REQ_RELEASE_PUBLICATION
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: docs/Syspilot Contracts/release.md

   Publication shall require Quality's direct ``proceed`` judgment from recorded
   commands/results and no open issue. Release shall push ``main`` before the
   tag, placing the tag only on R on ``main``.
   The tag shall satisfy ``SYSP_REQ_RELEASE_VERSION``.

   The record shall contain P and push authorization before R.
   Evidence unavailable in R (R SHA, tag, workflow run, GitHub Release, Pages
   URL and outcome) shall be committed after the tag in a later record-only
   commit without moving the tag.

   Any workflow failure after tagging, including Pages deployment followed by
   failed release creation, shall stop publication work, record a blocker and
   escalate to the User. The tag shall remain; moving/deleting it or force-pushing
   shall require the User's decision.

.. vc:: Publication follows verification on the authorized release commit
   :id: SYSP_VC_RELEASE_PUBLICATION_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_PUBLICATION

   Direct Quality proceed and no open issue precede publication; ``main`` is
   not published without that judgment.

.. vc:: Post-tag evidence does not retroactively change the tagged state
   :id: SYSP_VC_RELEASE_PUBLICATION_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE_PUBLICATION

   A later record-only commit contains R, tag, run, release, Pages and outcome
   evidence; it does not move the tag.

.. vc:: Partial publication remains a failure requiring escalation
   :id: SYSP_VC_RELEASE_PUBLICATION_3
   :status: approved
   :verifies: SYSP_REQ_RELEASE_PUBLICATION

   Failed post-tag runs, including documentation already deployed, have a
   blocker/escalation disposition and an unmoved tag absent a User decision.

.. vc:: Publication pushes main before the release tag
   :id: SYSP_VC_RELEASE_PUBLICATION_4
   :status: approved
   :verifies: SYSP_REQ_RELEASE_PUBLICATION

   ``main`` is pushed first; the conforming tag sits only on release commit R
   on ``main`` and is pushed afterwards.

.. req:: Release Closure
   :id: SYSP_REQ_RELEASE_CLOSURE
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_RELEASE_CONTRACT
   :realized_by: docs/Syspilot Contracts/release.md

   Release shall close only when every included artifact and gate has terminal
   status and completion evidence, and publication evidence is recorded.

.. vc:: Release closure has complete terminal evidence
   :id: SYSP_VC_RELEASE_CLOSURE_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_CLOSURE

   The closure checklist and release record contain terminal artifact/gate
   evidence and the publication outcome, with Release responsible for closure.
