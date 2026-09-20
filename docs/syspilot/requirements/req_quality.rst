Quality
=======

.. req:: Quality Role
   :id: SYSP_REQ_QUALITY
   :status: approved
   :implements: SYSP_US_QUALITY
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Quality.md

   The Quality actor shall:

   - independently review all applicable artifacts and evidence without
     producing the artifacts it judges;
   - evaluate the current outcome holistically against its intent,
     specifications, verification, and process contract;
   - apply horizontal coverage analysis and relationship analysis to the
     objects the applicable Contract records as impacted, and record the
     selected scope, evidence, findings, and limits of both methods;
   - record a current ``proceed`` or ``blocked`` judgment; and
   - keep only currently open quality issues, with each required correction
     returned to the owner of the affected artifact.

.. vc:: Quality records an independent current judgment
   :id: SYSP_VC_QUALITY_1
   :status: approved
   :verifies: SYSP_REQ_QUALITY

   Inspect the Quality role card and a completed quality artifact and confirm
   that the judgment covers all applicable evidence, remains independent, and
   contains either no open issue or an actionable correction for each issue.
   Confirm that the role card states the obligation to apply horizontal
   coverage analysis and relationship analysis, and that the quality artifact
   records both analyses with their selected scope, evidence, findings, and
   stated limits.