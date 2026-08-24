Syspilot Tester
===============

.. req:: Tester Role
   :id: SYSP_REQ_TESTER
   :status: approved
   :implements: SYSP_US_TESTER
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Syspilot Tester.md

   The Syspilot Tester shall:

   - determine the applicability of acceptance testing assigned by the
     applicable process;
   - derive black-box scenarios from the observable outcome, stories,
     acceptance criteria, and requirements without relying on implementation
     details;
   - challenge normal behavior, boundaries, loopholes, and failure conditions;
     and
   - record reproducible results and surface unclear or inconsistent
     specifications to their owner.

.. vc:: Tester provides requirement-based black-box evidence
   :id: SYSP_VC_TESTER_1
   :status: approved
   :verifies: SYSP_REQ_TESTER

   Inspect the Tester role card and applicable acceptance-test evidence and
   confirm that scenarios trace to specified outcomes, avoid implementation
   knowledge, exercise adverse conditions, and record reproducible results.