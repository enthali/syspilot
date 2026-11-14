Contract Documents
==================

.. req:: Contract Document Method
   :id: SYSP_REQ_CONTRACT_DOCUMENTS
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   The Contract Document method shall require each process to declare its
   applicability, canonical/instance locations, artifact types, ownership,
   completion evidence, initial/closure responsibility and closure conditions.

.. vc:: Contract method declares a checkable process
   :id: SYSP_VC_CONTRACT_DOCUMENTS_1
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_DOCUMENTS

   Every process declaration identifies the required fields and a checkable
   closure condition.

.. req:: Contract Current State And Evidence
   :id: SYSP_REQ_CONTRACT_STATE
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   A Contract shall retain durable current state and outcome, replacing resolved
   findings, blockers and assumptions. Inspectable artifacts, verification
   results and approvals shall evidence that outcome. Only the Handover log
   specified in ``SYSP_REQ_CONTRACT_LOG`` may accumulate intermediate state.

.. vc:: Contract state has only one bounded log exception
   :id: SYSP_VC_CONTRACT_DOCUMENTS_2
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_STATE

   Findings, blockers and assumptions are replaced in place; only transfer
   lines accumulate.

.. vc:: Contract outcome has inspectable evidence
   :id: SYSP_VC_CONTRACT_DOCUMENTS_9
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_STATE

   Artifacts, verification results and approvals support the recorded outcome,
   rather than a reconstruction of intermediate events.

.. req:: Contract Handover Log
   :id: SYSP_REQ_CONTRACT_LOG
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_STATE
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   The single append-only Handover log shall record every transfer as one
   ``Date | Time | From | To | Note`` line, appended as the last act before
   transfer in the header-changing commit. Date/time shall come from the
   system clock as ``YYYY-MM-DD`` and 24-hour local ``HH:MM``.
   The note shall state completed work and facts affecting the next owner's
   situation; evidence shall remain in the owner's section and work in open
   rows. The log shall retain no other resolved intermediate state and shall
   not override the authoritative ``Current responsibility`` header.

.. vc:: Handover log entries have committed clock provenance
   :id: SYSP_VC_CONTRACT_DOCUMENTS_10
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_LOG

   Each transfer line has the defined fields and clock-derived timestamp in
   the header-changing commit, appended last before transfer.

.. vc:: Handover notes retain only transition context
   :id: SYSP_VC_CONTRACT_DOCUMENTS_11
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_LOG

   Notes state completed work and the next owner's situation, leaving evidence
   and work in their sections/rows; neither other resolved state nor competing
   responsibility authority accumulates in the log.

.. req:: Contract Responsibility Transfer
   :id: SYSP_REQ_CONTRACT_RESPONSIBILITY
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   Temporary Contract responsibility shall preserve durable artifact ownership.
   A transfer shall commit owned work and Contract state consistently before
   handing responsibility to the next logical included owner able to progress
   the Contract.

.. vc:: Contract transfer preserves artifact authority
   :id: SYSP_VC_CONTRACT_DOCUMENTS_12
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_RESPONSIBILITY

   A consistent commit precedes transfer to an included owner able to progress;
   durable artifact ownership does not change with the header.

.. req:: Contract Single Ownership Statement
   :id: SYSP_REQ_CONTRACT_OWNERSHIP
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   An instance shall state each included artifact's owner only in its artifact
   table, with no second declaration in section headings or process prose.

.. vc:: Contract ownership has one authority source
   :id: SYSP_VC_CONTRACT_DOCUMENTS_3
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_OWNERSHIP

   Each included artifact has one owner declaration, in the artifact table.

.. req:: Contract Gate Authority
   :id: SYSP_REQ_CONTRACT_GATES
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   Every gate recorded alongside Contract artifacts shall have exactly one
   owner, who alone may set it.

.. vc:: Contract gates are set only by their owners
   :id: SYSP_VC_CONTRACT_DOCUMENTS_13
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_GATES

   Each gate has one recorded owner; gate decisions come from that owner.

.. req:: Contract Scope Widening
   :id: SYSP_REQ_CONTRACT_SCOPE
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   Widening approved intent shall return it to ``draft`` until reapproved.
   Each affected terminal-row owner shall reopen its row or record why the
   existing evidence still holds, with this rule at the intent/artifact boundary.

.. vc:: Contract scope widening reopens affected evidence
   :id: SYSP_VC_CONTRACT_DOCUMENTS_4
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_SCOPE

   A widened intent is ``draft`` until reapproved; every affected terminal
   artifact is reopened or its owner records why existing evidence still holds.

.. req:: Contract Point-Of-Use Tailoring
   :id: SYSP_REQ_CONTRACT_TAILORING
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   Each tailoring option shall carry its editing instruction at the point of
   use, without a central tailoring list.

.. vc:: Contract tailoring stays local
   :id: SYSP_VC_CONTRACT_DOCUMENTS_5
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_TAILORING

   Tailoring choices carry their editing instruction at the
   point of use, without a central list.

.. req:: Contract Shared-Rule Inheritance
   :id: SYSP_REQ_CONTRACT_INHERITANCE
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   Every registered Contract kind, including examples and later kinds, shall
   carry five shared rules in its template, adapted to its structure:
   ``SYSP_REQ_CONTRACT_LOG``, ``SYSP_REQ_CONTRACT_SCOPE``,
   ``SYSP_REQ_CONTRACT_OWNERSHIP``, ``SYSP_REQ_CONTRACT_PRESENTATION`` and
   ``SYSP_REQ_CONTRACT_REFRESH``. The method shall list these rules once.

.. vc:: Every registered Contract kind carries the shared rules
   :id: SYSP_VC_CONTRACT_DOCUMENTS_6
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_INHERITANCE

   A registry-based requirement check detects any missing shared rule in a
   process/example template, including structurally adapted kinds; the method's
   shared-rule list occurs once.

.. req:: Contract Composition Boundary
   :id: SYSP_REQ_CONTRACT_COMPOSITION
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   Multiple goals shall share one responsibility, release, validation and
   integration boundary as a composition invariant, not a tailoring choice.

.. vc:: Contract composition has one common boundary
   :id: SYSP_VC_CONTRACT_DOCUMENTS_7
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_COMPOSITION

   Multiple goals share responsibility, release, validation and integration;
   the method does not authorize composition across those boundaries.

.. req:: Contract Mode Definition Boundary
   :id: SYSP_REQ_CONTRACT_MODES
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   Collaboration and operation modes shall be defined by individual processes,
   not the Contract Document method.

.. vc:: Operation modes belong to individual processes
   :id: SYSP_VC_CONTRACT_DOCUMENTS_8
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_MODES

   The method defines no collaboration or operation mode; individual processes
   define their own applicable choices.

.. req:: Contract Presentation At User Gates
   :id: SYSP_REQ_CONTRACT_PRESENTATION
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   The actor requesting a User-owned gate shall present the Contract to the
   User in that same step.

.. vc:: User gate requests present the governing Contract
   :id: SYSP_VC_CONTRACT_DOCUMENTS_14
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_PRESENTATION

   The gate request and Contract presentation occur in one step.

.. req:: Contract Receiver Refresh
   :id: SYSP_REQ_CONTRACT_REFRESH
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   A receiver shall refresh its context, role card and Contract and verify
   committed ``Current responsibility`` before acknowledgement.

.. vc:: Contract acknowledgement follows refreshed authority
   :id: SYSP_VC_CONTRACT_DOCUMENTS_15
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_REFRESH

   Refresh and committed-header verification precede the receiver's acknowledgement.
