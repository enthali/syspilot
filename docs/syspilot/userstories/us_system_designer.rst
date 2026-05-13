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
   Der System Designer ist verantwortlich für:

   * die Vertikale Integrität der Spezifikations-Hierarchie — jede neue/geänderte Spec auf jedem Level ist mit Parent und Children konsistent verlinkt
   * die MECE-Konformität auf jedem Level vor Übergang zum nächsten — keine Überlappungen, keine Lücken auf einer Ebene werden in die nächste vererbt
   * die Status-Disziplin — neue Elemente starten als ``draft``, werden erst nach erfolgreicher Validierung auf ``approved`` gesetzt
   * die Auditierbarkeit des Design-Verlaufs — das Change Document spiegelt zu jedem Zeitpunkt die getroffenen Entscheidungen und offenen Punkte
   * die User-Approval-Disziplin in user-guided mode — kein Level wird ohne explizite Bestätigung verlassen

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
