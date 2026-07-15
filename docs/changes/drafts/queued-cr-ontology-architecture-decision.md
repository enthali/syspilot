# Queued CR Draft: ontology-architecture-decision

**GH Issue**: (noch offen — erstellen sobald dieser Draft formalisiert wird)
**Status**: queued (wartet auf Merge von spec-root-cause-principle)
**Proposed Operation Mode**: user-guided (Architekturentscheid — Design-Checkpoint gewünscht)

---

## Summary (draft — dient gleichzeitig als Architecture Decision Record)

**Architecture Decision: syspilot wird ontologie-agnostisch.**

syspilot bettet seine Standard-Ontologie (User Story → Requirement → Design Spec, L0/L1/L2) heute direkt in Agenten-Prose, Workflows, Templates und Tools ein. Das führt dazu, dass jede Kundenmigration auf eine andere Ontologie (z.B. ASPICE: SW_REQ → SW_DES → SW_DD → SW_VER) alle betroffenen Agenten einzeln umschreiben muss — ein wiederholbarer Aufwand ohne strukturelle Lösung.

**Entscheidung:** syspilot trennt vier Belange konsequent:
1. **Ontologie** — welche Work-Product-Typen existieren, wie sind sie verknüpft, welche Lifecycle-Regeln gelten.
2. **Capabilities** — welche Operationen können Work Products erzeugen, ändern, prüfen, validieren.
3. **Actors** — welche Capabilities und Work-Product-Typen ist jeder Actor verantwortlich für.
4. **Process** — in welcher Reihenfolge operieren Actors, welche Gates steuern Übergänge.

**Schlüssel-Invarianten:**
- `syspilot.toml` ist die einzige Quelle der Wahrheit für Ontologie-Auswahl und Tailoring — `conf.py` ist Adapter/Konsument, keine Autorität.
- Jeder aktive Work-Product-Typ hat exakt einen Primary-Actor-Owner (1:N Work-Product-Typ-zu-Actor verboten als Ownership; Lesen ist erlaubt).
- Ein Actor verarbeitet *alle und ausschließlich* seine eigenen betroffenen Typen in der Dependency-Order des Ontologie-Graphen.
- Branching Graphs sind First-Class — "Dependency Order" ist Graph-Order, nicht ein nummerierter L0/L1/L2-Loop.

**Motivation:** CRAFT (ASPICE 4-Ebenen-Ontologie ohne User-Story-Wurzel) ist der Auslöser; die eigentliche Ursache ist, dass syspilot heute keine generische Ontologie-Abstraktion hat. CRAFT ist explizit *Lernquelle, keine Produktabhängigkeit*. Erster Referenzkunde für die neue Architektur ist syspilot selbst (Phase 1: verhaltensneutrale Externalisierung der bestehenden Hierarchie in `syspilot.toml`).

**Namensgebung und Verzeichnisstruktur (Entscheidung):**

`.syspilot/` ist der Namespace für alle projekt-spezifischen, Installer-geschützten Konfigurationen. Alles in `.syspilot/` folgt der Invariante: **create-if-missing, never-overwrite**. Intern unterscheidet der Dateiname den Charakter:

```
.syspilot/
  ontology.toml           ← Projekt-Ontologie (Installer generiert aus Template, nie überschrieben)
  tailoring/
    syspilot.pm.tailoring.md
    syspilot.release.tailoring.md
    syspilot.branching.tailoring.md
    ...
```

`ontology.toml` liegt **direkt** in `.syspilot/`, *nicht* unter `tailoring/`. Begründung: `tailoring/` enthält Overrides auf syspilot-Defaults. `ontology.toml` ist Projekt-Identität, kein Override — es gibt keine sinnvolle syspilot-Default-Ontologie, die "überschrieben" wird. Die Installer-Invariante (.syspilot/ = nie überschreiben) gilt für beides gleichermaßen.

Tailoring-Dateien (heute noch unter `.github/agents/*.tailoring.md` und `.github/skills/*/tailoring.md`) migrieren zu `.syspilot/tailoring/` als Teil von Phase 1.

Workflows bleiben als SKILL.md + tailoring.md — sie sind instruktionale Prose für LLMs, keine strukturierten Daten; TOML wäre hier falsch.

**Delivery-Sequenz (Phasen — je separater CR):**
- Phase 0 (dieser CR): Architekturentscheid dokumentieren, `.syspilot/`-Struktur und `ontology.toml`-Schema in Specs verankern — kein Code.
- Phase 1: `.syspilot/`-Verzeichnis einführen, `ontology.toml` vom Installer generieren lassen, bestehende Ontologie verhaltensneutral abbilden, Tailoring-Dateien migrieren.
- Phase 2: Agents auf Ontologie-Runtime umstellen (L0/L1/L2-Hardcoding entfernen).
- Phase 3–8: Qualities-Capabilities, Verification Work Products, Actor-Topologie, Governance-Graph, Jarvis-Validation, optional CRAFT-Profil.

**Acceptance Criteria für Phase 0:**
- Architecture Decision Record (dieses Change Document / Summary) ist im Repo versioniert.
- `.syspilot/`-Struktur und `ontology.toml`-Schema (Candidate) in neuen Spec-Elementen dokumentiert: Verzeichnisstruktur, Installer-Invariante, typisierte Relations, Ownership-Zuweisungen, Lifecycle-States, Validation-Constraints.
- Neue US/REQ/SPEC-Elemente für "Projekt-Konfiguration/.syspilot/" existieren im Spec-Baum — bestehender Baum bleibt unverändert.
- sphinx-build `-W` clean.

**Non-Goals für Phase 0:** keine Dateien anlegen, keine Agenten ändern, kein Installer-Update — reine Architektur-Dokumentation und Schema-Definition.

---

## Next steps once branch is safe to create

1. `git checkout development && git pull && git checkout -b feature/ontology-architecture-decision`
2. GH Issue erstellen ("Architecture: ontology-driven syspilot — Phase 0 architecture decision")
3. `Copy-Item syspilot\templates\change-document.md docs\changes\ontology-architecture-decision.md`
4. Header + Summary aus diesem Entwurf füllen — Operation Mode: user-guided
5. Commit + push branch
6. SEND to Change Manager (System Designer-Checkpoint nach L2 gewünscht)
