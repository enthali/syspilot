Workflow Requirements
=====================

Requirements for the end-to-end workflows that orchestrate syspilot agents.

**Last Updated**: 2026-02-06


.. req:: Change Workflow Sequence
   :id: REQ_WF_CHANGE_SEQUENCE
   :status: implemented
   :priority: mandatory
   :tags: workflow, change, orchestration
   :links: US_WF_CHANGE, REQ_CHG_ANALYSIS_AGENT, REQ_CHG_IMPL_AGENT, REQ_CHG_VERIFY_AGENT, REQ_DX_MEMORY_AGENT

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
   with clear handoff points. The exit point after @memory supports
   iterative development (multiple changes) before bundling into a release.

   **Acceptance Criteria:**

   * AC-1: Workflow sequence is documented and accessible to users and agents
   * AC-2: Each step's output serves as input to the next step
   * AC-3: Change Document is the shared artifact between @change and @implement
   * AC-4: @verify references the Change Document for completeness checks
   * AC-5: @memory runs after successful verification
   * AC-6: After @memory, the workflow offers two exit paths: start a new
     change workflow (@change) or proceed to release (@release)


.. req:: Independent Quality Check Workflow
   :id: REQ_WF_QUALITY_INDEPENDENT
   :status: implemented
   :priority: high
   :tags: workflow, quality, mece, trace
   :links: US_WF_QUALITY

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
   :id: REQ_WF_RELEASE_SEQUENCE
   :status: implemented
   :priority: mandatory
   :tags: workflow, release, orchestration
   :links: US_WF_RELEASE

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


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_WF')
