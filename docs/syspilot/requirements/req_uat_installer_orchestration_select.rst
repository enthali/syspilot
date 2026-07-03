Installer Orchestration Select Test Data
=========================================

Test data requirements for
``SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT``.


.. req:: UAT Test Data: Installer Orchestration Select, General Mutex & Scaffold Regression
   :id: SYSP_REQ_UAT_INSTALLER_ORCHESTRATION_SELECT
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orchestration, mutex, regression, critical, test-data
   :links: SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT

   **Description:**

   To run the scenarios in
   ``SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT``, the following artifacts,
   fixtures, and reference data SHALL be available to the human tester.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 40 30 30

      * - Artifact
        - Location
        - Relevance
      * - ``spec_installer.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_INSTALLER_SKILL_MUTEX``,
          ``SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT``,
          ``SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD`` (AC-1, AC-2, AC-3)
      * - ``syspilot.installer.agent.md``
        - ``syspilot/agents/``
        - Updated Installer implementation (all ACs)

   **Target-Project Fixtures:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - Initial State
        - Used By Scenario
      * - ``F-GROUP-PAIR``
        - Target project with a syspilot installation; two non-product
          Skills prepared, ``Skill R1`` (installed, e.g.
          ``.github/skills/reporting-basic/SKILL.md`` declaring
          ``group: reporting``) and ``Skill R2`` (not yet installed,
          declaring the same ``group: reporting``, different content)
        - AC-1 (general mutex mechanism)
      * - ``F-FRESH-ANY``
        - A clean target project, no prior syspilot install; either
          ``.jarvis/`` present or absent (tester's choice — the scenario
          applies regardless of which default is inferred)
        - AC-2 (GH #48 regression)
      * - ``F-FRESH-JARVIS``
        - A clean target project containing a ``.jarvis/`` directory, no
          prior syspilot install
        - AC-3 (GH #22 regression)

   **Reference Data:**

   * GH #48 — original defect: fresh install wrote both
     ``syspilot.orchestration-jarvis`` and
     ``syspilot.orchestration-subagent`` to the installed skill location
     simultaneously
   * GH #22 — original defect: no ``.jarvis/sessions/`` scaffolds were ever
     created, even when the async variant was in effect
   * The eligible-agent set and scaffold-shape reference already documented
     in ``SYSP_REQ_UAT_INSTALLER_SESSION_FIRST`` apply unchanged to AC-3
     here (not restated)

   **Tooling:**

   * VS Code with Copilot, target project open, Installer accessible —
     all three scenarios
   * A directory listing tool for the installed skill location (AC-1,
     AC-2) and ``.jarvis/sessions/`` (AC-3)
   * Awareness of the Jarvis session-list scan-latency testability note
     already recorded against ``SYSP_REQ_UAT_INSTALLER_SESSION_FIRST`` —
     applies to AC-3's scaffold-presence check

   **Preconditions (all scenarios):**

   * AC-1: Fixture ``F-GROUP-PAIR`` is prepared before AC-1 is run; neither
     Skill in the pair is a product syspilot Skill (isolates the test from
     the real orchestration group).
   * AC-2: Fixture ``F-FRESH-ANY`` is prepared before AC-2 is run.
   * AC-3: Fixture ``F-FRESH-JARVIS`` is prepared before AC-3 is run.
