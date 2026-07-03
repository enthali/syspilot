Installer Frontmatter Sync UAT
==============================

User Acceptance Test Story for the ``installer-frontmatter-sync`` change
request — a pure implementation catch-up (no spec change): the Installer
agent file's Step 4 wording is brought in line with its already-corrected
design spec (``SYSP_SPEC_INSTALLER_WORKFLOW``).


.. story:: UAT: Installer Frontmatter Sync
   :id: SYSP_US_UAT_INSTALLER_FRONTMATTER_SYNC
   :status: draft
   :priority: mandatory
   :tags: uat, installer, tools, regression, critical
   :links: SYSP_US_INSTALLER

   **As a** syspilot Test Designer,
   **I want** a single, fast, self-contained scenario confirming
   ``syspilot.installer.agent.md`` Step 4 no longer describes the retired
   ``tools:``-preservation logic and instead matches
   ``SYSP_SPEC_INSTALLER_WORKFLOW`` verbatim-from-upstream wording,
   **so that** the agent that actually runs at a customer's install/update
   no longer contradicts its own already-corrected spec before the Monday
   demo.

   **Context:**

   ``remove-tools-frontmatter`` already corrected
   ``SYSP_SPEC_INSTALLER_WORKFLOW`` Step 4 to verbatim-from-upstream
   semantics, but never synced ``syspilot.installer.agent.md`` (product
   source and installed instance), which still described the retired
   preservation logic. This CR is a pure implementation catch-up — no spec
   change.

   **Artifacts Under Test:**

   * ``syspilot/agents/syspilot.installer.agent.md`` (product source) Step 4
   * ``.github/agents/syspilot.installer.agent.md`` (installed instance) Step 4
   * ``docs/syspilot/design/spec_installer.rst`` —
     ``SYSP_SPEC_INSTALLER_WORKFLOW`` (reference, unchanged by this CR)

   **Traceability:**

   Regression check against ``SYSP_SPEC_INSTALLER_WORKFLOW`` Step 4
   (already-correct target content).
   Test data is defined in ``SYSP_REQ_UAT_INSTALLER_FRONTMATTER_SYNC``;
   expected outcomes in ``SYSP_SPEC_UAT_INSTALLER_FRONTMATTER_SYNC``.

   **Acceptance Criteria:**

   1. **Agent Step 4 matches the already-corrected spec (product + instance).**
      *Precondition:* Branch ``feature/installer-frontmatter-sync`` checked
      out; Implement stage has updated both
      ``syspilot/agents/syspilot.installer.agent.md`` and
      ``.github/agents/syspilot.installer.agent.md``.
      *Action:* Open Step 4 in both files; search for the retired phrasing
      ("read the current ``tools:`` frontmatter value from disk",
      "replace the upstream ``tools:`` line with the saved value") and
      compare against ``SYSP_SPEC_INSTALLER_WORKFLOW`` Step 4.
      *Expected result:* Neither file contains the retired
      preservation phrasing; both state every file is written verbatim
      from upstream with no local field preserved, except the Setup
      Bootloader's ``tools:`` field which is also written verbatim from
      upstream (not preserved) — matching
      ``SYSP_SPEC_INSTALLER_WORKFLOW`` — traces to the CR's sole
      acceptance criterion
