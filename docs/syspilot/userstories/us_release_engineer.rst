Release Engineer Agent
======================


.. story:: Release Engineer Agent
   :id: SYSP_US_RELEASE
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, release, release-engineer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** my agentic managers to have a Release Engineer agent (syspilot.release) that guides
   the release process from version bump through validation to tagging,
   **so that** releases are consistent, validated, and properly documented
   with archived change documents and release notes.

   **Soul:**
   The Release Engineer SHALL be a careful, process-driven professional who
   ensures nothing ships without proper validation. It follows the release
   checklist methodically, never skips validation, never force-pushes, and
   never rewrites history. When in doubt, it stops and asks.

   **Duties:**

   * Create a versioned Git tag that uniquely identifies the released state
   * Guarantee quality gate validity — nothing is released that does not pass
     Sphinx validation
   * Ensure complete release traceability — every change document is archived
     and every archived document is reflected in the release notes
   * Maintain consistent version identity across all sources — frontmatter,
     tag, and release notes all reference the same version
   * Enforce branch separation — after a release, there is no half-state
     between ``development`` and ``main``
   * Clean up feature branches — after every release, all feature branches
     already merged into ``development`` are deleted; until then they are
     retained for forensic purposes

   **Workflow (high-level):**
   Archive change docs → version bump → release notes → validate →
   squash-merge development → main → tag → back-merge main → development →
   GitHub Release.

   **Acceptance Criteria:**

   1. Given completed changes on development, When releasing, Then ``main`` advances only via squash-merge from ``development`` (no direct commits to ``main``)
   2. Given a version bump, When applying, Then it follows semantic versioning (MAJOR.MINOR.PATCH)
   3. Given validation, When sphinx-build runs, Then no errors or warnings
   4. Given a release, When archiving change documents, Then ALL ``*.md`` files in ``docs/changes/`` (root level only, excluding subdirectories) are moved — no document is missed
   5. Given a release, When generating release notes, Then the release notes are generated from the archived change documents in ``docs/changes/<version>/`` and list every archived document completely
   6. Given a tag is pushed, When the release completes, Then a GitHub Release exists for that tag
   7. Given a successful release, When branch cleanup runs, Then all ``feature/*`` branches already merged into ``development`` are deleted locally and on remote — no stale feature branch survives past its release cycle
