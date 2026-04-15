# syspilot Agent Architecture v2 — Konzept

*Stand: 2026-04-11*

## Grundidee

Alle Rollen sind **Agenten** — sowohl Manager als auch Engineers.
Trennung in **Manager** (Orchestratoren, user-facing) und **Engineers**
(Spezialisten, Subagents). Manager planen und steuern, Engineers fuehren aus.
Beide Gruppen folgen der gleichen Struktur: Soul / Duties / Workflow.

## Manager (user-invocable: true)

Details siehe Agenten-Tabelle unten.

Jeder Manager bekommt seinen eigenen Projekt-Ordner:
- `projects/project-manager/` — bleibt
- `projects/change-manager/` — NEU (ersetzt `projects/developer/`)
- `projects/quality-manager/` — NEU (ersetzt `projects/qa-engineer/`)

## Alle Agenten

### Manager (user-invocable: true, orchestrieren)

| Persona | Agent | Aufgabe |
|---------|-------|------|
| Project Manager | syspilot.pm | Portfolio, Planung, Research, Feature-Diskussion |
| Change Manager | syspilot.cm | E2E Change-Prozess, orchestriert Engineers |
| Quality Manager | syspilot.qm | Unabhaengige Quality Checks, periodisch |

Manager haben .agent.md (stabile Rolle: Soul/Duties/Workflow) UND
einen Projekt-Ordner mit context.md (dynamisches Projektwissen).
- agent.md = WIE der Manager arbeitet (stabil, Product = Instance)
- context.md = WAS gerade ansteht (dynamisch, projektspezifisch)

### Engineers (user-invocable: false, Subagents)

| Persona | Agent | Aufgabe | Status |
|---------|-------|------|--------|
| System Designer | syspilot.change | Change-Analyse, US/REQ/SPEC per-level | UPDATE |
| Dev Engineer | syspilot.implement | Code/Config-Aenderungen umsetzen | UPDATE |
| Test Engineer | syspilot.uat | UAT-Artefakte generieren | **NEU** |
| Documentation Eng. | syspilot.docu | Interne + externe Docs pflegen | **NEU** |
| Quality Eng. MECE | syspilot.mece | Horizontale Konsistenz einer Ebene | UPDATE |
| Quality Eng. Trace | syspilot.trace | Vertikale Traceability eines Elements | UPDATE |
| Release Engineer | syspilot.release | Version, Tag, Release Notes | UPDATE |
| Setup Engineer | syspilot.setup | Installation/Update | UPDATE |
| Impl-Check Eng. | syspilot.verify | Implementierung vs. Spec Abgleich | ZUKUNFT (Phase 3) |
| Security Engineer | (tbd) | Security-Analyse | ZUKUNFT |
| Safety Engineer | (tbd) | Safety-Analyse (ASIL etc.) | ZUKUNFT |

### Aenderungen gegenueber heute

- **syspilot.uat** — NEU: Test Engineer fuer UAT-Artefakte
- **syspilot.docu** — NEU: Documentation Engineer (ersetzt syspilot.memory)
- **syspilot.memory** — ENTFAELLT: Aufgaben gehen an syspilot.docu
- **syspilot.verify** — ZUKUNFT (Phase 3): Impl-Check Engineer

**Documentation Engineer** (syspilot.docu) vereint zwei Duty-Bereiche:
- **Intern:** copilot-instructions.md, context.md, naming conventions
- **Extern:** README, methodology, release notes, architecture, workflows

Gleiche Soul ("halte Docs in Sync mit Realitaet"), unterschiedliche Duties.

## Spec-Struktur pro Agent

### Meta-Level: Agent-Architektur

```
US:   "Als syspilot-Nutzer will ich eine saubere Agent-Struktur"
REQ:  "Jeder Agent SOLL aus 3 Sektionen bestehen: Soul, Duties, Workflow"
SPEC_SOUL:     Was ist eine Soul — Definition, unveraenderbar
SPEC_DUTIES:   Was sind Duties — einzelne Aufgaben, kundenanpassbar
SPEC_WORKFLOW: Was ist ein Workflow — Schritte, kundenanpassbar
```

### Pro Agent

```
US_<ROLE>:           "Wir brauchen einen Agent fuer Rolle X"
  |
  +-- REQ_<ROLE>_SOUL:      Stichworte (Charakter, Perspektive)
  +-- REQ_<ROLE>_DUTIES:    Stichworte (Aufgaben-Liste)
  +-- REQ_<ROLE>_WORKFLOW:  Stichworte (Ablauf)
        |
        +-- SPEC_<ROLE>_SOUL:      Ausformuliert
        +-- SPEC_<ROLE>_DUTIES:    Ausformuliert
        +-- SPEC_<ROLE>_WORKFLOW:  Ausformuliert
```

### Customization-Achse

- **Soul** = unveraenderbar. Kern-Charakter des Agents.
  "Du bist der Quality Engineer — gewissenhaft, systematisch, nie Kompromisse bei Qualitaet."

- **Duties** = kundenanpassbar. Einzelne Aufgaben die der Kunde:
  - Entfernen kann (z.B. Safety Engineer nicht benoetigt)
  - Ergaenzen kann (z.B. domain-spezifische Pruefung)
  - Veraendern kann (z.B. anderes MECE-Kriterium)

- **Workflow** = kundenanpassbar. Schritte die angepasst werden koennen
  (z.B. andere Build-Reihenfolge, zusaetzliche Validierung)

## Handoffs

Handoffs werden NICHT in den Agents beschrieben. Die Manager orchestrieren,
die Engineers wissen nichts voneinander. Jeder Engineer:
- Bekommt einen klaren Input (z.B. Change Document)
- Liefert ein strukturiertes Output (z.B. UAT Results)
- Weiss nicht wer vorher oder nachher kommt

Das entkoppelt die Engineers vollstaendig — sie sind frei kombinierbar.

## Mapping zu Jarvis-Rollen

| Manager | Ordner | Kommentar |
|---------|--------|-----------|
| Project Manager | `projects/project-manager/` | Bleibt |
| Change Manager | `projects/change-manager/` | NEU (ersetzt developer/) |
| Quality Manager | `projects/quality-manager/` | NEU (ersetzt qa-engineer/) |

## Prozessflows

### Change Flow (Change Manager)

```
User/PM -> Change Manager
             |
             +-> System Designer (per-level: analyse, write RST)
             |     +-> Quality Eng. MECE (advisory pro Level)
             |     +-> (Security/Safety Eng. ad-hoc)
             |
             +-> Test Engineer (UAT-Artefakte)
             +-> Dev Engineer (Implementierung)
             +-> Quality Eng. MECE (finale Pruefung)
             +-> Release Engineer
             +-> Documentation Eng. (interne Docs update)
```

### Quality Flow (Quality Manager, periodisch)

```
Heartbeat/PM -> Quality Manager
                  |
                  +-> Quality Eng. MECE (alle Ebenen)
                  +-> Quality Eng. Trace (Stichproben)
                  +-> (Impl-Check Eng. — Phase 3)
                  +-> (Security Eng. — Zukunft)
                  +-> (Safety Eng.)
                  |
                  +-> Findings -> Change Request an Change Manager
```

### Research Flow (Project Manager)

```
User -> Project Manager
          |
          +-> Research Session (explorativ, kein RST-Output)
          +-> Research-Dokument mit Findings + Empfehlung
          +-> Change Request an Change Manager
```

## Offene Fragen

- ~~Gruene Wiese oder Migration?~~ **ENTSCHIEDEN: Gruene Wiese.**
- ~~Naming:~~ **ENTSCHIEDEN: Neuer Prefix `SYSP_` statt `SYSPILOT_`.**
  Klar erkennbar was neu ist und was alt ist. Keine Links zwischen SYSP_ und SYSPILOT_.
- Setup Engineer: Bleibt er ein Engineer oder wird er zum Manager?
  (Er interagiert direkt mit dem User)
- Impl-Check Engineer: Ist das der heutige Verify Agent oder was Neues?
  (Verify = Change Doc vs. Impl, Impl-Check = Spec vs. Code)
- Brauchen Manager eigene .agent.md oder reicht context.md + copilot-instructions?

## Entscheidungen

### Gruene Wiese
- Komplett neuer RST-Baum mit Prefix `SYSP_`
- Pro Agent ein eigener RST-Tree (US + REQs + SPECs)
- Ja, das gibt viele RSTs mit vielleicht nur einer US — so what
- Kein Zusammenwurschteln in Sammel-Dateien
- Alte SYSPILOT_ Specs bleiben als Referenz, werden nicht verlinkt

### Agent-Namen bleiben gleich
- `.agent.md` Dateinamen aendern sich NICHT
- Beim Kunden werden die Agents einfach ersetzt (neue Version)
- Keine Breaking Changes am Interface

### Phasenplan

**Phase 1: Agent-Architektur (dieser Change)**
- Alle Engineers und Manager beschreiben (Soul/Duties/Workflow)
- Pro Agent: US -> REQ_SOUL/DUTIES/WORKFLOW -> SPEC_SOUL/DUTIES/WORKFLOW
- Resultat: Neuer Spec-Baum unter `docs/syspilot/` mit SYSP_ Prefix
- Resultat: Neue .agent.md Dateien die den Specs entsprechen
- Neue Agents: syspilot.uat, syspilot.docu
- Entfaellt: syspilot.memory (Aufgaben gehen an syspilot.docu)
- Manager-Ordner umbenennen (developer -> change-manager, qa-engineer -> quality-manager)

**Phase 2: Alte SYSPILOT_ Specs loeschen**
- Alle alten RST-Dateien mit SYSPILOT_ Prefix loeschen
- Git hat die Historie, Change Document beschreibt was passiert ist
- Sauberer Schnitt, kein deprecated-Ballast

**Phase 3 (Zukunft): Impl-Check + weitere Engineers**
- syspilot.verify als Impl-Check Engineer reactivieren
- Security Engineer, Safety Engineer nach Bedarf

## RST-Struktur (neu)

Pro Agent ein eigener Baum:

```
docs/syspilot/
  userstories/
    us_system_designer.rst        <- SYSP_US_SYSTEM_DESIGNER
    us_dev_engineer.rst           <- SYSP_US_DEV_ENGINEER
    us_test_engineer.rst          <- SYSP_US_TEST_ENGINEER
    us_documentation_eng.rst      <- SYSP_US_DOCUMENTATION_ENG
    us_quality_mece.rst           <- SYSP_US_QUALITY_MECE
    us_release_engineer.rst       <- SYSP_US_RELEASE_ENGINEER
    us_setup_engineer.rst         <- SYSP_US_SETUP_ENGINEER
    us_agent_structure.rst        <- SYSP_US_AGENT_STRUCTURE (Meta)
    ...
  requirements/
    req_system_designer.rst       <- SYSP_REQ_SYSTEM_DESIGNER_SOUL/DUTIES/WORKFLOW
    req_dev_engineer.rst          <- ...
    req_test_engineer.rst
    req_agent_structure.rst       <- Meta: was ist Soul/Duties/Workflow
    ...
  design/
    spec_system_designer.rst      <- SYSP_SPEC_SYSTEM_DESIGNER_SOUL/DUTIES/WORKFLOW
    spec_dev_engineer.rst
    spec_test_engineer.rst
    spec_agent_structure.rst      <- Meta: Definition Soul/Duties/Workflow
    ...
```

Kein Zusammenwurschteln. Eine Datei pro Agent pro Level.

## Abgrenzung zu heute

| Heute | Neu |
|-------|-----|
| 8 gleichberechtigte Agents | 3 Manager + N Engineers |
| Handoffs in Agent-Frontmatter | Manager orchestriert |
| User ruft jeden Agent direkt | User spricht nur mit Managern |
| Agents beschreiben sich komplett | Soul/Duties/Workflow getrennt gespecct |
| Product != Instance (meist) | Product = Instance (Agent ist generisch genug) |
| Spec beschreibt Agent | Agent IST die Spec (via Soul/Duties/Workflow) |
