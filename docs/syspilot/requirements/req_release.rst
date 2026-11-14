Release
=======

.. req:: Release Role
   :id: SYSP_REQ_RELEASE
   :status: approved
   :implements: SYSP_US_RELEASE
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Release.md

   The Release actor shall:

   - own packaging and release delivery assigned by the applicable process;
   - own release preflight verification and the release notes, the one
     release-facing document;
   - check the Technical Writer's terminal documentation row for guides,
     portal and ownership map, leaving their authorship with that owner;
   - own what the release gate must check and publish, namely preflight
     content, the release run, and tag authorization, and decide as mandatory
     consultee whether a change to a release workflow definition is
     acceptable, while Admin owns that definition as tooling;
   - collaborate with artifact owners until release inputs satisfy their
     declared completion conditions; and
   - preserve completeness and verification without trading them for delivery
     pressure.

.. vc:: Release delivers a complete verified package
   :id: SYSP_VC_RELEASE_1
   :status: approved
   :verifies: SYSP_REQ_RELEASE

   Release evidence identifies packaging, preflight, release notes, unresolved
   inputs and delivery outcome. No unresolved required input is traded for
   delivery pressure.

.. vc:: Release preserves documentation ownership
   :id: SYSP_VC_RELEASE_2
   :status: approved
   :verifies: SYSP_REQ_RELEASE

   The role card and release record assign notes to Release and other
   user-facing documentation to Technical Writer, with its terminal row checked.

.. vc:: Release decides gate changes without owning workflow wiring
   :id: SYSP_VC_RELEASE_3
   :status: approved
   :verifies: SYSP_REQ_RELEASE

   A workflow change records Release's consultation and gate decision;
   workflow tooling remains Admin's.