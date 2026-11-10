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
   - own packaging and release delivery assigned by the applicable process;
   - own release preflight verification and the release notes, the one
     release-facing document, while the user-facing documentation, meaning the
     guides, the project portal, and the documentation ownership map, stays
     with the Technical Writer and Release ensures its completeness for a
     release through that owner's terminal artifact row and not by writing it;
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

   Inspect the Release role card and completed release evidence and confirm
   that packaging, preflight verification, release notes, unresolved
   inputs, and delivery outcome are explicit, that the user-facing
   documentation of the release is recorded as the Technical Writer's
   artifact and not as Release's, and that a change to a release
   workflow definition records Release's consultation and decision.