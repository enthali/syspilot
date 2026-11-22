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
   - record a current ``proceed`` or ``blocked`` judgment;
   - review the commands and results that artifact owners recorded, executing
     a check itself only when a recorded result cannot support its judgment,
     and record the reason; and
   - keep only currently open quality issues, with each required correction
     returned to the owner of the affected artifact.

.. vc:: Quality records an independent current judgment
   :id: SYSP_VC_QUALITY_1
   :status: approved
   :verifies: SYSP_REQ_QUALITY

   A completed review records an independent holistic ``proceed`` or ``blocked``
   judgment and only current issues, each with a correction and artifact owner.

.. vc:: Quality records both required review methods
   :id: SYSP_VC_QUALITY_2
   :status: approved
   :verifies: SYSP_REQ_QUALITY

   For impacted objects, review evidence records horizontal coverage and
   relationship analyses with scope, evidence, findings and limits.

.. vc:: Quality reviews existing verification before executing checks
   :id: SYSP_VC_QUALITY_3
   :status: approved
   :verifies: SYSP_REQ_QUALITY

   Recorded commands and results support the judgment; each check executed
   by Quality has a recorded reason why existing evidence was insufficient.