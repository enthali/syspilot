Quality Review Methods
======================

.. story:: Apply Named Quality Review Methods
   :id: SYSP_US_QUALITY_METHODS
   :status: approved
   :priority: mandatory
   :tags: quality, skill, review, method
   :tracked_by: ROOT_SYSPILOT

   **As** a stakeholder relying on a quality judgment,
   **I want** every Quality Review to apply named, inspectable analysis
   methods to the objects the applicable Contract records as impacted,
   **so that** the judgment rests on reproducible evidence rather than on an
   undefined instruction to review holistically.

   **Context:**

   Two methods answer different questions. Horizontal coverage analysis
   compares an object with its comparable peers and exposes overlap,
   duplication, contradiction, and missing coverage. Relationship analysis
   follows an object's declared relationships and exposes invalid, missing,
   or semantically inconsistent connections. Both methods report findings to
   the applicable Contract, which retains scope and decision authority.

.. ac:: Both review methods produce inspectable evidence
   :id: SYSP_AC_QUALITY_METHODS_1
   :status: approved
   :validates: SYSP_US_QUALITY_METHODS

   Given an applicable Contract records the impacted objects of a change,
   When Quality reviews the current outcome,
   Then it applies horizontal coverage analysis and relationship analysis to
   those objects, and records the examined peer set, the examined relationship
   neighborhood, the resulting findings, and the limits of both analyses in
   that Contract.
