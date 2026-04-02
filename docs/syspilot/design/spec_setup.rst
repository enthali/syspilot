Setup Agent Design
===================

Design specifications for the Setup Agent — installation, update, and environment management.

**Document Version**: 0.3
**Last Updated**: 2026-03-16


Installation
------------

.. spec:: Curl-Based Bootstrap
   :id: SYSPILOT_SPEC_INST_CURL_BOOTSTRAP
   :status: implemented
   :links: SYSPILOT_REQ_INST_AUTO_SETUP, SYSPILOT_REQ_INST_NEW_PROJECT, SYSPILOT_REQ_INST_ADOPT_EXISTING
   :tags: init, install, curl

   **Design:**
   Users bootstrap syspilot by downloading the Setup Agent directly from
   GitHub using curl (Unix) or Invoke-WebRequest (Windows). No local
   syspilot repository or init scripts are needed.

   **Bootstrap Steps:**

   1. Create agent directory: ``mkdir -p .github/agents/``
   2. Download Setup Agent from GitHub main:

      ::

         # Unix
         curl -o .github/agents/syspilot.setup.agent.md \
           https://raw.githubusercontent.com/OWNER/syspilot/main/syspilot/agents/syspilot.setup.agent.md

         # Windows (PowerShell)
         Invoke-WebRequest `
           -Uri "https://raw.githubusercontent.com/OWNER/syspilot/main/syspilot/agents/syspilot.setup.agent.md" `
           -OutFile ".github/agents/syspilot.setup.agent.md"

   3. Open VS Code, start GitHub Copilot Chat, invoke ``@syspilot.setup``

   **Rationale:**

   * No local syspilot repository needed
   * Platform-independent (curl/Invoke-WebRequest available everywhere)
   * Always fetches current version from main
   * Single command instead of finding and running init scripts


.. spec:: Setup Agent Design
   :id: SYSPILOT_SPEC_INST_SETUP_AGENT
   :status: implemented
   :links: SYSPILOT_REQ_INST_NEW_PROJECT, SYSPILOT_REQ_INST_ADOPT_EXISTING, SYSPILOT_REQ_INST_SPHINX_NEEDS_DEP, SYSPILOT_SPEC_INST_FILE_OWNERSHIP, SYSPILOT_SPEC_INST_UPDATE_PROCESS
   :tags: install, agent, setup

   **Design:**
   Installation is curl-based: user downloads setup agent, then runs it.

   **Step 1: Bootstrap (manual)**

   * User curls setup agent from GitHub (SYSPILOT_SPEC_INST_CURL_BOOTSTRAP)
   * No init scripts, no local syspilot repo needed

   **Step 2: Setup Agent (@syspilot.setup)**

   **Section 0: Detect Install Source (SYSPILOT_SPEC_INST_SOURCE_DETECTION)**

   1. Check if ``syspilot/`` directory exists in repository root
   2. If exists and contains ``version.json`` → prompt user: Local or GitHub?
   3. If not exists → use GitHub (no prompt)

   **Section 1: Determine Mode**

   1. Check if ``.syspilot/version.json`` exists
   2. If yes → UPDATE MODE (see SYSPILOT_SPEC_INST_UPDATE_PROCESS)
   3. If no → FRESH INSTALL (continue with Section 2)

   **Section 2: Check Dependencies (Interactive)**

   The setup agent checks whether sphinx-needs is available before
   offering to install:

   1. **Check Python**: Verify ``python --version`` available
   2. **Check pip/uv**: Verify package manager available
   3. **Detect sphinx-needs availability**:

      ::

         python -c "import sphinx_needs; print(sphinx_needs.__version__)"
         sphinx-build --version

      * If both succeed → sphinx-needs is available; skip to step 6 (Validate):

        ::

           ✅ sphinx-needs vX.Y.Z detected — skipping installation.

      * If either fails → sphinx-needs is NOT available; proceed to step 4.

   4. **Ask user** (only if sphinx-needs is NOT detected):

      ::

         sphinx-needs was not detected. How would you like to proceed?

         A) Install via pip/uv (standard install)
         B) Use custom mechanism — I will confirm availability manually
         C) Skip (build will be broken until sphinx-needs is available)

      * **Option A**: Install with user confirmation:

        ::

           uv pip install sphinx sphinx-needs furo myst-parser
           # or
           pip install sphinx sphinx-needs furo myst-parser

      * **Option B**: Prompt user:

        ::

           Please ensure sphinx-needs is accessible in your current
           Python environment (e.g. activate your venv, run your
           custom script), then confirm to continue.

        Wait for user confirmation, then proceed.

      * **Option C**: Warn and continue:

        ::

           ⚠️ Proceeding without sphinx-needs. Sphinx build will
           fail until sphinx-needs is available.

   5. **Graphviz (optional)**:

      * Check if ``dot --version`` works
      * If not: inform user that needflow diagrams won't render
      * Provide manual install instructions:

        ::

           Windows: winget install Graphviz.Graphviz
           macOS:   brew install graphviz
           Linux:   sudo apt install graphviz

      * Note: System package managers may require admin rights

   6. **Validate**: Run ``sphinx-build --version`` to confirm

   **Section 3: Fetch Files**

   If source = local, copy files from local ``syspilot/`` directory.
   If source = GitHub, fetch files from ``syspilot/`` on GitHub main:

   1. Fetch ``syspilot/version.json`` → determine version
   2. Use GitHub API to list ``syspilot/`` contents:
      ``api.github.com/repos/OWNER/syspilot/contents/syspilot/``
   3. Download and copy:

      * ``syspilot/agents/*.agent.md`` → ``.github/agents/``
      * ``syspilot/prompts/*.prompt.md`` → ``.github/prompts/``
      * ``syspilot/skills/*/SKILL.md`` → ``.github/skills/*/SKILL.md``
      * ``syspilot/scripts/python/`` → ``.syspilot/scripts/python/``
      * ``syspilot/sphinx/`` → ``docs/`` (build.ps1, build.sh)
      * ``syspilot/templates/change-document.md`` → ``.syspilot/templates/``

   4. Apply intelligent merge for existing projects (SYSPILOT_SPEC_INST_FILE_OWNERSHIP)

   **Section 4: Create Version Marker**

   * Write ``.syspilot/version.json`` with version, date, and source
     (see SYSPILOT_SPEC_INST_VERSION_MARKER)

   **Section 5: Validate and Confirm**

   * Validate successful ``sphinx-build``
   * Confirm success

   **Works for both new and existing projects.**

   **Existing Project Handling:**

   * Detects existing ``docs/conf.py`` and merges sphinx-needs config
   * Detects existing ``.github/`` content and merges safely
   * Prompts user for decisions on conflicts


Install Source Detection
------------------------

.. spec:: Install Source Detection
   :id: SYSPILOT_SPEC_INST_SOURCE_DETECTION
   :status: implemented
   :links: SYSPILOT_REQ_INST_LOCAL_SOURCE, SYSPILOT_SPEC_INST_SETUP_AGENT, SYSPILOT_SPEC_INST_UPDATE_PROCESS
   :tags: install, local, detection

   **Design:**
   Before fetching any files, the Setup Agent determines the install source
   by checking for a local ``syspilot/`` directory.

   **Detection Logic:**

   1. Check if ``syspilot/`` directory exists in repository root
   2. If exists, check for ``syspilot/version.json`` to confirm it's a valid source
   3. If valid local source found → prompt user:

      ::

         Local syspilot/ directory detected (v{version}).
         Where should I install from?

         A) Local — Copy from syspilot/ (fast, no network, for development/testing)
         B) GitHub — Fetch from GitHub main (current release)

   4. If no local source → proceed with GitHub fetch (no prompt needed)

   **Source Mode Affects:**

   * Fresh install (SYSPILOT_SPEC_INST_SETUP_AGENT Section 3)
   * Update (SYSPILOT_SPEC_INST_UPDATE_PROCESS Steps 0-2)
   * Self-update of setup agent

   **Local Copy Mechanism:**

   * Uses file system copy instead of curl/API
   * Same directory mapping as GitHub fetch:

     - ``syspilot/agents/*.agent.md`` → ``.github/agents/``
     - ``syspilot/prompts/*.prompt.md`` → ``.github/prompts/``
     - ``syspilot/skills/`` → ``.github/skills/``
     - ``syspilot/scripts/python/`` → ``.syspilot/scripts/python/``
     - ``syspilot/sphinx/`` → ``docs/`` (build.ps1, build.sh)
     - ``syspilot/templates/`` → ``.syspilot/templates/``

   **Version Marker:**

   When installing locally, the version marker's ``source`` field SHALL be
   set to ``"local"`` instead of the GitHub URL.

   **Rationale:**

   * Simple existence check — no complex heuristics
   * User always has the final choice (no auto-detection override)
   * Same file ownership rules apply regardless of source


Version Tracking
----------------

.. spec:: Installed Version Marker
   :id: SYSPILOT_SPEC_INST_VERSION_MARKER
   :status: implemented
   :links: SYSPILOT_REQ_INST_VERSION_MARKER, SYSPILOT_REQ_INST_VERSION_UPDATE
   :tags: install, update, version

   **Design:**
   After installation, the Setup Agent stores a version marker in the
   target project's ``.syspilot/`` directory.

   **File:** ``.syspilot/version.json``

   **Content:**

   ::

      {
        "version": "0.1.0",
        "installedAt": "2026-03-16",
        "source": "https://github.com/OWNER/syspilot"
      }

   **Fields:**

   * ``version``: Semantic version that was installed (from ``syspilot/version.json``)
   * ``installedAt``: ISO date of installation or last update
   * ``source``: Install source — GitHub repository URL (supports forks) or ``"local"`` for local installs

   **Usage:**

   * Update process compares ``version`` with ``syspilot/version.json`` from chosen source (GitHub main or local)
   * No hash tracking — agent compares files directly when needed

   **Rationale:**

   * Minimal file, no overhead
   * Sufficient for version comparison
   * ``source`` field enables forks and custom repos
   * ``.syspilot/`` directory serves as config home for future extensions


File Ownership & Updates
------------------------

.. spec:: File Layout and Ownership
   :id: SYSPILOT_SPEC_INST_FILE_OWNERSHIP
   :status: implemented
   :links: SYSPILOT_REQ_INST_CUSTOM_PRESERVE, SYSPILOT_REQ_INST_FILE_OWNERSHIP
   :tags: install, update, ownership

   **Design:**
   Every file managed by syspilot has a clear owner that determines
   update behavior.

   **Methodology-Owned (replaced on every update):**

   * ``.syspilot/version.json`` — version marker
   * ``.syspilot/scripts/**`` — utility scripts
   * ``.syspilot/templates/**`` — document templates
   * ``.github/agents/syspilot.change.agent.md``
   * ``.github/agents/syspilot.verify.agent.md``
   * ``.github/agents/syspilot.mece.agent.md``
   * ``.github/agents/syspilot.trace.agent.md``
   * ``.github/agents/syspilot.memory.agent.md``
   * ``.github/agents/syspilot.setup.agent.md``
   * ``.github/prompts/syspilot.change.prompt.md``
   * ``.github/prompts/syspilot.verify.prompt.md``
   * ``.github/prompts/syspilot.mece.prompt.md``
   * ``.github/prompts/syspilot.trace.prompt.md``
   * ``.github/prompts/syspilot.memory.prompt.md``
   * ``.github/prompts/syspilot.setup.prompt.md``
   * ``.github/skills/syspilot.*/SKILL.md``
   * ``docs/build.ps1``, ``docs/build.sh``

   **Project-Owned (copied once on install, never updated):**

   * ``.github/agents/syspilot.release.agent.md``
   * ``.github/agents/syspilot.implement.agent.md``
   * ``.github/prompts/syspilot.release.prompt.md``
   * ``.github/prompts/syspilot.implement.prompt.md``

   These are installed as generic templates with a customization reminder.
   The project team customizes them via @syspilot.change.
   Subsequent updates never modify these files.

   **User-Owned (never touched by setup):**

   * ``docs/syspilot/**`` (user's spec tree)
   * ``docs/inst/**`` (instance specs)
   * ``docs/changes/**`` (change documents)
   * ``docs/conf.py`` (after initial creation)
   * ``.github/copilot-instructions.md``
   * Any non-syspilot agents/prompts/skills


.. spec:: Update Process
   :id: SYSPILOT_SPEC_INST_UPDATE_PROCESS
   :status: implemented
   :links: SYSPILOT_REQ_INST_VERSION_UPDATE, SYSPILOT_REQ_INST_BOOTSTRAP_SELF, SYSPILOT_REQ_INST_FILE_OWNERSHIP, SYSPILOT_SPEC_INST_VERSION_MARKER, SYSPILOT_SPEC_INST_FILE_OWNERSHIP
   :tags: update, migration

   **Design:**
   Update is agent-driven with curl from GitHub and explicit file ownership rules.
   Git serves as the backup mechanism — no separate backup/rollback needed.

   **Update Flow:**

   **Step 0: Bootstrap Self-Update**

   1. Fetch ``syspilot/agents/syspilot.setup.agent.md`` from chosen source
      (local ``syspilot/`` or GitHub main per SYSPILOT_SPEC_INST_SOURCE_DETECTION)
   2. Compare with local ``.github/agents/syspilot.setup.agent.md``
   3. If different → replace local immediately
   4. All subsequent steps use the updated setup agent logic

   **Step 1: Check for Updates**

   1. Fetch ``syspilot/version.json`` from chosen source
   2. Compare with local ``.syspilot/version.json``
   3. If remote version > local version → proceed to Step 2
   4. If remote version <= local version → inform user, abort

   **Step 2: Fetch and Apply by Ownership**

   Download all files from ``syspilot/`` (local or GitHub main, per chosen source) and apply by category:

   .. list-table::
      :header-rows: 1

      * - Category
        - Files
        - Action
      * - Methodology agents
        - change, verify, mece, trace, memory (+ prompts)
        - Replace always
      * - Setup agent
        - syspilot.setup.agent.md (+ prompt)
        - Already updated in Step 0
      * - Project agents
        - release, implement (+ prompts)
        - Skip (never modify)
      * - Skills
        - syspilot.ask-questions/SKILL.md
        - Replace always
      * - Scripts & build files
        - ``.syspilot/scripts/``, ``docs/build.*``
        - Replace always
      * - Templates
        - ``.syspilot/templates/``
        - Replace always
      * - User content
        - ``docs/``, ``.github/copilot-instructions.md``
        - Never touch

   **Step 3: Update Version Marker**

   Update ``.syspilot/version.json`` with new version and date.

   **Step 4: Validate**

   Run ``sphinx-build`` to verify. Confirm success.

   **First Install Exception:**
   On initial install (no ``.syspilot/version.json``), ALL agents including
   release and implement are copied as generic templates. These templates
   include a customization reminder banner.


Distribution
------------

.. spec:: Release Structure
   :id: SYSPILOT_SPEC_INST_RELEASE_STRUCTURE
   :status: implemented
   :links: SYSPILOT_REQ_INST_GITHUB_RELEASES, SYSPILOT_REQ_REL_GITHUB_PUBLISH, SYSPILOT_SPEC_INST_TEMPLATE_LAYOUT
   :tags: install, distribution, release

   **Design:**
   syspilot releases correspond to the main branch. GitHub Releases
   with tags provide version history and optional archive downloads.

   **Release Contents:**

   * Complete syspilot repository structure
   * ``syspilot/version.json`` with release version
   * README with installation instructions (curl commands)
   * docs/releasenotes.md with release history

   **Primary Distribution Channel:**

   Users fetch files directly from GitHub main via curl/Invoke-WebRequest.
   The ``syspilot/`` directory on main is always the current release.

   **Directory Structure in Repository:**

   ::

      syspilot/
      ├── .github/
      │   ├── agents/       # syspilot's own installation (consumer)
      │   ├── prompts/      # syspilot's own prompts
      │   ├── skills/       # syspilot's own skills
      │   └── copilot-instructions.md
      ├── syspilot/         # Distribution source (PRODUCT)
      │   ├── version.json  # Release version
      │   ├── agents/       # Generic agent templates (*.agent.md)
      │   ├── prompts/      # Generic prompt templates (*.prompt.md)
      │   ├── skills/       # Generic skill templates (*/SKILL.md)
      │   ├── scripts/      # Utility scripts
      │   ├── sphinx/       # Build scripts
      │   └── templates/    # Document templates
      │       └── change-document.md
      ├── docs/             # Self-documentation (including releasenotes.md)
      └── README.md         # Installation instructions (curl commands)

   **GitHub Release Mechanism:**

   * Maintainer pushes annotated Git tag (e.g., ``v0.2.0``)
   * GitHub automatically creates source archives
   * GitHub Actions publishes documentation to GitHub Pages
   * Release notes from docs/releasenotes.md displayed on release page

   **Rationale:**

   * Main branch = current release, simplest possible distribution
   * ``syspilot/`` is the complete release package
   * curl from raw.githubusercontent.com works without GitHub API
   * GitHub's automatic archiving provides optional ZIP/tar.gz downloads


Template Distribution
---------------------

.. spec:: Template Directory Layout
   :id: SYSPILOT_SPEC_INST_TEMPLATE_LAYOUT
   :status: implemented
   :links: SYSPILOT_REQ_INST_TEMPLATE_SOURCE, SYSPILOT_REQ_INST_IMPL_SKELETON, SYSPILOT_REQ_INST_PORTABLE
   :tags: install, distribution, templates

   **Design:**
   The ``syspilot/`` directory is the single source for all files
   distributed to target projects, including the release version.
   Its structure mirrors the target project layout.

   **Directory Structure:**

   ::

      syspilot/
      ├── version.json                     # → .syspilot/version.json
      ├── agents/                          # → .github/agents/
      │   ├── syspilot.setup.agent.md
      │   ├── syspilot.change.agent.md
      │   ├── syspilot.implement.agent.md  # Skeleton with TODOs
      │   ├── syspilot.verify.agent.md
      │   ├── syspilot.mece.agent.md
      │   ├── syspilot.trace.agent.md
      │   ├── syspilot.memory.agent.md
      │   └── syspilot.release.agent.md
      ├── prompts/                         # → .github/prompts/
      │   └── syspilot.*.prompt.md
      ├── skills/                          # → .github/skills/
      │   └── syspilot.ask-questions/
      │       └── SKILL.md
      ├── scripts/                         # → .syspilot/scripts/
      │   └── python/
      │       └── get_need_links.py
      ├── sphinx/                          # → docs/
      │   ├── build.ps1
      │   └── build.sh
      └── templates/                       # → .syspilot/templates/
          └── change-document.md

   **Mapping Rule:**
   Each subdirectory in ``syspilot/`` maps to a specific location in the
   target project. The Setup Agent uses this mapping when copying files.

   **Skeleton vs Full Agents:**

   * Most agents (change, verify, mece, trace, memory, setup) are
     distributed as-is — they work at the specification level and are
     inherently project-agnostic.
   * The **implement agent** is a skeleton with TODO placeholders for
     build commands, test commands, and language-specific patterns.
   * The **release agent** may need minor project customization but
     is mostly generic.

   **Divergence from .github/:**

   syspilot's own ``.github/agents/`` is a consumer installation.
   It may contain project-specific customizations (e.g., Python/pytest
   in the implement agent, Sphinx-specific commands). These divergences
   are expected and correct — they demonstrate the customization path
   that every target project follows.


.. spec:: Release Self-Install Validation
   :id: SYSPILOT_SPEC_INST_SELF_INSTALL
   :status: implemented
   :links: SYSPILOT_REQ_INST_TEMPLATE_SOURCE, SYSPILOT_REQ_REL_VALIDATION, SYSPILOT_SPEC_REL_VALIDATION_CHECKLIST, SYSPILOT_SPEC_INST_SETUP_AGENT
   :tags: release, validation, self-install

   **Design:**
   During the release process, syspilot validates the distribution path by
   installing from its own ``syspilot/`` directory into its ``.github/``
   directory, simulating a fresh installation into a target project.

   **Validation Steps:**

   1. Run Setup Agent's copy logic using ``syspilot/`` as source
   2. Verify all agent files are valid (parseable YAML frontmatter)
   3. Verify the implement agent skeleton contains TODO placeholders
      (not Python-specific commands)
   4. Verify ``.syspilot/version.json`` is created with correct version
   5. Verify sphinx-build succeeds with the installed configuration

   **When:** Added to SYSPILOT_SPEC_REL_VALIDATION_CHECKLIST as an additional
   validation category.

   **Rationale:**
   This guarantees that every release actually works when installed
   into a "foreign" environment. syspilot dogfoods its own distribution
   path, catching issues before users encounter them.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SYSPILOT_SPEC_INST')
