Release Requirements
====================

This document contains requirements for the syspilot release process.

**Document Version**: 0.1  
**Last Updated**: 2026-01-30


.. req:: Semantic Versioning
   :id: REQ_RELEASE_001
   :status: implemented
   :priority: mandatory
   :tags: release, versioning
   :links: US_SYSPILOT_015

   **Description:**
   syspilot SHALL use Semantic Versioning (MAJOR.MINOR.PATCH) for all releases.

   **Rationale:**
   Semantic Versioning communicates compatibility and scope of changes
   clearly to users. GitHub Releases convention uses SemVer.

   **Acceptance Criteria:**

   * AC-1: Version numbers follow MAJOR.MINOR.PATCH format
   * AC-2: MAJOR increments indicate breaking changes
   * AC-3: MINOR increments indicate new features (backward compatible)
   * AC-4: PATCH increments indicate bug fixes
   * AC-5: Pre-release versions use suffixes (-beta, -alpha, -rc.1)
   * AC-6: Version is stored in version.json


.. req:: GitHub Release Publication
   :id: REQ_RELEASE_002
   :status: implemented
   :priority: mandatory
   :tags: release, distribution, github
   :links: US_SYSPILOT_015

   **Description:**
   syspilot SHALL publish releases via GitHub Releases.

   **Rationale:**
   GitHub Releases provides versioned distribution, release notes,
   and asset downloads in a standard platform.

   **Acceptance Criteria:**

   * AC-1: Each release creates a Git tag with version number
   * AC-2: Release includes release notes describing changes
   * AC-3: GitHub automatically creates .zip and .tar.gz archives
   * AC-4: Users can view release history on GitHub
   * AC-5: Latest release is clearly marked


.. req:: Release Notes Generation
   :id: REQ_RELEASE_003
   :status: approved
   :priority: mandatory
   :tags: release, documentation
   :links: US_SYSPILOT_015

   **Description:**
   syspilot SHALL generate release notes for each version.

   **Rationale:**
   Release notes communicate what changed to users and help them
   decide whether to update.

   **Acceptance Criteria:**

   * AC-1: Release notes list new features
   * AC-2: Release notes list bug fixes
   * AC-3: Release notes list breaking changes
   * AC-4: Release notes reference User Stories/Requirements where applicable
   * AC-5: Release notes include migration guidance for breaking changes
   * AC-6: Release notes stored in docs/releasenotes.md


.. req:: Pre-Release Validation
   :id: REQ_RELEASE_004
   :status: implemented
   :priority: mandatory
   :tags: release, quality, validation
   :links: US_SYSPILOT_016

   **Description:**
   syspilot SHALL validate releases before publication.

   **Rationale:**
   Pre-release validation prevents distributing broken releases
   and maintains user trust.

   **Acceptance Criteria:**

   * AC-1: All validation checks must pass before release
   * AC-2: Validation failure blocks release publication
   * AC-3: Validation report shows which checks failed
   * AC-4: Maintainer can review validation results before approving


.. req:: Documentation Build Verification
   :id: REQ_RELEASE_005
   :status: implemented
   :priority: mandatory
   :tags: release, validation, documentation
   :links: US_SYSPILOT_016

   **Description:**
   syspilot SHALL verify documentation builds successfully before release.

   **Rationale:**
   Broken documentation prevents users from understanding and using
   the system correctly.

   **Acceptance Criteria:**

   * AC-1: Sphinx build completes without errors
   * AC-2: All sphinx-needs links are valid
   * AC-3: No orphaned requirements or design elements
   * AC-4: Documentation is published to GitHub Pages


.. req:: Agent Functionality Testing
   :id: REQ_RELEASE_006
   :status: implemented
   :priority: mandatory
   :tags: release, validation, agents
   :links: US_SYSPILOT_016

   **Description:**
   syspilot SHALL verify agent functionality before release.

   **Rationale:**
   Agents are the primary user interface for syspilot.
   Non-functional agents render the system unusable.

   **Acceptance Criteria:**

   * AC-1: All agent definition files parse correctly
   * AC-2: Agent prompts contain no syntax errors
   * AC-3: Critical agent workflows are tested (setup, change, implement)
   * AC-4: Agent dependencies (scripts, templates) are verified


.. req:: GitHub Actions Automation
   :id: REQ_RELEASE_007
   :status: implemented
   :priority: high
   :tags: release, automation, ci-cd
   :links: US_SYSPILOT_015, US_SYSPILOT_016

   **Description:**
   syspilot SHOULD automate release validation and publication via GitHub Actions.

   **Rationale:**
   Automation reduces human error, ensures consistency, and
   speeds up the release process.

   **Acceptance Criteria:**

   * AC-1: GitHub Action validates releases on version tags
   * AC-2: GitHub Action builds documentation
   * AC-3: GitHub Action runs validation checks
   * AC-4: GitHub Action publishes to GitHub Releases on success
   * AC-5: GitHub Action publishes documentation to GitHub Pages
   * AC-6: GitHub Action can be triggered manually for testing


.. req:: Release Process Documentation
   :id: REQ_RELEASE_008
   :status: implemented
   :priority: medium
   :tags: release, documentation, template
   :links: US_SYSPILOT_017

   **Description:**
   syspilot SHALL document the release process as a template for users.

   **Rationale:**
   Documenting syspilot's own release process provides a working
   example that users can adapt for their projects.

   **Acceptance Criteria:**

   * AC-1: Release process documented in sphinx-needs format
   * AC-2: Documentation includes manual and automated approaches
   * AC-3: Documentation explains how to customize for user projects
   * AC-4: Release agent concept is documented (even if not fully automated)


Traceability
------------

All traceability is automatically generated by Sphinx-Needs.

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_RELEASE')
