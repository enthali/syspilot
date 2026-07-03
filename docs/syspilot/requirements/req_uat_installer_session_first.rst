Installer — Session-First Orchestration Test Data
=================================================

Test data requirements for ``SYSP_US_UAT_INSTALLER_SESSION_FIRST``.


.. req:: UAT Test Data: Installer Session-First Behavior
   :id: SYSP_REQ_UAT_INSTALLER_SESSION_FIRST
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orchestration, session-first, test-data
   :links: SYSP_US_UAT_INSTALLER_SESSION_FIRST

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_INSTALLER_SESSION_FIRST``, the
   following target-project fixtures and reference data SHALL be available to
   the human tester. Each scenario consumes one fixture state.

   **Target-Project Fixtures:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - Initial State
        - Used By Scenario
      * - ``F-JARVIS-CLEAN``
        - Clean project, ``.jarvis/`` directory present, no prior syspilot
          install
        - AC-1 (Jarvis path), AC-5 (bootstrap exception)
      * - ``F-NOJARVIS-CLEAN``
        - Clean project, NO ``.jarvis/`` directory, no prior syspilot install
        - AC-2 (subagent path)
      * - ``F-GROUP-INSTALLED``
        - Project with exactly one ``group: orchestration`` skill already
          installed
        - AC-3 (mutual exclusion)
      * - ``F-JARVIS-UPDATE``
        - Jarvis-path project with some scaffolds present (one with non-empty
          ``context.md``) and at least one eligible agent scaffold missing
        - AC-4 (update preservation)

   **Eligible-Agent Set:**

   The agents that SHALL receive a session scaffold on the Jarvis path are
   every agent in ``syspilot/agents/`` **except** ``syspilot.setup`` and
   ``syspilot.installer``:

   * ``syspilot.cm``, ``syspilot.pm``, ``syspilot.qm``
   * ``syspilot.design``, ``syspilot.uat``, ``syspilot.implement``,
     ``syspilot.mece``, ``syspilot.trace``, ``syspilot.docu``,
     ``syspilot.verify``, ``syspilot.release``

   **Scaffold Shape Reference:**

   For each eligible agent, the expected scaffold is::

      .jarvis/sessions/<name>/session.yaml

   where ``session.yaml`` contains a ``name:`` field and an ``agent:`` field,
   both read verbatim from the agent file's frontmatter. The directory segment
   ``<name>`` is the human-readable session name from the agent's ``name:``
   frontmatter.

   **Tooling:**

   * A BOM/byte-comparison tool or ``git status`` / file hashing to confirm
     that pre-existing ``session.yaml`` and ``context.md`` files are unchanged
     after an update (AC-4)
   * A directory listing tool for ``.jarvis/sessions/`` and the installed
     skill location
   * Access to each agent file's frontmatter to confirm the ``name:`` /
     ``agent:`` values used in scaffolds (AC-1, AC-12 of the story)

   **Acceptance Criteria:**

   * AC-1: The four fixtures above can be prepared on a real target project
     before the scenarios are run
   * AC-2: The eligible-agent set and scaffold-shape reference are available
     to the tester before they begin
   * AC-3: A byte-comparison mechanism is available to verify update
     preservation (AC-4 of the story)


   **Testability Note — Jarvis scan latency:**

   The Jarvis session list lags filesystem scaffold changes by up to one scan
   interval (≈ 1 minute) in **both** directions: a newly created
   ``session.yaml`` is not immediately addressable as a session, and a deleted
   one lingers in the session list until the next scan. Therefore:

   * The expected result for **scaffold creation** (AC-1, AC-4) SHALL be
     verified against the **filesystem** (the ``session.yaml`` file exists),
     not against the live Jarvis session list, which may not yet reflect it.
   * If a scenario depends on a scaffold being **addressable as a Jarvis
     session**, the tester SHALL allow for the scan delay (wait one scan
     interval or trigger a manual rescan) before asserting addressability.
   * Conversely, after a replacement (AC-3), a removed group member or a
     deleted scaffold may still appear in the session list until the next
     scan — this lingering entry is expected and is NOT a defect.
