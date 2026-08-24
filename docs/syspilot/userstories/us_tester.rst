Syspilot Tester
===============

.. story:: Syspilot Tester
   :id: SYSP_US_TESTER
   :status: approved
   :priority: mandatory
   :tags: actor, acceptance, testing
   :tracked_by: ROOT_SYSPILOT

   **As** a stakeholder evaluating a syspilot change,
   **I want** a Tester to challenge the specified behavior independently of
   its implementation,
   **so that** loopholes, edge cases, and unclear requirements are exposed
   before the outcome is accepted.

.. ac:: Specified behavior is tested independently
   :id: SYSP_AC_TESTER_1
   :status: approved
   :validates: SYSP_US_TESTER

   Given a change with an observable outcome and specification,
   When acceptance testing is applicable,
   Then black-box scenarios challenge the required behavior without relying on
   implementation knowledge and record reproducible results.