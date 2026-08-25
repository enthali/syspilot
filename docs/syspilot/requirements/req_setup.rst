Pristine Syspilot Setup
=======================

.. req:: Pristine Setup Contract
   :id: SYSP_REQ_SETUP
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Processes/setup.md

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
   - generates exactly the eight persistent Syspilot actors Project Manager,
     Architect, Developer, Tester, Quality, Release, Research, and Technical
     Writer without generating a Setup actor or opening their sessions, and
     verifies that Jarvis actor discovery includes all eight regardless of
     unrelated actors already present;
   - verifies the declared installation inventory and content integrity,
     installed structure, actor files and Jarvis discovery, successful
     zero-warning target documentation build with its selected ontology, and
     baseline readback before declaring the installation complete;
   - obtains User guidance to commit and merge the verified Setup branch into
     the selected target branch, completes that Git integration, and only then
     sends the Project Manager ``Installation complete, welcome to this
     project`` with the completion summary and first-Change guidance;
   - exposes every unmet mandatory condition as explicit Contract evidence and
     does not produce a successful Project Manager handoff while blocked;
   - does not install or retain a persistent Setup actor; and
   - permits a later technical update only when a separate project-specific
     Change records the old and proposed baselines, impact analysis,
     revalidation scope, authorization, and assigned technical executor.

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
   infrastructure remain intact; the eight expected persistent Syspilot actors
   are discovered without a Setup actor or Setup-opened sessions; every
   mandatory gate records passing evidence before baseline verification; Git
   commit and merge complete before the Project Manager handoff; blockers
   cannot report success; and later updates require an authorized
   project-specific Change.