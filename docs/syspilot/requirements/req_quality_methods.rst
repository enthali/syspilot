Quality Review Methods
======================

.. req:: MECE Horizontal Coverage Analysis
   :id: SYSP_REQ_MECE_ANALYSIS
   :status: approved
   :implements: SYSP_US_QUALITY_METHODS
   :realized_by: .github/skills/syspilot.mece/SKILL.md

   The MECE skill shall analyze an object recorded as impacted against its
   comparable peers, where a comparable peer is an object of the same type in
   the project's active ontology:

   - discover the peer set through supporting script output for at least two
     caller-selected scopes, namely peers declared in the same source
     document and all peers of that type;
   - report the selected scope and the exact discovered peer set, so the
     coverage of the analysis is inspectable and reproducible;
   - assess complete item coverage, overlapping or duplicated obligation,
     contradiction, missing coverage, ambiguous partitioning, and
     responsibility-boundary collision within that peer set;
   - read object types and source locations from the active ontology and the
     project's built specification data, rather than assuming Syspilot type
     names or a fixed specification level; and
   - state the limits of the analysis when peer data is incomplete or
     unavailable, instead of reporting an empty result as a clean outcome.

   The skill shall remain read-only with respect to versioned artifacts and
   the applicable Contract. It reports findings and shall not correct
   artifacts, decide scope, or transfer responsibility.

.. vc:: MECE reports a deterministic peer set and coverage findings
   :id: SYSP_VC_MECE_ANALYSIS_1
   :status: approved
   :verifies: SYSP_REQ_MECE_ANALYSIS

   Automated discovery returns the exact same-document and all-type peer sets
   for current project data and synthetic type names; repeated runs agree.

.. vc:: MECE reports semantic findings and data limits
   :id: SYSP_VC_MECE_ANALYSIS_2
   :status: approved
   :verifies: SYSP_REQ_MECE_ANALYSIS

   Fixtures with overlap, contradiction and missing coverage yield findings.
   Incomplete or missing peer data yields an explicit limitation, not a clean
   empty result.

.. vc:: MECE reports its exact coverage scope
   :id: SYSP_VC_MECE_ANALYSIS_3
   :status: approved
   :verifies: SYSP_REQ_MECE_ANALYSIS

   Reports identify the exact peer set, scope, coverage and responsibility
   boundaries.

.. vc:: MECE retains read-only authority
   :id: SYSP_VC_MECE_ANALYSIS_4
   :status: approved
   :verifies: SYSP_REQ_MECE_ANALYSIS

   The skill remains read-only and claims no artifact correction, scope
   decision or handoff authority.

.. req:: Trace Relationship And Chain Analysis
   :id: SYSP_REQ_TRACE_ANALYSIS
   :status: approved
   :implements: SYSP_US_QUALITY_METHODS
   :realized_by: .github/skills/syspilot.trace/SKILL.md

   The Trace skill shall analyze the declared relationships of an object
   recorded as impacted:

   - traverse that object's relationships to a caller-selected depth, so a
     review can inspect direct neighbors only or dependencies to a second,
     third, fourth, or deeper degree;
   - obtain that traversal from the ontology-driven discovery realized for
     ``SYSP_REQ_IMPACT_QUERY``, so depth handling, de-duplication, and cycle
     protection retain a single verified implementation;
   - report observed link names and directions from the project's configured
     Sphinx-Needs links and exported Needs data, including unresolved targets,
     without requiring Syspilot type-pair metadata;
   - not infer missing required links, graph completeness, or the semantic
     correctness of same-type links from observed type pairs;
   - assess whether each linked object's content remains semantically
     consistent with the analyzed object, including relationships that exist
     but were not touched by the change under review; and
   - report the examined depth and the exact relationship neighborhood it
     evaluated, including unresolved targets, so the analysis is
     reproducible.

   The skill shall remain read-only with respect to versioned artifacts and
   the applicable Contract. It reports findings and shall not correct
   artifacts, decide scope, or transfer responsibility.

   Reporting an absent relationship as a defect requires an explicit
   requiredness rule. That is outside this capability unless a future Contract
   explicitly includes it.

.. vc:: Trace reports a depth-bounded typed relationship assessment
   :id: SYSP_VC_TRACE_ANALYSIS_1
   :status: approved
   :verifies: SYSP_REQ_TRACE_ANALYSIS

   Automated fixtures return exact neighborhoods for depths one through four
   and a deeper value, preserving forward/backward sources and targets with
   both current and synthetic ontologies.

.. vc:: Trace uses the shared impact traversal
   :id: SYSP_VC_TRACE_ANALYSIS_2
   :status: approved
   :verifies: SYSP_REQ_TRACE_ANALYSIS

   Trace obtains traversal from ``SYSP_REQ_IMPACT_QUERY``; it introduces no
   second depth, de-duplication or cycle implementation.

.. vc:: Trace distinguishes observed links from semantic conclusions
   :id: SYSP_VC_TRACE_ANALYSIS_3
   :status: approved
   :verifies: SYSP_REQ_TRACE_ANALYSIS

   Reports state depth, exact neighborhood and unresolved targets without
   inferring required links, orphan status or graph completeness; an absent-link
   defect requires an explicit requiredness rule.

.. vc:: Trace preserves artifact and Contract authority
   :id: SYSP_VC_TRACE_ANALYSIS_4
   :status: approved
   :verifies: SYSP_REQ_TRACE_ANALYSIS

   The skill remains read-only and claims no correction, scope or handoff
   authority.

.. vc:: Trace assesses linked-content consistency
   :id: SYSP_VC_TRACE_ANALYSIS_5
   :status: approved
   :verifies: SYSP_REQ_TRACE_ANALYSIS

   The semantic assessment includes linked content reached through untouched
   and same-type relationships, separately from observed edge data.
