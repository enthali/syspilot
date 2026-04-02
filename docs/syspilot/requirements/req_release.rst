Release Requirements
====================

This document contains requirements for the syspilot release process.

**Document Version**: 0.1  
**Last Updated**: 2026-01-30


.. req:: Semantic Versioning
   :id: SYSPILOT_REQ_REL_SEMVER
   :status: implemented
   :priority: mandatory
   :tags: release, versioning
   :links: SYSPILOT_US_REL_CREATE

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
   :id: SYSPILOT_REQ_REL_GITHUB_PUBLISH
   :status: implemented
   :priority: mandatory
   :tags: release, distribution, github
   :links: SYSPILOT_US_REL_CREATE

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
   :id: SYSPILOT_REQ_REL_NOTES
   :status: approved
   :priority: mandatory
   :tags: release, documentation
   :links: SYSPILOT_US_REL_CREATE, SYSPILOT_REQ_DOC_RELEASE_NOTES

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


.. req:: Pre-Release Validation
   :id: SYSPILOT_REQ_REL_VALIDATION
   :status: implemented
   :priority: mandatory
   :tags: release, quality, validation
   :links: SYSPILOT_US_REL_VALIDATE

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
   :id: SYSPILOT_REQ_REL_DOC_BUILD
   :status: implemented
   :priority: mandatory
   :tags: release, validation, documentation
   :links: SYSPILOT_US_REL_VALIDATE, SYSPILOT_REQ_CORE_SPHINX_NEEDS

   **Description:**
   syspilot SHALL verify documentation builds successfully before release.

   **Rationale:**
   Broken documentation prevents users from understanding and using
   the system correctly.

   **Acceptance Criteria:**

   * AC-1: Sphinx build completes without errors
   * AC-2: All sphinx-needs links are valid
   * AC-3: No orphaned requirements or design elements


.. req:: Agent Functionality Testing
   :id: SYSPILOT_REQ_REL_AGENT_TEST
   :status: implemented
   :priority: mandatory
   :tags: release, validation, agents
   :links: SYSPILOT_US_REL_VALIDATE

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
   :id: SYSPILOT_REQ_REL_GITHUB_ACTIONS
   :status: implemented
   :priority: high
   :tags: release, automation, ci-cd
   :links: SYSPILOT_US_REL_CREATE, SYSPILOT_US_REL_VALIDATE, SYSPILOT_REQ_REL_VALIDATION, SYSPILOT_REQ_REL_DOC_BUILD, SYSPILOT_REQ_REL_AGENT_TEST, SYSPILOT_REQ_REL_GITHUB_PUBLISH

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


.. req:: Release Agent KISS Template
   :id: SYSPILOT_REQ_REL_PROCESS_DOC
   :status: implemented
   :priority: medium
   :tags: release, agent, template
   :links: SYSPILOT_US_REL_AGENT_TEMPLATE

   **Description:**
   syspilot SHALL provide a release agent template that is short, generic,
   and focuses on project-specific design decisions rather than prescribing
   every release step.

   **Rationale:**
   LLMs know how to perform standard release tasks (version bump, tagging,
   release notes). The agent only needs to document project-specific decisions
   to guide the LLM.

   **Acceptance Criteria:**

   * AC-1: Release agent template contains a "Release Decisions" section for project-specific configuration
   * AC-2: Decisions are stored in the agent file itself (no separate config file)
   * AC-3: On first invocation without existing decisions, the agent bootstraps by asking the user
   * AC-4: Agent does not prescribe individual release steps (LLM handles standard release flow)
   * AC-5: Template is usable for any project, not syspilot-specific


Traceability
------------

All traceability is automatically generated by Sphinx-Needs.

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('SYSPILOT_REQ_REL')
