---
name: syspilot.impact-python
group: impact
description: >
  Ontology-driven impact analysis using built Sphinx-Needs data.
  Discovers candidate affected elements through standard, project-defined,
  incoming, and outgoing links. USE FOR: Contract scoping, relationship
  inspection, and evidence before specification or implementation changes.
requirements: [SYSP_REQ_IMPACT_QUERY]
---

# Impact Analysis

## Tool

Run `.github/skills/syspilot.impact-python/scripts/get_need_links.py --help` for the complete CLI.

```powershell
python .github/skills/syspilot.impact-python/scripts/get_need_links.py NEED_ID --direction both --depth 2
```

The default inputs are:

- active ontology: `.syspilot/ontology.toml`;
- built per-ID Needs data: `docs/_build/html/needs_id/`.

Use `--ontology` or `--needs-dir` for project-specific paths. The tool attempts a Sphinx HTML build when default Needs data is absent; use `--no-build` when the caller must control that prerequisite.

## Traversal

The tool reads every `option` declared by the active ontology's `[[needs.extra_links]]`. It traverses each `<option>` and `<option>_back` field in addition to standard `links` and `links_back`, so customer-defined link types work without code changes.

- `--direction out` follows outgoing fields.
- `--direction in` follows incoming `*_back` fields.
- `--direction both` follows both.
- `--depth N` bounds traversal depth.
- `--flat` returns sorted unique linked IDs.
- `--simple` returns direct incoming and/or outgoing IDs plus metadata.
- Default output is a nested tree with cycle/repeated-node truncation.

IDs reached through multiple link options are de-duplicated. Cycles do not recurse indefinitely.

## Contract Use

Run impact analysis from existing elements whose relationships can expose affected work. Query output supplies candidate scope and traceability evidence to the applicable Contract. The Contract records the disposition of each candidate and remains authoritative for included artifacts, responsibility, and scope decisions.

Do not treat an empty or failed query as authoritative evidence. The command exits non-zero for an unknown Need, missing or invalid ontology, missing built Needs data, or an unusable build prerequisite. Resolve the reported prerequisite before recording impact conclusions.

## Verification

Run the focused automated suite after changing this skill:

```powershell
python .github/skills/syspilot.impact-python/scripts/test_get_need_links.py -v
```
