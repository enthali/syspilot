Syspilot Technical Writer
=========================

.. req:: Technical Writer Role
   :id: SYSP_REQ_TECHNICAL_WRITER
   :status: approved
   :implements: SYSP_US_TECHNICAL_WRITER
   :specializes: SYSP_REQ_ACTOR_MODEL
   :realized_by: docs/Syspilot Actors/Syspilot Technical Writer.md

   The Syspilot Technical Writer shall:

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
     transfers neither current responsibility nor artifact ownership.

.. vc:: Technical Writer preserves documentation authority boundaries
   :id: SYSP_VC_TECHNICAL_WRITER_1
   :status: approved
   :verifies: SYSP_REQ_TECHNICAL_WRITER

   Inspect the Technical Writer role card, ``doc`` Needs, and their realized
   user-facing documentation and confirm that each surface has a path and
   requirement traceability, changed requirements expose incoming
   ``included_in`` impact, source authority is preserved, factual review is
   recorded, and consultation did not implicitly transfer responsibility.