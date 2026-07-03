Installer Frontmatter Sync Expected Outcomes
=============================================

Expected outcomes specification for
``SYSP_REQ_UAT_INSTALLER_FRONTMATTER_SYNC``.


.. spec:: UAT Expected Outcomes: Installer Frontmatter Sync
   :id: SYSP_SPEC_UAT_INSTALLER_FRONTMATTER_SYNC
   :status: draft
   :priority: mandatory
   :tags: uat, installer, tools, regression, critical, expected-outcomes
   :links: SYSP_REQ_UAT_INSTALLER_FRONTMATTER_SYNC

   **Definition:**

   The single scenario is self-contained: the human tester runs the
   action and confirms the expected result. A check item passes when the
   exact condition is met; it fails otherwise.

   ---

   **TC-IFS-SYNC — Agent Step 4 matches the already-corrected spec**

   *Precondition:* Branch ``feature/installer-frontmatter-sync`` checked
   out; Implement stage complete on both agent file copies.

   *Action:* Open Step 4 in ``syspilot/agents/syspilot.installer.agent.md``
   and ``.github/agents/syspilot.installer.agent.md``; search both for the
   retired preservation phrasing; compare wording against
   ``SYSP_SPEC_INSTALLER_WORKFLOW`` Step 4.

   *Expected result:*

   * [ ] Zero occurrences of "read the current ``tools:`` frontmatter
     value from disk" in either file
   * [ ] Zero occurrences of "replace the upstream ``tools:`` line with
     the saved value" in either file
   * [ ] Both files state every file is written verbatim from upstream,
     with no local field preserved
   * [ ] Both files state the Setup Bootloader's ``tools:`` field is also
     written verbatim from upstream (not preserved) — same exception
     wording as ``SYSP_SPEC_INSTALLER_WORKFLOW``

   *Traces to:* ``SYSP_US_UAT_INSTALLER_FRONTMATTER_SYNC`` AC-1
