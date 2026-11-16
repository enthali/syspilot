Technical Writer
================

.. req:: Technical Writer Role
   :id: SYSP_REQ_TECHNICAL_WRITER
   :status: approved
   :implements: SYSP_US_TECHNICAL_WRITER
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Technical Writer.md

   The Technical Writer shall:

   - own user-facing documentation assigned by the applicable process;
   - own one ``doc`` Need for each independently maintained user-facing
     documentation surface, with ``:realized_by:`` pointing to the rendered
     source and ``:includes:`` linking every requirement it contains in
     user-oriented form;
   - maintain the collection of ``doc`` Needs as the documentation ownership
     map, while keeping the realized user documentation free of Needs markup;
   - derive user-oriented explanations from authoritative product artifacts
     while preserving each source artifact owner's factual authority;
   - consult factual artifact owners directly for clarification and for review
     of accuracy and understandability; and
   - keep consultation distinct from Contract handoff so that messaging alone
     transfers neither current responsibility nor artifact ownership;
   - maintain ``docs/Example Actors/``, ``docs/Example Contracts/`` and
     ``docs/Example Ontology/`` in
     every Change through its ``Example sync`` row, deciding for each changed
     role card, Contract process or ontology type or link whether the change
     also holds for a general project, and declaring each deliberate deviation
     of an example role card
     in the ``Deviations`` table of ``docs/Example Actors/index.md``.

.. vc:: Technical Writer maintains complete documentation traceability
   :id: SYSP_VC_TECHNICAL_WRITER_1
   :status: approved
   :verifies: SYSP_REQ_TECHNICAL_WRITER

   Each independently maintained user-facing surface has a ``doc`` Need with
   a valid realization path and complete ``includes`` links; changed
   requirements expose it through ``included_in``.

.. vc:: Documentation preserves factual authority
   :id: SYSP_VC_TECHNICAL_WRITER_2
   :status: approved
   :verifies: SYSP_REQ_TECHNICAL_WRITER

   Documentation evidence records direct factual-owner review of accuracy and
   understandability; consultation transfers neither ownership nor responsibility.

.. vc:: Documentation maintenance includes generic examples
   :id: SYSP_VC_TECHNICAL_WRITER_3
   :status: approved
   :verifies: SYSP_REQ_TECHNICAL_WRITER

   The role card assigns example maintenance; a closed Change's ``Example
   sync`` row records its result and declared role-card deviations.

.. vc:: Realized user documentation remains markup-free
   :id: SYSP_VC_TECHNICAL_WRITER_4
   :status: approved
   :verifies: SYSP_REQ_TECHNICAL_WRITER

   Realized user-facing documents contain no Needs markup.