---
name: syspilot.mece
description: >
  Ontology-driven horizontal coverage analysis for impacted objects. Discovers
  exact same-type peer sets and reports overlap, contradiction, coverage, and
  responsibility-boundary evidence. USE FOR: every Syspilot Quality Review.
requirements: [SYSP_REQ_MECE_ANALYSIS]
---

# MECE Horizontal Coverage Analysis

Start from each impacted object recorded by the active Contract. Select one peer scope explicitly:

```powershell
python .github/skills/syspilot.mece/scripts/analyze_mece.py NEED_ID --scope same-document
python .github/skills/syspilot.mece/scripts/analyze_mece.py NEED_ID --scope all-type
```

The script reads the active ontology and built per-ID Needs data. It reports the analyzed object, its active-ontology type, selected scope, exact peer IDs, reproducible structural findings, and limitations. A missing or empty peer data set is a limitation, not a clean outcome.

The default ontology is the literal `needs_from_toml` string in `docs/conf.py`, resolved relative to that configuration file without executing it. Use `--ontology` for an explicit path or a computed binding, and `--needs-dir` to override `docs/_build/html/needs_id/`. Missing or invalid bindings fail explicitly. Ontology discovery uses the installed `syspilot.impact-python` runtime.

Review the complete reported peer set. Assess every item for duplicated or overlapping obligation, contradiction, missing coverage, ambiguous partitioning, and responsibility-boundary collision. Script findings are evidence for that semantic review, not a substitute for reading the objects.

Record scope, peer set, evidence, findings, and limitations in the Quality Review section of the applicable Contract. This skill is read-only: do not modify artifacts or the Contract, decide scope, transfer responsibility, or resolve findings while executing it.

Release QA is maintained in Syspilot's repository test suite, outside the installed skill folder.