Installer — Session-First Orchestration UAT
===========================================

User Acceptance Test Story for the ``session-first-orchestration`` change
request, covering the Installer's variant selection, mutual-exclusion
installation, and session-scaffold creation behaviour.


.. story:: UAT: Installer Session-First Behavior
   :id: SYSP_US_UAT_INSTALLER_SESSION_FIRST
   :status: draft
   :priority: mandatory
   :tags: uat, installer, orchestration, session-first
   :links: SYSP_US_INSTALLER, SYSP_US_SKILL_ARCH

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the
   Installer installs exactly one orchestration-group skill, creates session
   scaffolds for every eligible agent on the session-based path, and preserves
   existing scaffolds and the agent's accumulated context on update,
   **so that** the session-first orchestration model is delivered correctly
   on the customer installation path — which cannot be auto-dry-run and is
   precisely why syspilot UAT exists.

   **Context:**

   The ``session-first-orchestration`` CR makes async session-messaging
   the orchestration default. The Installer is the component that
   materialises this on a target project:

   * It infers a default from the presence of a session-messaging
     infrastructure and lets the user override it.
   * It installs **exactly one** member of ``group: orchestration`` —
     replacing any previously installed group member (mutual exclusion,
     ``SYSP_US_SKILL_ARCH`` AC-5).
   * On the session-based path it creates a session scaffold for every
     installed agent except the bootstrap layer (``syspilot.setup`` and
     ``syspilot.installer``).
   * On update it creates only the missing scaffolds and leaves existing
     scaffolds and any agent-owned context untouched.

   The Installer cannot be auto-dry-run: it mutates the workspace, interacts
   with the session infrastructure, and asks the user a question. These
   scenarios are therefore framed as **self-contained human-execution guidance**
   (precondition / action / expected result). The Test Designer authors them;
   a human runs them on a real target project.

   **Artifacts Under Test:**

   * ``syspilot/agents/syspilot.installer.agent.md`` — Installer agent
   * ``docs/syspilot/design/spec_installer.rst`` — ``SYSP_SPEC_INSTALLER_*``
     (orchestration-select, session-scaffold, skill-mutex)
   * The installed skill location (e.g. ``.github/skills/``) on the target
     project
   * The session scaffold directory on the target project (session-based path)

   **Traceability:**

   Covers ``SYSP_US_INSTALLER`` AC-9 (variant default + override), AC-10
   (session scaffold creation), AC-11 (update preserves existing scaffold +
   context), and ``SYSP_US_SKILL_ARCH`` AC-5 (mutual exclusion by replacement).
   Test data is defined in ``SYSP_REQ_UAT_INSTALLER_SESSION_FIRST``; expected
   outcomes in ``SYSP_SPEC_UAT_INSTALLER_SESSION_FIRST``.

   **Acceptance Criteria:**

   1. **Session-based path — single skill + scaffolds.**
      *Precondition:* A clean target project that contains a ``.jarvis/``
      directory and no prior syspilot install.
      *Action:* Run the Installer and accept the default orchestration
      variant.
      *Expected result:* Exactly one ``group: orchestration`` skill is present
      in the installed skill location, AND a session scaffold is reachable for
      every installed agent except ``syspilot.setup`` and
      ``syspilot.installer`` — each scaffold carries the agent's identity as
      declared in its frontmatter — traces to ``SYSP_US_INSTALLER`` AC-9,
      AC-10; ``SYSP_US_SKILL_ARCH`` AC-5

   2. **Synchronous-fallback path — no scaffolds.**
      *Precondition:* A clean target project with no ``.jarvis/`` directory.
      *Action:* Run the Installer and accept the default orchestration
      variant.
      *Expected result:* The synchronous fallback orchestration skill is the
      one installed (still exactly one group member), and NO session scaffolds
      are created — traces to ``SYSP_US_INSTALLER`` AC-9;
      ``SYSP_US_SKILL_ARCH`` AC-5

   3. **Mutual exclusion by replacement.**
      *Precondition:* A target project that already has one
      ``group: orchestration`` skill installed.
      *Action:* Run the Installer and select the other orchestration variant.
      *Expected result:* The previously installed group member is removed
      before the new one is written; exactly one group member remains
      afterwards — traces to ``SYSP_US_SKILL_ARCH`` AC-5;
      ``SYSP_US_INSTALLER`` AC-9

   4. **Update preserves existing scaffolds and context.**
      *Precondition:* A target project on the session-based path with some
      session scaffolds present, at least one of which has a non-empty agent
      context, and at least one eligible agent whose scaffold is missing.
      *Action:* Re-run the Installer as an update.
      *Expected result:* The missing scaffold(s) are created; every
      pre-existing scaffold and every agent context file is byte-for-byte
      unchanged — traces to ``SYSP_US_INSTALLER`` AC-11

   5. **Bootstrap exception — no session for setup/installer.**
      *Precondition:* Any completed session-based installation.
      *Action:* List the session scaffold directory and inspect the Setup → Installer
      hand-off description in the Installer/Setup specs.
      *Expected result:* No session scaffold exists for ``syspilot.setup`` or
      ``syspilot.installer``, and the Setup → Installer call is a direct
      synchronous invocation outside the orchestration contract — traces to
      ``SYSP_US_INSTALLER`` AC-10
