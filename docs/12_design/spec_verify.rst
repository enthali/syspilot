Verify Agent Design
====================

Design specifications for the Verify Agent — implementation verification and status lifecycle.

**Document Version**: 0.1
**Last Updated**: 2026-02-06


.. spec:: Five-Category Verification
   :id: SPEC_VERIFY_CATEGORIES
   :status: implemented
   :links: REQ_CHG_VERIFY_AGENT, REQ_CORE_TRACEABILITY
   :tags: verify, agent, categories

   **Design:**
   The Verify Agent validates implementations across five categories,
   each with specific check questions.

   **Category 1 — Requirements Verification:**

   | Check | Question |
   | Exists | Is REQ_xxx documented? |
   | Complete | Does it have all required fields (status, priority, AC)? |
   | Implemented | Is there a SPEC linking to it? |
   | Tested | Is there a test referencing it? |

   **Category 2 — Design Verification:**

   | Check | Question |
   | Exists | Is SPEC_xxx documented? |
   | Linked | Does it reference requirements? |
   | Implemented | Is there code implementing it? |
   | Accurate | Does code match the design? |

   **Category 3 — Code Verification:**

   | Check | Question |
   | Traceability | Does code reference SPEC IDs? |
   | Completeness | Are all design items implemented? |
   | Quality | Does it follow project conventions? |

   **Category 4 — Test Verification:**

   | Check | Question |
   | Coverage | Is every Acceptance Criterion tested? |
   | References | Do tests reference REQ IDs? |
   | Passing | Do all tests pass? |

   **Category 5 — Traceability Verification:**

   Bidirectional link chain:

   ::

      REQ → SPEC → Code → Test
       ↑      ↑      ↑      ↑
       └──────┴──────┴──────┘ (all linked back)

   **Common Issues Checklist:**

   * Requirements: missing AC, untestable requirements, orphan requirements
   * Design: design–implementation mismatch, missing error handling
   * Code: missing traceability comments, coding standard violations
   * Tests: missing tests for AC, tests don't reference REQ IDs
   * Traceability: broken links, missing matrix entries

   **File:** ``.github/agents/syspilot.verify.agent.md``


.. spec:: Verification Report Format
   :id: SPEC_VERIFY_REPORT
   :status: implemented
   :links: REQ_CHG_VERIFY_AGENT
   :tags: verify, report, format

   **Design:**
   The Verify Agent produces a structured Verification Report with
   coverage matrix and issue tracking.

   **Report Header:**

   ::

      # Verification Report: [Feature/Change Name]
      **Date**: YYYY-MM-DD
      **Change Proposal**: [reference]
      **Status**: ✅ PASSED | ⚠️ PARTIAL | ❌ FAILED

   **Summary Table:**

   ::

      | Category       | Total | Verified | Issues |
      |----------------|-------|----------|--------|
      | Requirements   | n     | n        | 0      |
      | Designs        | n     | n        | 0      |
      | Implementations| n     | n        | 0      |
      | Tests          | n     | n        | 0      |
      | Traceability   | n     | n        | 0      |

   **Requirements Coverage Matrix:**

   Per-REQ row showing SPEC link, Code presence, Test presence, and Status.

   **Acceptance Criteria Verification:**

   Per-REQ section listing each AC with test mapping:

   ::

      ### REQ_xxx_1
      - [x] AC-1: [criterion] → Test: test_module.py::test_ac1
      - [ ] AC-2: [criterion] → **MISSING TEST**

   **Issue Format:**

   Each issue includes: Severity (High/Medium/Low), Category, Description,
   Expected vs Actual, and Recommendation.


.. spec:: Verification Status Lifecycle
   :id: SPEC_VERIFY_STATUS_LIFECYCLE
   :status: implemented
   :links: REQ_CHG_VERIFY_AGENT, REQ_CHG_FINAL_CHECK
   :tags: verify, status, lifecycle

   **Design:**
   The Verify Agent manages the ``approved → implemented`` status transition
   based on verification results.

   **Transition Rules:**

   * **✅ PASSED** — Update all verified REQ_* and SPEC_* from
     ``:status: approved`` to ``:status: implemented``
   * **⚠️ PARTIAL** — Do NOT update statuses; hand off to Implement Agent
     for fixes, then re-verify
   * **❌ FAILED** — Do NOT update statuses; hand off to Implement Agent
     or Change Agent depending on issue severity

   **Severity Levels and Actions:**

   * **High** — Requirement not implemented or major deviation → block merge
   * **Medium** — Partial implementation or missing traceability → should fix before merge
   * **Low** — Minor issues, documentation gaps → can fix in follow-up

   **Status Update Process:**

   ::

      # Edit docs/11_requirements/req_*.rst
      # Edit docs/12_design/spec_*.rst
      # Change :status: approved → :status: implemented for verified items

      git commit -m "docs: mark verified specs as implemented"

   **Rationale:** Status reflects actual verification, not just code existence.
   Only the Verify Agent updates status to ``implemented``, ensuring independent
   confirmation that the implementation matches the specification.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_VERIFY')
