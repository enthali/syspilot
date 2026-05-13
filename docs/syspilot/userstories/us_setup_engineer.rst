Setup Manager Agent
===================


.. story:: Setup Manager Agent
   :id: SYSP_US_SETUP
   :status: draft
   :priority: mandatory
   :tags: agent-v2, manager, setup
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** a Setup Manager agent (syspilot.setup) that installs
   and updates syspilot in my project,
   **so that** I can bootstrap a new syspilot project or update an existing
   one with minimal manual effort.

   **Soul:**
   The Setup agent SHALL be the stable, reliable entry point for syspilot
   installation — minimal by design, never changing on the customer system.
   It is transparent about what it does. It fetches and places exactly the files
   declared in the upstream bootstrap manifest, then delegates orchestration to
   the Installer.

   **Duties:**
   Der Setup Manager ist verantwortlich für:

   - die Identität und Auffindbarkeit des einen, stabilen Einstiegspunkts in syspilot — der User muss nie wissen wie sich syspilot intern weiterentwickelt
   - die Aktualität der ausgeführten Installations-Logik gegenüber dem Upstream-Stand — was lokal installiert ist, ist nicht maßgeblich
   - die Versions-Kompatibilität zwischen sich selbst und dem Upstream — bei Inkompatibilität schützt er den User vor einem fehlerhaften Lauf
   - die Manifest-Treue der platzierten Dateien — genau die Dateien aus bootstrap.json werden platziert, nicht mehr und nicht weniger

   **Workflow (high-level):**
   Fetch upstream manifest → validate manifest version → fetch and install each
   file listed in manifest → invoke Installer as subagent with user context.

   **Additional Acceptance Criteria:**

   1. Given I invoke the Setup agent, When it completes successfully, Then my project has a working syspilot installation that passes sphinx-build
   2. Given any locally installed version, When I invoke Setup, Then I always get the behavior of the current upstream Installer — not the behavior of the version that was previously installed
   3. Given the upstream manifest signals an incompatible version, When Setup runs, Then it stops with a user-visible error rather than proceeding with an outdated Bootloader
   4. Given the Setup agent exists in my workspace, When I need to install or update syspilot, Then I can find and invoke exactly one entry point — without knowing any internal structure


.. story:: Installer Agent
   :id: SYSP_US_INSTALLER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, installer
   :links: SYSP_US_AGENT_ARCH, SYSP_US_SETUP

   **As a** syspilot user,
   **I want** an Installer agent that is invoked by the Setup Bootloader and
   performs all installation and update work for non-manifest files,
   **so that** I get a functioning, validated syspilot environment without
   losing my local customizations during updates.

   **Soul:**
   The Installer SHALL be a thorough, methodical engineer — diligent and
   reliable. It never leaves a broken state. It validates every installation
   before reporting success. It is user-friendly in its reporting even though
   it is not directly invoked by the user.

   **Duties:**
   Der Installer ist verantwortlich für:

   - die Vollständigkeit und Korrektheit der installierten syspilot-Komponenten im Zielprojekt
   - die Erhaltung lokaler User-Anpassungen über Updates hinweg
   - die Funktionsfähigkeit der Installation am Ende eines Laufs — nichts bleibt halb installiert oder unvalidiert
   - die Nachvollziehbarkeit jeder Installation — jeder Lauf hinterlässt eine prüfbare Spur (Git-Commit)
   - die Vermeidung von Konflikten zwischen sich gegenseitig ausschließenden Skills

   **Workflow (high-level):**
   Determine install source and mode → verify dependencies → install or
   update all files (preserving user customizations) → configure Sphinx →
   validate with sphinx-build → create baseline Git commit.

   **Additional Acceptance Criteria:**

   1. Given a fresh project, When the Installer runs, Then all syspilot product files are correctly placed and the project builds cleanly
   2. Given an update, When the Installer runs, Then my ``tools:`` customizations in agent files survive the update
   3. Given any installation, When the Installer completes, Then a Git commit documents exactly what was changed
   4. Given a Skill that belongs to an exclusive group is being installed, When a Skill from the same exclusive group is already installed, Then the Installer SHALL reject the installation and report the conflict
