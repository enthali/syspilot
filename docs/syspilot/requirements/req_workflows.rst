Workflow Requirements
=====================

Requirements for the end-to-end workflows that orchestrate syspilot agents.

**Last Updated**: 2026-02-06


.. req:: Change Workflow Sequence
   :id: SYSPILOT_REQ_WF_CHANGE_SEQUENCE
   :status: implemented
   :priority: mandatory
   :tags: workflow, change, orchestration
   :links: SYSPILOT_US_WF_CHANGE, SYSPILOT_REQ_CHG_ANALYSIS_AGENT, SYSPILOT_REQ_CHG_IMPL_AGENT, SYSPILOT_REQ_CHG_VERIFY_AGENT, SYSPILOT_REQ_DX_MEMORY_AGENT

   **Description:**
   syspilot SHALL define a change workflow with the following sequence:

   1. **@change** — Analyze change request, create Change Document (US → REQ → SPEC)
   2. **@implement** — Execute approved changes from Change Document
   3. **@verify** — Validate implementation against Change Document
   4. **@memory** — Update project memory (copilot-instructions.md)

   After @memory completes, the user SHALL be offered to either start a new
   change workflow or proceed to a release.

   **Rationale:**
   A defined sequence ensures consistent change processing. Each step
   produces output that the next step consumes, creating a pipeline
   with clear handoff points. Documentation is maintained by the implement
   agent as part of its implementation artifacts. The exit point after
   @memory supports iterative development (multiple changes) before
   bundling into a release.

   **Acceptance Criteria:**

   * AC-1: Workflow sequence is documented and accessible to users and agents
   * AC-2: Each step's output serves as input to the next step
   * AC-3: Change Document is the shared artifact between @change and @implement
   * AC-4: @verify references the Change Document for completeness checks
   * AC-5: @memory runs after successful verification
   * AC-6: After @memory, the workflow offers two exit paths: start a new
     change workflow (@change) or proceed to release (@release)


.. req:: Independent Quality Check Workflow
   :id: SYSPILOT_REQ_WF_QUALITY_INDEPENDENT
   :status: implemented
   :priority: high
   :tags: workflow, quality, mece, trace
   :links: SYSPILOT_US_WF_QUALITY

   **Description:**
   syspilot SHALL support independent quality checks that can be invoked
   at any time without requiring a Change Document:

   * **@mece** — Horizontal consistency check on one specification level
   * **@trace** — Vertical traceability check for one element

   **Rationale:**
   Quality checks should be usable both during change processing
   (integrated) and as standalone tools (independent). This enables
   proactive quality management.

   **Acceptance Criteria:**

   * AC-1: @mece and @trace can be invoked without an active change workflow
   * AC-2: Quality check results are self-contained reports
   * AC-3: Quality findings can trigger a new change workflow
   * AC-4: Quality checks do not modify specifications (read-only)


.. req:: Release Workflow Sequence
   :id: SYSPILOT_REQ_WF_RELEASE_SEQUENCE
   :status: implemented
   :priority: mandatory
   :tags: workflow, release, orchestration
   :links: SYSPILOT_US_WF_RELEASE, SYSPILOT_REQ_REL_SEMVER, SYSPILOT_REQ_REL_VALIDATION, SYSPILOT_REQ_REL_GITHUB_PUBLISH

   **Description:**
   syspilot SHALL define a release workflow that bundles multiple changes:

   1. **Version** — Determine version number, update version.json
   2. **Validate** — Run documentation build, agent tests, quality checks
   3. **Publish** — Create Git tag, GitHub Release, publish documentation

   **Rationale:**
   A release aggregates multiple changes into a distributable version.
   Unlike the change workflow (per-change), the release workflow operates
   across changes.

   **Acceptance Criteria:**

   * AC-1: Release workflow operates on a set of merged changes (not single change)
   * AC-2: Version determination follows semantic versioning
   * AC-3: Validation gates block publication on failure
   * AC-4: Release workflow is documented as a reusable template
   * AC-5: After release publication, the workflow offers to start a new
     change workflow (@change) for continued development


.. req:: Branching Strategy
   :id: SYSPILOT_REQ_WF_BRANCHING_STRATEGY
   :status: implemented
   :priority: mandatory
   :tags: workflow, branching, git
   :links: SYSPILOT_US_WF_CHANGE

   **Description:**
   syspilot SHALL follow a defined branching strategy for all development work.

   **Rationale:**
   Consistent branch management keeps changes isolated, reviewable, and
   cleanly bundled into releases. Chaining feature branches preserves the
   incremental change history during multi-change development streams.

   **Acceptance Criteria:**

   * AC-1: New changes are made on dedicated ``feature/<name>`` branches
   * AC-2: Feature branches are created from the latest feature branch in the
     current development stream, not directly from main
   * AC-3: Main branch always equals the latest released version
   * AC-4: Changes are squash-merged to main only during the release workflow
   * AC-5: Agents creating branches SHALL default to branching from the current
     feature branch (not from main)


.. req:: Commit Message Conventions
   :id: SYSPILOT_REQ_WF_COMMIT_CONVENTIONS
   :status: implemented
   :priority: high
   :tags: workflow, git, conventions
   :links: SYSPILOT_US_WF_CHANGE

   **Description:**
   syspilot agents SHALL follow defined commit message conventions when
   creating commits as part of their workflow.

   **Rationale:**
   Consistent commit messages improve history readability, enable changelog
   generation, and make it clear which agent or workflow step produced each
   commit.

   **Acceptance Criteria:**

   * AC-1: Commit messages use ``<type>: <subject>`` format
   * AC-2: Type SHALL be one of: ``feat``, ``fix``, ``docs``, ``chore``,
     ``refactor``, ``test``, ``change``, ``verify``, ``memory``, ``specs``
   * AC-3: Subject is a concise description of the change in present tense
   * AC-4: Breaking changes are noted in the commit body with ``BREAKING CHANGE:``
   * AC-5: Commit messages reference the related issue or Change Document name
     where applicable (e.g., ``fix: resolve link errors (issue #9)``)


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('SYSPILOT_REQ_WF')
