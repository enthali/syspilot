Installer Orchestration Select Expected Outcomes
=================================================

Expected outcomes specification for
``SYSP_REQ_UAT_INSTALLER_ORCHESTRATION_SELECT``. This document is the
per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Installer Orchestration Select, General Mutex & Scaffold Regression
   :id: SYSP_SPEC_UAT_INSTALLER_ORCHESTRATION_SELECT
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orchestration, mutex, regression, critical, expected-outcomes
   :links: SYSP_REQ_UAT_INSTALLER_ORCHESTRATION_SELECT

   **Definition:**

   For each scenario in ``SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT``, the
   following outcomes SHALL be observable. Each scenario is self-contained:
   the human tester prepares the named fixture, runs the action, and
   confirms the expected result. A check item passes when the exact
   condition is met; it fails otherwise.

   ---

   **TC-IOS-GENMUTEX — General mutex mechanism (non-orchestration group)**

   *Precondition:* Fixture ``F-GROUP-PAIR`` (Skill R1 installed declaring
   ``group: reporting``; Skill R2 not yet installed, same group value).

   *Action:* Trigger the Installer to install Skill R2.

   *Expected result:*

   * [ ] Skill R1 is absent from the installed skill location after the run
   * [ ] Skill R2 is present after the run
   * [ ] Exactly one Skill declaring ``group: reporting`` exists afterward
   * [ ] The run summary names Skill R1 as replaced

   *Traces to:* ``SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT`` AC-1

   ---

   **TC-IOS-GH48 — GH #48 regression: never both orchestration Skills**

   *Precondition:* Fixture ``F-FRESH-ANY`` (clean target project, no prior
   syspilot install).

   *Action:* Run a fresh install; accept the inferred default orchestration
   variant.

   *Expected result:*

   * [ ] Exactly one of ``syspilot.orchestration-jarvis`` /
     ``syspilot.orchestration-subagent`` is present in the installed skill
     location after the run
   * [ ] The other orchestration variant is absent
   * [ ] Neither variant appears twice or in a partially-written state

   *Traces to:* ``SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT`` AC-2. **This
   is the direct regression test for GH #48** — the original defect
   installed both variants unconditionally; this check fails if that
   recurs.

   ---

   **TC-IOS-GH22 — GH #22 regression: session scaffolds actually exist**

   *Precondition:* Fixture ``F-FRESH-JARVIS`` (clean target project,
   ``.jarvis/`` present, no prior syspilot install).

   *Action:* Run a fresh install; accept the default orchestration variant.

   *Expected result:*

   * [ ] ``.jarvis/sessions/`` directory exists after the run
   * [ ] A ``session.yaml`` file exists under
     ``.jarvis/sessions/<name>/`` for every eligible installed agent (all
     agents except ``syspilot.setup`` and ``syspilot.installer``)
   * [ ] The scaffold count is not zero

   *Traces to:* ``SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT`` AC-3. **This
   is the direct regression test for GH #22** — the original defect never
   created any scaffold; this check fails if that recurs. Verify against
   the filesystem, not the live Jarvis session list (scan-latency
   testability note, see ``SYSP_REQ_UAT_INSTALLER_SESSION_FIRST``).
