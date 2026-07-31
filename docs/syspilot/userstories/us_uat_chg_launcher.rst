Change Launcher UAT
===================

User Acceptance Test Story for the ``chg-launcher`` change request —
verifying that ``launch_change.py`` automates branch creation, template
copy, header pre-fill, and initial commit correctly, and that error
conditions are handled cleanly.


.. story:: UAT: Change Launcher Automation
   :id: SYSP_US_UAT_CHG_LAUNCHER
   :status: draft
   :priority: mandatory
   :tags: uat, skill, pm, automation
   :links: SYSP_US_CHG_LAUNCHER

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the
   change-launcher script performs all four mechanical steps correctly and
   exits cleanly on precondition failures,
   **so that** the PM can trust the automation before relying on it for
   every new change initiative.

   **Artifacts Under Test:**

   * ``syspilot/skills/syspilot.change-launcher/launch_change.py`` — main script
   * ``syspilot/templates/change-document.md`` — template source
   * ``syspilot/skills/syspilot.change-launcher/SKILL.md`` — skill documentation

   **Acceptance Criteria:**

   1. Given the script is invoked with all three required arguments (``--name``, ``--author``, ``--mode``), When the preconditions are met, Then a feature branch is created from ``development``, the Change Document is copied and pre-filled, an initial commit is made, and the script exits with code 0.
   2. Given the target feature branch already exists, When the script is run, Then it emits a warning to stdout, switches to the existing branch, and continues without error.
   3. Given the target Change Document file already exists at ``docs/changes/<name>.md``, When the script is run, Then it exits with code 1 and an error message — no branch or file changes are made.
   4. Given the template file is absent, When the script is run, Then it exits with code 1 and an error message.
   5. Given the installed skill directory, When I read ``SKILL.md``, Then it documents the three parameters and the error/warning conditions.

   **Traceability:**

   Test data is defined in ``SYSP_REQ_UAT_CHG_LAUNCHER``; expected outcomes
   in ``SYSP_SPEC_UAT_CHG_LAUNCHER``.
