Pristine Syspilot Setup
=======================

.. req:: Pristine Setup Contract
   :id: SYSP_REQ_SETUP
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/setup.md

   Pristine Syspilot setup shall use a release-bound Setup Contract that:

   - receives the exact SemVer release tag and materialized release-bound
     Contract from the external bootstrap prompt, uses the supplied release
     without selecting or resolving another version, verifies its full Git
     commit identity, and uses that commit tree as the authoritative
     installation source;
   - owns all behavior after execution starts, including prerequisite checks,
     user interaction, installation, evidence, blockers, and handoff;
   - proceeds to its dedicated Setup branch only after confirming that the
     target is version controlled, the bootstrap-materialized
     ``.syspilot/setup-contract.md`` is its only working-tree change, and the
     User has approved the branch from the selected project state;
   - treats a confirmed existing Syspilot baseline as outside pristine Setup,
     but presents other possible Syspilot artifacts to the User for disposition
     instead of treating every similar artifact as an installation or deleting
     it;
   - copies Syspilot instructions and skills additively into an occupied
     ``.github/instructions/`` or ``.github/skills/`` directory, preserving
     existing unrelated files rather than requiring an empty destination, and
     surfaces an existing ignore rule that would silently exclude a generated
     destination as a blocker instead of a silent installation gap;
   - verifies Jarvis Core before any Jarvis-dependent action and records an
     actionable blocker without claiming success when a mandatory prerequisite
     is unavailable;
   - distinguishes immutable release-owned product artifacts, generated
     project-instance artifacts, and protected user-owned configuration;
   - preserves an existing configured ontology regardless of whether it is
     defined in ``conf.py``, ``ubproject.toml``, or another TOML source, and
     installs the Syspilot baseline ontology only when no ontology exists;
   - independently preserves an existing Sphinx-Needs environment or, when
     Sphinx-Needs is absent, installs a supported project-local environment
     without overwriting existing project dependency or documentation files,
     and obtains User guidance for additive integration rather than replacing
     or evaluating project-owned configuration;
   - generates and audits one platform-appropriate installation script whose
     dry run and execution use the same declared operation path, retains
     identical destinations, and blocks on differing release-owned
     destinations that are not an approved integration;
   - records the supplied release tag, corresponding commit, and approved
     project baseline in the versioned ``.syspilot/project.toml`` file;
   - generates exactly the nine persistent Syspilot actors Project Manager,
     Architect, Developer, Tester, Quality, Release, Research, Technical
     Writer, and Admin without generating a Setup actor or opening their
     sessions, and verifies that Jarvis actor discovery includes all nine
     regardless of unrelated actors already present;
   - verifies the declared installation inventory and content integrity,
     installed structure, actor files and Jarvis discovery, successful
     zero-warning target documentation build with its selected ontology, and
     baseline readback before declaring the installation complete;
   - obtains User guidance to commit and merge the verified Setup branch into
     the selected target branch, completes that Git integration, and only then
     sends the Project Manager ``Installation complete, welcome to this
     project`` with the completion summary, the identity of the selected
     ontology, and first-project guidance that requires the Project Manager to
     explain its artifact types, statuses, and relationships and ask the User
     whether it fits the project;
   - continues normal project intake without an ontology Change when the User
     accepts the selected ontology, but when the User requests an adjustment,
     requires the Project Manager to start a normal Change before any ontology
     modification and uses the existing Ontology skill only as technical
     guidance within that Change;
   - exposes every unmet mandatory condition as explicit Contract evidence and
     does not produce a successful Project Manager handoff while blocked;
   - does not install or retain a persistent Setup actor;
   - permits a later technical update only when a separate project-specific
     Change records the old and proposed baselines, impact analysis,
     revalidation scope, authorization, and assigned technical executor; and
   - carries the shared rules of the Contract Document method in the form its
     single executor allows: a Handover log whose entry records the one
     handoff to the Project Manager in the commit that changes the header, the
     scope-change rule applied to gates that already passed, one statement of
     installed-artifact ownership in the inventory, one statement of
     verification-gate ownership naming the executor as sole owner, the Setup
     Contract opened in the User's editor in the step that asks for the Setup
     branch, and the
     Project Manager's refresh and header check before it acts on the
     completion message.

.. vc:: Setup Contract establishes a reproducible project baseline
   :id: SYSP_VC_SETUP_1
   :status: approved
   :verifies: SYSP_REQ_SETUP

   Execute the materialized Setup Contract against a version-controlled
   project whose only initial working-tree change is that Contract, using the
   exact release tag supplied by the bootstrap prompt, and inspect the
   completed Contract, target Git history, installed inventory, Jarvis actor
   and session lists, target documentation build, and
   ``.syspilot/project.toml``. Confirm that Setup uses the supplied release and
   corresponding full commit without selecting another version; possible
   pre-existing artifacts and documentation integration receive User-guided
   disposition; any existing ontology remains authoritative and the baseline
   ontology is installed only when none exists; Sphinx-Needs is independently
   preserved or installed as needed; unrelated project work and documentation
   infrastructure remain intact; the nine expected persistent Syspilot actors
   are discovered without a Setup actor or Setup-opened sessions; every
   mandatory gate records passing evidence before baseline verification and
   the Contract names the executor as the single owner of those gates; Git
   commit and merge complete before the Project Manager handoff; the handoff
   identifies the selected ontology and directs the Project Manager to explain
   its artifact types, statuses, and relationships and ask the User whether it
   fits; acceptance continues normal intake without an ontology Change, while
   a requested adjustment starts a normal Change before modification and uses
   the existing Ontology skill only for technical guidance; blockers cannot
   report success; and later updates require an authorized project-specific
   Change. Confirm that an occupied ``.github/instructions/`` or
   ``.github/skills/`` destination keeps its existing unrelated files after
   installation, and that an ignore rule which would silently exclude a
   generated destination is reported as a blocker rather than passed over.