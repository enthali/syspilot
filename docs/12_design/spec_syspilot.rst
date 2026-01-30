syspilot Design Specifications
===============================

This document contains design specifications for the syspilot toolkit.

**Document Version**: 0.1  
**Last Updated**: 2026-01-28


Agent Architecture
------------------

.. spec:: Four-Agent Workflow
   :id: SPEC_SYSPILOT_001
   :status: approved
   :links: REQ_SYSPILOT_003, REQ_SYSPILOT_004, REQ_SYSPILOT_005, REQ_SYSPILOT_006, REQ_SYSPILOT_012
   :tags: architecture, agents

   **Design:**
   syspilot implements a four-agent workflow for structured change management.

   **Agent Responsibilities:**

   1. **change agent**: Analyze request + current implementation → Change Document + US/REQ/SPEC updates
   2. **implement agent**: Read Change Document → Code + Scripts + Tests (no spec changes)
   3. **verify agent**: Implementation → Verification Report
   4. **memory agent**: Project → Updated copilot-instructions.md

   **Workflow:**

   ::

      User Request
           │
           ▼
      ┌─────────────┐
      │   change    │ ──→ Change Document + US/REQ/SPEC RST updates
      └─────────────┘
           │
           ▼ (approved)
      ┌─────────────┐
      │  implement  │ ──→ Code + Scripts + Tests (reads SPECs from Change Doc)
      └─────────────┘
           │
           ▼
      ┌─────────────┐
      │   verify    │ ──→ Verification Report
      └─────────────┘
           │
           ▼ (passed)
      ┌─────────────┐
      │   memory    │ ──→ Updated copilot-instructions.md
      └─────────────┘

   **Files:**

   * ``.github/agents/syspilot.change.agent.md``
   * ``.github/agents/syspilot.implement.agent.md``
   * ``.github/agents/syspilot.verify.agent.md``
   * ``.github/agents/syspilot.memory.agent.md``

   **VS Code Handoffs:**

   Each agent file includes YAML frontmatter with ``handoffs:`` that enable
   VS Code to suggest the next agent in the workflow.

   **Main Chain:**

   ::

      change → implement → verify
          ↑                   │
          └───────────────────┘ (if issues found)

   **Analysis Agents (bidirectional):**

   ::

      mece ↔ trace
        │       │
        └───────┴──→ change (to fix issues)

   **Memory Agent:**

   Standalone - invoked after verify or on-demand. Has description but no handoffs.

   **Handoff Format:**

   ::

      ---
      description: Short agent purpose for UI display
      handoffs:
        - label: Display name
          agent: syspilot.targetagent
          prompt: Default prompt text
      ---

   **Initial Prompt Recommendations:**

   To show syspilot agents as suggestions when opening a new chat,
   configure VS Code workspace settings:

   **File:** ``.vscode/settings.json``

   ::

      {
        "chat.promptFilesRecommendations": {
          "syspilot.change": true,
          "syspilot.implement": true,
          "syspilot.verify": true,
          "syspilot.mece": true,
          "syspilot.trace": true,
          "syspilot.memory": true
        }
      }

   This ensures users see syspilot workflow options immediately.


.. spec:: sphinx-needs Documentation Structure
   :id: SPEC_SYSPILOT_002
   :status: approved
   :links: REQ_SYSPILOT_001, REQ_SYSPILOT_002
   :tags: sphinx-needs, structure

   **Design:**
   Documentation organized in numbered folders following esp32-distance pattern.

   **Directory Structure:**

   ::

      docs/
      ├── conf.py                    # sphinx-needs configuration
      ├── index.rst                  # Main index
      ├── 11_requirements/
      │   ├── index.rst              # Requirements overview
      │   ├── req_syspilot.rst       # syspilot requirements
      │   └── req_<component>.rst    # Component requirements
      ├── 12_design/
      │   ├── index.rst              # Design overview
      │   └── spec_<component>.rst   # Component designs
      └── 31_traceability/
          └── index.rst              # Auto-generated traceability

   **Naming Conventions:**

   * Requirements: ``REQ_<COMPONENT>_<NUMBER>`` (e.g., ``REQ_SYSPILOT_001``)
   * Designs: ``SPEC_<COMPONENT>_<NUMBER>`` (e.g., ``SPEC_SYSPILOT_001``)


.. spec:: Implementation Quality Gates
   :id: SPEC_SYSPILOT_003
   :status: approved
   :links: REQ_SYSPILOT_004
   :tags: quality, validation

   **Design:**
   implement agent runs sphinx-build as quality gate before coding.

   **Quality Gate Workflow:**

   1. Update requirement docs (``.rst``)
   2. Update design docs (``.rst``)
   3. **Run sphinx-build** → validates syntax + traceability
   4. If FAIL → fix docs, do not proceed to code
   5. If PASS → implement code with SPEC references
   6. Write tests with REQ references
   7. Run tests
   8. **Run sphinx-build again** → final validation

   **Commands:**

   ::

      # Build docs (validates all)
      sphinx-build -b html docs docs/_build/html -W --keep-going

      # Run tests
      pytest tests/ -v


.. spec:: Init Scripts for Environment Setup
   :id: SPEC_SYSPILOT_004
   :status: approved
   :links: REQ_SYSPILOT_009, REQ_SYSPILOT_008, REQ_SYSPILOT_019, REQ_SYSPILOT_020
   :tags: init, scripts, install

   **Design:**
   Minimal init scripts copy only the Setup Agent to enable installation.
   All other setup is handled interactively by the Setup Agent.

   **Script Locations (in syspilot installation):**

   * Windows: ``scripts/powershell/init.ps1``
   * Unix: ``scripts/bash/init.sh``

   **Script Behavior (minimal):**

   1. Create ``.github/agents/`` in target project
   2. Copy ``syspilot.setup.agent.md`` from syspilot's ``.github/agents/``
   3. Display message: "Open VS Code, start GitHub Copilot Chat, and select @syspilot.setup"

   **Rationale:**

   * Scripts are static and cannot adapt to user environment
   * Agent can interactively handle dependencies, conflicts, and user choices
   * Minimal script = less maintenance, fewer platform-specific issues

   **Usage:**

   ::

      # Windows (from target project directory)
      C:\path\to\syspilot\scripts\powershell\init.ps1

      # Unix (from target project directory)
      /path/to/syspilot/scripts/bash/init.sh

   **Note:** This is Step 1 of the installation process.
   Step 2 is invoking ``@syspilot.setup`` agent.


.. spec:: Agent Pre-Implementation Check
   :id: SPEC_SYSPILOT_005
   :status: approved
   :links: REQ_SYSPILOT_009, REQ_SYSPILOT_004
   :tags: agent, init

   **Design:**
   The implement agent checks for sphinx-needs availability before starting work.

   **Check Sequence:**

   1. Run ``sphinx-build --version`` (or ``uv run sphinx-build --version``)
   2. If NOT found → run init script
   3. If found → proceed with implementation

   **Integration:**
   Documented in ``.github/agents/syspilot.implement.agent.md`` under
   "Pre-Implementation Check" section.


.. spec:: Prompt-Agent Separation
   :id: SPEC_SYSPILOT_006
   :status: approved
   :links: REQ_SYSPILOT_001
   :tags: architecture, prompts

   **Design:**
   Strict separation between prompt files and agent files.

   **Prompt Files** (``.github/prompts/*.prompt.md``):
   
   - Minimal frontmatter only
   - Reference the agent, nothing else
   - User-facing entry point

   **Format:**

   ::

      ---
      agent: syspilot.change
      ---

   **Agent Files** (``.github/agents/*.agent.md``):
   
   - Full instructions
   - Workflow descriptions
   - Examples
   - All the logic

   **Rationale:**

   - Prompts are stable entry points
   - Agents can be updated without changing invocation
   - Separation of concerns: WHAT to invoke vs HOW to execute
   - Consistent with speckit design pattern


Installation & Update Specifications
------------------------------------

.. spec:: Release Structure
   :id: SPEC_SYSPILOT_007
   :status: draft
   :links: REQ_SYSPILOT_018
   :tags: install, distribution, release

   **Design:**
   syspilot releases are downloadable zips from GitHub Releases.

   **Release Contents:**

   * Complete syspilot repository structure
   * ``version.json`` with release version
   * README with installation instructions

   **Version Identification:**

   * ``version.json`` at ``.syspilot`` root contains release version
   * After successful install: renamed to ``version_installed.json``

   **Directory Structure in Release:**

   ::

      syspilot-vX.Y.Z/
      ├── .github/
      │   ├── agents/       # Agent definitions (*.agent.md)
      │   ├── prompts/      # Prompt files (*.prompt.md)
      │   └── copilot-instructions.md
      ├── scripts/          # Init and utility scripts
      ├── templates/        # Document templates
      ├── docs/             # Self-documentation
      ├── version.json      # Release version
      └── README.md         # Installation instructions

   **Rationale:**

   * ``.github/agents/`` is the standard location for GitHub Copilot agents
   * Single source of truth - no duplication between ``agents/`` and ``.github/agents/``
   * Works immediately after ``git clone`` without additional setup


.. spec:: Setup Agent Design
   :id: SPEC_SYSPILOT_008
   :status: draft
   :links: REQ_SYSPILOT_019, REQ_SYSPILOT_020, REQ_SYSPILOT_023
   :tags: install, agent, setup

   **Design:**
   Installation is a two-step process: init script, then setup agent.

   **Step 1: Init Script (manual)**

   * User runs ``scripts/powershell/init.ps1`` (or ``bash/init.sh``) from syspilot location
   * Script copies ``syspilot.setup.agent.md`` from ``.github/agents/`` to target project's ``.github/agents/``
   * Covered by SPEC_SYSPILOT_004

   **Step 2: Setup Agent (@syspilot.setup)**

   * User invokes ``@syspilot.setup`` in Copilot Chat
   * Agent copies remaining agents from syspilot's ``.github/agents/`` to target's ``.github/agents/``
   * Agent copies prompts from syspilot's ``.github/prompts/`` to target's ``.github/prompts/``
   * Agent checks and installs dependencies (see below)
   * Agent validates successful ``sphinx-build``
   * Agent renames ``version.json`` to ``version_installed.json``
   * Agent confirms success

   **Dependency Installation (Interactive with User):**

   The setup agent guides the user through installing required dependencies:

   1. **Check Python**: Verify ``python --version`` available
   2. **Check pip/uv**: Verify package manager available
   3. **Inform user** about what will be installed:

      ::

         Required dependencies:
         - sphinx >= 7.0.0 (documentation generator)
         - sphinx-needs >= 2.0.0 (requirements traceability)
         - furo >= 2024.0.0 (documentation theme)
         - myst-parser >= 2.0.0 (Markdown support)
         
         Optional (for diagrams):
         - graphviz (Python package + system tool)

   4. **Install with user confirmation**:

      ::

         pip install sphinx sphinx-needs furo myst-parser

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

   **Works for both new and existing projects.**

   **Existing Project Handling:**

   * Detects existing ``docs/conf.py`` and merges sphinx-needs config
   * Detects existing ``.github/`` content and merges safely
   * Prompts user for decisions on conflicts


.. spec:: File Layout and Ownership
   :id: SPEC_SYSPILOT_009
   :status: draft
   :links: REQ_SYSPILOT_022
   :tags: install, update, ownership

   **Design:**
   Clear separation between syspilot core files and user content.

   **Syspilot Core (with intelligent merge):**

   * ``.syspilot/**`` (entire folder) - replaceable
   * ``.github/agents/syspilot.*.agent.md`` - merge if modified
   * ``.github/prompts/syspilot.*.prompt.md`` - merge if modified

   **Intelligent Merge for Agent Files:**

   When updating agent/prompt files, the setup agent SHALL:

   1. **Check for modifications**: Compare target file with original syspilot version
   2. **If unmodified**: Replace silently
   3. **If modified**: Show diff to user and ask:

      * **Overwrite**: Replace with new syspilot version (lose customizations)
      * **Keep**: Keep user's version (may miss new features)
      * **Merge**: Agent attempts to merge changes interactively

   **User Content (preserved during updates):**

   * ``docs/10_userstories/**`` (user's stories)
   * ``docs/11_requirements/**`` (user's requirements)
   * ``docs/12_design/**`` (user's design)
   * ``docs/changes/**`` (user's change documents)
   * ``.github/copilot-instructions.md`` (user's memory)
   * ``.github/agents/*.agent.md`` (non-syspilot agents)
   * ``.github/prompts/*.prompt.md`` (non-syspilot prompts)

   **Shared/Merged (require interactive merge):**

   * ``docs/conf.py`` (syspilot config + user additions)
   * ``docs/pyproject.toml`` or ``docs/requirements.txt``


.. spec:: Update Process
   :id: SPEC_SYSPILOT_010
   :status: draft
   :links: REQ_SYSPILOT_021
   :tags: update, migration

   **Design:**
   Update is agent-driven with backup and rollback support.

   **Update Flow:**

   1. User invokes ``@syspilot.setup`` (same agent for install and update)
   2. Agent detects existing ``.syspilot/version.json`` → update mode
   3. Agent queries GitHub API for latest release version
   4. Compare versions: if current >= latest, inform user "already up to date"
   5. If newer version available:

      a. **Backup**: Check for ``.syspilot_backup/`` → delete if exists
      b. **Backup**: Rename ``.syspilot/`` → ``.syspilot_backup/``
      c. **Download**: Fetch latest release ZIP from GitHub
      d. **Extract**: Unpack to ``.syspilot/``
      e. **Merge**: Copy agents/prompts with intelligent merge (see SPEC_009)
      f. **Validate**: Run ``sphinx-build`` to verify
      g. **Success**: Delete ``.syspilot_backup/``
      h. **Failure**: Restore ``.syspilot_backup/`` → ``.syspilot/``, inform user

   **GitHub Release Query:**

   ::

      # Agent uses fetch_webpage or terminal curl
      curl -s https://api.github.com/repos/OWNER/syspilot/releases/latest

   **Rollback on Failure:**

   If any step fails after backup:

   * Remove partial ``.syspilot/``
   * Rename ``.syspilot_backup/`` back to ``.syspilot/``
   * Inform user: "Update failed, rolled back to previous version"


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_SYSPILOT')

.. needflow:: SPEC_SYSPILOT_001
