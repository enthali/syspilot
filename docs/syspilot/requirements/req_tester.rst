Tester
======

.. req:: Tester Role
   :id: SYSP_REQ_TESTER
   :status: approved
   :implements: SYSP_US_TESTER
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Tester.md

   The Tester shall:

   - determine the applicability of acceptance testing assigned by the
     applicable process;
   - derive black-box scenarios from the observable outcome, stories,
     acceptance criteria, and requirements without relying on implementation
     details;
   - write and run requirement tests from those scenarios, provide the means
     for User validation, and record commands and results;
   - challenge normal behavior, boundaries, loopholes, and failure conditions;
     and
   - record reproducible results and surface unclear or inconsistent
     specifications to their owner.

.. vc:: Tester provides requirement-based black-box evidence
   :id: SYSP_VC_TESTER_1
   :status: approved
   :verifies: SYSP_REQ_TESTER

   Acceptance scenarios trace to specified outcomes, cover normal, boundary
   and adverse cases, and require no implementation knowledge.

.. vc:: Tester delivers reproducible validation support
   :id: SYSP_VC_TESTER_2
   :status: approved
   :verifies: SYSP_REQ_TESTER

   Applicable test evidence records the Tester's commands and results, the
   reproducible outcome and means for User validation.

.. vc:: Tester returns specification questions to their owner
   :id: SYSP_VC_TESTER_3
   :status: approved
   :verifies: SYSP_REQ_TESTER

   Unclear or inconsistent specifications have explicit questions for their
   owner rather than unowned assumptions in the test result.