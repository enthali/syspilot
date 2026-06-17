Quality Engineer Schema Check
==============================


.. story:: Schema Validation for Specification Files
   :id: SYSP_US_SCHEMA
   :status: draft
   :priority: mandatory
   :tags: agent-v2, quality, schema, validation
   :links: SYSP_US_AGENT_ARCH, SYSP_US_QM

   **As a** syspilot user,
   **I want** the Quality Manager to validate that all specification files
   conform to the sphinx-needs schema (required fields, valid status values,
   correct ID prefixes, and consistent link separators),
   **so that** structural defects in spec files are caught before they
   silently corrupt traceability or cause sphinx-build failures.

   **Context:**

   The syspilot specification hierarchy uses sphinx-needs directives with
   mandatory fields (``id``, ``status``, ``priority``, ``tags``, ``links``).
   Structural violations — missing fields, non-standard status values, wrong
   ID prefixes, mixed link separators — are not always caught by sphinx-build
   and can silently break traceability queries, need filters, and impact
   analysis.

   A Schema Check complements MECE (horizontal consistency) and Trace
   (vertical linkage) by verifying the structural correctness of each
   individual need item against the defined field schema.

   The QM's mandatory check trio is: MECE + Trace + Schema. All three
   must run in every full audit.

   **Acceptance Criteria:**

   1. Given a full quality audit, When QM executes checks, Then a Schema check
      runs alongside MECE and Trace — it is never omitted
   2. Given a specification file, When the Schema check runs, Then every need
      item is verified for: presence of ``id``, ``status``, ``priority``,
      ``tags``, and ``links`` fields
   3. Given a need with a non-standard ``status`` value, When detected, Then
      the Schema check flags it as a finding
   4. Given a need with an ID that does not match the expected prefix pattern
      (SYSP_US_*, SYSP_REQ_*, SYSP_SPEC_*), When detected, Then it is flagged
   5. Given a need with mixed link separators (semicolons vs. commas), When
      detected, Then it is flagged with a recommendation to use commas
