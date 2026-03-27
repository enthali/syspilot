Instance Release Design
=======================

Project-specific release design specifications for syspilot.

**Last Updated**: 2026-03-27


.. spec:: Release Agent Configuration
   :id: INST_SYSPILOT_SPEC_REL_AGENT_CONFIG
   :status: approved
   :tags: instance, release, agent
   :links: INST_SYSPILOT_REQ_REL_VERSION_FILE, INST_SYSPILOT_REQ_REL_GITHUB_PUBLISH, INST_SYSPILOT_REQ_REL_NOTES_FORMAT

   **Design:**
   syspilot's customized release agent lives at ``.github/agents/syspilot.release.agent.md``.
   It contains a Release Decisions table with project-specific configuration:

   .. list-table::
      :header-rows: 1

      * - Decision
        - Value
      * - Version file
        - ``syspilot/version.json``
      * - Tag format
        - ``v{version}``
      * - Release notes
        - ``docs/releasenotes.md``
      * - Change doc policy
        - Archive to ``docs/changes/archive/{version}/``
      * - Pre-release validation
        - Sphinx build, link check
      * - Platform
        - GitHub Releases

   **File:** ``.github/agents/syspilot.release.agent.md``

   This file is the *instance-level* customization of the product template
   at ``syspilot/agents/syspilot.release.agent.md``.


.. spec:: Release CI/CD Workflow
   :id: INST_SYSPILOT_SPEC_REL_WORKFLOW
   :status: approved
   :tags: instance, release, ci-cd
   :links: INST_SYSPILOT_REQ_REL_CI_PIPELINE

   **Design:**
   GitHub Actions workflow at ``.github/workflows/release.yml``.

   **Trigger:** Push of tag matching ``v*``

   **Steps:**

   1. Validate ``syspilot/version.json`` matches tag version
   2. Build Sphinx documentation (verify 0 errors)
   3. Extract current version release notes from ``docs/releasenotes.md``
   4. Create GitHub Release with extracted notes
   5. Attach ``syspilot/version.json`` as release asset
   6. Deploy documentation to GitHub Pages

   **File:** ``.github/workflows/release.yml``


.. spec:: Change Document Archive Process
   :id: INST_SYSPILOT_SPEC_REL_ARCHIVE_PROCESS
   :status: approved
   :tags: instance, release, traceability
   :links: INST_SYSPILOT_REQ_REL_CHANGE_ARCHIVE

   **Design:**
   During release, the release agent moves completed change documents:

   .. code-block:: text

      docs/changes/<name>.md → docs/changes/archive/<version>/<name>.md

   **Rules:**

   * Only documents with status ``approved`` or ``implemented`` are archived
   * The ``archive/`` directory is organized by release version
   * Git history is preserved (``git mv``, not copy+delete)
   * After archival, ``docs/changes/`` contains only ``archive/`` and new drafts
