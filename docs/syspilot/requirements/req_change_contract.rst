Change Contract
===============

.. req:: Change Contract Process
   :id: SYSP_REQ_CHANGE_CONTRACT
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Processes/change.md

   Every modification to versioned source code or documentation shall use a
   Change Contract that:

   - is initialized on a branch named from the change according to the project's
     branching policy, using a tailored copy of the canonical template committed
     before the first responsibility transfer;
   - starts artifact work after user approval of the intent and observable
     outcome is recorded, or after the collaboration agreement's autonomous
     authority makes that checkpoint not applicable;
   - transfers first responsibility to the Architect to determine the required
     architecture and specification work;
   - identifies each applicable artifact, its owner, completion evidence, and
     current status;
   - lets each artifact owner determine the applicability and completeness of
     that owner's artifact;
   - uses the open applicable artifacts and their dependencies to determine
     which owner can progress next rather than prescribing an actor sequence;
   - records durable architecture and implementation decisions with their
     evidence, changed implementation artifacts and unit verification, and
     applicable acceptance-test results;
   - records Quality's current verification judgment and only currently open
     quality issues, with responsibility for correction transferred to the
     affected artifact's owner;
   - assigns validation of the observable outcome to the User after Quality can
     proceed, while allowing autonomous authority to make that validation not
     applicable without claiming that user validation occurred;
   - keeps unattended user checkpoints pending until the user returns; and
   - closes through the Project Manager only when all included artifacts have
     terminal status and completion evidence, Quality can proceed, the intended
     outcome is demonstrated, the user-validation disposition is explicit, and
     the integration state is recorded.

.. vc:: Change Contract exposes a complete outcome-driven change state
   :id: SYSP_VC_CHANGE_CONTRACT_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_CONTRACT

   Inspect the realized Change Process and confirm that it defines branch and
   contract initialization, collaboration-mode approval handling, first
   handoff to the Architect, owner-decided applicability, artifact status and
   evidence, autonomous later-owner selection, durable decisions, Quality
   verification, User validation, and checkable closure.