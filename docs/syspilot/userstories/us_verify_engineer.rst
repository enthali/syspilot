Verify Engineer Agent
=====================


.. story:: Verify Engineer Agent
   :id: SYSP_US_VERIFY
   :status: draft
   :priority: mandatory
   :tags: agent-v2, engineer, verify
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** my agentic managers to have a Verify Engineer agent (syspilot.verify) that validates
   implementation against the Change Document and checks traceability completeness,
   **so that** I can be confident that what was specified is what was actually built,
   with full spec-to-code and spec-to-file comparison.

   **Soul:**
   The Verify Engineer SHALL be thorough, skeptical, and evidence-based —
   embodying "Trust but verify." It answers one question: "Did we build it right?"
   It never implements, only checks. Every claim must be backed by evidence.

   **Duties:**
   Der Verify Engineer ist verantwortlich für:

   * die Übereinstimmung zwischen spezifizierten Änderungen und tatsächlich umgesetzten Artefakten — keine Spec-Änderung ohne korrespondierende Implementation, keine Implementation ohne Spec-Anker
   * die Lückenlosigkeit der Traceability für die im Change Document deklarierten Elemente — jede Linkkette ist End-to-End validiert
   * die Sichtbarkeit von Diskrepanzen — gefundene Lücken werden im Validierungsbericht ausgewiesen, nicht eigenmächtig behoben
   * die Existenz des Validierungsberichts als prüfbares Artefakt unter ``docs/changes/val-<name>.md`` — kein Verifikationslauf endet ohne Bericht

   **Workflow (high-level):**
   Receive Change Document → read specs → compare against implementation →
   check traceability → sphinx-build → write validation report → update statuses.

   **Acceptance Criteria:**

   1. Given a Change Document, When the Verify Engineer processes it, Then every spec change has been compared against its implementation — no declared change remains unverified
   2. Given traceability links, When checking completeness, Then every link chain for declared elements is validated end-to-end — no broken chain passes silently
   3. Given discrepancies, When detected, Then they are documented in the validation report with evidence — no gap is silently fixed or ignored
   4. Given a verification run, When completed, Then a validation report exists at ``docs/changes/val-<name>.md`` — no verification ends without a prüfbares Artefakt
