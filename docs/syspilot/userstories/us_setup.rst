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
   When the initiating Copilot session executes the materialized Setup
   Contract on a User-approved dedicated branch,
   Then the installed project records and verifies the supplied release and
   commit, preserves existing project work and documentation infrastructure,
   and receives User-guided commit and merge before the Project Manager
   receives the successful handoff; or the Contract remains blocked with
   actionable evidence and does not claim installation success.