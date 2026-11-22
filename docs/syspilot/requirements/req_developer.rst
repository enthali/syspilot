Developer
=========

.. req:: Developer Role
   :id: SYSP_REQ_DEVELOPER
   :status: approved
   :implements: SYSP_US_DEVELOPER
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Developer.md

   The Developer shall:

   - own implementation and unit verification assigned by the applicable
     process;
   - realize the approved specification in maintainable product artifacts;
   - write and run focused automated unit tests that show the implementation
     behaves as intended, and record their commands and results; and
   - surface simpler approaches, specification conflicts, and material
     implementation improvements to the responsible owner.

.. vc:: Developer provides a verified realization
   :id: SYSP_VC_DEVELOPER_1
   :status: approved
   :verifies: SYSP_REQ_DEVELOPER

   Completed implementation evidence identifies changed files and realization
   decisions, and records the Developer's unit-test commands and results.

.. vc:: Developer surfaces decisions outside implementation authority
   :id: SYSP_VC_DEVELOPER_2
   :status: approved
   :verifies: SYSP_REQ_DEVELOPER

   The role card and implementation evidence leave specification conflicts,
   simpler alternatives and material improvements with the responsible owner.