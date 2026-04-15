---
name: syspilot.impact-python
description: >
  Impact analysis using sphinx-needs dependency trees.
  Discovers affected specification elements by traversing
  traceability links. USE FOR: change scoping, blast radius
  analysis, element discovery before spec writing.
---

# Skill: Impact Analysis (Python)

> **Implements**: SYSP_SPEC_SKILL_IMPACT_QUERY, SYSP_SPEC_SKILL_IMPACT_EXCHANGE
> **Requirements**: SYSP_REQ_SKILL_IMPACT_QUERY, SYSP_REQ_SKILL_IMPACT_EXCHANGE

## Tool

`scripts/python/get_need_links.py` — run with `--help` for parameter details.

Requires `docs/_build/html/needs.json` — run `sphinx-build` first if stale.

## Domain Rules

### 1. Search from consumer elements, not from new elements

A newly created element has no incoming links. Run the query from each **consumer**
element that the new element satisfies.

**Example:** You created `SYSP_US_SKILL_IMPACT` which `:links:` to `SYSP_US_DESIGN`
and `SYSP_US_PM`. Run the impact query from `SYSP_US_DESIGN` and `SYSP_US_PM`
(not from the new US).

### 2. Use `--direction in` for level transitions

`in` = "who links to me" = "who implements me at the next level down".
REQs link upward to USes, SPECs link upward to REQs. So querying a US with
`--direction in` yields its REQ candidates.

### 3. Depth strategy

| Transition | Depth | Rationale |
|---|---|---|
| Level 0 → Level 1 | 1 | US → REQ, direct links |
| Level 1 → Level 2 | 1 | REQ → SPEC, direct links |
| Level 2 cross-check | 2 | Catches second-order consumers (e.g. doc SPECs aggregating workflow SPECs) |

### 4. Raw output at Level 0, assessment at Level 1/2

At Level 0 present candidates to the user **without verdicts**. Assessment
(affected / not affected) happens when writing the next level.

## Exchange Contract

To replace this implementation: create a new skill folder, provide the same
query-by-ID capability, update the `description` for Copilot discovery.
No agent changes required.
