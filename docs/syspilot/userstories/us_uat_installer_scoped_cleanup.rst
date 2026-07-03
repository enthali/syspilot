Installer — Scoped Orphan Cleanup UAT
=====================================

User Acceptance Test Story for the ``installer-scoped-cleanup`` change
request, covering the Installer's two-part orphan-removal condition:
only files carrying the ``syspilot.`` filename prefix **and** not
matching ``*.tailoring.md`` are eligible for removal.


.. story:: UAT: Installer Scoped Orphan Cleanup
   :id: SYSP_US_UAT_INSTALLER_SCOPED_CLEANUP
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orphan-cleanup, scoped-cleanup
   :links: SYSP_US_INSTALLER

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the
   Installer's two-part orphan-removal condition — ``syspilot.`` prefix AND
   not ``*.tailoring.md`` — so that customer-owned agents, project-specific
   agents, and instance tailoring files in ``.github/agents/``,
   ``.github/prompts/``, and ``.github/skills/`` survive an install or
   update run untouched,
   **so that** no workspace-local customisation is ever silently deleted by
   a syspilot update.

   **Context:**

   The ``installer-scoped-cleanup`` CR restricts the orphan-cleanup step to
   a two-part eligibility condition: a file must carry the ``syspilot.``
   filename prefix **and** must not match ``*.tailoring.md``. Files failing
   either condition are unconditionally preserved. This protects
   customer-owned agents (no prefix), project-specific agents (no prefix),
   and instance tailoring files (``syspilot.*.tailoring.md`` suffix). The
   Installer cannot be auto-dry-run — it mutates the workspace — so these
   scenarios are framed as self-contained human-execution guidance
   (precondition / action / expected result).

   **Artifacts Under Test:**

   * ``syspilot/agents/syspilot.installer.agent.md`` — Installer agent
   * ``docs/syspilot/design/spec_installer.rst`` —
     ``SYSP_SPEC_INSTALLER_DUTIES``, ``SYSP_SPEC_INSTALLER_WORKFLOW``
   * ``.github/agents/``, ``.github/prompts/``, ``.github/skills/``
     on the target project

   **Traceability:**

   Covers ``SYSP_US_INSTALLER`` AC-11 (two-part eligibility condition:
   non-``syspilot.``-prefixed files and ``syspilot.*.tailoring.md`` files
   are never orphan-removed) and ``SYSP_REQ_INSTALLER_SCOPE`` AC-6
   (same two-part condition at requirement level).
   Test data is defined in ``SYSP_REQ_UAT_INSTALLER_SCOPED_CLEANUP``;
   expected outcomes in ``SYSP_SPEC_UAT_INSTALLER_SCOPED_CLEANUP``.

   **Acceptance Criteria:**

   1. **Customer-owned file survives update.**
      *Precondition:* A target project with a completed syspilot installation.
      A file named ``myproject.pm.agent.md`` has been manually placed in
      ``.github/agents/``. No file with that name exists in
      ``syspilot/agents/``.
      *Action:* Re-run the Installer as an update.
      *Expected result:* ``myproject.pm.agent.md`` is still present in
      ``.github/agents/`` and its content is byte-for-byte unchanged after
      the Installer completes — traces to ``SYSP_US_INSTALLER`` AC-11;
      ``SYSP_REQ_INSTALLER_SCOPE`` AC-6

   2. **Genuine syspilot orphan is removed.**
      *Precondition:* A target project with a completed syspilot installation.
      A file named ``syspilot.oldagent.agent.md`` is present in
      ``.github/agents/``. No file with that name exists in
      ``syspilot/agents/`` (it has been removed from the upstream product).
      *Action:* Re-run the Installer as an update.
      *Expected result:* ``syspilot.oldagent.agent.md`` is absent from
      ``.github/agents/`` after the Installer completes; all current-product
      ``syspilot.``-prefixed agent files remain present and current — traces
      to ``SYSP_REQ_INSTALLER_SCOPE`` AC-6

   3. **Tailoring file survives update.**
      *Precondition:* A target project with a completed syspilot installation.
      A file named ``syspilot.pm.tailoring.md`` has been manually placed in
      ``.github/agents/``. No file with that name exists in
      ``syspilot/agents/``.
      *Action:* Re-run the Installer as an update.
      *Expected result:* ``syspilot.pm.tailoring.md`` is still present in
      ``.github/agents/`` and its content is byte-for-byte unchanged after
      the Installer completes — traces to ``SYSP_US_INSTALLER`` AC-11;
      ``SYSP_REQ_INSTALLER_SCOPE`` AC-6
