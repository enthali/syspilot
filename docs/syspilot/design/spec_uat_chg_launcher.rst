Change Launcher UAT Expected Outcomes
=======================================

Expected outcomes specification for ``SYSP_REQ_UAT_CHG_LAUNCHER``.
This document is the per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Change Launcher Automation
   :id: SYSP_SPEC_UAT_CHG_LAUNCHER
   :status: draft
   :priority: mandatory
   :tags: uat, skill, pm, automation, expected-outcomes
   :links: SYSP_REQ_UAT_CHG_LAUNCHER

   **Definition:**

   For each scenario in ``SYSP_US_UAT_CHG_LAUNCHER``, the following outcomes
   SHALL be observable. Each scenario is self-contained: the human tester
   prepares the named fixture, runs the invocation command, and confirms each
   check item. A check item passes when the exact condition is met; it fails
   otherwise.

   All scenarios require a working Python environment and Git on ``development``
   (or the fixture variant). See ``SYSP_REQ_UAT_CHG_LAUNCHER`` for invocation
   commands and cleanup steps.

   ---

   **TC-HAPPY — Full happy path (AC-1)**

   *Precondition:* Fixture ``F-CLEAN`` active.

   *Action:* Run the invocation command for AC-1 from the repo root.

   *Expected result:*

   * [ ] The script exits with code 0
   * [ ] A branch ``feature/uat-test-launch`` exists (``git branch`` shows it)
   * [ ] The file ``docs/changes/uat-test-launch.md`` exists
   * [ ] The file ``docs/changes/uat-test-launch.md`` contains exactly:
     ``Status: in-progress`` (not ``draft``)
   * [ ] The file contains ``Branch: feature/uat-test-launch``
   * [ ] The file contains ``Created:`` followed by today's date in
     ``YYYY-MM-DD`` format
   * [ ] The file contains ``Author: TestRunner``
   * [ ] The file contains ``Operation Mode: autonomous``
   * [ ] ``git log --oneline -1`` shows a commit with message
     ``pm(cr): scaffold Change Document for uat-test-launch``
   * [ ] stdout confirms the branch name and file path

   *Traces to:* ``SYSP_REQ_CHG_LAUNCHER`` AC-1, AC-2, AC-4, AC-5, AC-6

   ---

   **TC-BRANCH-EXISTS — Existing branch: warn and continue (AC-2)**

   *Precondition:* Fixture ``F-BRANCH-EXISTS`` active (``feature/uat-test-launch``
   exists, ``docs/changes/uat-test-launch.md`` does not).

   *Action:* Run the invocation command for AC-2 from the repo root.

   *Expected result:*

   * [ ] stdout contains a warning message indicating the branch already exists
   * [ ] The script does NOT exit with code 1 (it continues past the warning)
   * [ ] The working branch after the run is ``feature/uat-test-launch``
     (``git branch --show-current`` confirms)
   * [ ] ``docs/changes/uat-test-launch.md`` is created and pre-filled with
     all five header fields (same checks as TC-HAPPY header items)
   * [ ] An initial commit is made (``git log --oneline -1`` shows the
     scaffold commit message)
   * [ ] The script exits with code 0

   *Traces to:* ``SYSP_REQ_CHG_LAUNCHER`` AC-3

   ---

   **TC-CD-EXISTS — Change Document already exists: exit 1 (AC-3)**

   *Precondition:* Fixture ``F-CD-EXISTS`` active
   (``docs/changes/uat-test-launch.md`` already exists).

   *Action:* Run the invocation command for AC-3 from the repo root.

   *Expected result:*

   * [ ] The script exits with code 1
   * [ ] An error message is printed to stdout or stderr referencing the
     existing file
   * [ ] No new branch is created (``git branch`` does not show
     ``feature/uat-test-launch`` if it did not exist before the run)
   * [ ] No new commit is made (``git log --oneline -1`` is unchanged from
     before the run)
   * [ ] The pre-existing ``docs/changes/uat-test-launch.md`` is unmodified

   *Traces to:* ``SYSP_REQ_CHG_LAUNCHER`` AC-7

   ---

   **TC-TEMPLATE-MISSING — Template absent: exit 1 (AC-4)**

   *Precondition:* Fixture ``F-TEMPLATE-MISSING`` active (template renamed
   or removed; restore after this test).

   *Action:* Run the invocation command for AC-4 from the repo root.

   *Expected result:*

   * [ ] The script exits with code 1
   * [ ] An error message is printed to stdout or stderr referencing the
     missing template
   * [ ] No branch is created, no file is written, no commit is made
   * [ ] Restoring the template (rename back) leaves the repository in
     its original state

   *Traces to:* ``SYSP_REQ_CHG_LAUNCHER`` AC-8

   ---

   **TC-SKILL-MD — SKILL.md documentation (AC-5)**

   *Precondition:* ``syspilot/skills/syspilot.change-launcher/SKILL.md``
   present in the working tree (no fixture preparation required).

   *Action:* Open and read
   ``syspilot/skills/syspilot.change-launcher/SKILL.md``.

   *Expected result:*

   * [ ] A description section explains what the script automates
   * [ ] A parameters section documents ``--name``, ``--author``, and
     ``--mode`` — including types and any constraints (e.g. kebab-case for
     ``--name``, allowed values for ``--mode``)
   * [ ] An error/warning conditions section describes at minimum:
     branch-exists (warn + continue), CD-already-exists (exit 1), and
     template-missing (exit 1)
   * [ ] Exit codes (0 = success, 1 = precondition failure) are documented

   *Traces to:* ``SYSP_REQ_CHG_LAUNCHER`` AC-9
