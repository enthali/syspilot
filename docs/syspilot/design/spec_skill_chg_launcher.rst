Change Launcher Skill Design
============================

.. spec:: Change Launcher Script
   :id: SYSP_SPEC_CHG_LAUNCHER
   :status: draft
   :priority: mandatory
   :tags: skill, pm, automation
   :links: SYSP_REQ_CHG_LAUNCHER

   **Definition:**

   The change-launcher is a Python script at
   ``syspilot/skills/syspilot.change-launcher/launch_change.py``.

   **Interface:**

   ::

      python launch_change.py --name <change-name> --author <author> --mode <mode>

   * ``--name`` — Change name (used for branch and file naming, kebab-case)
   * ``--author`` — Author string for the header (e.g. ``PM``)
   * ``--mode`` — Operation mode: ``autonomous`` or ``user-guided``

   All three arguments are required. No interactive prompts.

   **Behaviour:**

   1. **Validate preconditions:**

      * Current branch is ``development`` (or error)
      * ``syspilot/templates/change-document.md`` exists (or error)
      * ``docs/changes/<name>.md`` does not already exist (or error)

   2. **Create or switch to branch:**

      * If ``feature/<name>`` does not exist: ``git checkout -b feature/<name>``
      * If ``feature/<name>`` already exists: warn to stdout, ``git checkout feature/<name>``

   3. **Copy template:**

      * Copy ``syspilot/templates/change-document.md`` to ``docs/changes/<name>.md``

   4. **Pre-fill header fields** (regex replacement in the copied file):

      * ``{NAME}`` → ``<name>``
      * ``draft | in-progress | review | approved | merged`` → ``in-progress``
      * ``feature/{NAME}`` → ``feature/<name>``
      * ``{DATE}`` → today's date (YYYY-MM-DD)
      * ``{AUTHOR(S)}`` → ``<author>``
      * ``user-guided (default) | autonomous`` → ``<mode>``

   5. **Commit:**

      * ``git add docs/changes/<name>.md``
      * ``git commit -m "pm(cr): scaffold Change Document for <name>"``

   **Exit Codes:**

   * 0 — success
   * 1 — precondition failure (template missing, CD already exists, not on
     development)

   **Output:** stdout confirmation with branch name and file path.

   **SKILL.md Content:**

   The skill directory contains a ``SKILL.md`` with:

   * Description: what the script automates
   * Parameters: ``--name``, ``--author``, ``--mode`` with types and constraints
   * Error/warning conditions and exit codes

   **Installation:**

   The Setup Agent copies ``syspilot/skills/syspilot.change-launcher/`` to
   ``.github/skills/syspilot.change-launcher/`` during installation.
