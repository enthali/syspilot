Setup Agent Design
===================

Design specifications for the Setup Agent — installation, update, and environment management.

**Document Version**: 0.2
**Last Updated**: 2026-02-06


Installation
------------

.. spec:: Init Scripts for Environment Setup
   :id: SPEC_INST_INIT_SCRIPTS
   :status: implemented
   :links: REQ_INST_AUTO_SETUP, REQ_INST_PORTABLE, REQ_INST_NEW_PROJECT, REQ_INST_ADOPT_EXISTING
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


.. spec:: Setup Agent Design
   :id: SPEC_INST_SETUP_AGENT
   :status: implemented
   :links: REQ_INST_NEW_PROJECT, REQ_INST_ADOPT_EXISTING, REQ_INST_SPHINX_NEEDS_DEP
   :tags: install, agent, setup

   **Design:**
   Installation is a two-step process: init script, then setup agent.

   **Step 1: Init Script (manual)**

   * User runs ``scripts/powershell/init.ps1`` (or ``bash/init.sh``) from syspilot location
   * Script copies ``syspilot.setup.agent.md`` from ``.github/agents/`` to target project's ``.github/agents/``
   * Covered by SPEC_INST_INIT_SCRIPTS

   **Step 2: Setup Agent (@syspilot.setup)**

   **Section 1: Auto-Detect syspilot Location**

   1. Run Find-SyspilotInstallation (SPEC_INST_AUTO_DETECT)
   2. Log all found versions for transparency
   3. Select newest version
   4. If none found: Error with helpful instructions

   **Section 2: Check Dependencies (Interactive)**

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

   **Section 3: Copy Files from syspilot**

   Using ``$syspilotRoot`` from auto-detection:

   * Copy agents: ``$syspilotRoot/.github/agents/*.agent.md`` → ``.github/agents/``
   * Copy prompts: ``$syspilotRoot/.github/prompts/*.prompt.md`` → ``.github/prompts/``
   * Copy skills: ``$syspilotRoot/.github/skills/*.skill.md`` → ``.github/skills/``
   * Apply intelligent merge (SPEC_INST_FILE_OWNERSHIP)

   **Section 4: Validate and Confirm**

   * Validate successful ``sphinx-build``
   * Rename ``version.json`` to ``version_installed.json``
   * Confirm success

   **Works for both new and existing projects.**

   **Existing Project Handling:**

   * Detects existing ``docs/conf.py`` and merges sphinx-needs config
   * Detects existing ``.github/`` content and merges safely
   * Prompts user for decisions on conflicts


File Ownership & Updates
------------------------

.. spec:: File Layout and Ownership
   :id: SPEC_INST_FILE_OWNERSHIP
   :status: implemented
   :links: REQ_INST_CUSTOM_PRESERVE
   :tags: install, update, ownership

   **Design:**
   Clear separation between syspilot core files and user content.

   **Syspilot Core (with intelligent merge):**

   * ``.syspilot/**`` (entire folder) - replaceable
   * ``.github/agents/syspilot.*.agent.md`` - merge if modified
   * ``.github/prompts/syspilot.*.prompt.md`` - merge if modified
   * ``.github/skills/syspilot.*.skill.md`` - merge if modified

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
   :id: SPEC_INST_UPDATE_PROCESS
   :status: implemented
   :links: REQ_INST_VERSION_UPDATE
   :tags: update, migration

   **Design:**
   Update is agent-driven with backup and rollback support.

   **Update Flow:**

   **Step 0: Find Newest syspilot Version**

   1. Run Find-SyspilotInstallation (SPEC_INST_AUTO_DETECT)
   2. Log all found versions for transparency
   3. Select newest version as source for update
   4. Compare with currently installed version (``.syspilot/version.json``)
   5. If found version <= installed version:

      * Warn user: "Found version X.Y.Z is not newer than installed X.Y.Z"
      * Suggest checking for latest release on GitHub
      * Abort update

   6. If found version > installed version: Proceed to Step 1

   **Step 1: Detect Update Mode**

   1. User invokes ``@syspilot.setup`` (same agent for install and update)
   2. Agent detects existing ``.syspilot/version.json`` → update mode
   3. Inform user of current and target versions

   **Step 2: Backup and Update**

   If newer version available (from Step 0):

      a. **Backup**: Check for ``.syspilot_backup/`` → delete if exists
      b. **Backup**: Rename ``.syspilot/`` → ``.syspilot_backup/``
      c. **Download**: Fetch latest release ZIP from GitHub
      d. **Extract**: Unpack to ``.syspilot/``
      e. **Merge**: Copy agents/prompts/skills with intelligent merge (see SPEC_INST_FILE_OWNERSHIP)
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


Auto-Detection
--------------

.. spec:: syspilot Auto-Detection Algorithm
   :id: SPEC_INST_AUTO_DETECT
   :status: draft
   :links: REQ_INST_AUTO_DETECT
   :tags: install, autodetect, powershell

   **Design:**
   PowerShell/Bash function that finds syspilot installation via version.json search.

   **Algorithm (PowerShell):**

   ::

      function Find-SyspilotInstallation {
          # Search up to 3 parent directory levels
          $searchPaths = @(
              Get-Location,
              (Get-Location).Parent,
              (Get-Location).Parent.Parent,
              (Get-Location).Parent.Parent.Parent
          ) | Where-Object { $_ -ne $null }
          
          $foundVersions = @()
          
          foreach ($path in $searchPaths) {
              # Find all version.json files recursively (max depth 3)
              $versionFiles = Get-ChildItem -Path $path -Filter "version.json" `
                                           -Recurse -Depth 3 -ErrorAction SilentlyContinue
              
              foreach ($file in $versionFiles) {
                  try {
                      $content = Get-Content $file.FullName | ConvertFrom-Json
                      $version = $content.version
                      
                      # Skip if not syspilot version format
                      if ($version -notmatch '^(\d+)\.(\d+)\.(\d+)(-\w+(\.\d+)?)?$') {
                          continue
                      }
                      
                      $foundVersions += [PSCustomObject]@{
                          Path = $file.Directory.FullName
                          Version = $version
                          File = $file.FullName
                      }
                  } catch {
                      # Skip invalid JSON
                      continue
                  }
              }
          }
          
          if ($foundVersions.Count -eq 0) {
              Write-Error "No syspilot installation found (no version.json)"
              Write-Host "Searched in:"
              $searchPaths | ForEach-Object { Write-Host "  $_" }
              return $null
          }
          
          # Sort by version (newest first)
          $sorted = $foundVersions | Sort-Object {
              if ($_.Version -match '^(\d+)\.(\d+)\.(\d+)(-(\w+)\.?(\d+)?)?') {
                  $major = [int]$matches[1]
                  $minor = [int]$matches[2]
                  $patch = [int]$matches[3]
                  $prerelease = $matches[5]
                  $prereleaseNum = if ($matches[6]) { [int]$matches[6] } else { 0 }
                  return @($major, $minor, $patch, $(if ($prerelease) { 0 } else { 999 }), $prereleaseNum)
              }
          } -Descending
          
          # Log all found versions
          Write-Host "Found syspilot installations:"
          $sorted | ForEach-Object {
              Write-Host "  v$($_.Version) at $($_.Path)"
          }
          
          # Return newest
          $newest = $sorted[0]
          Write-Host "Selected newest: v$($newest.Version)" -ForegroundColor Green
          
          return $newest.Path
      }

   **Bash Version:**

   Equivalent logic in bash using find, jq, and sort.

   **Edge Cases:**

   1. **No version.json found**: Error with helpful message
   2. **Multiple identical versions**: Pick first found (arbitrary but consistent)
   3. **Invalid JSON**: Skip file and continue search
   4. **Non-syspilot version.json**: Skip (version format check)

   **Rationale:**

   * Works with release ZIP structure (syspilot-0.1.0-beta.3/)
   * Works with git clone
   * Works with multiple versions side-by-side
   * Always selects newest (important for updates)
   * Transparent debugging (logs all found versions)


Distribution
------------

.. spec:: Release Structure
   :id: SPEC_INST_RELEASE_STRUCTURE
   :status: implemented
   :links: REQ_INST_GITHUB_RELEASES, REQ_REL_GITHUB_PUBLISH
   :tags: install, distribution, release

   **Design:**
   syspilot releases are distributed via GitHub Releases, which automatically
   creates .zip and .tar.gz archives of the repository at tagged commits.

   **Release Contents:**

   * Complete syspilot repository structure
   * ``version.json`` with release version
   * README with installation instructions
   * docs/releasenotes.md with release history

   **Version Identification:**

   * ``version.json`` at repository root contains release version
   * After successful install: copied to project's ``.syspilot/version.json``

   **Directory Structure in Release Archive:**

   ::

      syspilot-X.Y.Z/
      ├── .github/
      │   ├── agents/       # Agent definitions (*.agent.md)
      │   ├── prompts/      # Prompt files (*.prompt.md)
      │   ├── skills/       # Skill files (*.skill.md)
      │   └── copilot-instructions.md
      ├── scripts/          # Init and utility scripts
      ├── templates/        # Document templates
      ├── docs/             # Self-documentation (including releasenotes.md)
      ├── version.json      # Release version
      └── README.md         # Installation instructions

   **GitHub Release Mechanism:**

   * Maintainer pushes annotated Git tag (e.g., ``v0.2.0``)
   * GitHub automatically creates source archives
   * GitHub Actions publishes documentation to GitHub Pages
   * Release notes from docs/releasenotes.md displayed on release page

   **Rationale:**

   * ``.github/agents/`` is the standard location for GitHub Copilot agents
   * Single source of truth - no duplication between ``agents/`` and ``.github/agents/``
   * Works immediately after ``git clone`` or archive extraction without additional setup
   * GitHub's automatic archiving ensures consistent distribution


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_INST')
