Contract Documents
==================

.. story:: Contract Documents
   :id: SYSP_US_CONTRACT_DOCUMENTS
   :status: approved
   :priority: mandatory
   :tags: process, contract, collaboration
   :tracked_by: ROOT_SYSPILOT

   **As** a participant in a syspilot process,
   **I want** one durable Contract Document to express the currently valid
   agreement, responsibility, evidence, and outcome of a process instance,
   **so that** participants can collaborate autonomously while the work remains
   understandable, inspectable, and closable without reconstructing its history
   from conversations or an actor's internal reasoning.

   **Context:**

   Contract Documents provide a common method for process-specific agreements.
   They preserve the state and evidence that remain relevant to the outcome;
   version control preserves how that state evolved.

.. ac:: Participants can determine the valid process state
   :id: SYSP_AC_CONTRACT_DOCUMENTS_1
   :status: approved
   :validates: SYSP_US_CONTRACT_DOCUMENTS

   Given participants inspect a Contract Document during or after a process,
   When they determine what is valid, who must act, and whether the process can
   close,
   Then they can do so from the current document and its referenced evidence
   without reconstructing prior conversations or internal reasoning.
