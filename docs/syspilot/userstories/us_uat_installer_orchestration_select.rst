Installer Orchestration Select UAT
===================================

User Acceptance Test Story for the ``installer-orchestration-select`` change
request — the Implementation stage that finally delivers three previously
designed-but-never-implemented Installer specs from the incomplete
``session-first-orchestration`` CR (#35): orchestration variant selection,
general Skill mutual exclusion, and session scaffold creation. This chain
adds coverage the prior design-only UAT chain could not yet exercise, and
provides explicit regression scenarios for GH #48 and GH #22.


.. story:: UAT: Installer Orchestration Select, General Mutex & Scaffold Regression
   :id: SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orchestration, mutex, regression, critical
   :links: SYSP_US_INSTALLER, SYSP_US_SKILL_ARCH

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the
   Skill mutual-exclusion mechanism is genuinely general (works for any
   ``group:``-tagged Skill pair, not only orchestration), and that the two
   specific defects reported in GH #48 (both orchestration Skills installed
   simultaneously) and GH #22 (no session scaffolds ever created) cannot
   recur,
   **so that** the specs already written for ``session-first-orchestration``
   are confirmed correctly implemented before the Monday partner demo.

   **Context:**

   ``SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT``,
   ``SYSP_SPEC_INSTALLER_SKILL_MUTEX``, and
   ``SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD`` were fully designed by CR #35
   but never implemented — the Installer previously installed both
   orchestration Skills unconditionally on every fresh install (GH #48) and
   never created session scaffolds at all (GH #22). This CR implements the
   already-existing specs with no design change.

   ``SYSP_US_UAT_INSTALLER_SESSION_FIRST`` (authored earlier, when these
   specs were design-only) already covers the core variant-selection,
   single-scaffold-creation, and update-preservation scenarios — those
   scenarios are **finally executable** now that Implementation has landed,
   and remain the primary coverage for that behavior; they are not
   duplicated here. This chain adds what that earlier chain could not yet
   address: (1) proof the mutex mechanism is general-purpose, not hardcoded
   to the orchestration group specifically, and (2) scenarios framed
   explicitly as regression tests for the two reported GitHub issues.

   **Artifacts Under Test:**

   * ``syspilot/agents/syspilot.installer.agent.md`` — Installer agent
   * ``docs/syspilot/design/spec_installer.rst`` —
     ``SYSP_SPEC_INSTALLER_SKILL_MUTEX``,
     ``SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT``,
     ``SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD``
   * A hypothetical second ``group:``-tagged Skill pair (non-orchestration)
     installed in the installed skill location, for the general-mutex
     scenario
   * The installed skill location and session scaffold directory on a
     target project

   **Traceability:**

   Covers ``SYSP_REQ_SETUP_SKILL_MUTEX`` AC-1/AC-2/AC-3 (general mutual
   exclusion, any group), ``SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT`` AC-4
   (exactly one orchestration Skill — GH #48 regression), and
   ``SYSP_REQ_INSTALLER_SESSION_SCAFFOLD`` (scaffolds actually created — GH
   #22 regression).
   Test data is defined in ``SYSP_REQ_UAT_INSTALLER_ORCHESTRATION_SELECT``;
   expected outcomes in ``SYSP_SPEC_UAT_INSTALLER_ORCHESTRATION_SELECT``.

   **Acceptance Criteria:**

   1. **General mutex mechanism — proven with a non-orchestration group pair.**
      *Precondition:* A target project with a syspilot installation. Two
      Skills, each declaring the same non-orchestration ``group:`` value
      (e.g. a hypothetical ``group: reporting`` pair — ``Skill R1`` already
      installed, ``Skill R2`` about to be installed), are prepared as test
      fixtures; neither is a product syspilot Skill.
      *Action:* Trigger the Installer to install ``Skill R2``.
      *Expected result:* ``Skill R1`` is removed before ``Skill R2`` is
      written; exactly one Skill declaring ``group: reporting`` is present
      afterward, and the run summary names the replacement — proving the
      mechanism keys off the generic ``group:`` field rather than an
      orchestration-specific check — traces to ``SYSP_REQ_SETUP_SKILL_MUTEX``
      AC-1, AC-2, AC-3

   2. **⚠ Regression — GH #48: fresh install never installs both orchestration Skills.**
      *Precondition:* A clean target project, no prior syspilot install, any
      ``.jarvis/`` presence/absence state.
      *Action:* Run a fresh install and accept the inferred default
      orchestration variant.
      *Expected result:* Exactly one orchestration-group Skill exists in the
      installed skill location after the run completes — never both
      ``syspilot.orchestration-jarvis`` and ``syspilot.orchestration-subagent``
      simultaneously. This is the literal defect reported in GH #48; a
      result of two Skills present is a fail — traces to
      ``SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT`` AC-4;
      ``SYSP_REQ_SETUP_SKILL_MUTEX`` AC-3

   3. **⚠ Regression — GH #22: session scaffolds are actually created, not silently skipped.**
      *Precondition:* A clean target project containing a ``.jarvis/``
      directory (async variant expected as default), no prior syspilot
      install.
      *Action:* Run a fresh install and accept the default orchestration
      variant.
      *Expected result:* ``.jarvis/sessions/<name>/session.yaml`` exists on
      disk for every eligible installed agent (all agents except
      ``syspilot.setup`` and ``syspilot.installer``) — the scaffold
      directory is not empty and is not absent entirely. This is the
      literal defect reported in GH #22 (no scaffolds ever created); zero
      scaffolds present after this run is a fail — traces to
      ``SYSP_REQ_INSTALLER_SESSION_SCAFFOLD``

      .. note::
         The Jarvis session list may lag the filesystem by up to one scan
         interval (see the testability note already recorded against
         ``SYSP_REQ_UAT_INSTALLER_SESSION_FIRST``). Verify scaffold
         existence against the filesystem directly, not the live session
         list.
