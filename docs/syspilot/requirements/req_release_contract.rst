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
     as the only statement of ownership and the shared rules of the Contract
     Document method for every Contract kind, namely the Handover log, the
     scope-change rule, the single ownership statement, the presentation of the
     Contract to the User in the step that asks for ``Release start``, and the
     receiving actor's refresh before it acknowledges;
   - requires every included Change Contract to be closed, or a User decision
     recorded for an open one;
   - requires the preflight to run on the ``development`` commit to be
     released, after the release notes and release-facing documentation are
     committed there and with any later commit requiring a new preflight, and
     to record commands, commit, and result for the
     documentation build tests, the strict clean documentation build, the
     release QA suites, an automated version check, and a validation-only run
     of the release workflow, states that the validation-only run exercises
     only the validation and documentation build jobs and so does not show
     that publication works, and records the User's authorization before a
     branch is pushed for that run;
   - takes the tag as the version of the release, requires the form
     ``vMAJOR.MINOR.PATCH`` and exactly one matching release-notes heading,
     and checks both by the automated version check before the tag is pushed;
   - requires, before publication, that the release commit on ``main`` carries
     the tree of the preflighted commit, the User's explicit authorization to
     push ``main`` and the tag recorded separately from the ``Release start``
     gate, ``main`` pushed before the tag, and the tag placed only on the
     release commit on ``main``;
   - requires Quality's direct ``proceed`` judgment, reached by reviewing the
     recorded commands and results, and no open quality issue before
     publication;
   - records publication evidence: the preflighted commit, the release commit
     on ``main``, the User's authorization, the tag, the release workflow run,
     the GitHub Release, and the published documentation's Pages URL;
   - stops, records a blocker, and escalates to the User when the release
     workflow fails after the tag is pushed, leaving the tag in place until
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
   table names one owner per row and the sections name none, that the
   preflight rows record command, commit, and result for the five required
   checks, the limits of the validation-only run, and the User's authorization
   before a branch is pushed, that the version is the tag and the version rule
   matches the tag check in the release workflow, that the publication steps
   verify the tree of the release commit, record the User's authorization to
   push ``main`` and the tag, push ``main`` before the tag, and state the
   failure path after the tag, that Quality's judgment is direct and rests on
   recorded commands and results, and that the publication table records the
   preflighted commit, release commit, authorization, tag, workflow run,
   GitHub Release, and Pages URL. Confirm that the Release Process is listed
   in the process registry.
