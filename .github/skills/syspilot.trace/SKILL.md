---
name: syspilot.trace
description: >
  Ontology-driven relationship and chain analysis using Impact discovery.
  Reports depth-bounded typed neighborhoods, invalid edges, orphans, and
  semantic-review limits. USE FOR: every Syspilot Quality Review.
requirements: [SYSP_REQ_TRACE_ANALYSIS]
---

# Trace Relationship And Chain Analysis

Start from every impacted object recorded by the active Contract and choose the review depth explicitly:

```powershell
python .github/skills/syspilot.trace/scripts/analyze_trace.py NEED_ID --direction both --depth 2
```

The analyzer imports the tested traversal from `syspilot.impact-python`; it does not implement a second graph walk. It evaluates each discovered typed edge against `[[syspilot.type_links]]`, reports unresolved targets, undeclared relationship directions/type pairs, and objects with no relationship in either direction as orphans, and returns the exact examined neighborhood. Declared type relationships are permitted, not required; their absence is not a finding because the ontology expresses no requiredness or cardinality.

Read every resolved neighbor and assess semantic consistency, including links not changed by the active work. The `semantic-content-review-required` limitation remains until that human or actor judgment is recorded.

Record depth, direction, neighborhood, evidence, findings, and limitations in the applicable Contract. This skill is read-only: do not modify artifacts or the Contract, decide scope, transfer responsibility, or resolve findings while executing it.

Run focused verification with:

```powershell
python .github/skills/syspilot.trace/scripts/test_analyze_trace.py -v
```