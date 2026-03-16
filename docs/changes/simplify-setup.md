# Change Document: simplify-setup

**Status**: approved
**Branch**: feature/simplify-setup
**Created**: 2026-03-16
**Author**: Change Agent

---

## Summary

Simplify syspilot installation and update to use direct curl/fetch from GitHub main instead of local init scripts and auto-detection. Move version.json into templates/ so the templates directory becomes the complete release package. Replace the complex auto-detect + local-copy workflow with a lightweight curl-based approach. Replace backup/rollback update mechanism with intelligent AI-driven 3-way merge using a stored installed-version marker.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| US_INST_BOOTSTRAP | Automatic Environment Bootstrap | modified | AC1: "run init script" → "curl setup agent and invoke it" |
| US_INST_NEW_PROJECT | Install syspilot in New Project | modified | AC2: auto-detect → curl from GitHub main |
| US_INST_ADOPT_EXISTING | Adopt syspilot in Existing Project | modified | AC4: auto-detect → curl from GitHub main |
| US_INST_UPDATE | Update syspilot to Latest Version | no change | ACs remain semantically correct, mechanism changes at lower levels |

### Unchanged User Stories (checked, no impact)

- US_INST_CROSS_PROJECT: Still valid, simpler delivery mechanism
- US_INST_AGNOSTIC: Skeleton approach unchanged
- US_DOC_MAINTAIN: Doc process independent of install mechanism

### Decisions

- Decision 1: version.json moves into templates/ — templates/ becomes the complete release package
- Decision 2: No file hashes for change detection — agent compares files directly when needed
- Decision 3: Init scripts (init.ps1, init.sh) are completely removed — curl replaces them
- Decision 4: US_INST_BOOTSTRAP stays as separate US — unique CI/CD situation

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] No documentation impact at US level

---

## Level 1: Requirements

**Status**: ✅ completed

### Removed Requirements

| ID | Title | Rationale |
|----|-------|-----------|
| REQ_INST_AUTO_DETECT | Auto-Detection of syspilot Installation | Obsolete — no local syspilot copy, everything via curl from GitHub |

### Modified Requirements

| ID | Title | Changes |
|----|-------|---------|
| REQ_INST_AUTO_SETUP | Automatic Environment Setup | Remove init script reference, setup agent handles deps after curl |
| REQ_INST_NEW_PROJECT | New Project Installation | AC4/5: auto-detect → curl from GitHub; remove REQ_INST_AUTO_DETECT link |
| REQ_INST_ADOPT_EXISTING | Existing Project Adoption | AC5/6: auto-detect → curl from GitHub; remove REQ_INST_AUTO_DETECT link |
| REQ_INST_VERSION_UPDATE | Version Update and Migration | AC1/5: auto-detect → compare local marker with GitHub main; remove REQ_INST_AUTO_DETECT link |
| REQ_INST_GITHUB_RELEASES | syspilot Distribution via GitHub Releases | Primary channel = curl from main raw files; ZIP/tar.gz remain as convenience |
| REQ_INST_TEMPLATE_SOURCE | Template-First Distribution | version.json becomes part of templates/ |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| REQ_INST_VERSION_MARKER | Installation Version Tracking | US_INST_UPDATE | mandatory |

> syspilot SHALL store the installed version in the target project so that the update process can determine the currently installed version.

### Decisions

- Decision 1: REQ_INST_AUTO_DETECT removed — curl replaces local auto-detection
- Decision 2: REQ_INST_VERSION_MARKER new — explicit REQ for installed version tracking (location decided at L2)
- Decision 3: version.json moves into templates/ (REQ_INST_TEMPLATE_SOURCE)
- Decision 4: No L1 doc impact — SPEC_INST_INIT_SCRIPTS references in doc-scope SPECs are L2 content-source refs, not formal links

### Horizontal Check (MECE)

- [x] No contradictions with remaining Requirements
- [x] REQ_INST_AUTO_DETECT removal: all referencing REQs updated
- [x] REQ_INST_VERSION_MARKER fills gap from auto-detect removal
- [x] No redundancies

---

## Level 2: Design

**Status**: ✅ completed

### Removed SPECs

| ID | Title | Rationale |
|----|-------|-----------|
| SPEC_INST_INIT_SCRIPTS | Init Scripts for Environment Setup | Curl replaces init scripts entirely |
| SPEC_INST_AUTO_DETECT | syspilot Auto-Detection Algorithm | No local syspilot repo, everything via curl |

### New SPECs

#### SPEC_INST_CURL_BOOTSTRAP: Curl-Based Bootstrap

```rst
.. spec:: Curl-Based Bootstrap
   :id: SPEC_INST_CURL_BOOTSTRAP
   :status: draft
   :links: REQ_INST_AUTO_SETUP, REQ_INST_NEW_PROJECT, REQ_INST_ADOPT_EXISTING
   :tags: init, install, curl

   **Design:**
   Users bootstrap syspilot by downloading the Setup Agent directly from
   GitHub using curl (Unix) or Invoke-WebRequest (Windows).

   **Bootstrap Steps:**

   1. Create agent directory: ``mkdir -p .github/agents/``
   2. Download Setup Agent from GitHub main:

      ::

         # Unix
         curl -o .github/agents/syspilot.setup.agent.md \
           https://raw.githubusercontent.com/OWNER/syspilot/main/templates/agents/syspilot.setup.agent.md

         # Windows (PowerShell)
         Invoke-WebRequest -Uri "https://raw.githubusercontent.com/OWNER/syspilot/main/templates/agents/syspilot.setup.agent.md" `
           -OutFile ".github/agents/syspilot.setup.agent.md"

   3. Open VS Code, start GitHub Copilot Chat, invoke ``@syspilot.setup``

   **Rationale:**

   * No local syspilot repository needed
   * Platform-independent (curl/Invoke-WebRequest available everywhere)
   * Always fetches current version from main
   * Single command instead of finding and running init scripts
```

#### SPEC_INST_VERSION_MARKER: Installed Version Marker

```rst
.. spec:: Installed Version Marker
   :id: SPEC_INST_VERSION_MARKER
   :status: draft
   :links: REQ_INST_VERSION_MARKER, REQ_INST_VERSION_UPDATE
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

   * ``version``: Semantic version that was installed
   * ``installedAt``: ISO date of installation/last update
   * ``source``: GitHub repository URL (supports forks)

   **Usage:**

   * Update process compares local version with ``templates/version.json`` on GitHub main
   * No hash tracking — agent compares files directly when needed

   **Rationale:**

   * Minimal file, no overhead
   * Sufficient for version comparison
   * ``source`` field enables forks and custom repos
   * ``.syspilot/`` directory serves as config home for future extensions
```

### Modified SPECs

#### SPEC_INST_SETUP_AGENT: Setup Agent Design (major rewrite)

```rst
   **Design:**
   Installation is curl-based: user downloads setup agent, then runs it.

   **Step 1: Bootstrap (manual)**

   * User curls setup agent from GitHub (SPEC_INST_CURL_BOOTSTRAP)
   * No init scripts, no local syspilot repo needed

   **Step 2: Setup Agent (@syspilot.setup)**

   **Section 1: Determine Mode**

   1. Check if ``.syspilot/version.json`` exists
   2. If yes → UPDATE MODE (Section 7 / SPEC_INST_UPDATE_PROCESS)
   3. If no → FRESH INSTALL (continue with Section 2)

   **Section 2: Check Dependencies (Interactive)**

   (unchanged — same interactive Python/Sphinx dependency flow)

   **Section 3: Fetch Files from GitHub**

   1. Fetch ``templates/version.json`` from GitHub main → determine version
   2. Use GitHub API to list ``templates/`` contents:
      ``api.github.com/repos/OWNER/syspilot/contents/templates/``
   3. Download and copy:

      * ``templates/agents/*.agent.md`` → ``.github/agents/``
      * ``templates/prompts/*.prompt.md`` → ``.github/prompts/``
      * ``templates/skills/*.skill.md`` → ``.github/skills/``
      * ``templates/scripts/python/`` → ``.syspilot/scripts/python/``
      * ``templates/sphinx/`` → ``docs/`` (build.ps1, build.sh)
      * ``templates/change-document.md`` → ``.syspilot/templates/``
      * ``templates/version.json`` → ``.syspilot/version.json`` (with installedAt added)

   4. Apply intelligent merge for existing projects (SPEC_INST_FILE_OWNERSHIP)

   **Section 4: Validate and Confirm**

   * Validate successful ``sphinx-build``
   * Confirm success

   **Section 5: Hand off to Documentation Agent**

   After file copy and validation, hand off to @doc (init mode).
```

#### SPEC_INST_UPDATE_PROCESS: Update Process (major rewrite)

```rst
   **Design:**
   Update is agent-driven with curl from GitHub and intelligent merge.

   **Step 0: Check for Updates**

   1. Fetch ``templates/version.json`` from GitHub main
   2. Compare with local ``.syspilot/version.json``
   3. If remote version > local version → proceed
   4. If remote version <= local version → inform user, abort

   **Step 1: Fetch New Files**

   * Download all files from ``templates/`` on GitHub main

   **Step 2: Intelligent Merge (per file)**

   For each file:

   * Agent reads local file and new file
   * If identical → skip
   * If different → Agent merges intelligently, asks user on conflicts

   **Step 3: Update Version Marker**

   * Update ``.syspilot/version.json`` with new version and date

   **Rationale:**

   * No backup/rollback mechanism needed — Git is the backup
   * AI agent handles merge intelligently, no programmatic diff needed
   * Simple and reliable
```

#### SPEC_INST_FILE_OWNERSHIP: File Layout and Ownership (modified)

Changes:
- Remove ``.syspilot/**`` as "replaceable" category (was full repo copy)
- Add ``.syspilot/version.json`` as syspilot-managed
- ``.syspilot/scripts/`` as syspilot-managed (replaceable)

#### SPEC_INST_RELEASE_STRUCTURE: Release Structure (modified)

Changes:
- ``version.json`` moves from repo root to ``templates/version.json``
- Remove ``scripts/`` from directory tree (init scripts gone)
- Remove "copied to project's ``.syspilot/version.json``" (now created by setup agent)
- Update directory listing accordingly

#### SPEC_INST_TEMPLATE_LAYOUT: Template Directory Layout (modified)

Changes:
- Add ``version.json`` to template directory listing
- Mapping: ``templates/version.json`` → ``.syspilot/version.json``

#### SPEC_DOC_README_STRUCTURE: README Chapter Structure (modified)

Changes:
- Ch.2 "Quick Start": Content Source ``SPEC_INST_INIT_SCRIPTS`` → ``SPEC_INST_CURL_BOOTSTRAP``

#### SPEC_DOC_INDEX_STRUCTURE: docs/index.rst Chapter Structure (modified)

Changes:
- Ch.2 "Getting Started": Content Source ``SPEC_INST_INIT_SCRIPTS, SPEC_INST_SETUP_AGENT`` → ``SPEC_INST_CURL_BOOTSTRAP, SPEC_INST_SETUP_AGENT``

#### SPEC_REL_VALIDATION_CHECKLIST: Validation Checklist (modified)

Changes:
- Remove checkbox: "init.ps1 / init.sh work on target platforms"
- Add checkbox: "curl bootstrap command works (download setup agent from GitHub)"

#### SPEC_INST_SELF_INSTALL: Release Self-Install Validation (modified)

Changes:
- Step 1: "Run Setup Agent's copy logic" now includes fetching from templates/ and creating .syspilot/version.json
- Add: Verify .syspilot/version.json is created with correct version

### Decisions

- Decision 1: .syspilot/ as config directory (version marker, scripts, templates)
- Decision 2: Root scripts/ folder removed entirely (init scripts gone, get_need_links.py lives in templates/)
- Decision 3: SPEC_INST_SELF_INSTALL updated to validate new curl-based flow
- Decision 4: Git is the backup — no backup/rollback mechanism in update process

### Horizontal Check (MECE)

- [x] All SPEC_INST_INIT_SCRIPTS references cleaned up (setup, doc-scope, release)
- [x] All SPEC_INST_AUTO_DETECT references cleaned up (setup, update)
- [x] New SPECs (CURL_BOOTSTRAP, VERSION_MARKER) cover the gaps
- [x] Doc-scope content source references updated
- [x] Release validation checklist updated

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| US_INST_BOOTSTRAP (mod) | REQ_INST_AUTO_SETUP (mod) | SPEC_INST_CURL_BOOTSTRAP (new) | ✅ |
| US_INST_NEW_PROJECT (mod) | REQ_INST_NEW_PROJECT (mod) | SPEC_INST_SETUP_AGENT (mod) | ✅ |
| US_INST_ADOPT_EXISTING (mod) | REQ_INST_ADOPT_EXISTING (mod) | SPEC_INST_SETUP_AGENT (mod) | ✅ |
| US_INST_UPDATE (no change) | REQ_INST_VERSION_UPDATE (mod) | SPEC_INST_UPDATE_PROCESS (mod) | ✅ |
| US_INST_UPDATE (no change) | REQ_INST_VERSION_MARKER (new) | SPEC_INST_VERSION_MARKER (new) | ✅ |
| — | REQ_INST_GITHUB_RELEASES (mod) | SPEC_INST_RELEASE_STRUCTURE (mod) | ✅ |
| — | REQ_INST_TEMPLATE_SOURCE (mod) | SPEC_INST_TEMPLATE_LAYOUT (mod) | ✅ |

### Removed Elements (clean removal)

| Removed | Referenced By (updated) |
|---------|------------------------|
| REQ_INST_AUTO_DETECT | REQ_INST_NEW_PROJECT, REQ_INST_ADOPT_EXISTING, REQ_INST_VERSION_UPDATE |
| SPEC_INST_INIT_SCRIPTS | SPEC_INST_SETUP_AGENT, SPEC_DOC_README_STRUCTURE, SPEC_DOC_INDEX_STRUCTURE |
| SPEC_INST_AUTO_DETECT | SPEC_INST_SETUP_AGENT, SPEC_INST_UPDATE_PROCESS |

### Cross-Level Consistency

- ✅ US intent (simpler install) → REQ behavior (curl-based, no auto-detect) → SPEC implementation (curl bootstrap, version marker, AI merge)
- ✅ No semantic drift between levels
- ✅ All removals tracked and referencing elements updated

### Side-Effect Changes (no L0/L1 impact, L2 only)

- SPEC_DOC_README_STRUCTURE: content source reference updated
- SPEC_DOC_INDEX_STRUCTURE: content source reference updated
- SPEC_REL_VALIDATION_CHECKLIST: init script checkbox → curl checkbox
- SPEC_INST_SELF_INSTALL: validation steps updated
- SPEC_INST_FILE_OWNERSHIP: .syspilot/ redefined as config dir
