Change Contract
===============

.. req:: Change Contract Process
   :id: SYSP_REQ_CHANGE_CONTRACT
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CONTRACT_HANDLING
   :realized_by: docs/Syspilot Contracts/change.md

   Every modification to versioned source code or documentation shall use a
   tailored Change Contract, initialized by Project Manager on a feature branch
   named from the Change, committed before first handoff to Architect.

   The template shall carry the inherited Contract rules, including a Project
   Manager-owned Handover log. Its note states the completed work and facts
   affecting the next owner's situation; evidence and remaining work stay in
   the owner's section and open rows. Compact initialization prose shall not
   duplicate shared handling rules.

.. vc:: Change initialization establishes the first artifact owner
   :id: SYSP_VC_CHANGE_CONTRACT_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_CONTRACT

   The process applies to versioned code/document changes and initializes a
   committed tailored Contract with Architect as first receiver.

.. vc:: Change reuses the shared handling contract
   :id: SYSP_VC_CHANGE_CONTRACT_2
   :status: approved
   :verifies: SYSP_REQ_CHANGE_CONTRACT

   The template carries inherited rules without a second handling procedure
   in its compact initialization prose.

.. req:: Change Operation Mode
   :id: SYSP_REQ_CHANGE_MODE
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CHANGE_CONTRACT
   :realized_by: docs/Syspilot Contracts/change.md

   The canonical Change template shall offer ``user-guided (default) |
   autonomous | unattended`` with the complete governing rule for each.
   The User shall agree one mode before Contract release; the instance shall
   retain only that rule, without template notes or external rule lookup.

   In unattended mode, an actor unable to reach the User shall record ``USER
   REVIEW REQUIRED``, choose the simplest path cheapest to reverse or amend,
   and continue. Project Manager shall review flagged points when the User
   returns; decision ownership shall remain with the deciding actor and User
   checkpoints shall remain pending.

.. vc:: A Change carries its selected mode rule
   :id: SYSP_VC_CHANGE_MODE_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_MODE

   The template offers three complete rules; an instance retains exactly the
   User-agreed rule with no template note or external dependency.

.. vc:: Unattended decisions remain reviewable and owned
   :id: SYSP_VC_CHANGE_MODE_2
   :status: approved
   :verifies: SYSP_REQ_CHANGE_MODE

   Unreachable-User decisions have the review flag and reversible disposition;
   Project Manager review does not take decision ownership or close User checkpoints.

.. req:: Change Start Authorization
   :id: SYSP_REQ_CHANGE_START
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CHANGE_CONTRACT
   :realized_by: docs/Syspilot Contracts/change.md

   Artifact work shall start only when the User-owned ``Contract release``
   gate is ``approved``. The gate shall record authorization exactly once as
   ``pending`` or ``approved``; intent approval and Operation Mode shall provide
   no alternative start condition. Project Manager shall open the Contract
   in the User's editor in the step requesting the gate.

.. vc:: Only the User release gate authorizes Change work
   :id: SYSP_VC_CHANGE_START_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_START

   Every process start path requires the single User-owned gate's approval;
   neither intent approval nor Operation Mode supplies another authorization.

.. vc:: Change start request opens the governing Contract
   :id: SYSP_VC_CHANGE_START_2
   :status: approved
   :verifies: SYSP_REQ_CHANGE_START

   Project Manager opens the Contract in the User's editor in the same step
   that requests Contract release.

.. req:: Change Artifact Applicability
   :id: SYSP_REQ_CHANGE_ARTIFACTS
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CHANGE_CONTRACT
   :realized_by: docs/Syspilot Contracts/change.md

   A Change shall record each artifact's applicability, owner, completion
   evidence and status; each owner shall judge its own applicability and completion.
   Optional elements shall state their reason and edit/delete instruction at
   the choice; required elements shall offer no omission, and no separate
   tailoring list shall duplicate the choices.

   The table shall offer optional Admin-owned infrastructure impact supported
   by direct workflow, CI and packaging confirmation, not Needs-only inference.
   An optional Architect-owned ``Ontology Binding`` subsection shall map
   Contract roles to realized kinds only when the active ontology lacks ``doc``
   Needs or typed links.

   The Architect shall build the ``Affected Artifacts`` table with the
   project's impact skill, naming it by purpose and not by skill name or
   file. The table shall carry an ``Impact query`` line with the start IDs,
   direction and depth, give every reported ID one row with the disposition
   ``no change``, ``modified``, ``added`` or ``removed``, and add by hand the
   artifacts the query cannot report, such as new ones. The query output is a
   candidate list, not a complete scope. The Architect's completion evidence
   shall require this table.

.. vc:: Change artifacts have owner-decided applicability
   :id: SYSP_VC_CHANGE_ARTIFACTS_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_ARTIFACTS

   Every artifact has an owner-decided applicability/completion row and evidence.

.. vc:: Change infrastructure evidence comes from its owner
   :id: SYSP_VC_CHANGE_ARTIFACTS_2
   :status: approved
   :verifies: SYSP_REQ_CHANGE_ARTIFACTS

   Optional infrastructure impact belongs to Admin and requires infrastructure
   observations, not Needs-only inference.

.. vc:: Change ontology binding applies only where needed
   :id: SYSP_VC_CHANGE_ARTIFACTS_3
   :status: approved
   :verifies: SYSP_REQ_CHANGE_ARTIFACTS

   Ontology Binding is optional, Architect-owned and limited to the stated
   ontology case.

.. vc:: Change tailoring preserves required artifacts
   :id: SYSP_VC_CHANGE_ARTIFACTS_4
   :status: approved
   :verifies: SYSP_REQ_CHANGE_ARTIFACTS

   Only optional elements carry omission choices, reasons and editing
   instructions at their point of use; no central list duplicates them.

.. vc:: Change affected artifacts come from the impact query
   :id: SYSP_VC_CHANGE_ARTIFACTS_5
   :status: approved
   :verifies: SYSP_REQ_CHANGE_ARTIFACTS

   The template and example name the impact skill by purpose, carry an
   ``Impact query`` line, offer the four dispositions and require the table in
   the Architect's completion evidence.

.. req:: Change Version Control
   :id: SYSP_REQ_CHANGE_VERSION_CONTROL
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CHANGE_CONTRACT
   :realized_by: docs/Syspilot Contracts/change.md

   Project Manager shall own one Version control artifact recording the feature
   branch and integration state: ``active`` during work and ``merged`` after
   squash-integration into ``development``. The branch name shall appear only
   in that row; no-branch cases shall use ``Included``, not a special branch value.
   This authority shall cover branch creation and squash-integration only,
   leaving promotion to ``main`` to Release under a Release Contract.
   Branch creation and integration shall stay with the single actor holding
   current responsibility at those moments.

.. vc:: Change branch authority ends at development integration
   :id: SYSP_VC_CHANGE_VERSION_CONTROL_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_VERSION_CONTROL

   The sole version-control row has Project Manager ownership and the defined
   branch/status semantics; it grants no promotion to ``main``.

.. req:: Change Documentation And Example Applicability
   :id: SYSP_REQ_CHANGE_DOCUMENTATION
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CHANGE_CONTRACT
   :realized_by: docs/Syspilot Contracts/change.md

   A Change shall offer optional Technical Writer-owned user-facing documentation
   with evidence of agreed surfaces, coherent explanations, factual-owner
   review, current ``doc``/``includes`` links and a clean build.
   Incoming ``included_in`` links shall inform impact review.
   Purpose and authority, not path or format, shall distinguish derived
   documentation from authoritative textual artifacts.

   The ``Example sync`` row shall be included by default and owned by Technical
   Writer. It shall require generic changes in ``docs/Example Actors/``,
   ``docs/Example Contracts/`` and ``docs/Example Ontology/``, declared
   role-card deviations and a clean build;
   ``not applicable`` shall require a reason in the row.

.. vc:: Change documentation evidence covers its declared surfaces
   :id: SYSP_VC_CHANGE_DOCUMENTATION_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_DOCUMENTATION

   Documentation applicability uses incoming impact and authority/purpose;
   the optional row requires complete Technical Writer evidence.

.. vc:: Change examples have an explicit maintenance disposition
   :id: SYSP_VC_CHANGE_DOCUMENTATION_2
   :status: approved
   :verifies: SYSP_REQ_CHANGE_DOCUMENTATION

   Example sync starts included, with Technical Writer ownership; closure
   records generic updates and deviations or a reasoned not-applicable result.

.. req:: Change Verification Evidence
   :id: SYSP_REQ_CHANGE_VERIFICATION
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CHANGE_CONTRACT
   :realized_by: docs/Syspilot Contracts/change.md

   A Change shall record durable architecture/implementation decisions and
   evidence, changed artifacts, unit verification and applicable acceptance results.
   Artifact rows shall assign unit-test writing/execution to Developer,
   requirement tests and User-validation means to Tester, and recorded-result
   review to Quality, with commands and results. Quality's own check execution
   shall require a recorded insufficiency reason.

   Verification shall be automated; missing automation shall remain an open
   quality issue with task, owner and completion evidence. Markdown content
   without an automated check shall receive Quality's recorded review.
   Quality evidence shall record a current judgment, applied methods with scope,
   evidence, findings and limits, and only open issues returned to affected owners.

.. vc:: Change test evidence identifies the responsible producer
   :id: SYSP_VC_CHANGE_VERIFICATION_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_VERIFICATION

   Decision and test records identify artifacts, commands, results and the
   assigned Developer/Tester duties.

.. vc:: Change verification gaps remain actionable
   :id: SYSP_VC_CHANGE_VERIFICATION_2
   :status: approved
   :verifies: SYSP_REQ_CHANGE_VERIFICATION

   Missing automation has an open issue with task, owner and completion evidence;
   unautomated Markdown content has a recorded Quality review.

.. vc:: Change Quality state remains current
   :id: SYSP_VC_CHANGE_VERIFICATION_3
   :status: approved
   :verifies: SYSP_REQ_CHANGE_VERIFICATION

   Review fields expose the current judgment, method scope/evidence/findings/limits
   and only actionable open issues assigned back to artifact owners.

.. vc:: Change Quality reviews existing results before execution
   :id: SYSP_VC_CHANGE_VERIFICATION_4
   :status: approved
   :verifies: SYSP_REQ_CHANGE_VERIFICATION

   Quality reviews recorded results first; each check it executes has a recorded
   reason why those results could not support the judgment.

.. req:: Change Validation And Closure
   :id: SYSP_REQ_CHANGE_CLOSURE
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CHANGE_CONTRACT
   :realized_by: docs/Syspilot Contracts/change.md

   Quality shall communicate ``proceed`` and evidence directly to Project
   Manager before outcome presentation and User validation.
   Applicable User decisions shall reach Project Manager directly before recording;
   forwarded claims shall establish neither Quality nor User decisions.
   User validation shall become ``not applicable`` only through explicit
   delegation recorded at its row, never through Operation Mode or a claim of
   validation that did not occur.

   Project Manager shall close only with terminal evidence for all included
   artifacts/gates, Quality proceed, demonstrated outcome, explicit validation
   disposition and recorded integration state.

   The Closure checklist shall explicitly require the feature branch to be
   squash-integrated into ``development`` before closure. A ``Version control``
   row marked ``not applicable`` shall satisfy that item only with its recorded
   reason. The generic example shall use ``{integration branch}`` for the
   corresponding target.

.. vc:: Change validation has direct decision provenance
   :id: SYSP_VC_CHANGE_CLOSURE_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_CLOSURE

   Presentation follows Quality's direct result; validation is the User's direct
   decision or explicit row-level delegation, not an Operation Mode inference.

.. vc:: Change closure has no incomplete included artifact
   :id: SYSP_VC_CHANGE_CLOSURE_2
   :status: approved
   :verifies: SYSP_REQ_CHANGE_CLOSURE

   The closure checklist and completed Contract show terminal evidence,
   proceed, demonstrated outcome, validation disposition and integration.

.. vc:: Change closure explicitly checks integration
   :id: SYSP_VC_CHANGE_INTEGRATION_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_CLOSURE

   Both Closure checklists contain the integration item: ``development`` in
   the canonical template and ``{integration branch}`` in the example. An
   active, unintegrated branch does not satisfy it; completed squash integration
   or a reasoned ``not applicable`` Version control row does.
