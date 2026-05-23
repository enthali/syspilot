Installer — Spec Rewrite UAT
============================

User Acceptance Test Story for the ``installer-spec-rewrite`` change request.
Covers all nine CR acceptance criteria against ``SYSP_US_INSTALLER``.


.. story:: UAT: Installer Spec Rewrite
   :id: SYSP_US_UAT_INSTALLER_SPEC_REWRITE
   :status: draft
   :priority: mandatory
   :tags: uat, installer, spec-rewrite
   :links: SYSP_US_INSTALLER

   **As a** syspilot Test Engineer,
   **I want** to verify that the rewritten Installer agent and specification
   deliver a correct, transactional, customer-path-validated installation,
   **so that** customers on the released installer receive a working syspilot
   environment on first contact and the release is not blocked by Installer
   defects.

   **Context:**

   CR ``installer-spec-rewrite`` rewrote the Installer spec and agent to fix
   the customer installation path.  The previous spec described a workflow that
   only worked inside the dogfooding workspace: it offered a local-source
   shortcut, performed a Mode-Detect comparison, asked an after-the-fact
   customization question, and was silent on UTF-8 encoding, wrapper-script
   discipline, and rollback.  A live install attempt on 2026-05-23 confirmed
   the impact: BOM corruption in 26 files and a generated wrapper script.

   This test story covers end-to-end verification of all nine CR ACs.

   **Artifacts Under Test:**

   * ``syspilot/agents/syspilot.installer.agent.md`` — rewritten Installer agent
   * ``docs/syspilot/design/spec_installer.rst`` — SYSP_SPEC_INSTALLER_* nodes
   * ``docs/syspilot/requirements/req_setup_engineer.rst`` — SYSP_REQ_INSTALLER_* nodes
   * Clean test repository (no existing ``.github/`` syspilot install)

   **Traceability:**

   Covers all nine ACs of the ``installer-spec-rewrite`` CR against
   ``SYSP_US_INSTALLER`` and the six in-scope REQs:
   ``SYSP_REQ_INSTALLER_WORKFLOW``, ``SYSP_REQ_INSTALLER_DUTIES``,
   ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``, ``SYSP_REQ_INSTALLER_ENCODING``,
   ``SYSP_REQ_INSTALLER_DIRECT_OPS``, ``SYSP_REQ_INSTALLER_ROLLBACK``.

   **Acceptance Criteria:**

   1. Given a clean test repository with no local ``syspilot/`` directory,
      When ``@syspilot.setup`` is invoked with ``branch=development``,
      Then the installation completes end-to-end without error and produces
      the per-directory summary table — traces to CR AC1, CR AC9,
      ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``, ``SYSP_REQ_INSTALLER_WORKFLOW``

   2. Given an existing syspilot installation,
      When the installer is re-invoked on the same repository,
      Then the operation completes without error and file content is correct
      (Mode-Detect does not block the re-run) — traces to CR AC2,
      ``SYSP_REQ_INSTALLER_GITHUB_SOURCE``

   3. Given a completed installation,
      When every written file is inspected with a BOM detector,
      Then zero BOM markers are found in any file — traces to CR AC3,
      ``SYSP_REQ_INSTALLER_ENCODING``

   4. Given a completed installation,
      When ``temp/`` and the project root are inspected,
      Then no ``install.ps1`` or equivalent wrapper script is present —
      traces to CR AC4, ``SYSP_REQ_INSTALLER_DIRECT_OPS``

   5. Given an agent file with a locally edited ``tools:`` field,
      When the installer is re-run,
      Then the edited ``tools:`` value is preserved and all other frontmatter
      fields are reset to upstream values; the Bootloader is overwritten
      verbatim — traces to CR AC5, ``SYSP_REQ_INSTALLER_DUTIES``

   6. Given ``sphinx-needs`` is absent from the active Python environment,
      When the installer is invoked,
      Then it prints installation instructions and stops without modifying
      any file — traces to CR AC6, ``SYSP_REQ_INSTALLER_WORKFLOW``

   7. Given the installer has created its pre-install commit,
      When a simulated failure occurs mid-install,
      Then ``git reset --hard`` restores the repository to the pre-install
      commit state — traces to CR AC7, ``SYSP_REQ_INSTALLER_ROLLBACK``

   8. Given the installer specification Step 4,
      When reviewed by a human tester,
      Then no customization-question prompt and no double-write flow are
      present — traces to CR AC8, ``SYSP_REQ_INSTALLER_WORKFLOW``

   9. Given a successful installation,
      When the installer's run summary is inspected,
      Then a per-directory summary table is present with rows for
      ``agents/``, ``prompts/``, ``skills/``, and ``templates/``, each row
      containing an integer file count — traces to CR AC9,
      ``SYSP_REQ_INSTALLER_WORKFLOW``
