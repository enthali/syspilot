Release Engineer Agent
======================


.. story:: Release Engineer Agent
   :id: SYSP_US_RELEASE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, release, release-engineer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** my agentic managers to have a Release Engineer agent (syspilot.release) that guides
   the release process from version bump through validation to tagging,
   **so that** releases are consistent, validated, and properly documented
   with archived change documents and release notes.

   **Context:**

   The Release Engineer handles the end-to-end release process: squash merge
   to main, version bump, validation (sphinx-build), release notes generation,
   change document archival, and Git tagging. It reads project-specific release
   decisions (version file location, tag format, etc.) from its configuration.

   **Acceptance Criteria:**

   1. Given completed changes on development, When releasing, Then the Release Engineer prepares on development and squash-merges to main
   2. Given a version bump, When applying, Then it follows semantic versioning (MAJOR.MINOR.PATCH)
   3. Given validation, When sphinx-build runs, Then no errors or warnings
   4. Given a release, When complete, Then change documents are archived and release notes updated
