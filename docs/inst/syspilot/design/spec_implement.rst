Instance Implementation Design
==============================

Project-specific implementation design specifications for syspilot.

**Last Updated**: 2026-03-27


.. spec:: Product Directory Structure
   :id: INST_SYSPILOT_SPEC_IMPL_DIR_STRUCTURE
   :status: approved
   :tags: instance, implement, structure
   :links: INST_SYSPILOT_REQ_IMPL_WRITE_BOUNDARY

   **Design:**
   The Implement Agent writes exclusively to the ``syspilot/`` directory:

   .. code-block:: text

      syspilot/
      ├── agents/             # Agent templates (*.agent.md)
      ├── prompts/            # Prompt configurations (*.prompt.md)
      ├── skills/             # Shared skills (*.skill.md)
      ├── scripts/python/     # Utility scripts
      ├── sphinx/             # Sphinx build scripts
      ├── version.json        # Release version
      └── change-document.md  # Change Document template

   **Write Rules:**

   * Implement Agent: MAY write to ``syspilot/`` and ``docs/syspilot/``
   * Implement Agent: SHALL NOT write to ``.github/``
   * Setup Agent: syncs ``syspilot/`` → ``.github/`` on user request


.. spec:: Setup Agent Synchronization Process
   :id: INST_SYSPILOT_SPEC_IMPL_SYNC_PROCESS
   :status: approved
   :tags: instance, implement, setup
   :links: INST_SYSPILOT_REQ_IMPL_SETUP_SYNC

   **Design:**
   The Setup Agent is the only agent that writes to ``.github/``.
   It synchronizes product artifacts from ``syspilot/`` to ``.github/``:

   .. list-table::
      :header-rows: 1

      * - Source (syspilot/)
        - Target (.github/)
        - Strategy
      * - ``agents/*.agent.md``
        - ``agents/``
        - Intelligent merge (preserve user customizations)
      * - ``prompts/*.prompt.md``
        - ``prompts/``
        - Intelligent merge
      * - ``skills/*.skill.md``
        - ``skills/``
        - Intelligent merge
      * - ``scripts/python/*``
        - N/A (``.syspilot/scripts/``)
        - Replace

   **Merge Strategy:**

   * If local file identical to product → replace silently
   * If local file differs → present choices: Overwrite / Keep / Merge
   * User-only files in ``.github/`` are never touched
