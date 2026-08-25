Change Contract
===============

.. req:: Change Contract Process
   :id: SYSP_REQ_CHANGE_CONTRACT
   :status: approved
   :implements: SYSP_US_CHANGE_CONTRACT
   :specializes: SYSP_REQ_CONTRACT_HANDLING
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
   - includes user-facing documentation as an optional artifact owned by the
     Technical Writer when a change must add or update derived explanations,
     with completion evidence covering the agreed documentation surface,
     coherent user-oriented structure, relevant factual-owner review, updated
     ``doc`` Needs and ``includes`` links, and a clean documentation build;
   - uses incoming ``included_in`` links on changed requirements to identify
     documentation surfaces that require Technical Writer impact review;
   - distinguishes user-facing documentation from authoritative textual product
     artifacts by purpose and authority rather than by path or file format;
   - records durable architecture and implementation decisions with their
     evidence, changed implementation artifacts and unit verification, and
     applicable acceptance-test results;
   - records Quality's current verification judgment and only currently open
     quality issues, with responsibility for correction transferred to the
     affected artifact's owner;
   - requires Quality to communicate its ``proceed`` judgment and supporting
     evidence directly to the Project Manager before the outcome is presented
     for validation, without accepting another actor's forwarded claim as
     evidence of Quality's decision;
   - assigns validation of the observable outcome to the User after Quality can
     proceed, while allowing autonomous authority to make that validation not
     applicable without claiming that user validation occurred;
   - requires the User to communicate an applicable validation decision
     directly to the Project Manager before it is recorded, without accepting
     another actor's forwarded claim as evidence of the User's decision;
   - keeps unattended user checkpoints pending until the user returns; and
   - closes through the Project Manager only when all included artifacts have
     terminal status and completion evidence, Quality can proceed, the intended
     outcome is demonstrated, the user-validation disposition is explicit, and
     the integration state is recorded.

.. vc:: Change Contract exposes a complete outcome-driven change state
   :id: SYSP_VC_CHANGE_CONTRACT_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_CONTRACT

   Inspect the realized Change Process and confirm that its compact pre-template
   content defines applicability, branch and Contract initialization,
   collaboration-mode approval handling, tailoring, and the first handoff to
   the Architect without repeating generic Contract-handling rules; and that
   the canonical template retains owner-decided applicability, artifact status,
   direct Quality and User decision provenance, autonomous and unattended
   validation handling, evidence, and checkable Closure for every included
   artifact.