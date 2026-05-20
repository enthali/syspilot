# Change Request: agent-duties-english-translation

**Status**: merged
**Created**: 2026-05-13
**Author**: PM

---

## WHY

The project convention requires all documentation, specs, commit messages, and code
comments to be in English. During the Duties/Workflow conformance sweep (v0.5.4),
Duty names were written in German as shorthand labels. These German Duty names now
appear in agent files and their corresponding spec files, violating the English-only
convention and reducing accessibility for non-German-speaking users and contributors.

---

## WHAT

All German Duty name labels in agent files and their corresponding spec files shall
be translated to English. The Duty descriptions (the text after the dash) are already
in English and shall not be changed.

Affected agents (Duty names to translate):

- `syspilot.cm.agent.md`: Intent-Übersetzung, Pipeline-Vollständigkeit, PM-Rückmeldung
- `syspilot.design.agent.md`: Vertikale Integrität, MECE-Konformität
- `syspilot.implement.agent.md`: Spec-Implementation-Übereinstimmung, Funktionsfähigkeit
- `syspilot.installer.agent.md`: Vollständigkeit und Korrektheit, Funktionsfähigkeit
- `syspilot.mece.agent.md`: Vollständige Item-Abdeckung, Überlappungs-Sichtbarkeit, Lücken-Sichtbarkeit
- `syspilot.pm.agent.md`: Vollständige CR-Übersetzung, CR-Sprache-Trennschärfe, Merge-und-Release-Autorität
- `syspilot.qm.agent.md`: Unabhängige Qualitätsbewertung, Per-Level-Trennschärfe, Klare Qualitätsaussage
- `syspilot.release.agent.md`: Vollständige Nachvollziehbarkeit, Konsistente Versions-Identität, Trennschärfe
- `syspilot.uat.agent.md`: Manuelle Ausführbarkeit, Sichtbarkeit von Untestbarkeit
- `syspilot.verify.agent.md`: Spec-Implementation-Übereinstimmung, Traceability-Lückenlosigkeit

All corresponding spec files (`.rst`) that reference these Duty names shall be
updated in the same CR.

Both the product files (`syspilot/agents/`) and the installed instance
(`.github/agents/`) shall be updated.

---

## Acceptance Criteria

- No German words appear in any agent Duty name label in `syspilot/agents/` or `.github/agents/`.
- All corresponding spec files use the translated English Duty names.
- All Duty descriptions (text after the dash) are unchanged.
- sphinx-build passes without warnings.
