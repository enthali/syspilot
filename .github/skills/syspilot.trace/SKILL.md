---
name: syspilot.trace
description: >
  Relationship and chain analysis using Impact discovery and configured
  Sphinx-Needs links. Reports depth-bounded typed neighborhoods, unresolved
  targets, and semantic-review limits. USE FOR: every Syspilot Quality Review.
requirements: [SYSP_REQ_TRACE_ANALYSIS]
---

# Trace Relationship And Chain Analysis

Start from every impacted object recorded by the active Contract and choose the review depth explicitly:

```powershell
python .github/skills/syspilot.trace/scripts/analyze_trace.py NEED_ID --direction both --depth 2
```

The analyzer imports the tested traversal from `syspilot.impact-python`; it does not implement a second graph walk. It reports observed named and directed edges from standard links and configured Sphinx-Needs extra links, unresolved targets, and the exact examined neighborhood. An object with no observed edges in the selected direction and depth is an observation, not a defect. Neither an absent link nor the semantic correctness of an observed edge can be inferred from link configuration.

The default ontology is the literal `needs_from_toml` string in `docs/conf.py`, resolved relative to that configuration file without executing it. Use `--ontology` for an explicit path or a computed binding, and `--needs-dir` to override `docs/_build/html/needs_id/`. Missing or invalid bindings fail explicitly.

Read every resolved neighbor and assess semantic consistency, including links not changed by the active work. The `semantic-content-review-required` limitation remains until that human or actor judgment is recorded.

Record depth, direction, neighborhood, evidence, findings, and limitations in the applicable Contract. This skill is read-only: do not modify artifacts or the Contract, decide scope, transfer responsibility, or resolve findings while executing it.

Release QA is maintained in Syspilot's repository test suite, outside the installed skill folder.