Syspilot Release
================

.. req:: Release Role
   :id: SYSP_REQ_RELEASE
   :status: approved
   :implements: SYSP_US_RELEASE
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Syspilot Release.md

   The Syspilot Release actor shall:

   - own packaging and release delivery assigned by the applicable process;
   - own release preflight verification and release-facing user
     documentation;
   - collaborate with artifact owners until release inputs satisfy their
     declared completion conditions; and
   - preserve completeness and verification without trading them for delivery
     pressure.

.. vc:: Release delivers a complete verified package
   :id: SYSP_VC_RELEASE_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE

   Inspect the Release role card and completed release evidence and confirm
   that packaging, preflight verification, user documentation, unresolved
   inputs, and delivery outcome are explicit.