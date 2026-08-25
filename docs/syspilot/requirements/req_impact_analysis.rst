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
       preserving cycle protection; and
    - fail explicitly for an unknown Need, missing or invalid ontology, missing
       built Needs data, or an unusable build prerequisite.

    The Skill guidance shall describe the tested behavior and treat impact
    output as input to Contract-owned scope decisions and evidence. It shall not
    declare the query result to be authoritative scope or establish a parallel
    governance source.

.. vc:: Impact Python traverses active ontology links
   :id: SYSP_VC_IMPACT_QUERY_1
   :status: approved
   :verifies: SYSP_REQ_IMPACT_QUERY

    Run focused automated tests that confirm standard links and active-ontology
    extra links are traversed in both directions; current v2 typed links and a
    synthetic customer-defined link type are discovered; direction, depth,
    output modes, de-duplication, and cycle protection behave consistently; and
    unknown Needs, missing or invalid ontology, missing built data, and failed
    build prerequisites return explicit non-success results. Inspect ``SKILL.md``
    and confirm its discovery and authority claims match the tested behavior and
    Contract-owned scope boundary.
