Installer — Scoped Orphan Cleanup Expected Outcomes
====================================================

Expected outcomes specification for ``SYSP_REQ_UAT_INSTALLER_SCOPED_CLEANUP``.
This document is the per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Installer Scoped Orphan Cleanup
   :id: SYSP_SPEC_UAT_INSTALLER_SCOPED_CLEANUP
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orphan-cleanup, scoped-cleanup, expected-outcomes
   :links: SYSP_REQ_UAT_INSTALLER_SCOPED_CLEANUP

   **Definition:**

   For each scenario in ``SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP``, the
   following outcomes SHALL be observable on the target project. Each
   scenario is self-contained: the human tester prepares the named fixture,
   runs the action, and confirms the expected result. A check item passes
   when the exact condition is met; it fails otherwise.

   ---

   **TC-SC-CUSTOMER — Customer-owned file survives orphan cleanup**

   *Precondition:* Fixture ``F-CUSTOMER-FILE`` (completed syspilot
   installation; ``myproject.pm.agent.md`` present in ``.github/agents/``;
   no upstream counterpart).

   *Action:* Re-run the Installer as an update.

   *Expected result:*

   * [ ] ``myproject.pm.agent.md`` is present in ``.github/agents/``
     after the Installer completes
   * [ ] The byte content (or hash) of ``myproject.pm.agent.md`` is
     identical to its pre-run state — no modification, truncation, or
     re-creation occurred
   * [ ] The Installer run summary does not list ``myproject.pm.agent.md``
     under removed files

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP`` AC-1

   ---

   **TC-SC-ORPHAN — Genuine syspilot orphan is removed**

   *Precondition:* Fixture ``F-SYSPILOT-ORPHAN`` (completed syspilot
   installation; ``syspilot.oldagent.agent.md`` present in
   ``.github/agents/``; that filename absent from current upstream
   ``syspilot/agents/``).

   *Action:* Re-run the Installer as an update.

   *Expected result:*

   * [ ] ``syspilot.oldagent.agent.md`` is absent from ``.github/agents/``
     after the Installer completes
   * [ ] All ``syspilot.``-prefixed files that ARE present in the current
     upstream ``syspilot/agents/`` are present in ``.github/agents/`` and
     have the expected current-product content
   * [ ] The Installer run summary lists ``syspilot.oldagent.agent.md``
     under removed files (orphan cleanup reported)

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP`` AC-2

   ---

   **TC-SC-TAILORING — Tailoring file survives orphan cleanup**

   *Precondition:* Fixture ``F-TAILORING`` (completed syspilot installation;
   ``syspilot.pm.tailoring.md`` present in ``.github/agents/``; no upstream
   counterpart).

   *Action:* Re-run the Installer as an update.

   *Expected result:*

   * [ ] ``syspilot.pm.tailoring.md`` is present in ``.github/agents/``
     after the Installer completes
   * [ ] The byte content (or hash) of ``syspilot.pm.tailoring.md`` is
     identical to its pre-run state — no modification, truncation, or
     re-creation occurred
   * [ ] The Installer run summary does not list ``syspilot.pm.tailoring.md``
     under removed files

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP`` AC-3
