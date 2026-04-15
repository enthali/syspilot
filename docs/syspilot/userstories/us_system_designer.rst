System Designer Agent
=====================


.. story:: System Designer Agent
   :id: SYSP_US_DESIGN
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, change, system-designer
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want to** have a System Designer agent (syspilot.design) that analyzes
   change requests level-by-level through the specification hierarchy,
   **so that** every change is systematically analyzed from User Stories through
   Requirements to Design Specs with full traceability.

   **Context:**

   The System Designer is the analytical core of the change workflow. It processes
   change requests iteratively: Level 0 (User Stories) → Level 1 (Requirements) →
   Level 2 (Design Specs). At each level it identifies impacted elements, proposes
   new/modified specs, runs horizontal MECE checks, and writes RST files after
   approval. It maintains a persistent Change Document as decision log.

   **Acceptance Criteria:**

   1. Given a change request, When the System Designer starts, Then it creates a Change Document
   2. Given a level to process, When analyzing, Then it identifies all impacted elements via link discovery
   3. Given user approval of a level, When writing RST, Then all elements have ``:status: draft``
   4. Given all levels complete, When final check passes, Then all elements are set to ``:status: approved``
