# syspilot.release — Tailoring for the syspilot project

## Versioning Scheme

syspilot uses **Semantic Versioning (semver)**: `MAJOR.MINOR.PATCH`
(e.g. `1.4.2`). The Git tag keeps the `v` prefix per the generic workflow
(e.g. `v1.4.2`).

Determine the bump by reviewing the change documents archived for this
release cycle:

- **MAJOR** — any change that breaks an existing agent/skill contract or
  the installed file layout
- **MINOR** — any change that adds a new capability, backward-compatible
- **PATCH** — fixes, docs, internal refactors with no user-visible
  contract change

If more than one applies, use the highest. If uncertain, ask PM before
computing the version.

## Version Write-Target

Write the new version to the `version:` field in
`syspilot/agents/syspilot.setup.agent.md`.

This field doubles as "the currently installed syspilot version" for any
project that installs syspilot — but for this repository specifically,
syspilot's own product IS syspilot, so this field is also this project's
own release version marker. No other file needs updating.
