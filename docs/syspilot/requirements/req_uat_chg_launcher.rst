Change Launcher UAT Test Data
==============================

Test data requirements for ``SYSP_US_UAT_CHG_LAUNCHER``.


.. req:: UAT Test Data: Change Launcher Automation
   :id: SYSP_REQ_UAT_CHG_LAUNCHER
   :status: draft
   :priority: mandatory
   :tags: uat, skill, pm, automation, test-data
   :links: SYSP_US_UAT_CHG_LAUNCHER

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_CHG_LAUNCHER``, the following
   artifacts, fixtures, and reference data SHALL be available to the human
   tester. All scenarios require a Git repository on the ``development``
   branch (or a controlled variant) and the ability to run Python scripts.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 40 30 30

      * - Artifact
        - Location
        - Relevance
      * - ``launch_change.py``
        - ``syspilot/skills/syspilot.change-launcher/``
        - All ACs (script under test)
      * - ``change-document.md`` (template)
        - ``syspilot/templates/``
        - AC-1, AC-3, AC-4 (template source)
      * - ``SKILL.md``
        - ``syspilot/skills/syspilot.change-launcher/``
        - AC-5

   **Fixtures:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - State
        - Used By
      * - ``F-CLEAN``
        - Repo on ``development`` branch; template present at
          ``syspilot/templates/change-document.md``; no branch
          ``feature/uat-test-launch`` and no file
          ``docs/changes/uat-test-launch.md`` exist
        - AC-1
      * - ``F-BRANCH-EXISTS``
        - Same as ``F-CLEAN`` except ``feature/uat-test-launch`` already
          exists (create with ``git checkout -b feature/uat-test-launch``
          then ``git checkout development``)
        - AC-2
      * - ``F-CD-EXISTS``
        - Same as ``F-CLEAN`` except an empty file (or any file) exists
          at ``docs/changes/uat-test-launch.md``
        - AC-3
      * - ``F-TEMPLATE-MISSING``
        - Same as ``F-CLEAN`` except the template is temporarily renamed
          or removed (restore after test)
        - AC-4

   **Invocation Commands:**

   .. code-block:: shell

      # AC-1, AC-2 — happy path / branch-exists
      python syspilot/skills/syspilot.change-launcher/launch_change.py \
          --name uat-test-launch --author TestRunner --mode autonomous

      # AC-3 — CD already exists (same command, F-CD-EXISTS fixture)
      python syspilot/skills/syspilot.change-launcher/launch_change.py \
          --name uat-test-launch --author TestRunner --mode autonomous

      # AC-4 — template missing (same command, F-TEMPLATE-MISSING fixture)
      python syspilot/skills/syspilot.change-launcher/launch_change.py \
          --name uat-test-launch --author TestRunner --mode autonomous

   **Reference Data:**

   * Expected branch name: ``feature/uat-test-launch``
   * Expected output file: ``docs/changes/uat-test-launch.md``
   * Expected header fields after pre-fill:

     * ``Status: in-progress``
     * ``Branch: feature/uat-test-launch``
     * ``Created: <today's date in YYYY-MM-DD format>``
     * ``Author: TestRunner``
     * ``Operation Mode: autonomous``

   * Expected commit message: ``pm(cr): scaffold Change Document for uat-test-launch``
   * Expected exit code on success: ``0``
   * Expected exit code on precondition failure: ``1``

   **Cleanup:**

   After AC-1 and AC-2 runs, restore the repo state:

   .. code-block:: shell

      git checkout development
      git branch -D feature/uat-test-launch
      git rm --cached docs/changes/uat-test-launch.md
      git reset HEAD~1
      rm docs/changes/uat-test-launch.md
