Change Launcher Skill Requirements
===================================

.. req:: Change Launcher Automation
   :id: SYSP_REQ_CHG_LAUNCHER
   :status: draft
   :priority: mandatory
   :tags: skill, pm, automation
   :links: SYSP_US_CHG_LAUNCHER

   **Description:**
   The ``syspilot.change-launcher`` skill SHALL provide a Python script that
   automates the four mechanical steps at the start of every change: create
   feature branch from ``development``, copy the change-document template,
   pre-fill the five header fields, and make the initial commit.

   **Rationale:**
   These steps are deterministic and require no judgment. Automating them
   eliminates a recurring source of errors and lets the PM focus on the
   Summary — the one part that requires human intent.

   **Acceptance Criteria:**

   * AC-1: The script accepts three required arguments: change name, author, and operation mode.
   * AC-2: The script creates a feature branch ``feature/<name>`` from ``development``.
   * AC-3: If the branch already exists, the script warns and continues (switches to existing branch).
   * AC-4: The script copies the change-document template to ``docs/changes/<name>.md``.
   * AC-5: The script pre-fills: Status = ``in-progress``, Branch = ``feature/<name>``, Created = today (YYYY-MM-DD), Author = provided author, Operation Mode = provided mode.
   * AC-6: The script makes an initial commit with the pre-filled Change Document.
   * AC-7: The script exits with an error if the Change Document file already exists.
   * AC-8: The script exits with an error if the template file is missing.
   * AC-9: The skill directory contains a ``SKILL.md`` documenting the script parameters and error conditions.
