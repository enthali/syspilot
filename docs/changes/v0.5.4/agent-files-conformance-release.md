# Change: agent-files-conformance-release

**CR:** agent-files-conformance-release
**Branch:** feature/agent-files-conformance-release
**Status:** in-progress

## Summary

Top-to-bottom Duties conformance refactor for the Release Engineer agent.
Duties are rewritten as outcome guarantees (PM-vorgabe wörtlich) instead of
workflow steps. Bullets instead of numbered lists. REQ ACs as end-state
guarantees.

## Affected Elements

- SYSP_US_RELEASE (add Soul/Duties/Workflow sections)
- SYSP_REQ_RELEASE_DUTIES (ACs → outcome guarantees)
- SYSP_SPEC_RELEASE_DUTIES (numbered → bullets, outcome language)
- syspilot.release.agent.md (numbered → bullets, outcome language)

## PM-Mandated Duties (wörtlich)

- die versionierte Markierung im Git-Tree, die den freigegebenen Zustand eindeutig identifizierbar macht (Tag)
- die Validität des released Stands gegenüber den Qualitätsgates
- die vollständige Nachvollziehbarkeit dessen, was in dieser Version steckt
- die konsistente Versions-Identität über alle Quellen hinweg
- die Trennschärfe zwischen Entwicklungslinie und freigegebener Linie
