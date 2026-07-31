---
name: syspilot.change-launcher
description: "Automates CR scaffolding: creates feature branch, copies and pre-fills the Change Document template, commits. USE FOR: starting a new Change Request from the PM workflow. DO NOT USE FOR: editing existing Change Documents or managing branches after creation."
implements: [SYSP_SPEC_CHG_LAUNCHER]
requirements: [SYSP_REQ_CHG_LAUNCHER]
---

# Skill: Change Launcher

## Script

`syspilot/skills/syspilot.change-launcher/launch_change.py`

```
python launch_change.py --name <change-name> --author <author> --mode <mode>
```

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--name` | yes | Change name in kebab-case (used for branch and file naming) |
| `--author` | yes | Author string for the CD header (e.g. `PM`) |
| `--mode` | yes | `autonomous` or `user-guided` |

## Preconditions

- Current branch must be `development`
- Template `syspilot/templates/change-document.md` must exist
- `docs/changes/<name>.md` must not already exist

## Behaviour

1. Validates preconditions (exits 1 on failure)
2. Creates `feature/<name>` branch (or warns and switches if it exists)
3. Copies template to `docs/changes/<name>.md`
4. Pre-fills header placeholders (`{NAME}`, `{DATE}`, `{AUTHOR(S)}`, status, mode)
5. Commits the scaffolded Change Document

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Precondition failure (wrong branch, missing template, CD exists) |
