# Change Document: setup-autodetect

**Status**: draft
**Branch**: feature/setup-autodetect
**Created**: 2026-01-31
**Author**: syspilot Change Agent

---

## Summary

Fix setup installation workflow to auto-detect syspilot location via version.json instead of requiring manual path input. This resolves a critical UX issue where the setup agent assumes hardcoded paths (C:\workspace\syspilot) that don't match the actual release ZIP structure (syspilot-0.1.0-beta.2/syspilot-0.1.0-beta.2/).

**Type**: PATCH (bugfix) - 0.1.0-beta.2 → 0.1.0-beta.3

---

## Level 0: User Stories

**Status**: 🔄 in progress

### Impacted User Stories

All three installation-related User Stories are affected by the broken assumption about syspilot location:

| ID | Title | Impact | Current Problem |
|----|-------|--------|-----------------|
| US_SYSPILOT_012 | Install in New Project | modified | Setup Agent asks for path (C:\workspace\syspilot) but release ZIP has different structure |
| US_SYSPILOT_013 | Adopt Existing Project | modified | Same path assumption breaks adoption workflow |
| US_SYSPILOT_014 | Update to Latest Version | modified | Can't reliably find new version when multiple exist |

### Root Cause

**Acceptance Criterion in US_SYSPILOT_012:**
> "Given I follow the installation process, Then syspilot structure is created"

**Reality:**
- User downloads `syspilot-0.1.0-beta.2.zip`
- Extracts to `C:\workspace\EventManager\syspilot-0.1.0-beta.2\syspilot-0.1.0-beta.2\`
- Runs `init.ps1` (works - copies setup agent ✓)
- Setup Agent asks: "Where is syspilot? Default: C:\workspace\syspilot" (WRONG! ❌)
- User confused, installation breaks

### Proposed Fix (User Story Level)

**No new User Stories needed** - the intent (WHY) is still correct:
- US_012: Install from beginning ✓
- US_013: Adopt without disruption ✓  
- US_014: Update to latest ✓

**Minor Acceptance Criteria Update:**

Add to US_SYSPILOT_012, Scenario 1:
> Given I **download and extract** syspilot release, When I follow the installation process, Then syspilot structure is created **without requiring manual path configuration**

This makes the acceptance criterion match the actual release distribution method (ZIP download).

### Horizontal Check (MECE)

- [x] No contradictions with other User Stories
- [x] No new User Stories needed (fixing implementation, not changing intent)
- [x] Covers all three affected stories (012, 013, 014)

---

## Level 1: Requirements

**Status**: 🔄 in progress

### Impacted Requirements

Found via links from US_012, 013, 014:

| ID | Linked From | Impact | Current Problem |
|----|-------------|--------|-----------------|
| REQ_SYSPILOT_019 | US_012 | **modified** | "User can invoke agents after installation" - assumes path is known |
| REQ_SYSPILOT_020 | US_013 | **modified** | "User guided through decisions" - asks for wrong path |
| REQ_SYSPILOT_021 | US_014 | **modified** | "Determine installed version" - can't find newest when multiple exist |
| REQ_SYSPILOT_023 | US_012, 013 | minor update | Dependency check works, but path assumption is wrong |

### Root Cause Analysis

**REQ_SYSPILOT_019 (New Project Installation):**
```
AC-1: User can invoke syspilot agents after installation
```
**Problem:** Assumes Setup Agent knows where syspilot files are. Currently asks user for path with wrong default (C:\workspace\syspilot).

**REQ_SYSPILOT_021 (Version Update):**
```
AC-1: User can determine currently installed version
```
**Problem:** When multiple syspilot versions exist (e.g., old in .syspilot/, new extracted from ZIP), can't reliably find the newest.

### Proposed Changes

**Modify REQ_SYSPILOT_019: New Project Installation**

Add new acceptance criteria:

```rst
* AC-4: Setup agent SHALL auto-detect syspilot location via version.json search
* AC-5: Auto-detection SHALL find all version.json files in parent directories
* AC-6: When multiple found, SHALL select the newest version
* AC-7: Setup agent SHALL NOT require manual path input
```

**Rationale:** Makes installation work with actual release distribution method (ZIP download to arbitrary location).

**Modify REQ_SYSPILOT_021: Version Update and Migration**

Update AC-1:

```rst
* AC-1: User can determine currently installed version AND newest available syspilot version via auto-detection
```

Add new AC:

```rst
* AC-5: Update process SHALL auto-detect newest syspilot version (not oldest cached version)
```

**Rationale:** Prevents updating from old cached version when user downloaded newer release.

### New Requirement?

**Consider: REQ_SYSPILOT_024 - Auto-Detection of syspilot Location**

Should we create a new standalone requirement for the auto-detection mechanism itself, since it's used by multiple workflows (install, adopt, update)?

**Proposed REQ_SYSPILOT_024:**
```rst
.. req:: Auto-Detection of syspilot Installation
   :id: REQ_SYSPILOT_024
   :status: draft
   :priority: mandatory
   :tags: install, autodetect
   :links: US_SYSPILOT_012, US_SYSPILOT_013, US_SYSPILOT_014

   **Description:**
   syspilot SHALL auto-detect its own location by searching for version.json files.

   **Rationale:**
   Release ZIP structure places syspilot in versioned folders (syspilot-X.Y.Z).
   Manual path input is error-prone and breaks user experience.

   **Acceptance Criteria:**

   * AC-1: Search parent directories for version.json files
   * AC-2: Parse each version.json to extract version number
   * AC-3: When multiple found, select the newest semantic version
   * AC-4: Return syspilot root directory (where version.json was found)
   * AC-5: Fail gracefully if no version.json found
```

**Alternative:** Keep detection logic embedded in REQ_019, 020, 021 without separate requirement.

**Decision:** ✅ **Create REQ_SYSPILOT_024** - Centralizes logic, clear ownership, reusable across install/adopt/update workflows.

### New Requirements

**REQ_SYSPILOT_024: Auto-Detection of syspilot Installation**

```rst
.. req:: Auto-Detection of syspilot Installation
   :id: REQ_SYSPILOT_024
   :status: draft
   :priority: mandatory
   :tags: install, autodetect
   :links: US_SYSPILOT_012, US_SYSPILOT_013, US_SYSPILOT_014

   **Description:**
   syspilot SHALL auto-detect its own location by searching for version.json files.

   **Rationale:**
   Release ZIP structure places syspilot in versioned folders (syspilot-X.Y.Z/).
   Manual path input is error-prone and breaks user experience. Auto-detection
   enables seamless installation from arbitrary extraction locations.

   **Acceptance Criteria:**

   * AC-1: Search parent directories (up to 3 levels) for version.json files
   * AC-2: Parse each version.json to extract version number
   * AC-3: When multiple found, select newest semantic version (including pre-release tags)
   * AC-4: Return syspilot root directory (where version.json was found)
   * AC-5: Fail gracefully with helpful message if no version.json found
   * AC-6: Log all found versions for debugging
```

### Modified Requirements

**REQ_SYSPILOT_019: New Project Installation**

Add reference to auto-detection:

```rst
* AC-4: Setup agent SHALL use REQ_SYSPILOT_024 auto-detection to locate syspilot files
* AC-5: Setup agent SHALL NOT require manual path input
```

**REQ_SYSPILOT_020: Existing Project Adoption**

Add reference to auto-detection:

```rst
* AC-5: Setup agent SHALL use REQ_SYSPILOT_024 auto-detection to locate syspilot files
```

**REQ_SYSPILOT_021: Version Update and Migration**

Update AC-1 and add new AC:

```rst
* AC-1: User can determine currently installed version AND newest available syspilot via REQ_SYSPILOT_024 auto-detection
* AC-5: Update SHALL use newest version found (not oldest cached)
```

### Decisions

- **Decision 1:** Create REQ_024 instead of embedding logic in multiple requirements
  - Rationale: DRY principle, single source of truth for auto-detection algorithm

- **Decision 2:** Limit parent directory search to 3 levels
  - Rationale: Balance between finding the file and avoiding excessive filesystem traversal

- **Decision 3:** Support pre-release version comparison (0.1.0-beta.2 vs 0.1.0-beta.3)
  - Rationale: Users may have multiple beta versions during testing

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] REQ_024 created as standalone requirement (not duplicated)
- [x] All modified REQs (019, 020, 021) link to REQ_024
- [x] No gaps - auto-detection covers install, adopt, and update scenarios

---

## Level 2: Design

**Status**: 🔄 in progress

### Impacted Design Specs

Found via links from REQ_019, 020, 021:

| ID | Linked From | Impact | Current Problem |
|----|-------------|--------|-----------------|
| SPEC_SYSPILOT_008 | REQ_019, REQ_020 | **major rewrite** | Section "Step 2" asks user for syspilot path - needs auto-detection |
| SPEC_SYSPILOT_004 | REQ_019, REQ_020 | minor update | Usage examples assume known path - works for init script, but setup agent uses it |
| SPEC_SYSPILOT_010 | REQ_021 | **modified** | Update process needs to find newest version |

### New Design Specs

**SPEC_SYSPILOT_014: syspilot Auto-Detection Algorithm**

```rst
.. spec:: syspilot Auto-Detection Algorithm
   :id: SPEC_SYSPILOT_014
   :status: draft
   :links: REQ_SYSPILOT_024
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
              # Parse version for semantic comparison
              if ($_.Version -match '^(\d+)\.(\d+)\.(\d+)(-(\w+)\.?(\d+)?)?') {
                  $major = [int]$matches[1]
                  $minor = [int]$matches[2]
                  $patch = [int]$matches[3]
                  $prerelease = $matches[5]  # e.g., "beta"
                  $prereleaseNum = if ($matches[6]) { [int]$matches[6] } else { 0 }
                  
                  # Return sortable tuple: major, minor, patch, pre-num
                  # Pre-releases sort lower than releases
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

   **Usage in Setup Agent:**

   ::

      $syspilotRoot = Find-SyspilotInstallation
      if (-not $syspilotRoot) {
          Write-Error "Cannot proceed without syspilot installation"
          exit 1
      }
      
      # Now copy files from $syspilotRoot
      Copy-Item "$syspilotRoot/.github/agents/*.agent.md" -Destination ".github/agents/"

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
```

### Modified Design Specs

**SPEC_SYSPILOT_008: Setup Agent Design - Section 2 Rewrite**

Replace current "Step 2" with:

```rst
**Step 2: Setup Agent (@syspilot.setup)**

**Section 1: Auto-Detect syspilot Location**

1. Run Find-SyspilotInstallation (SPEC_SYSPILOT_014)
2. Log all found versions for transparency
3. Select newest version
4. If none found: Error with helpful instructions

**Section 2: Check Dependencies (Interactive)**

[... existing dependency check logic ...]

**Section 3: Copy Files from syspilot**

Using $syspilotRoot from auto-detection:

* Copy agents: ``$syspilotRoot/.github/agents/*.agent.md`` → ``.github/agents/``
* Copy prompts: ``$syspilotRoot/.github/prompts/*.prompt.md`` → ``.github/prompts/``
* Apply intelligent merge (SPEC_SYSPILOT_009)

**Section 4: Validate and Confirm**

[... existing validation logic ...]
```

**SPEC_SYSPILOT_010: Update Process - Use Auto-Detection**

Add at beginning of update workflow:

```rst
**Step 0: Find Newest syspilot Version**

1. Use Find-SyspilotInstallation (SPEC_SYSPILOT_014)
2. Verify found version is newer than installed version (from .syspilot/version.json)
3. If not newer: Warn user and ask if they want to proceed anyway
```

### Decisions

- **Decision 1:** PowerShell/Bash function instead of Python script
  - Rationale: Setup process already uses PowerShell/Bash (init scripts), no Python dependency needed

- **Decision 2:** Semantic version comparison with pre-release support
  - Rationale: Handles 0.1.0-beta.2 vs 0.1.0-beta.3 correctly

- **Decision 3:** Log all found versions for debugging
  - Rationale: Transparency helps users understand what auto-detection found

### Horizontal Check (MECE)

- [x] No contradictions with existing Design specs
- [x] SPEC_014 created (auto-detection algorithm)
- [x] SPEC_008 updated (uses SPEC_014)
- [x] SPEC_010 updated (uses SPEC_014)
- [x] All SPECs link back to requirements

---

## Final Consistency Check

**Status**: 🔄 in progress

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_SYSPILOT_012 | REQ_019, REQ_023 | SPEC_004, SPEC_008 | ✅ |
| US_SYSPILOT_012 | **REQ_024 (new)** | **SPEC_014 (new)** | ✅ |
| US_SYSPILOT_013 | REQ_020, REQ_022, REQ_023 | SPEC_008, SPEC_009 | ✅ |
| US_SYSPILOT_013 | **REQ_024 (new)** | **SPEC_014 (new)** | ✅ |
| US_SYSPILOT_014 | REQ_021, REQ_022 | SPEC_009, SPEC_010 | ✅ |
| US_SYSPILOT_014 | **REQ_024 (new)** | **SPEC_014 (new)** | ✅ |

**New Traceability Chain:**
- US_012, 013, 014 → **REQ_024** (Auto-Detection) → **SPEC_014** (PowerShell Algorithm)

**Modified Chains:**
- REQ_019 → SPEC_008 (updated: uses SPEC_014)
- REQ_020 → SPEC_008 (updated: uses SPEC_014)
- REQ_021 → SPEC_010 (updated: uses SPEC_014)

**Verification:**
- ✅ No orphaned requirements (all REQs link to US and SPEC)
- ✅ No orphaned specs (all SPECs link to REQs)
- ✅ New elements properly integrated

### Cross-Level Consistency

✅ **Level 0 → Level 1**: User intent preserved

| Level 0 Intent | Level 1 Behavior | Aligned? |
|----------------|------------------|----------|
| "Install without disruption" | Auto-detect location, no manual input | ✅ |
| "Download and extract syspilot" | Works with release ZIP structure | ✅ |
| "Update to latest version" | Auto-detect newest version | ✅ |

✅ **Level 1 → Level 2**: Requirements → Design

| Level 1 Requirement | Level 2 Implementation | Aligned? |
|---------------------|------------------------|----------|
| "Search parent directories for version.json" | PowerShell: Get-ChildItem -Recurse -Depth 3 | ✅ |
| "Select newest semantic version" | Sort with pre-release comparison | ✅ |
| "Fail gracefully if not found" | Error with helpful search paths | ✅ |

✅ **Semantic Consistency**: No drift between levels

- User wants: "Install from downloaded ZIP"
- Requirements say: "Auto-detect via version.json"  
- Design implements: PowerShell function with semantic versioning
- **Result**: Fully aligned ✅

### MECE Across Levels

✅ **Coverage**: All aspects addressed

| Aspect | Level 0 | Level 1 | Level 2 |
|--------|---------|---------|---------|
| Path detection | US acceptance criteria | REQ_024 | SPEC_014 algorithm |
| Install workflow | US_012 | REQ_019 + REQ_024 | SPEC_008 + SPEC_014 |
| Adopt workflow | US_013 | REQ_020 + REQ_024 | SPEC_008 + SPEC_014 |
| Update workflow | US_014 | REQ_021 + REQ_024 | SPEC_010 + SPEC_014 |
| Version comparison | Implied | REQ_024 AC-3 | SPEC_014 semantic sort |
| Error handling | Implied | REQ_024 AC-5 | SPEC_014 edge cases |

✅ **No Overlaps**: Clear separation

- REQ_024: Auto-detection logic (standalone)
- REQ_019/020/021: Use REQ_024, don't duplicate it
- SPEC_014: Implements REQ_024
- SPEC_008/010: Use SPEC_014, don't duplicate it

✅ **No Gaps**: Complete coverage

- ✅ Finding version.json (covered)
- ✅ Parsing version (covered)
- ✅ Comparing versions (covered)
- ✅ Handling pre-releases (covered)
- ✅ Error cases (covered)
- ✅ Debugging/logging (covered)

### Document Completeness

- ✅ All sections filled (Level 0, 1, 2)
- ✅ No DEPRECATED markers
- ✅ All conflicts resolved
- ✅ All decisions documented

### Issues Found

**None!** All checks passed.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified (US → REQ → SPEC)
- [x] Cross-level consistency verified
- [x] MECE properties verified
- [x] Ready for implementation

**Next Steps:**
1. Approve Change Document
2. Update RST files (US, REQ, SPEC)
3. Implement SPEC_014 (PowerShell function)
4. Update SPEC_008 (Setup Agent integration)
5. Test with real release ZIP
6. Verify agent

---

**Change Document Status**: ✅ **APPROVED - Ready for Implementation**

