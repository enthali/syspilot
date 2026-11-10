Release Contract
================

.. req:: Release Contract Process
   :id: SYSP_REQ_RELEASE_CONTRACT
   :status: approved
   :implements: SYSP_US_RELEASE_CONTRACT
   :specializes: SYSP_REQ_CONTRACT_HANDLING
   :realized_by: docs/Syspilot Contracts/release.md

   Every publication of a syspilot version shall use a Release Contract that:

   - is initialized by the Project Manager as a tailored copy of the canonical
     template at ``docs/changes/release-v{version}.md`` and committed before
     the first responsibility transfer;
   - names Release as process owner and closure owner, transfers first
     responsibility to Release, and carries an ``Operation Mode`` field that
     offers ``autonomous | user-guided`` with the complete rule for each,
     because an irreversible publication always runs with the User reachable;
   - records the User's authorization in a User-owned ``Release start`` gate
     that no other actor may set, starts release work only after that gate
     reads ``approved``, and has the Project Manager open the Contract in the
     User's editor within the step that asks for it;
   - records one owner and completion evidence for the objective and scope,
     the change inventory, the version, the preflight, the release notes, the
     user-facing documentation, the infrastructure impact, the release
     verification, the publication, and the closure, with the artifact table
     as the only statement of ownership, the release notes owned by Release as
     the only writer and the user-facing documentation owned by the Technical
     Writer, whose terminal row is a completion condition that Release checks
     and does not write, and the shared rules of the Contract
     Document method for every Contract kind, namely the Handover log with its
     short note, the
     scope-change rule, the single ownership statement, the presentation of the
     Contract to the User in the step that asks for ``Release start``, and the
     receiving actor's refresh before it acknowledges;
   - requires every included Change Contract to be closed, or a User decision
     recorded for an open one, and verifies the ``Example sync`` row of each
     included Change Contract that carries one as ``complete`` or as
     ``not applicable`` with its reason, instead of merging the example
     changes at the release;
   - requires the preflight to run on the ``development`` commit to be
     released, the preflighted commit, after the release notes, the version
     heading, and the user-facing documentation of the release are committed
     there, and to record commands, commit, and result for exactly four local
     checks: the documentation build tests, the strict clean documentation
     build, the release QA suites, and the automated version check of
     ``SYSP_REQ_RELEASE_VERSION``; it requires no validation-only run of the
     release workflow in every release, because the tag-triggered workflow
     validates the tagged commit before anything is published and a mandatory
     second remote run per version adds ceremony without a different
     guarantee;
   - states for the preflight what local evidence does not show: that it does
     not run on the workflow's platform, that platform-specific failures such
     as path case, line endings, or tools installed only on the runner may
     appear first after the tag exists, that publication is not exercised,
     and that this trade-off is accepted, so that the User's authorization to
     push ``main`` and the tag acknowledges it in the evidence of that
     authorization; a failure of the validation or of the documentation build
     after the tag publishes nothing, because publication follows them, whereas
     a failure after the documentation was published, as when the creation of
     the GitHub Release fails after the Pages deployment, leaves a partial
     publication that the failure path below handles and that is not covered
     by that statement;
   - requires a validation-only run of the release workflow on a pushed
     branch of the preflighted commit only when a revalidation trigger has
     fired, namely a difference between the commit of the last successful
     tag-triggered run and the preflighted commit in a path of the trigger
     list, an environment change that the Admin recorded since that run, or
     the absence of a successful tag-triggered run of the immediately
     preceding release, and records the User's explicit authorization, which
     names the run, before any branch is pushed for it, because the evidence
     of the last successful run is not assumed to hold for later versions;
     the trigger list names at least the workflow definition, the version
     checker, the dependency and lock files, the Python and Sphinx versions
     that the workflow installs, and every file the documentation
     configuration reads except the release notes, which change with every
     release by design and whose heading format the automated version check
     verifies, on the condition that the parsing of release headings stays
     only in the version checker and the documentation configuration, because
     a file that takes over that parsing then joins the list; the Admin states
     the facts of the workflow and of
     the last run for the Infrastructure impact artifact under
     ``SYSP_REQ_ADMIN``, Release decides at the release start whether the
     list and the triggers are sufficient as the mandatory consultee and
     records whether a trigger has fired, and a tag run that succeeds records
     its run, commit, runner image, and the resolved versions of the build
     tools in the release record, which becomes the baseline of the
     environment comparison for the next release, because the platform log of
     an old run does not stay available;
   - states in the Release Contract that the strict documentation build needs
     network access, because the documentation configuration fetches an
     external inventory, so that a preflight or a run in an environment
     without it fails for that reason and not for the content;
   - takes the tag as the version of the release and requires the form
     ``vMAJOR.MINOR.PATCH``, exactly one matching release-notes heading, and
     the consistency of the version with the published documentation's
     version metadata, as ``SYSP_REQ_RELEASE_VERSION`` specifies, checked by
     the same automated check before the tag is pushed and by the
     tag-triggered workflow, so that the preflight and the workflow cannot
     disagree;
   - records the preflight evidence in the Release Contract of the release,
     ``docs/changes/release-v{version}.md``, which is the one path that may
     differ between the preflighted commit P and the release commit R, with
     the difference bounded to that one file, checked by one automated record
     check, ``scripts/check_release_record.py``, which Release runs at
     publication in place of a bare comparison of trees, and reviewed in full
     by Quality and by Release: the automation enforces a named set and the
     review covers every other difference, so that no claim is made that the
     check alone enforces evidence-only changes. The check requires that R has
     P as an
     ancestor, the
     difference from P to R consists of exactly that path, with no other
     file, rename, mode change, or deletion, and a comparison of the record at
     P and at R, both read from the commits, fails on any change in the
     protected content, namely the
     Operation Mode, the sections ``Objective And Scope``, ``Version``, and
     ``Change Inventory``, the columns ``Artifact or gate``, ``Included``, and
     ``Owner`` of every row of the artifact table, every cell of the rows
     ``Objective and scope``, ``Release start``, and ``Version``, the list of
     preflight commands, and the version and tag text of the Release
     Verification section, and requires every second-level heading of the
     Release Contract template to be present at R, presence only and not
     order or content, so that a deleted evidence section fails; the header status, responsibility and
     blocker, the Handover log, the preflight results, Release Verification and
     Open Quality Issues, the publication evidence, the closure, and the
     status and evidence cells of the other rows, and the narrative of the
     unprotected sections, may differ at R, and the review of the complete
     difference from P to R by Quality and by Release before publication
     rejects any change that alters release content, a procedure or a
     failure rule, or requires a new preflight, because the check does not
     see them; the commit of P is recorded in
     an evidence cell; the check takes P, R, and the tag as arguments, reads
     the commits with ``git`` and no working tree, writes nothing, exits ``0``
     when every condition holds and ``1`` otherwise with a message on the
     standard error that begins with the failing condition, namely P not an
     ancestor of R, a path other than the record, a rename, mode change, or
     deletion, the record absent at P or at R, because the record is committed
     before the preflight and the comparison of protected content needs both,
     a change in protected content naming
     the block, a template heading missing at R naming it, the full commit of
     P missing from the record at R, the version
     stated in the ``Version:`` line of the record's ``Version`` section at R
     differing from the tag's version without its leading ``v`` or from the
     newest release-notes heading of R, which it reads through the version
     check so that no second parser exists, and the
     template's headings or table rows that the check reads not found, which fails and never passes;
     any other
     difference, whether product, documentation, dependency, workflow, test,
     release-notes, or another Change Contract, requires a new preflight on
     the new commit, so that recording results cannot cause a recheck loop
     and an untested change cannot inherit earlier evidence; this holds
     only while the documentation build excludes ``docs/changes/`` and the
     record check is the only reader of the record, which the
     documentation configuration's exclusion and a recorded run of the
     documentation build and of the release QA suites with an altered record,
     made once for the Change that introduces the rule and again by any later
     Change that adds a reader of ``docs/changes/``, establish, and not a
     scan of the repository for references;
   - requires, before publication, the User's explicit authorization to
     push ``main`` and the tag recorded separately from the ``Release start``
     gate, stating that the tests ran locally on the preparing platform only,
     that execution on the workflow's platform is first proven by the tag run,
     that a failed tag run is corrected by a new version and the tag is not
     moved, and, when a trigger fired, the validation-only run that precedes
     the push; the authorization and its acknowledgement are committed in the
     record on ``development`` after P and before the merge, so that R
     contains them and the review of the difference from P to R covers them,
     and the evidence that cannot exist in R, namely the commit of R, the tag,
     the workflow run, the GitHub Release, the Pages URL, and the outcome, is
     recorded in a later commit that changes only the record, after the tag,
     which does not move the tag; the authorization cell is protected by its
     content, since the acknowledgement must be present in R, and by the
     review, and not by an append-only mechanism, which a comparison of two
     commits cannot check;
     ``main`` pushed before the tag, and the tag placed only on the
     release commit on ``main``;
   - requires Quality's direct ``proceed`` judgment, reached by reviewing the
     recorded commands and results, and no open quality issue before
     publication;
   - records publication evidence: the preflighted commit, the release commit
     on ``main``, the User's authorization, the tag, the release workflow run,
     the GitHub Release, and the published documentation's Pages URL;
   - stops, records a blocker, and escalates to the User when the release
     workflow fails after the tag is pushed, including a partial publication
     in which the documentation was published and a later job failed, leaving
     the tag in place until
     the User decides on any move, deletion, or force-push; and
   - closes through Release only when every included artifact and gate has
     terminal status and completion evidence and the publication evidence is
     recorded.

.. vc:: Release Contract exposes a verified irreversible publication
   :id: SYSP_VC_RELEASE_CONTRACT_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE_CONTRACT

   Inspect the realized Release Process and confirm that its template names
   Release as process and closure owner, offers only the autonomous and
   user-guided modes with their rules, and carries a User-owned ``Release
   start`` gate that alone starts release work. Confirm that the artifact
   table names one owner per row and the sections name none, that the release
   notes row is Release's and the user-facing documentation row the Technical
   Writer's, that the
   preflight rows record command, commit, and result for the four local
   checks and that no validation-only run is required in every release, that
   the limits of local evidence and the accepted trade-off are stated and
   acknowledged in the User's authorization to push, that the revalidation
   triggers are listed, each tied to a path or condition that can be
   observed, with the last successful tag-triggered run recorded and the
   User's authorization required before a branch is pushed for a triggered
   run, that the version is the tag and the version check is the same one the
   release workflow runs, that the preflight evidence lives in the release's
   own Contract, that the record check ``scripts/check_release_record.py``
   accepts a release record that differs from the preflighted commit's in
   evidence only and rejects, one at a time, with the failing condition
   first in its message and exit status ``1``, a change of the Operation Mode, of the scope, version, or change inventory
   sections, of an owner, of the ``Release start`` row, of the preflight
   command list, of the version text, a record missing at P or at R, the full
   commit of P missing from the record at R, a template heading missing at R,
   a template heading or table row that the check reads and cannot find, a
   version stated in the ``Version:`` line of the
   record that differs from the tag's version or from the newest
   release-notes heading, a release commit that lacks
   the preflighted commit as ancestor, and a second changed file, rename,
   mode change, or deletion, that the Contract states the network need of the
   strict build and the trigger list with the files named above and the
   exception of the release notes with its condition, that the Contract
   states what the check enforces and requires Quality and Release to review
   the complete difference of the record from P to R, rejecting a changed
   procedure, failure rule, or content or requiring a new preflight, and makes
   no claim that the check alone enforces evidence-only changes, that the
   publication steps run in an order that can be committed, namely the User's
   authorization and acknowledgement recorded in the record on ``development``
   after P, then the merge and the record check and the review of the
   difference including the authorization, then ``main`` and the tag pushed,
   then the evidence that cannot exist in R recorded in a later commit that
   changes only the record, that the publication steps record the User's
   authorization to
   push ``main`` and the tag with the three statements, push ``main`` before
   the tag, and state the
   failure path after the tag, which separates a failed validation or build
   that publishes nothing from a partial publication after the documentation
   was published, handled by stop, blocker, and escalation with the tag left
   in place, that Quality's judgment is direct and rests on
   recorded commands and results, and that the publication table records the
   preflighted commit, release commit, authorization, tag, workflow run,
   GitHub Release, and Pages URL. Confirm that the documentation build
   excludes ``docs/changes/``, that the record check is the only reader of the
   record, and that a build and a QA run with an altered record are recorded
   for the Change that introduces the rule. Confirm that the Change inventory records
   the ``Example sync`` disposition of each included Change that carries the
   row. Confirm that the Release Process is listed
   in the process registry.
