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

   - is initialized on a feature branch that the Syspilot Project Manager
     creates from the change name, using a tailored copy of the canonical
     template committed before the first responsibility transfer;
   - carries an ``Operation Mode`` field in its canonical template that offers
     ``user-guided (default) | autonomous | unattended`` together with the
     complete behavioral rule for each of the three modes, so that an actor
     reads the rule governing its work inside the Contract it is executing
     rather than in another document;
   - retains exactly one selected mode and its rule in a concrete Contract,
     because initialization removes the template note and the two
     non-applicable mode rules;
   - requires, in ``unattended`` mode, that an actor which cannot reach the User
     records ``USER REVIEW REQUIRED`` in the Contract, chooses the simplest
     path that is cheapest to reverse or amend, and keeps the change moving,
     while the Project Manager reviews the flagged points once the User is
     reachable and decision ownership stays with the actor that decided;
   - agrees the selected mode with the User before the Contract is released;
   - records the User's release exactly once, in a User-owned gate named
     ``Contract release`` holding ``pending`` or ``approved``, which no other
     actor may set, so that an approved intent text no longer also asserts the
     authorization to start;
   - describes each tailoring option at the field, row, or section where that
     choice is made, stating the reason to record and the edit or delete
     instruction to follow there, and carries no separate list of
     process-specific tailoring rules;
   - offers no omission option on a required element, so that an element the
     process always needs cannot be tailored away;
   - starts artifact work only after the ``Contract release`` gate reads
     ``approved``, and admits no alternative start condition; a settled intent
     text does not authorize starting, and the operation mode governs how
     actors work within the released scope rather than whether release is
     required;
   - transfers first responsibility to the Architect to determine the required
     architecture and specification work;
   - identifies each applicable artifact, its owner, completion evidence, and
     current status;
   - includes version control as one artifact owned by the Syspilot Project
     Manager, whose completion evidence is the Change's branch name together
     with its integration state, and whose status is ``active`` while the
     branch carries the work and ``merged`` once that branch has been
     squash-integrated into ``development``;
   - records the branch name only in that artifact row, so a Change states its
     branch in exactly one place and no preamble field repeats it;
   - expresses a Change that requires no branch through the artifact table's
     ``Included`` column rather than through a special branch value;
   - limits that version-control authority to creating the Change's branch and
     squash-integrating it into ``development``, and excludes promotion of
     ``development`` to ``main``, which is release publication owned by the
     Syspilot Release actor within a Release Contract;
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
   - records the review methods Quality applied, with their selected scope,
     evidence, findings, and stated limits;
   - requires Quality to communicate its ``proceed`` judgment and supporting
     evidence directly to the Project Manager before the outcome is presented
     for validation, without accepting another actor's forwarded claim as
     evidence of Quality's decision;
   - assigns validation of the observable outcome to the User after Quality can
     proceed, and makes that validation ``not applicable`` only when an explicit
     User delegation is recorded at the validation row itself; the operation
     mode never delegates it, and no Contract may claim that user validation
     occurred when it did not;
   - requires the User to communicate an applicable validation decision
     directly to the Project Manager before it is recorded, without accepting
     another actor's forwarded claim as evidence of the User's decision;
   - keeps ``unattended`` user checkpoints pending until the user returns; and
   - closes through the Project Manager only when all included artifacts and
     gates have terminal status and completion evidence, Quality can proceed,
     the intended outcome is demonstrated, the user-validation disposition is
     explicit, and the integration state is recorded.

   All actors share one working tree, so a branch switch changes state for every
   actor at once. Branch creation and integration therefore stay with the single
   actor that holds responsibility at exactly those two moments. Because
   ``merged`` is a terminal status, the existing closure condition that every
   included artifact or gate carries a terminal status already enforces
   integration, and no separate integration rule is required.

.. vc:: Change Contract exposes a complete outcome-driven change state
   :id: SYSP_VC_CHANGE_CONTRACT_1
   :status: approved
   :verifies: SYSP_REQ_CHANGE_CONTRACT

   Inspect the realized Change Process and confirm that its compact pre-template
   content defines applicability, branch and Contract initialization, operation
   mode selection, and the first handoff to the Architect without repeating
   generic Contract-handling rules, and that it contains no separate list of
   process-specific tailoring rules; and that
   the canonical template retains owner-decided applicability, artifact status,
   direct Quality and User decision provenance, evidence, and checkable Closure
   for every included artifact or gate. Confirm that the template's Quality Review section provides
   explicit fields for the applied review methods and their selected scope,
   evidence, findings, and limits. Confirm that the template carries a
   Project Manager-owned version-control artifact using the ``active`` and
   ``merged`` statuses, that the branch name appears only in that row and in no
   preamble field, that a Change needing no branch is expressed through
   ``Included`` rather than a special branch value, and that no surface grants
   promotion of ``development`` to ``main`` as part of that authority. Confirm
   that the template's ``Operation Mode`` field offers
   ``user-guided (default) | autonomous | unattended`` and carries the complete
   rule for all three modes, that a concrete Contract retains exactly one mode
   and its rule with the template note removed, that no surface sends the reader
   to another document for the governing rule, that the
   artifact table carries a User-owned ``Contract release`` gate, and that the
   User's release appears in no other section. Confirm that every start path in
   the realized process requires that gate to read ``approved`` and that no
   surface offers an alternative start condition based on intent approval or on
   the operation mode. Confirm that every optional element states its own
   omission option with the reason to record and the edit or delete instruction
   at that element, that no required element offers such an option, and that
   the ``User validation and approval`` row becomes ``not applicable`` only
   through an explicit User delegation recorded at that row rather than through
   the operation mode.