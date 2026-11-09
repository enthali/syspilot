Pristine Syspilot Setup
=======================

.. story:: Pristine Syspilot Setup
   :id: SYSP_US_SETUP
   :status: approved
   :priority: mandatory
   :tags: setup, bootstrap, installation
   :tracked_by: ROOT_SYSPILOT

   **As** a project lead adopting syspilot in a new project,
   **I want** a minimal bootstrap prompt to load, materialize, and execute the
   Setup Contract of a selected release,
   **so that** the project receives a reproducible, verified, and permanently
   pinned syspilot baseline without installing a persistent Setup actor.

.. ac:: A pristine project receives a verified pinned baseline
   :id: SYSP_AC_SETUP_1
   :status: approved
   :validates: SYSP_US_SETUP

   Given a supported project with no confirmed Syspilot installation and the
   exact release tag supplied by the bootstrap prompt,
   When the materialized Setup Contract is executed from the initiating
   Copilot session on a User-approved dedicated branch, and continued by the
   Admin actor when that session lacks the Jarvis tools a later step needs,
   Then the installed project records and verifies the supplied release and
   commit, preserves existing project work and documentation infrastructure,
   and receives User-guided commit and merge before the Project Manager
   receives the successful handoff; or the Contract remains blocked with
   actionable evidence and does not claim installation success.

.. ac:: Setup continues when the starting session lacks Jarvis tools
   :id: SYSP_AC_SETUP_2
   :status: approved
   :validates: SYSP_US_SETUP

   Given an ordinary Copilot session that does not offer the Jarvis messaging
   tools,
   When it starts Setup,
   Then Setup records which tools were missing and transfers the Setup record
   to the Admin actor, which continues from the same record, or it reports the
   failure and gives the User a manual path with a prompt in the User's
   language, and it never reports a check or a delivery that did not happen.

.. ac:: Setup creates usable Actors and a building documentation
   :id: SYSP_AC_SETUP_3
   :status: approved
   :validates: SYSP_US_SETUP

   Given a pristine project, possibly with some of the nine Actors present,
   When Setup completes,
   Then the Actors were created through Jarvis and the pre-existing ones are
   unchanged, each created Actor's context names the installed role card and
   Contract registry by paths that resolve, and the project's documentation
   builds with zero warnings without any page or asset of the source project.

.. ac:: Setup claims only what its gates show
   :id: SYSP_AC_SETUP_4
   :status: approved
   :validates: SYSP_US_SETUP

   Given a Setup run in which Actor discovery is still pending or the
   documentation build reports a warning,
   When Setup evaluates its mandatory gates,
   Then the baseline is not verified, the Contract stays blocked with the gate
   named, and no successful handoff to the Project Manager is made.

.. ac:: Setup finds Jarvis Core where the session runs
   :id: SYSP_AC_SETUP_5
   :status: approved
   :validates: SYSP_US_SETUP

   Given a Copilot session in a VS Code instance and profile that lack
   Jarvis Core, possibly while another VS Code installation on the machine has
   it,
   When Setup checks its prerequisites,
   Then it detects the missing extension in the instance that hosts the
   session, installs it from the Marketplace only after the User's consent
   there, rechecks the version and the tools the session actually offers, asks
   for a reload only when the installed extension's tools are not offered, and
   reports a refusal or a failed installation as a blocker with a manual path.

.. ac:: Installed folders carry the project's name
   :id: SYSP_AC_SETUP_6
   :status: approved
   :validates: SYSP_US_SETUP

   Given a project whose name differs from Syspilot,
   When Setup installs the role cards and Contract processes,
   Then they are in two folders named after the project that the User
   confirmed before anything was written, every reference to them resolves, the
   copies are unchanged, and no folder carries Syspilot's name.