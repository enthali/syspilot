# Change Document: detect-scope

**Status**: approved
**Branch**: feature/detect-scope
**Created**: 2026-02-11
**Author**: Change Agent

---

## Summary

The auto-detection algorithm (REQ_INST_AUTO_DETECT / SPEC_INST_AUTO_DETECT) currently searches parent directories up to 3 levels above the current working directory. When a user downloads syspilot to a location outside the project directory, this causes the search to escape the project root — which is a security/correctness issue.

**Fix**: Restrict auto-detection to the project directory only (no parent traversal). If syspilot is not found within the project, inform the user and offer to download the latest version from GitHub (reusing the update flow's GitHub download mechanism).

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_INST_NEW_PROJECT | Install syspilot in New Project | modified | AC-1 reworded: precondition is setup agent availability, not prior download. New AC-2: GitHub fallback when not found locally. |
| US_INST_ADOPT_EXISTING | Adopt syspilot in Existing Project | modified | New AC-4: GitHub fallback when not found locally. |
| US_INST_UPDATE | Update syspilot to Latest Version | none | Already describes GitHub download — no change needed |

### New User Stories

_None needed — the existing stories cover the intent. The change is in HOW detection works (Level 1/2)._

### Modified User Stories

#### US_INST_NEW_PROJECT: Install syspilot in New Project

```rst
.. story:: Install syspilot in New Project
   :id: US_INST_NEW_PROJECT
   :status: draft
   :priority: mandatory
   :tags: install, distribution
   :links: US_INST_BOOTSTRAP

   **As a** developer starting a new project,
   **I want to** install syspilot from the beginning,
   **so that** I have requirements engineering built-in from day one.

   **Acceptance Scenarios:**

   1. Given the setup agent is available in .github/agents/, When I invoke @syspilot.setup, Then syspilot structure is created without requiring manual path configuration
   2. Given syspilot is not found in the project directory, When I invoke @syspilot.setup, Then the agent offers to download the latest version from GitHub
   3. Given installation completes, When I check, Then I'm ready to run bootstrap
   4. Given I need a specific version, When I install, Then I can obtain that version
```

#### US_INST_ADOPT_EXISTING: Adopt syspilot in Existing Project

```rst
.. story:: Adopt syspilot in Existing Project
   :id: US_INST_ADOPT_EXISTING
   :status: draft
   :priority: mandatory
   :tags: install, adoption, distribution
   :links: US_INST_BOOTSTRAP

   **As a** developer with an existing project,
   **I want to** adopt syspilot without disrupting my current work,
   **so that** I can add requirements engineering to a project already in progress.

   **Acceptance Scenarios:**

   1. Given I have an existing project with code, When I follow the adoption process, Then syspilot is added alongside existing files
   2. Given I have existing documentation, When I adopt syspilot, Then my existing docs are not overwritten
   3. Given adoption completes, When I check, Then I can start creating User Stories
   4. Given syspilot is not found in the project directory, When I start adoption, Then the agent offers to download the latest version from GitHub
```

### Decisions

- **D-1**: The minimal precondition for installation is that the setup agent file exists in `.github/agents/` — how it got there is irrelevant (init script, manual copy, etc.)
- **D-2**: Auto-detection SHALL only search within the project directory (workspace root + subdirectories), never parent directories
- **D-3**: When syspilot is not found locally, the agent SHALL offer GitHub download (reusing the update flow mechanism)

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies — US_INST_UPDATE already has GitHub download, now install/adopt gain fallback consistently
- [x] Gaps identified and addressed — the "not found locally" scenario was missing, now covered

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| REQ_INST_AUTO_DETECT | US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING, US_INST_UPDATE | modified | Core change: restrict search to project directory, add GitHub fallback |
| REQ_INST_NEW_PROJECT | US_INST_NEW_PROJECT | modified | AC-4: clarify "within project directory" |
| REQ_INST_ADOPT_EXISTING | US_INST_ADOPT_EXISTING | modified | AC-5: clarify "within project directory" |

### Modified Requirements

#### REQ_INST_AUTO_DETECT: Auto-Detection of syspilot Installation

```rst
.. req:: Auto-Detection of syspilot Installation
   :id: REQ_INST_AUTO_DETECT
   :status: draft
   :priority: mandatory
   :tags: install, autodetect
   :links: US_INST_NEW_PROJECT, US_INST_ADOPT_EXISTING, US_INST_UPDATE

   **Description:**
   syspilot SHALL auto-detect its own location by searching for version.json files
   within the project directory only.

   **Rationale:**
   Release ZIP structure places syspilot in versioned folders (syspilot-X.Y.Z/).
   Manual path input is error-prone and breaks user experience. Auto-detection
   enables seamless installation from arbitrary extraction locations.
   Searching above the project root is a security/correctness risk when the
   download location is outside the workspace.

   **Acceptance Criteria:**

   * AC-1: Search within the project directory (workspace root and subdirectories) for version.json files
   * AC-2: Parse each version.json to extract version number
   * AC-3: When multiple found, select newest semantic version (including pre-release tags)
   * AC-4: Return syspilot root directory (where version.json was found)
   * AC-5: If no version.json found within project directory, inform user and offer to download the latest version from GitHub Releases
   * AC-6: Log all found versions for debugging
   * AC-7: SHALL NOT search above the project root directory
```

#### REQ_INST_NEW_PROJECT: New Project Installation (AC-4 only)

```rst
   * AC-4: Setup agent SHALL use REQ_INST_AUTO_DETECT auto-detection to locate syspilot files within the project directory
```

#### REQ_INST_ADOPT_EXISTING: Existing Project Adoption (AC-5 only)

```rst
   * AC-5: Setup agent SHALL use REQ_INST_AUTO_DETECT auto-detection to locate syspilot files within the project directory
```

### Decisions

- **D-4**: Search scope restricted to workspace root + subdirectories only
- **D-5**: GitHub fallback added as AC-5 in REQ_INST_AUTO_DETECT
- **D-6**: Explicit prohibition of parent traversal added as AC-7

### Horizontal Check (MECE)

- [x] No contradictions — REQ_INST_VERSION_UPDATE already has GitHub download, consistent
- [x] No redundancies — GitHub fallback in auto-detect complements, not duplicates, update flow
- [x] All modified REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SPEC_INST_AUTO_DETECT | REQ_INST_AUTO_DETECT | modified | Restrict search to project root only, add GitHub fallback |
| SPEC_INST_SETUP_AGENT | REQ_INST_NEW_PROJECT, REQ_INST_ADOPT_EXISTING | modified | Section 1 Step 4: GitHub download instead of just error |

### Modified Design Elements

#### SPEC_INST_AUTO_DETECT: syspilot Auto-Detection Algorithm

```rst
.. spec:: syspilot Auto-Detection Algorithm
   :id: SPEC_INST_AUTO_DETECT
   :status: draft
   :links: REQ_INST_AUTO_DETECT
   :tags: install, autodetect, powershell

   **Design:**
   PowerShell/Bash function that finds syspilot installation via version.json search
   within the project directory only.

   **Algorithm (PowerShell):**

   ::

      function Find-SyspilotInstallation {
          # Search ONLY within the project directory (workspace root)
          $projectRoot = Get-Location

          $foundVersions = @()

          # Find all version.json files recursively within project directory
          $versionFiles = Get-ChildItem -Path $projectRoot -Filter "version.json" `
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

          if ($foundVersions.Count -eq 0) {
              Write-Host "No syspilot installation found in project directory: $projectRoot"
              Write-Host ""
              Write-Host "Would you like to download the latest version from GitHub?"
              Write-Host "  The setup agent can fetch the latest release automatically."
              return $null  # Agent handles GitHub download interactively
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

   1. **No version.json found**: Inform user, offer GitHub download
   2. **Multiple identical versions**: Pick first found (arbitrary but consistent)
   3. **Invalid JSON**: Skip file and continue search
   4. **Non-syspilot version.json**: Skip (version format check)
   5. **syspilot downloaded outside project**: Not found — GitHub fallback offered

   **Rationale:**

   * Searches only within project directory — never escapes project root
   * Works with release ZIP extracted into project directory
   * Works with git clone within project directory
   * Works with multiple versions side-by-side
   * Always selects newest (important for updates)
   * Transparent debugging (logs all found versions)
   * Falls back to GitHub download when not found locally
```

#### SPEC_INST_SETUP_AGENT: Setup Agent Design (Section 1 only)

```rst
   **Section 1: Auto-Detect syspilot Location**

   1. Run Find-SyspilotInstallation (SPEC_INST_AUTO_DETECT)
   2. Log all found versions for transparency
   3. Select newest version
   4. If none found: Inform user that syspilot was not found in the project
      directory. Offer to download the latest version from GitHub Releases
      (reuse GitHub Release Query mechanism from SPEC_INST_UPDATE_PROCESS).
      After download and extraction into the project directory, re-run
      Find-SyspilotInstallation to locate the downloaded version.
```

### Decisions

- **D-7**: Search depth set to `-Depth 3` from single project root (sufficient for extracted ZIP)
- **D-8**: GitHub fallback in SPEC_INST_SETUP_AGENT reuses the GitHub Release Query from SPEC_INST_UPDATE_PROCESS
- **D-9**: After GitHub download, re-run auto-detect to locate the downloaded version

### Horizontal Check (MECE)

- [x] No contradictions — SPEC_INST_UPDATE_PROCESS unchanged, GitHub download mechanism reused
- [x] No redundancies — fallback references update process, doesn't duplicate code
- [x] All SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|-------------|--------|-----------|
| US_INST_NEW_PROJECT | REQ_INST_AUTO_DETECT, REQ_INST_NEW_PROJECT | SPEC_INST_AUTO_DETECT, SPEC_INST_SETUP_AGENT | ✅ |
| US_INST_ADOPT_EXISTING | REQ_INST_AUTO_DETECT, REQ_INST_ADOPT_EXISTING | SPEC_INST_AUTO_DETECT, SPEC_INST_SETUP_AGENT | ✅ |

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified (US → REQ → SPEC)
- [x] All touched elements set to `:status: approved`
- [x] RST files updated atomically
- [x] Ready for implementation

---

*Generated by syspilot Change Agent*
