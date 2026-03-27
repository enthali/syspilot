Traceability Agents Design
===========================

Design specifications for the MECE Agent and Trace Agent — horizontal and vertical quality analysis.

**Document Version**: 0.1
**Last Updated**: 2026-02-06


MECE Agent
----------

.. spec:: Horizontal MECE Analysis
   :id: SYSPILOT_SPEC_MECE_HORIZONTAL_ANALYSIS
   :status: implemented
   :links: SYSPILOT_REQ_TRACE_MECE, SYSPILOT_REQ_CHG_MECE_PER_LEVEL
   :tags: mece, agent, horizontal

   **Design:**
   The MECE Agent analyzes ONE level at a time for Mutually Exclusive,
   Collectively Exhaustive properties.

   **Scope:**

   ::

      ┌──────────────────────────────────────────────────┐
      │  US_001  ←→  US_002  ←→  US_003  ←→  US_004     │  ← MECE checks
      └──────────────────────────────────────────────────┘

   Horizontal only — vertical traceability is the Trace Agent's job.

   **Input:** Level parameter (US, REQ, SPEC). Defaults to REQ if unspecified.

   **Six Analysis Categories:**

   1. **Redundancy Detection** — Same requirement stated differently.
      Symptoms: identical AC in multiple items, different wording / same meaning,
      subset relationships.

   2. **Contradiction Detection** — Conflicting requirements.
      Symptoms: mutually exclusive behaviors, different values for same parameter.

   3. **Gap Analysis** — Missing requirements for completeness.
      Symptoms: CRUD incomplete, error paths unspecified, edge cases missing.

   4. **Overlap Detection** — Partial coverage of same ground.
      Symptoms: shared AC, unclear scope boundaries.

   5. **Abstraction Level Mismatch** — Mixed granularity.
      Symptoms: system-level next to component-level, goals next to
      implementation details.

   6. **Missing Horizontal Links** — Implicit dependencies not expressed
      in ``:links:``. Check: does item use terms defined in another item
      at the same level without linking?

   **File:** ``.github/agents/syspilot.mece.agent.md``


.. spec:: MECE Report Format
   :id: SYSPILOT_SPEC_MECE_REPORT
   :status: implemented
   :links: SYSPILOT_REQ_TRACE_MECE
   :tags: mece, report, format

   **Design:**
   The MECE Agent produces a structured report with categorized findings.

   **Report Structure:**

   ::

      # MECE Analysis Report
      **Level**: US | REQ | SPEC
      **Date**: YYYY-MM-DD
      **Total Items Analyzed**: N

   **Summary Table:**

   ::

      | Category        | Count | Severity |
      |-----------------|-------|----------|
      | Redundancies    | 0     | -        |
      | Contradictions  | 0     | -        |
      | Gaps            | 0     | -        |
      | Overlaps        | 0     | -        |
      | Missing Links   | 0     | -        |

   **Findings by Severity:**

   * 🔴 Contradictions (Critical) — with item IDs, issue description, recommendation
   * 🟡 Redundancies (Medium) — with merge recommendation
   * 🟢 Missing Links (Low) — with suggested ``:links:`` additions
   * ❓ Gaps Identified — with recommendation for new items

   **Handoffs:** After analysis, suggests ``@syspilot.change`` to fix issues
   or ``@syspilot.trace`` for vertical verification.


Trace Agent
-----------

.. spec:: Vertical Traceability Analysis
   :id: SYSPILOT_SPEC_TRACE_VERTICAL_ANALYSIS
   :status: implemented
   :links: SYSPILOT_REQ_TRACE_VERTICAL, SYSPILOT_REQ_CHG_BIDIR_NAV
   :tags: trace, agent, vertical

   **Design:**
   The Trace Agent traces ONE item vertically through all levels
   (US → REQ → SPEC → Code → Test) and validates semantic correctness.

   **Scope:**

   ::

      ┌─────────────┐
      │  SYSPILOT_US_CFG_001 │  ← START HERE
      └──────┬──────┘
             ↓ :links:
      ┌──────┴──────┬──────────────┐
      │ SYSPILOT_REQ_CFG_001 │ SYSPILOT_REQ_CFG_002  │  ← Find linked REQs
      └──────┬──────┴──────┬───────┘
             ↓              ↓
      ┌──────┴──────┬──────┴───────┐
      │SYSPILOT_SPEC_CFG_001 │SYSPILOT_SPEC_CFG_002  │  ← Find linked SPECs
      └──────┬──────┴──────┬───────┘
             ↓              ↓
             Code  ←→  Tests          ← Find implementation

   Vertical only — horizontal consistency is the MECE Agent's job.

   **Input:** Starting item (us_xxx or req_xxx). Asks user if unspecified.

   **Four Check Types:**

   1. **Link Completeness** — Does the item have links at each level?
      US→REQ, REQ→SPEC, SPEC→Code, REQ→Test.

   2. **Horizontal Dependencies** — Does the item depend on other items
      at the same level? If so, are there explicit ``:links:``?

   3. **Semantic Validity** — Does the link make sense? Does the REQ
      actually address the US intent? Does the SPEC implement the REQ behavior?

   4. **Acceptance Criteria Coverage** — For each AC in the starting item,
      is there a corresponding REQ/Test that addresses it?

   **Link Discovery:**

   ::

      # Trace downward with depth
      python scripts/python/get_need_links.py us_xxx --depth 3 --direction out

      # Trace upward
      python scripts/python/get_need_links.py spec_xxx --depth 2 --direction in

   **File:** ``.github/agents/syspilot.trace.agent.md``


.. spec:: Trace Report Format
   :id: SYSPILOT_SPEC_TRACE_REPORT
   :status: implemented
   :links: SYSPILOT_REQ_TRACE_VERTICAL
   :tags: trace, report, format

   **Design:**
   The Trace Agent produces a report with a visual trace tree and coverage summary.

   **Report Structure:**

   ::

      # Trace Report: [NEED_ID]
      **Date**: YYYY-MM-DD
      **Starting Point**: [NEED_ID]
      **Direction**: Downward | Upward | Both

   **Trace Tree Visualization:**

   ::

      SYSPILOT_US_CFG_001: "Edit user settings"
      ├── SYSPILOT_REQ_CFG_001: "Allow email editing" ✅
      │   ├── SYSPILOT_SPEC_CFG_001: "Settings form design" ✅
      │   │   └── Code: src/settings.py ✅
      │   └── Test: test_settings.py::test_email_edit ✅
      ├── SYSPILOT_REQ_CFG_002: "Persist to YAML" ✅
      │   ├── SYSPILOT_SPEC_CFG_002: "YAML file format" ✅
      │   │   └── Code: src/config.py ✅
      │   └── Test: test_config.py::test_yaml_save ✅
      └── SYSPILOT_REQ_CFG_003: "Validate email format" ⚠️
          └── SPEC: MISSING ❌

   **Coverage Summary Table:**

   Per-level counts of Total, Complete, and Missing items.

   **Sections:** Gaps Found, Semantic Issues, Recommendations.

   **Handoffs:** After analysis, suggests ``@syspilot.mece`` for level
   consistency or ``@syspilot.change`` to fix gaps.


Quality Check Workflow
----------------------

.. spec:: Independent Quality Check Workflow
   :id: SYSPILOT_SPEC_TRACE_QUALITY_WORKFLOW
   :status: implemented
   :links: SYSPILOT_REQ_WF_QUALITY_INDEPENDENT, SYSPILOT_REQ_TRACE_MECE, SYSPILOT_REQ_TRACE_VERTICAL
   :tags: workflow, quality, mece, trace

   **Design:**
   MECE and Trace agents are usable as independent quality checks
   outside of a change workflow.

   **Usage Modes:**

   * **Standalone**: Invoke @mece or @trace directly without a Change Document
   * **Integrated**: Change Agent invokes horizontal MECE checks per level
     during change processing (via SYSPILOT_REQ_CHG_MECE_PER_LEVEL)

   **Standalone Flow:**

   ::

      Developer
          │
          ├──→ @mece <level>  ──→ Horizontal MECE Report
          │
          └──→ @trace <ID>    ──→ Vertical Coverage Report
                                      │
                                      ▼ (issues found?)
                                  @change  ──→ Fix via change workflow

   **Key Property:**
   Quality checks are read-only — they never modify specification files.
   If issues are found, the developer starts a change workflow to fix them.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SYSPILOT_SPEC_MECE') or id.startswith('SYSPILOT_SPEC_TRACE')
