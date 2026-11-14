Impact Analysis
===============

.. req:: Ontology-Driven Impact Query
   :id: SYSP_REQ_IMPACT_QUERY
   :status: approved
   :implements: SYSP_US_IMPACT_QUERY
   :realized_by: .github/skills/syspilot.impact-python/scripts/get_need_links.py

    The Impact Python skill shall query built Sphinx-Needs data through link
    options declared by the project's active ontology:

    - read every ``option`` from ``[[needs.extra_links]]`` in the active
       ontology and traverse its ``<option>`` and ``<option>_back`` fields;
    - continue to traverse Sphinx-Needs standard ``links`` and ``links_back``;
    - use the project's configured ontology where practical, while permitting
       an explicit ontology-path option whose default is the project baseline;
    - support incoming, outgoing, or combined traversal to a caller-selected
       depth, with nested tree, flat ID list, and direct-link output modes;
    - de-duplicate Need IDs reached through multiple link options while
       preserving cycle protection;
    - report, on request, the link option and direction that connects each
      traversed pair, so a consumer that evaluates relationship types does not
      require a second traversal implementation; and
    - fail explicitly for an unknown Need, missing or invalid ontology, missing
       built Needs data, or an unusable build prerequisite.

    Skill guidance shall match tested behavior and treat query results as
    candidates for Contract-owned scope and evidence, not as scope authority.

.. vc:: Impact Python traverses active ontology links
   :id: SYSP_VC_IMPACT_QUERY_1
   :status: approved
   :verifies: SYSP_REQ_IMPACT_QUERY

    Automated fixtures discover the expected standard, configured Syspilot and
    synthetic customer-defined links for each direction and depth, without
    duplicates or unbounded cycles.

.. vc:: Impact query outputs preserve the selected relationship information
   :id: SYSP_VC_IMPACT_QUERY_2
   :status: approved
   :verifies: SYSP_REQ_IMPACT_QUERY

   Tree, flat and direct outputs match their expected shapes. Requested
   per-pair output names link option and direction; default output is unchanged.

.. vc:: Impact query failures are explicit
   :id: SYSP_VC_IMPACT_QUERY_3
   :status: approved
   :verifies: SYSP_REQ_IMPACT_QUERY

   Unknown Needs, missing or invalid ontology, missing built data and failed
   build prerequisites each produce a non-success result with a diagnostic.

.. vc:: Impact guidance preserves Contract authority
   :id: SYSP_VC_IMPACT_QUERY_4
   :status: approved
   :verifies: SYSP_REQ_IMPACT_QUERY

   Skill guidance matches tested discovery behavior and assigns scope decisions
   and evidence disposition to the applicable Contract.
