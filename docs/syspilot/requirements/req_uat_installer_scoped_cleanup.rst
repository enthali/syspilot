Installer — Scoped Orphan Cleanup Test Data
===========================================

Test data requirements for ``SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP``.


.. req:: UAT Test Data: Installer Scoped Orphan Cleanup
   :id: SYSP_REQ_UAT_INSTALLER_SCOPED_CLEANUP
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orphan-cleanup, scoped-cleanup, test-data
   :links: SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP``, the
   following target-project fixtures and reference data SHALL be available
   to the human tester. Each scenario consumes one fixture state.

   **Target-Project Fixtures:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - Initial State
        - Used By Scenario
      * - ``F-CUSTOMER-FILE``
        - Completed syspilot installation; file ``myproject.pm.agent.md``
          manually placed in ``.github/agents/``; no upstream counterpart
          in ``syspilot/agents/``
        - AC-1 (customer-owned file preserved)
      * - ``F-SYSPILOT-ORPHAN``
        - Completed syspilot installation; file
          ``syspilot.oldagent.agent.md`` present in ``.github/agents/``;
          that filename does not exist in ``syspilot/agents/`` of the
          current upstream
        - AC-2 (genuine orphan removed)
      * - ``F-TAILORING``
        - Completed syspilot installation; file
          ``syspilot.pm.tailoring.md`` manually placed in
          ``.github/agents/``; no file with that name exists in
          ``syspilot/agents/``
        - AC-3 (tailoring file preserved)

   **Reference Data:**

   * The exact byte content of ``myproject.pm.agent.md`` before the update
     run (captured as a hash or stored copy) — used to confirm no
     modification in AC-1
   * The exact byte content of ``syspilot.pm.tailoring.md`` before the
     update run (captured as a hash or stored copy) — used to confirm no
     modification in AC-3
   * The list of all ``syspilot.``-prefixed files in ``syspilot/agents/``
     for the current upstream — used to confirm AC-2 removes only the
     orphan and leaves all current files intact

   **Tooling:**

   * ``git status`` or a file-hash utility to confirm ``myproject.pm.agent.md``
     is byte-for-byte unchanged after the update (AC-1)
   * A directory listing of ``.github/agents/`` before and after the run
     to confirm the orphan is absent post-update (AC-2) and the
     non-prefixed file is present post-update (AC-1)

   **Acceptance Criteria:**

   * AC-1: Fixture ``F-CUSTOMER-FILE`` can be prepared on a real target
     project before scenario AC-1 is run
   * AC-2: Fixture ``F-SYSPILOT-ORPHAN`` can be prepared on a real target
     project before scenario AC-2 is run; the orphan filename is confirmed
     absent from the current upstream product
   * AC-3: Fixture ``F-TAILORING`` can be prepared on a real target
     project before scenario AC-3 is run
