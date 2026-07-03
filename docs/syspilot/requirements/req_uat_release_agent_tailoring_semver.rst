Release Agent Tailoring Semver Test Data
=========================================

Test data requirements for ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER``.


.. req:: UAT Test Data: Release Agent Tailoring & Semver Regression Prevention
   :id: SYSP_REQ_UAT_RELEASE_TAILORING_SEMVER
   :status: draft
   :priority: mandatory
   :tags: uat, release, tailoring, skill-arch, branching, semver, test-data
   :links: SYSP_US_UAT_RELEASE_TAILORING_SEMVER

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_RELEASE_TAILORING_SEMVER``, the
   following artifacts, fixtures, and reference data SHALL be available to
   the human tester.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 40 30 30

      * - Artifact
        - Location
        - Relevance
      * - ``spec_release_engineer.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_RELEASE_WORKFLOW`` (AC-1, AC-2)
      * - ``spec_skill_arch.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_SKILL_ARCH_TAILORING`` (AC-6)
      * - ``spec_skill_branching.rst``
        - ``docs/syspilot/design/``
        - ``SYSP_SPEC_SKILL_BRANCHING_RETENTION`` (AC-7)
      * - ``syspilot.release.agent.md``
        - ``syspilot/agents/``
        - Updated Release Engineer agent (AC-3)
      * - ``syspilot.release.tailoring.md``
        - ``.github/agents/`` (syspilot's own instance)
        - syspilot's own tailoring content (AC-4)

   **Target-Project Fixtures:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - Initial State
        - Used By Scenario
      * - ``F-NO-TAILORING``
        - Target project with a syspilot installation; no
          ``.github/agents/syspilot.release.tailoring.md`` present
        - AC-3 (missing tailoring escalation)
      * - ``F-PROJECT-SEMVER``
        - Target project ("Project A") with a syspilot installation and
          ``syspilot.release.tailoring.md`` specifying semver; at least
          one prior ``docs/changes/<version>/`` archive folder present to
          establish a current version
        - AC-5 (cross-project isolation, semver side)
      * - ``F-PROJECT-CALVER``
        - A second, independent target project ("Project B") with a
          syspilot installation and ``syspilot.release.tailoring.md``
          specifying CalVer; at least one prior
          ``docs/changes/<version>/`` archive folder present
        - AC-5 (cross-project isolation, CalVer side)
      * - ``F-RETAIN-DEFAULT``
        - Target project with a syspilot installation, no
          ``.github/skills/syspilot.branching/tailoring.md`` override, and
          at least one ``feature/*`` branch fully merged into
          ``development`` and ready for release
        - AC-7 (retention default)

   **Reference Data:**

   * The exact scheme-name strings to search for in AC-1's negative check:
     ``CalVer``, ``semver``, ``vYYYY.MM.DD`` (or any literal date/semver
     pattern) — a match found in the *rule* text (not an illustrative
     example) fails the scenario
   * Project A's and Project B's respective computed next versions,
     recorded independently before each release run, to compare against
     post-release output in AC-5

   **Tooling:**

   * A text search tool for scanning spec RST node bodies (VS Code Search,
     ``grep``, PowerShell ``Select-String``) — AC-1, AC-2, AC-6
   * VS Code with Copilot, each target project open, ``@syspilot.release``
     (or the PM-triggered release flow) accessible — AC-3, AC-5, AC-7
   * ``git branch -a`` or equivalent to confirm branch existence
     post-release — AC-7

   **Preconditions (all scenarios):**

   * AC-1: Branch ``feature/release-agent-tailoring-semver`` is checked out
     in the syspilot workspace before AC-1, AC-2, AC-4, AC-6 are run.
   * AC-2: Fixture ``F-NO-TAILORING`` is prepared before AC-3 is run.
   * AC-3: Fixtures ``F-PROJECT-SEMVER`` and ``F-PROJECT-CALVER`` are
     prepared as two fully independent target projects before AC-5 is run.
   * AC-4: Fixture ``F-RETAIN-DEFAULT`` is prepared before AC-7 is run.
