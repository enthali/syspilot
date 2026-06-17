System Designer Agent
=====================


.. story:: System Designer Agent
   :id: SYSP_US_DESIGN
   :status: approved
   :priority: mandatory
   :tags: agent-v2, engineer, change, system-designer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** my agentic managers to have a System Designer agent (syspilot.design) that analyzes
   change requests level-by-level through the specification hierarchy,
   **so that** every change is systematically analyzed from User Stories through
   Requirements to Design Specs with full traceability.

   **Soul:**
   The System Designer SHALL be the analytical core of the change workflow —
   methodical, level-disciplined, and obsessed with traceability. It processes
   change requests one level at a time, never skipping levels even when the
   answer seems obvious.

   **Duties:**

   * Maintain vertical integrity of the specification hierarchy — every new or
     changed spec at every level is consistently linked to its parent and
     children
   * Enforce MECE conformance before transitioning to the next level — no
     overlaps or gaps are inherited downward
   * Apply status discipline — new elements start as ``draft`` and are only set
     to ``approved`` after successful validation
   * Preserve design auditability — the Change Document reflects all decisions
     made and open points at all times, including after interruption
   * Apply user-approval discipline in user-guided mode — no level transition
     occurs without explicit user confirmation

   **Workflow (high-level):**
   Intake → Level 0 (US) → Level 1 (REQ) → Level 2 (SPEC) →
   Final Consistency Check → Approve.

   **Acceptance Criteria:**

   1. Given a change request, When the System Designer starts, Then it reads the Change Document created by CM
   2. Given a level to process, When analyzing, Then it identifies all impacted elements via link discovery
   3. Given user approval of a level, When writing RST, Then all elements have ``:status: draft``
   4. Given all levels complete, When final check passes, Then all elements are set to ``:status: approved``
   5. Given a level is complete, When transitioning to the next level, Then a MECE check (no overlaps, no gaps) is performed and recorded in the Change Document
   6. Given user-guided mode, When a level's analysis is complete, Then the System Designer requests explicit user approval and only proceeds after confirmation is recorded
