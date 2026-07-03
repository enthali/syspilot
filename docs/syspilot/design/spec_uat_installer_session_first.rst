Installer — Session-First Orchestration Expected Outcomes
=========================================================

Expected outcomes specification for ``SYSP_REQ_UAT_INSTALLER_SESSION_FIRST``.
This document is the per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Installer Session-First Behavior
   :id: SYSP_SPEC_UAT_INSTALLER_SESSION_FIRST
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orchestration, session-first, expected-outcomes
   :links: SYSP_REQ_UAT_INSTALLER_SESSION_FIRST

   **Definition:**

   For each scenario in ``SYSP_US_UAT_INSTALLER_SESSION_FIRST``, the following
   outcomes SHALL be observable on the target project. Each scenario is
   self-contained: the human tester prepares the named fixture, runs the
   action, and confirms the expected result. A check item passes when the
   exact condition is met; it fails otherwise.

   ---

   **TC-SF-JARVIS — Jarvis path: single skill + scaffolds**

   *Precondition:* Fixture ``F-JARVIS-CLEAN`` (clean project, ``.jarvis/``
   present).

   *Action:* Run the Installer; accept the default orchestration variant.

   *Expected result:*

   * [ ] Exactly one skill with ``group: orchestration`` is present in the
     installed skill location (the Jarvis variant)
   * [ ] A directory ``.jarvis/sessions/<name>/`` with a ``session.yaml``
     exists for every eligible agent (all agents except ``syspilot.setup``
     and ``syspilot.installer``)
   * [ ] Each ``session.yaml`` carries ``name:`` and ``agent:`` values that
     match the corresponding agent file's frontmatter verbatim
   * [ ] No scaffold exists for ``syspilot.setup`` or ``syspilot.installer``

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SESSION_FIRST`` AC-1, AC-5

   ---

   **TC-SF-NOJARVIS — No-Jarvis path: subagent variant, no scaffolds**

   *Precondition:* Fixture ``F-NOJARVIS-CLEAN`` (clean project, no
   ``.jarvis/``).

   *Action:* Run the Installer; accept the default orchestration variant.

   *Expected result:*

   * [ ] The installed ``group: orchestration`` skill is the synchronous
     subagent variant (still exactly one group member)
   * [ ] No ``.jarvis/sessions/`` directory is created and no session
     scaffolds are written

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SESSION_FIRST`` AC-2

   ---

   **TC-SF-MUTEX — Mutual exclusion by replacement**

   *Precondition:* Fixture ``F-GROUP-INSTALLED`` (one orchestration-group
   skill already installed).

   *Action:* Run the Installer; select the *other* orchestration variant.

   *Expected result:*

   * [ ] After the run, exactly one ``group: orchestration`` skill is present
     in the installed skill location
   * [ ] The previously installed group member is no longer present (it was
     removed before the new one was written — replacement, not rejection)

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SESSION_FIRST`` AC-3

   ---

   **TC-SF-UPDATE — Update preserves existing scaffolds and context**

   *Precondition:* Fixture ``F-JARVIS-UPDATE`` (some scaffolds present, one
   with non-empty ``context.md``, at least one eligible agent scaffold
   missing). Record a byte hash of each pre-existing ``session.yaml`` and
   ``context.md`` before the run.

   *Action:* Re-run the Installer as an update.

   *Expected result:*

   * [ ] Every eligible agent that was missing a scaffold now has a
     ``.jarvis/sessions/<name>/session.yaml``
   * [ ] Every pre-existing ``session.yaml`` is byte-for-byte unchanged
     (hash matches the pre-run value)
   * [ ] Every pre-existing ``context.md`` is byte-for-byte unchanged (the
     agent owns its ``context.md``; the Installer never overwrites it)

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SESSION_FIRST`` AC-4

   ---

   **TC-SF-BOOTSTRAP — Bootstrap exception (setup, installer)**

   *Precondition:* Any completed Jarvis-path installation (e.g. result of
   ``TC-SF-JARVIS``).

   *Action:* List ``.jarvis/sessions/`` and read the Setup → Installer
   hand-off description in ``spec_setup_engineer.rst`` /
   ``spec_installer.rst``.

   *Expected result:*

   * [ ] ``.jarvis/sessions/`` contains no directory for ``syspilot.setup``
     or ``syspilot.installer``
   * [ ] The Setup → Installer call is described as a direct synchronous
     invocation explicitly outside the orchestration contract (no session,
     no SEND/RECEIVE/RESPOND)

   *Traces to:* ``SYSP_US_UAT_INSTALLER_SESSION_FIRST`` AC-5

   ---

   **Testability Note — verify the filesystem, not the live session list:**

   Because the Jarvis session list lags filesystem changes by up to one scan
   interval (≈ 1 minute) in both directions
   (see ``SYSP_REQ_UAT_INSTALLER_SESSION_FIRST``), every scaffold-presence
   check above (TC-SF-JARVIS, TC-SF-UPDATE) SHALL be evaluated against the
   **filesystem** — the existence and content of ``session.yaml`` — rather
   than against the live Jarvis session list. A scaffold that is present on
   disk but not yet listed by Jarvis is a **pass** (it will become addressable
   on the next scan). A removed scaffold (TC-SF-MUTEX) that still lingers in
   the session list until the next scan is likewise expected and not a defect.
   Where session **addressability** itself is under test, the tester allows
   one scan interval or triggers a manual rescan before asserting.
