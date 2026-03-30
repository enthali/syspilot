Release Design Specifications
==============================

This document contains design specifications for the syspilot release process.

**Document Version**: 0.1  
**Last Updated**: 2026-01-30


.. spec:: Version Number Format
   :id: SYSPILOT_SPEC_REL_VERSION_FORMAT
   :status: implemented
   :links: SYSPILOT_REQ_REL_SEMVER
   :tags: release, versioning

   **Design:**
   syspilot uses Semantic Versioning with structure stored in ``syspilot/version.json``.

   **Version Format:**

   * Pattern: ``MAJOR.MINOR.PATCH[-prerelease]``
   * MAJOR: Breaking changes (incompatible API/structure changes)
   * MINOR: New features (backward compatible)
   * PATCH: Bug fixes (backward compatible)
   * Pre-release suffixes: ``-alpha``, ``-beta``, ``-rc.N``

   **syspilot/version.json Structure:**
   
   .. code-block:: json

      {
          "version": "0.2.0"
      }

   Note: The ``installedAt`` and ``source`` fields only exist in consumer
   projects' ``.syspilot/version.json`` (see SYSPILOT_SPEC_INST_VERSION_MARKER).

   **Version Bump Rules:**

   * Breaking: User Stories/Requirements change behavior users depend on
   * Feature: New agents, new capabilities, enhanced workflows
   * Patch: Bug fixes, documentation updates, internal refactoring

   **Examples:**

   * ``0.1.0`` → ``0.2.0``: New release agent added (feature)
   * ``0.2.0`` → ``1.0.0``: Change agent API changes (breaking)
   * ``0.2.0`` → ``0.2.1``: Bug fix in init script (patch)


.. spec:: Git Tag Creation
   :id: SYSPILOT_SPEC_REL_GIT_TAG
   :status: implemented
   :links: SYSPILOT_REQ_REL_GITHUB_PUBLISH
   :tags: release, git, tagging

   **Design:**
   Releases are created via annotated Git tags that trigger GitHub Releases.

   **Tag Naming Convention:**

   * Format: ``vMAJOR.MINOR.PATCH`` (e.g., ``v0.2.0``)
   * Prefix ``v`` required by GitHub convention
   * Must match version in syspilot/version.json

   **Tag Creation Process:**
   
   .. code-block:: bash

      # 1. Update syspilot/version.json with new version
      # 2. Commit version.json change
      git add syspilot/version.json
      git commit -m "chore: bump version to 0.2.0"

      # 3. Create annotated tag
      git tag -a v0.2.0 -m "Release v0.2.0: Description"

      # 4. Push tag (triggers GitHub Actions if configured)
      git push origin v0.2.0

   **Tag Content:**

   * Annotated tag with release summary message
   * Points to commit where syspilot/version.json was updated
   * Triggers GitHub Actions workflow (if configured)

   **Validation:**

   * Tag version must match syspilot/version.json
   * All tests must pass on tagged commit
   * Documentation must build successfully


.. spec:: Release Notes Structure
   :id: SYSPILOT_SPEC_REL_NOTES_STRUCTURE
   :status: implemented
   :links: SYSPILOT_REQ_REL_NOTES, SYSPILOT_SPEC_DOC_RELEASE_NOTES_STRUCTURE
   :tags: release, documentation

   **Design:**
   Release notes follow structured markdown format with traceability.

   **Release Notes File:**

   * Location: ``docs/releasenotes.md``
   * Format: Markdown with newest releases at top
   * Generated from merged Change Documents

   **Release Notes Template:**

   .. code-block:: markdown

      # syspilot Release Notes

      ## v0.2.0 - 2026-01-30

      ### Summary
      [One paragraph describing the release, generated from Change Documents]

      ### ⚠️ Breaking Changes
      - [List breaking changes with migration guidance]
      - References: SYSPILOT_US_XXX, SYSPILOT_REQ_YYY

      ### ✨ New Features
      - [Feature description] (SYSPILOT_US_XXX, SYSPILOT_REQ_YYY)
      - [Feature description] (SYSPILOT_US_XXX, SYSPILOT_REQ_YYY)

      ### 🐛 Bug Fixes
      - [Fix description] (SYSPILOT_REQ_YYY)
      - [Fix description] (SYSPILOT_REQ_YYY)

      ### 📚 Documentation
      - [Doc updates]

      ### 🔧 Internal Changes
      - [Refactoring, cleanup]

      ---

      ## v0.1.0 - 2026-01-15
      ...

   **Generation Process:**

   1. Release agent reads merged Change Documents
   2. Extracts summaries, decisions, impacted elements
   3. Generates release note entry
   4. Appends to docs/releasenotes.md
   5. Commits: "chore: add release notes for vX.Y.Z"

   **Traceability:**

   * Each item references User Story or Requirement ID
   * Breaking changes include migration guidance
   * Links back to Change Documents (preserved in Git history)


.. spec:: Validation Checklist
   :id: SYSPILOT_SPEC_REL_VALIDATION_CHECKLIST
   :status: implemented
   :links: SYSPILOT_REQ_REL_VALIDATION, SYSPILOT_REQ_REL_DOC_BUILD, SYSPILOT_REQ_REL_AGENT_TEST, SYSPILOT_SPEC_REL_GITHUB_ACTIONS
   :tags: release, validation, quality

   **Design:**
   Pre-release validation ensures release quality through manual checklist.

   **Validation Checklist:**

   **Documentation:**

   * [ ] syspilot/version.json updated with new version
   * [ ] docs/releasenotes.md updated with release entry
   * [ ] All sphinx-needs links valid (sphinx-build succeeds)
   * [ ] No orphaned requirements or specs
   * [ ] Documentation builds without warnings
   * [ ] copilot-instructions.md up to date

   **Agents:**

   * [ ] All agent files parse correctly (no syntax errors)
   * [ ] Agent prompts reference correct tools
   * [ ] Setup agent tested in clean environment
   * [ ] Change agent tested with sample request

   **Scripts:**

   * [ ] Curl bootstrap command works (download setup agent from GitHub)
   * [ ] get_need_links.py executes correctly
   * [ ] Build scripts execute successfully

   **Git:**

   * [ ] All changes committed
   * [ ] Working directory clean
   * [ ] Branch up to date with main
   * [ ] All Change Documents merged or archived

   **Validation Execution:**

   * Manual checklist completed by maintainer before creating release tag
   * Release agent guides maintainer through checklist
   * Future: Automate via GitHub Actions (SYSPILOT_SPEC_REL_GITHUB_ACTIONS)

   **Manual Fallback Process:**

   If GitHub Actions fails or is unavailable:

   1. Run validation checklist manually
   2. Build docs locally: ``cd docs && sphinx-build -b html . _build/html``
   3. Verify no errors or broken links
   4. Create Git tag manually (see SYSPILOT_SPEC_REL_GIT_TAG)
   5. Create GitHub Release manually with release notes from docs/releasenotes.md


.. spec:: GitHub Actions Workflow
   :id: SYSPILOT_SPEC_REL_GITHUB_ACTIONS
   :status: implemented
   :links: SYSPILOT_REQ_REL_GITHUB_ACTIONS, SYSPILOT_REQ_REL_DOC_BUILD, SYSPILOT_REQ_REL_AGENT_TEST
   :tags: release, automation, ci-cd, github-actions

   **Design:**
   GitHub Actions automate validation, documentation build, and release publication.

   **Workflow File:** ``.github/workflows/release.yml``

   **Workflow Trigger:**

   * On: Push tags matching ``v*.*.*``
   * Manual: ``workflow_dispatch`` for testing

   **Workflow Steps:**

   1. **Checkout** - Clone repository at tag

      .. code-block:: yaml

         - uses: actions/checkout@v4

   2. **Setup Python** - Install Python 3.11+

      .. code-block:: yaml

         - uses: actions/setup-python@v5
           with:
             python-version: '3.11'

   3. **Install Dependencies** - Install Sphinx and sphinx-needs

      .. code-block:: yaml

         - run: pip install -r docs/requirements.txt

   4. **Validate version.json** - Ensure tag matches version file

      .. code-block:: yaml

         - run: |
             VERSION=$(jq -r .version syspilot/version.json)
             TAG=${GITHUB_REF#refs/tags/v}
             if [ "$VERSION" != "$TAG" ]; then
               echo "Version mismatch: syspilot/version.json=$VERSION tag=$TAG"
               exit 1
             fi

   5. **Build Documentation** - Run sphinx-build

      .. code-block:: yaml

         - run: |
             cd docs
             sphinx-build -b html . _build/html

   6. **Check Links** - Verify all sphinx-needs links valid

      .. code-block:: yaml

         - run: |
             if grep -r "WARNING" docs/_build/html/needs.json; then
               echo "Sphinx warnings found"
               exit 1
             fi

   7. **Deploy to GitHub Pages** - Publish HTML to gh-pages branch

      .. code-block:: yaml

         - uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

   8. **Create GitHub Release** - Publish with release notes

      .. code-block:: yaml

         - uses: softprops/action-gh-release@v1
           with:
             body_path: docs/releasenotes.md
             draft: false
             prerelease: false

   **Environment Variables:**

   * ``GITHUB_TOKEN``: Automatic (provided by GitHub)
   * No secrets required for basic workflow

   **Failure Handling:**

   * If any step fails, workflow stops
   * GitHub Release is not created
   * Maintainer investigates and re-tags after fix
   * Manual fallback available (see SYSPILOT_SPEC_REL_VALIDATION_CHECKLIST)


.. spec:: GitHub Pages Publishing
   :id: SYSPILOT_SPEC_REL_GITHUB_PAGES
   :status: implemented
   :links: SYSPILOT_REQ_REL_DOC_BUILD
   :tags: release, documentation, github-pages

   **Design:**
   Documentation is automatically published to GitHub Pages on release.

   **GitHub Pages Configuration:**

   * Source: ``gh-pages`` branch (created by Actions)
   * Path: ``/`` (root)
   * Custom domain: Optional (e.g., syspilot.dev)

   **Build Process:**
   
   .. code-block:: bash

      # Install dependencies
      pip install -r docs/requirements.txt
      
      # Build Sphinx documentation
      cd docs
      sphinx-build -b html . _build/html
      
      # Deploy to gh-pages branch
      # (handled by GitHub Actions peaceiris/actions-gh-pages)

   **Dependencies:**

   From ``docs/requirements.txt``:

   * Python 3.11+
   * sphinx >= 7.0.0
   * sphinx-needs >= 2.0.0
   * furo >= 2024.0.0
   * myst-parser >= 2.0.0
   * graphviz >= 0.20.0 (optional, for diagrams)

   **URL Structure:**

   * Format: ``https://<username>.github.io/<repo>/``
   * Example: ``https://yourorg.github.io/syspilot/``
   * Latest documentation always reflects latest release

   **Update Frequency:**

   * On every release tag push
   * Manual trigger available for testing

   **Initial Setup (one-time):**

   1. Enable GitHub Pages in repository settings
   2. Select source: Deploy from a branch
   3. Select branch: ``gh-pages`` / ``/ (root)``
   4. Wait for first release to create gh-pages branch


.. spec:: Release Agent Template
   :id: SYSPILOT_SPEC_REL_AGENT
   :status: implemented
   :links: SYSPILOT_REQ_REL_PROCESS_DOC, SYSPILOT_REQ_REL_NOTES, SYSPILOT_REQ_CHG_CHANGE_DOC
   :tags: release, agent, template

   **Design:**
   The release agent is a short, generic template. It does NOT prescribe
   individual release steps — LLMs know standard release procedures.
   Instead, it documents project-specific **design decisions**.

   **Agent File:** ``.github/agents/syspilot.release.agent.md``

   **Structure:**

   1. **Purpose** — One-liner: guide maintainer through releases
   2. **Release Decisions** — Project-specific config (see below)
   3. **Constraints** — What the agent must NOT do (e.g., no force-push)

   **Release Decisions Section:**

   Embedded in the agent file as a structured block:

   * **Version file**: Path and format (e.g., ``version.json``, ``pyproject.toml``)
   * **Change doc policy**: Archive location (e.g., ``docs/changes/archive/``)
   * **Validation commands**: Build/test commands to run before release
   * **Release notes**: Location and format
   * **Tag format**: Git tag convention (e.g., ``vX.Y.Z``)

   **Bootstrapping:**

   On first invocation without existing decisions:

   1. Agent detects empty/missing Release Decisions section
   2. Asks user project-specific questions
   3. Writes answers to the Release Decisions section in the agent file
   4. Proceeds with release

   **What the Agent Does NOT Include:**

   * Step-by-step release instructions
   * Shell commands or scripts
   * Platform-specific code
   * Detailed interaction examples


Release Workflow
----------------

.. spec:: Release Workflow Orchestration
   :id: SYSPILOT_SPEC_REL_WORKFLOW
   :status: implemented
   :links: SYSPILOT_REQ_WF_RELEASE_SEQUENCE, SYSPILOT_REQ_REL_SEMVER, SYSPILOT_REQ_REL_VALIDATION, SYSPILOT_REQ_REL_GITHUB_PUBLISH, SYSPILOT_SPEC_REL_AGENT
   :tags: workflow, release, orchestration

   **Design:**
   The release workflow bundles multiple merged changes into a versioned release.

   **Release Flow:**

   ::

      Merged Changes (on main)
          │
          ▼
      ┌─────────────────┐
      │  1. Version      │ ──→ Update syspilot/version.json, determine SemVer bump
      └─────────────────┘
          │
          ▼
      ┌─────────────────┐
      │  2. Validate     │ ──→ sphinx-build, agent tests, quality checks
      └─────────────────┘
          │
          ▼ (all pass)
      ┌─────────────────┐
      │  3. Publish      │ ──→ Git tag, GitHub Release, GitHub Pages
      └─────────────────┘
          │
          ▼
      ┌─────────────────┐
      │  change / end   │  (user decides)
      └─────────────────┘

   **Scope:**
   Unlike the change workflow (operates on one change), the release
   workflow operates across all changes since the last release.

   **Automation:**
   GitHub Actions automates steps 2 and 3 (see SYSPILOT_SPEC_REL_GITHUB_ACTIONS).
   Step 1 (version determination) requires maintainer judgment.


Traceability
------------

All traceability is automatically generated by Sphinx-Needs.

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('SYSPILOT_SPEC_REL')
