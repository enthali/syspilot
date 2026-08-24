Syspilot Quality
================

.. story:: Syspilot Quality
   :id: SYSP_US_QUALITY
   :status: approved
   :priority: mandatory
   :tags: actor, quality, review
   :tracked_by: ROOT_SYSPILOT

   **As** a stakeholder deciding whether syspilot work may proceed,
   **I want** an independent Quality actor to judge the complete current
   outcome,
   **so that** unresolved issues are visible and acceptance is based on
   coherent evidence rather than the confidence of artifact producers.

.. ac:: Independent quality judgment gates validation
   :id: SYSP_AC_QUALITY_1
   :status: approved
   :validates: SYSP_US_QUALITY

   Given the included change artifacts and their completion evidence,
   When Quality reviews the current outcome,
   Then it records either a ``proceed`` judgment with no open quality issue or
   a ``blocked`` judgment with each required correction assigned to its
   artifact owner.