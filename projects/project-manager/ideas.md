# Ideas (intern, noch nicht Issue-reif)

## Idee: Multi-Agent Orchestration Pattern (aus Jarvis gelernt)

**Beobachtung aus Jarvis (2026-04-10):**
In Jarvis hat sich organisch ein Pattern entwickelt das weit ueber das
hinausgeht was wir hier in syspilot bisher hatten:

### Die zwei Rollen — KEINE Spezialagenten!

Wichtig: PM und Developer sind **ganz normale Standard-Copilot-Agenten**.
Keine custom Extension, kein spezielles Framework. Der einzige Unterschied:
- In `.github/copilot-instructions.md` steht welche Rolle sie haben
- Jede Rolle hat ihr eigenes Verzeichnis (`projects/<role>/`)
- Jede Rolle hat ihr eigenes `context.md` (Zustand, Aufgaben, Grenzen)

Das ist das Multi-Project-Management Pattern: jeder Agent = eigenes Projekt.

1. **Project Manager (PM)** — `projects/project-manager/context.md`
   - Plant naechste Changes, diskutiert Features mit User
   - Pflegt roadmap.md, priorisiert Backlog
   - Delegiert Change Requests per `jarvis_sendToSession` an Developer
   - Kein Code, kein Git, keine RST-Aenderungen

2. **Developer** — `projects/developer/context.md`
   - Steuert syspilot Agenten aus (change -> implement -> verify -> memory)
   - Empfaengt Change Requests vom PM per Message Queue
   - Interagiert mit User fuer technische Entscheidungen

### Kommunikation: Jarvis Message Queue

- VS Code Extension registriert LM Tool `jarvis_sendToSession`
- Messages landen in `.jarvis/messages.json` (destination, sender, text, timestamp)
- Jeder Agent kann an jede Session eine Nachricht schicken
- `jarvis_listSessions` listet verfuegbare Sessions (aus state.vscdb)
- Open Source, koennte auch in syspilot genutzt werden

### Hammer 1: UAT Agent laeuft NUR im Background

- `syspilot.uat.agent.md` hat `user-invocable: false`
- Wird ausschliesslich als Subagent vom Change Agent aufgerufen
- Generiert automatisch UAT-Kette: US_UAT_* -> REQ_UAT_* -> SPEC_UAT_*
- User muss nie direkt mit UAT Agent interagieren

### Hammer 2: Autonome Agent-Chain ohne User-Feedback

Entstanden "aus Versehen" — User ging essen, Developer Agent sollte
"mal alleine durchlaufen". Und es funktioniert:

1. User diskutiert mit PM (oder Developer) -> Change-Beschreibung entsteht
2. Developer startet Change Agent als Subagent im Background
3. Change Agent -> Implement Agent -> Verify Agent -> Memory Agent
4. Alles ohne User-Rueckfragen, alles im Background

**Warum das funktioniert:**
- Die Change-Beschreibung war gut genug (vorher durchdiskutiert)
- Per-Level RST Write + MECE Check geben automatisches Quality Gate
- Developer Agent als Orchestrator faengt Fehler ab

**Zwei Sessions weil zwei Aufgaben:**
- PM-Session: "Was machen wir als naechstes?" (Planung)
- Developer-Session: "Fuehre diesen Change aus" (Execution)
- Parallel nutzbar: waehrend Developer Change X ausfuehrt,
  plant PM mit User schon Change Y

### Was bedeutet das fuer syspilot?

**Frage: Braucht syspilot selbst dieses Pattern?**

Option A: syspilot bleibt ein Toolkit (Agenten die man einzeln aufruft)
- Jarvis/andere Projekte bauen die Orchestrierung drumherum
- syspilot liefert die Agenten, das Projekt liefert PM + Developer
- Pro: syspilot bleibt schlank, Orchestrierung ist projektspezifisch

Option B: syspilot liefert ein Orchestrierungs-Pattern mit
- `syspilot.orchestrator` Agent der die Chain steuert
- Message-basierte Kommunikation als optionales Feature
- Pro: Best Practice gleich mitgeliefert, weniger Boilerplate pro Projekt

Option C: Kombi — syspilot + Jarvis als empfohlenes Stack
- syspilot = Spec-Engine (Agenten fuer US/REQ/SPEC)
- Jarvis = Orchestrierung (Message Queue, Sessions, Projects, Heartbeat)
- Pro: Separation of Concerns, beide Produkte haben klare Grenzen
- Con: Zwei Dependencies statt einer

**Tendenz: Option C** — Jarvis ist bereits die Orchestrierungsschicht,
syspilot die Specification Engine. Zusammen decken sie den ganzen
Workflow ab. Jarvis ist Open Source, syspilot auch.

### Beziehung: syspilot ist der Prozess-Spezialist

syspilot = Prozess-Know-how (US/REQ/SPEC, Change-Lifecycle, MECE, Trace)
Jarvis = Projekt-Management-Infrastruktur (Sessions, Messages, Heartbeat)

Jarvis ist ein **Kunde** von syspilot: nutzt syspilot-Agenten um sein
eigenes Projekt zu managen. Und das funktioniert hervorragend.

### Dogfooding: syspilot nutzt Jarvis

syspilot koennte selbst Jarvis als Projekt-Management-Tool nutzen:
- Nicht die Email-Anbindung oder Tasks-Integration (brauchen wir nicht)
- Aber **Messages** fuer Rollen-Kommunikation (PM -> Developer -> QA)
- Und **Heartbeat** fuer automatisierte wiederkehrende Aufgaben

**Beispiel: QA Engineer Rolle mit Heartbeat**
- Woechentlicher Security Check: Heartbeat triggert Analyse
- QA Engineer Agent bewertet Findings
- Bei Handlungsbedarf: QA schickt Change-Vorschlag per Message an Developer
- Developer steuert den Change durch die syspilot-Chain
- Kein manuelles Anstossen noetig — laeuft automatisch

**Weitere Heartbeat-Kandidaten:**
- Dependency Update Check (woechentlich)
- Sphinx-Needs Konsistenz-Check (nach jedem Push)
- MECE-Audit auf allen Ebenen (woechentlich)
- Trace-Completeness-Report (vor jeder Release)

**Effekt:** syspilot waere Vorbild fuer andere Projekte — nicht nur
als Toolkit sondern als lebendes Beispiel wie man syspilot + Jarvis
zusammen nutzt.

**Migration bei Dogfooding:**
- `temp/ideas.md` → `projects/project-manager/ideas.md` (PM besitzt Backlog)
- Roadmap kommt dazu: `projects/project-manager/roadmap.md`
- Developer bekommt `projects/developer/context.md`
- `temp/` wird obsolet — alles was dort lag gehoert dem PM

### Naechste Schritte

- [ ] Jarvis Message Queue als Kommunikations-Pattern dokumentieren
- [ ] `user-invocable: false` Pattern in syspilot Spec aufnehmen
- [ ] Autonome Agent-Chain als supported Modus dokumentieren
  (Voraussetzung: gute Change-Beschreibung, per-level quality gates)
- [ ] Klarstellen: wann braucht man User-Feedback, wann nicht?
- [ ] QA Engineer Rolle fuer syspilot definieren (context.md)
- [ ] Heartbeat-Jobs fuer automatisierte Quality Checks aufsetzen
- [ ] syspilot-Repo mit Jarvis bootstrappen (dogfooding)

## Idee: Learning Skill + Template-First Architektur

**Kern-Erkenntnis (aus ProjectManager uebernommen):**

### Learning Skill als Mandatory Startup

- Standard Skill Format: `.github/skills/syspilot.learning/SKILL.md`
- ZUSAETZLICH: Verankerung in `copilot-instructions.md` als Startup Sequence
  (wie in ProjectManager: "Your FIRST action in every session — read learning skill")
- Ohne Verankerung in Instructions wird der Skill nur on-demand geladen
- Mit Verankerung ist er IMMER aktiv — egal welcher Prompt reinkommt

### Learning endet bei Change Request, nicht bei File-Edit

In ProjectManager: Learning -> File-Edit (knowledge/*.md, skill update)
In syspilot: Learning -> **Change Request**

Warum? Weil bei uns Prozess-Wissen in Specs lebt (RST mit Traceability).
Ein "wir sollten das anders machen" ist kein File-Edit sondern ein formaler
Change durch US -> REQ -> SPEC. Der Learning Loop erkennt die Verbesserung,
formuliert den Change Request, und schickt ihn an den Developer.

Knowledge-Speicherorte in syspilot:
- Prozess-Wissen: Specs (RST) -> Aenderung = Change Request
- Rollen-Wissen: `projects/<role>/context.md` -> direkt editierbar
- Projekt-Wissen: `copilot-instructions.md` -> via @syspilot.memory

### Template-First Architektur (Produkt-Entscheidung)

**syspilot liefert Templates, keine fertigen Implementierungen.**

Jedes Projekt ist anders — unterschiedliche Domaene, andere Rollen,
andere Konventionen. syspilot kann nicht fuer alle die gleiche
Implementierung liefern. Stattdessen:

`syspilot/templates/` = Muster die instanziiert werden
`@syspilot.setup` = Instanziierung fuer ein konkretes Projekt

Beispiele:
- `syspilot/templates/learning-skill.md` -> Projekt instanziiert als
  `.github/skills/syspilot.learning/SKILL.md` mit projekt-spezifischen
  Knowledge-Speicherorten und Change-Request-Routing
- `syspilot/templates/agent-structure.md` -> Template fuer Soul/Duties/Workflow
  das jeder Agent-Autor fuer seinen Agent ausfuellt
- `syspilot/templates/context.md` -> Template fuer Rollen-Context

**Mehr Arbeit fuer Kunden, aber korrekt** — denn jeder Kunde MUSS
seine Domaene selbst einbringen. One-size-fits-all funktioniert nicht
bei Requirements Engineering.

**Konsequenz fuer Issue #7:**
- Agent Structure Template definieren (Soul/Duties/Workflow + Positive Framing)
- Als Template in `syspilot/templates/` ablegen
- Bestehende Agents refactoren als Referenz-Implementierung
- Setup Agent bietet Instanziierung an

## Idee: Research / Spike Mode vor dem Change Workflow

**Problem:**
Nicht alles kann Top-Down spezifiziert werden. Manchmal weiss man nicht
genug ueber ein Thema um sinnvolle US/REQ/SPEC zu schreiben — man muss
erst ausprobieren, experimentieren, verstehen. Beispiele:
- Wie funktioniert ubCode MCP genau? Was liefert es zurueck?
- Wie verhaelt sich sphinx-needs bei breaking changes in einer neuen Version?
- Welche VS Code API brauche ich fuer Feature X?

**Aktuelles Problem:**
Der Change Agent geht sofort in die Spec-Hierarchie (US -> REQ -> SPEC).
Aber wenn das Wissen fehlt um gute Specs zu schreiben, kommt Muell raus.
"Fake it till you make it" in Specs fuehrt zu Draft-Specs die spaeter
komplett neu gemacht werden muessen — Aufwand ohne Mehrwert.

**Idee: `@syspilot.research` Agent (oder Research-Modus)**

Input: Eine Forschungsfrage oder ein Thema ("Wie kann ich ubCode MCP
       fuer Traceability-Queries nutzen?")

Output: Ein strukturiertes Research-Dokument (`docs/research/<name>.md`)
        mit Findings, Entscheidungen, offenen Fragen

Uebergang zu Change:
- Research-Dokument enthaelt am Ende: "Empfehlung: Change X anlegen"
- Klarer Prompt / Briefing fuer den Change Agent wird generiert
- `@syspilot.change` bekommt das Research-Dokument als Kontext-Input

**Abgrenzung zu Change:**
- Research = Erkunden, Ausprobieren, Lernen (kein RST-Output)
- Change = Spezifizieren, Entscheiden, Umsetzen (RST-Output)
- Research endet mit einem Change-Briefing, nicht mit Specs

**Moegliche Formen:**
1. Eigener Agent `@syspilot.research` — strukturiert die Erkundung
2. Research-Prompt der an den Explore-Subagenten delegiert
3. Research-Dokument-Template in `syspilot/templates/research.md`
   das manuell befuellt und dann an Change Agent uebergeben wird

**Konkrete Faelle wo das gebraucht wird:**
- Issue #13 (ubCode MCP): Erst verstehen wie die API funktioniert,
  dann spezifizieren wie syspilot sie nutzt
- Neue sphinx-needs Features: Erst ausprobieren, dann in Specs nutzen
- Neue VS Code Agent-Features (z.B. `agents:` Frontmatter)

**Kern-Anforderung: Konsistenz der Change-Empfehlung**

Waehrend der Research-Phase entstehen inkrementell Erkenntnisse — Dinge
die funktionieren, Dinge die nicht gehen, Ueberraschungen. Das Research-
Dokument muss diese Erkenntnisse konsistent buendeln und am Ende eine
kohaerente Change-Empfehlung formulieren. Das heisst:

- Die Empfehlung kann auf jeder Ebene ansetzen: User Story, Requirement
  oder Design Spec — je nachdem worauf die Research abzielt
- Die Change-Empfehlung muss in sich konsistent sein. Ueberholte
  Erkenntnisse muessen NICHT dokumentiert werden — ausser sie sind
  relevant als "so nicht"-Warnung fuer den Change Agent (z.B.
  "Ansatz X funktioniert nicht weil Y")
- Die Change-Empfehlung am Ende muss aus den dokumentierten Findings
  logisch folgen — kein Sprung von "wir haben X getestet" zu "wir
  empfehlen Y" ohne Begruendung
- Das Research Paper ist ein Entscheidungslog mit Zeitachse:
  Finding 1 -> Finding 2 -> Erkenntnis -> Empfehlung
- Der Change Agent muss das Paper als Input akzeptieren und die
  Empfehlung als Ausgangsbasis fuer die Spec-Hierarchie verwenden

**Beispiel-Ablauf:**
1. Research: "Wie funktioniert ubCode MCP?" -> Findings ueber API
2. Erkenntnis: "query_needs liefert gefilterte Needs, aber kein
   Traceability-Graph" -> das beeinflusst SPEC-Level-Design
3. Empfehlung: "Neuer SPEC fuer MCP-basierte Queries + Aenderung an
   REQ_TRACE_VERIFICATION um MCP als Datenquelle zu erlauben"
4. `@syspilot.change` bekommt Paper -> startet bei REQ-Level (nicht US)

**Status:** Fruehe Idee. Stufe 1 waere ein einfaches Template das den
Forscher durch eine strukturierte Research Session fuehrt und am Ende
ein Change-Briefing generiert. Kein eigener Agent noetig fuer Stufe 1.

## Idee: User Expertentest (UAT / Expert Review Phase)

**Konzept:**
Eine formale "User Expertentest"-Phase im syspilot-Workflow, bei der ein
Domänenexperte oder der Auftraggeber die implementierten Änderungen gegen
die ursprünglichen Anforderungen testet — bevor die Release geht.

**Beobachtet in Jarvis-Projekt:**
Dort bereits implementiert. Jarvis als Referenz-Implementierung ansehen
und das Pattern nach syspilot zurückportieren.

**Abgrenzung zu Verify Agent:**
- `@syspilot.verify` = technische Verifikation (Code gegen Spec)
- User Expertentest = fachliche Validierung (Verhalten gegen User-Intent)
- Das ist der Unterschied zwischen Verification und Validation (V&V)

**Mögliche Integration:**
- Eigener Agent `@syspilot.validate` (oder als Phase im Verify Agent)?
- Checklist-basiert: für jede US ein Prüfszenario das der Experte manuell durchläuft
- Output: signierter Validation Report (analog zu val-<name>.md)

**Nächster Schritt:**
Jarvis-Implementierung anschauen und als Grundlage für syspilot-Spec nutzen.

## Idee: Change Document Consistency Check als Subagent nach MECE Check

**Problem:**
Vor der Uebergabe an den Implement Agent — also nach dem MECE Check aber
noch innerhalb des Change Agent Workflows — wird das Change Document nicht
auf Konsistenz mit den tatsaechlich geschriebenen RSTs geprueft. In der Praxis entsteht dort Drift:
- RSTs wurden per-level geschrieben und dann nochmal angepasst
- Change Document spiegelt nicht mehr den tatsaechlichen End-Zustand wider
- IDs die im Change Doc stehen existieren evtl. nicht (mehr) in den RSTs
- IDs die in den RSTs stehen fehlen evtl. im Change Doc

**Idee:**
Neuer Agent oder Subagent: `@syspilot.consistency` (o.ae. Name)
- Liest das Change Document
- Vergleicht alle erwahnten IDs gegen die tatsaechlichen RST-Inhalte
- Prueft: Ist jedes Item aus dem Change Doc auch in den RSTs? Stimmen Status, Links?
- Prueft: Gibt es RST-Aenderungen (via git diff) die NICHT im Change Doc erwaehnt sind?
- Output: Konsistenz-Report oder "alles passt"

**Einhaengepunkt:**
Nach dem MECE Advisory pro Level — also als letzter Schritt im Level Write
Protocol, nachdem MECE Findings angezeigt und (ggf.) abgearbeitet wurden.
Der Consistency Check prueft dann: "Stimmt das Change Document noch mit dem
was wir gerade in die RSTs geschrieben haben ueberein?"
Alternativ: zusaetzlich nochmal am Ende nach dem Final Consistency Check.

**Abgrenzung:**
- `@syspilot.mece` = horizontale Konsistenz INNERHALB einer Ebene
- `@syspilot.trace` = vertikale Traceability eines Elements
- `@syspilot.verify` = Code gegen Spec
- Neuer Agent = Change Document gegen RST-Realitaet

**Nächster Schritt:**
Konkrete Faelle aus Jarvis sammeln wo dieser Check etwas gefunden haette.

## Idee: Change Agent fuehrt MECE-Pruefung als Subagent aus

**Konzept:** Nach dem Sphinx-Needs-Build im Change-Workflow soll der
Change Agent den MECE Agent als Subagent aufrufen, um die Konsistenz
der gerade geaenderten Ebene automatisch zu pruefen.

**Problem mit aktuellem Ablauf:**
Aktuell schreibt der Change Agent die RST-Dateien erst ganz am Ende, wenn
alle Ebenen im Change Document durchlaufen sind. Das heisst:
- Waehrend der Analyse gibt es keine aktuellen RSTs zum Pruefen
- Sphinx-Needs-Build und MECE-Pruefung koennen erst nach finaler Umsetzung laufen
- Traceability-Links existieren noch nicht wenn die naechste Ebene bearbeitet wird
- Das ist auch Teil des Problems aus Issue #6 (fehlende Subsystem-Constraint-Traversal)

**Idee: RST-Schreiben pro Ebene statt am Ende:**
1. Change Agent analysiert Ebene (z.B. Level 1 Requirements) im Change Document
2. User approved die Ebene
3. Change Agent schreibt die RSTs fuer diese Ebene sofort
4. Sphinx-Needs-Build laeuft -> Traceability-Links sind verfuegbar
5. MECE Agent wird als Subagent aufgerufen fuer die gerade geschriebene Ebene
6. Bei Findings: Change Agent zeigt Ergebnisse, Korrekturen moeglich
7. Weiter zur naechsten Ebene (mit funktionierenden Links!)

**Vorteile gegenueber heute:**
- Traceability ist bei jeder Ebene schon da -> Issue #6 wird mit adressiert
- MECE-Pruefung pro Ebene statt nur am Ende
- Fehler werden frueher gefunden
- Jede Ebene ist nach Approval sofort in den RSTs manifestiert

**Offene Fragen:**
- Was passiert wenn eine spaetere Ebene Aenderungen an einer frueheren erfordert?
  (Heute kein Problem weil alles erst am Ende geschrieben wird)
- Rollback-Strategie: Wenn Level 2 scheitert, muessen Level 1 RSTs zurueckgerollt werden?
- Oder reicht es, bei Rueckwaerts-Navigation die RSTs einfach zu aktualisieren?
- Zusammenspiel mit Issue #6: Kann beides in einem Change geloest werden oder besser getrennt?

**Nachtrag: Erfahrung aus Kundenprojekt (Jarvis) bestaetigt das Problem:**

Der aktuelle Workflow hat ein fundamentales Traceability-Loch:
1. Change Agent arbeitet im Change Document (Markdown, nicht sphinx-needs-traceable)
2. Implement Agent uebertraegt ins RST (sphinx-needs-traceable)
3. Dabei wird das Change Document nochmal angepasst
4. Ergebnis: Change Document und RSTs divergieren, Traceability geht verloren

**Das Kernproblem:** Das Change Document ist NICHT traceable ueber
sphinx-needs. Es ist ein temporaeres Arbeitsartefakt in Markdown, aber
die eigentliche Traceability lebt nur in den RSTs. Solange der Change Agent
nur im Change Document arbeitet, existiert keine maschinelle Traceability.

**Radikalere Alternative: RSTs als primaeres Arbeitsmedium**
- Change Agent schreibt direkt die RSTs (nicht erst das Change Document)
- Git zeigt was geaendert wurde (diff als "Change Log")
- Change Document wird zur kompakten Zusammenfassung / Entscheidungslog
  statt zum primaeren Arbeitsartefakt
- Vorteil: Traceability ist von Anfang an da, kein Uebertragungsschritt
- Risiko: Sphinx-Needs-Build koennte bei unfertigen RSTs brechen
  (z.B. Links auf IDs die noch nicht existieren)

**Spannungsfeld:**
- RSTs direkt schreiben = sofortige Traceability, aber Build-Risiko
- Change Document zuerst = sauberer Entwurfsprozess, aber Traceability-Loch
- Hybrid (pro Ebene, siehe oben) = Kompromiss, aber komplexer Workflow

**Entscheidung:** Muss im Zusammenhang mit Issue #6 geloest werden.
Alle drei Ideen (MECE-Subagent, RST-pro-Ebene, RST-als-primaer) haengen
zusammen und sollten als kohaerentes Paket durchdacht werden.

**Tendenz: Option 1 (RSTs direkt) mit Build bei Ebenenuebergang**

Argumentation:
- Wir arbeiten top-down: US -> REQ -> SPEC
- Links gehen immer nach unten: REQ `:links:` US (outgoing von REQ zu US)
- Von US nach REQ gibt es keine outgoing Links — US existieren zuerst
- Daher: RSTs direkt schreiben bricht den Build NICHT, weil wir nie
  auf IDs linken die erst spaeter kommen
- Sphinx-Needs-Build bei jedem Ebenenuebergang (nicht nach jedem einzelnen
  Need), also: US schreiben -> Build -> REQ schreiben -> Build -> SPEC schreiben -> Build
- Build validiert dass alle Links aufloesen und keine Fehler entstanden sind
- Wenn Build fehlschlaegt: Korrektur bevor naechste Ebene beginnt

**Warum das die sauberste Loesung ist:**
- Traceability ist sofort da wenn die naechste Ebene beginnt (loest Issue #6!)
- Change Agent kann Links traversieren um Kontext fuer die naechste Ebene zu holen
- MECE-Pruefung pro Ebene wird moeglich (Subagent-Idee, siehe oben)
- Kein Traceability-Loch mehr — RSTs sind die Single Source of Truth
- Git diff zeigt exakt was geaendert wurde
- Change Document wird zum Entscheidungslog / Zusammenfassung, nicht
  zum primaeren Datentraeger

**Restrisiko:**
- Innerhalb einer Ebene: Wenn ein neues REQ auf ein anderes neues REQ
  linkt das noch nicht geschrieben ist -> Build-Fehler. Aber: das waere
  ein horizontaler Link, die sind selten und koennen nachtraeglich ergaenzt
  werden.
- Rueckwaerts-Aenderungen: Wenn SPEC-Analyse zeigt dass ein REQ falsch ist,
  muss REQ geaendert und neu gebaut werden. Aufwaendiger als im Change Doc,
  aber dafuer ist die Aenderung sofort traceable.

**Naechster Schritt:** Als Change fuer Issue #6 formalisieren. Betrifft
primaer den Change Agent Workflow (spec_change.rst) und den Implement
Agent (der dann weniger Uebertragungsarbeit hat).

## Idee: Agent-Chaining via `agent:` Syntax (Subagent-Automatisierung)

**Kontext:** GH Copilot unterstuetzt `agent:` Aufrufe — Agenten koennen andere
Agenten als Subagenten starten. Interessant fuer Agenten die keine User-Interaktion
benoetigen.

**Kandidaten fuer automatischen Subagent-Aufruf:**

1. **Memory als Subagent von Verify**
   - Wenn verify erfolgreich -> memory automatisch ausfuehren
   - Memory hat nie Fragen an den User, rein analytisch
   - Handoff-Chain wird kuerzer: `change -> implement -> verify(+memory) -> release`
   - Verify hat den vollen Kontext ueber alle Aenderungen, ideal fuer Memory

2. **MECE + Trace als Subagenten von Change**
   - Change Agent nutzt MECE fuer semantischen Konsistenzcheck seiner Arbeit
   - Change Agent nutzt Trace fuer vertikale Vollstaendigkeitspruefung
   - Ergaenzt die Idee "RST-Schreiben pro Ebene" (siehe oben)
   - Beide Agenten sind read-only, kein Risiko

**Allgemeines Muster:**
- Agenten OHNE User-Fragen eignen sich als automatische Subagenten
- Agenten MIT User-Fragen bleiben eigenstaendige Workflow-Schritte
- Jeder Subagent-Kandidat bleibt auch manuell aufrufbar (standalone)

**Status:** Fruehe Idee. Erst den `agent:` Mechanismus in der Praxis testen,
dann entscheiden welche Kombinationen sinnvoll sind.

**Abwaegung:** Potenziell fuer v0.3.0 zusammen mit Issue #6, aber nur wenn
der Scope beherrschbar bleibt. Lieber wenige solide Aenderungen pro Release.

**Verankerung:** Erweiterung/Umbau von SYSPILOT_REQ_CHG_ANALYSIS_AGENT +
SYSPILOT_SPEC_CHANGE_WORKFLOW. Eventuell neues REQ unter Change-Theme.
Design in spec_change.rst.

## Idee: Agent-Handover sauber spezifizieren (Issue #8)

**Konzept:** Die Uebergaben zwischen Agents sind aktuell nur teilweise
formal spezifiziert. Das sollte im Rahmen von Issue #8 (Agent-Workflow-
Dokumentation) sauber aufgeraeumt werden.

**Was bereits definiert ist:**
- Hauptkette change -> implement -> verify -> memory in SYSPILOT_SPEC_AGENT_WORKFLOW
- YAML-Handoffs in allen .agent.md-Dateien (label, target agent, prompt)
- Verify-Verzweigung (PASSED -> memory, PARTIAL -> implement, FAILED -> change)
- Quality-Agents (mece <-> trace) bidirektional + handoff zu change

**Was fehlt:**
- **Datenuebergabe:** Nirgends formal spezifiziert *welche Daten* uebergeben werden
  (Change Document Pfad, Verification Report Pfad, etc.)
- **Vorbedingungen:** Wann ist ein Change Document "ready for implement"?
  Wann darf Verify starten? Nur implizit, nicht als Precondition spezifiziert.
- **Fehlerpfade:** Was passiert wenn Implement das Change Document nicht findet?
  Wenn sphinx-build nach dem Schreiben fehlschlaegt? Keine Error-Handoff-Specs.
- **Release-Handoffs:** Nur Sketch-Level, Rueck-Handoffs bei Validierungsfehlern fehlen.
- **Entscheidungstabelle Verify -> Implement vs. Change:** Spec sagt "depending on
  severity", aber keine formale Entscheidungsregel.

**Zusammenhang mit anderen Ideen:**
- Zentraler Project Manager Agent (oben) koennte die Handover-Orchestrierung uebernehmen
- RST-Schreiben pro Ebene (oben) aendert den Change->Implement-Handover grundlegend
- Eventuell Issue #8 + diese Idee + MECE-Subagent-Idee zusammen angehen

**Verankerung:** Erweiterung von SYSPILOT_SPEC_AGENT_WORKFLOW +
alle agenten-spezifischen Specs (spec_change, spec_implement, spec_verify,
spec_memory, spec_release). Eventuell neues REQ unter WF-Theme.

## Idee: Issue-Lifecycle und Backlog-Governance

**Problem:**
Issues werden teilweise direkt auf kuenftige Releases gemappt, obwohl sie
noch nicht durchdacht oder entschieden sind. Einige Issues sind eigentlich
noch auf Ideen-Level, andere kommen aus anwendenden Projekten und sind
eher Feature Requests als konkrete Changes.

**Beobachtungen:**
- Nicht jedes Issue ist ein Change — manche sind Ideen, Beobachtungen,
  oder Feedback aus Konsumenten-Projekten
- Fruehes Release-Mapping erzeugt falschen Druck und cluttered Milestones
- Es fehlt eine klare Trennung zwischen "Idee", "analysierter Change",
  und "committed fuer Release X"

**Einfache Loesung: 2 Stages**
1. **Next Release** — Urgent, klar, wird aktiv angegangen.
   Milestone zuweisen.
2. **Backlog** — Alles andere. Kein Milestone, kein Release-Mapping.
   Wird erst "Next Release" wenn explizit entschieden.

**Logik:** Sobald ein Change Document existiert, ist das Issue quasi
schon in Arbeit — dann ist der Weg zum Release kurz. Die eigentliche
Entscheidung ist vorher: "Machen wir das jetzt oder nicht?"
Alles was nicht aktiv bearbeitet wird, bleibt im Backlog ohne Milestone.

**Zusammenhang mit anderen Ideen:**
- Project Manager Agent (oben) koennte Triage und Reifegrad-Tracking uebernehmen
- Release Agent braucht klare Regeln welche Issues "ready" sind
- Betrifft auch wie anwendende Projekte Feedback/Wuensche einbringen

**Status:** Noch offen. Erst Muster beobachten, dann entscheiden ob
Labels, Discussions, oder ein formaler Prozess der richtige Weg ist.

## Idee: Setup Agent liest README und fragt nach Projektkontext

**Problem:**
Wenn syspilot zum ersten Mal in einem Projekt eingerichtet wird (via
`@syspilot.setup`), hat der Agent keinen Kontext darueber worum es in dem
Projekt eigentlich geht. Die Docs existieren noch nicht, und die einzige
vorhandene Informationsquelle — die README — wird nicht ausgewertet.

**Beobachtung:**
Beim ersten Einsatz in einem neuen Projekt waere es hilfreich, wenn der
Setup Agent:
1. Die README.md (falls vorhanden) liest und daraus Projektkontext ableitet
2. Falls keine README existiert oder sie zu duenn ist: den User kurz fragt
   worum es in dem Projekt geht (Domaene, Zweck, Zielgruppe)
3. Diesen Kontext nutzt um z.B. sinnvolle initiale User Stories oder
   zumindest eine Grundstruktur fuer die Docs vorzuschlagen

**Offene Fragen:**
- Wie weit soll der Setup Agent gehen? Nur Kontext sammeln, oder gleich
  initiale Specs (US/REQ) vorschlagen?
- Soll der Kontext irgendwo persistent abgelegt werden (z.B. in einer
  Projekt-Beschreibung in den Instance-Docs)?
- Zusammenspiel mit dem Change Agent: Waere es besser, Setup nur die
  Grundstruktur anlegen zu lassen und dann einen initialen Change fuer
  die ersten User Stories zu triggern?
- Wie viel soll der Agent automatisch ableiten vs. explizit nachfragen?

**Status:** Fruehe Idee. Erfahrungen aus weiteren Projekt-Setups sammeln,
dann konkreter spezifizieren.

## Idee: Setup Agent zeigt konkrete naechste Schritte nach Erstinstallation

**Problem:**
Nach dem ersten `@syspilot.setup` schlaegt der Agent aktuell nur vor:
"Starte `@syspilot.change` um deinen ersten Change Request zu erstellen."
Das ist zu unspezifisch — ein neuer User weiss nicht *was* er als Erstes
aendern sollte und in welcher Reihenfolge er vorgehen soll.

**Beobachtung:**
Nach dem Setup gibt es typischerweise mehrere Dinge die angepasst werden
muessen, bevor das Projekt produktiv mit syspilot arbeiten kann:

1. **Initiale User Stories / Requirements erstellen** — Das Projekt hat
   nach Setup nur die Verzeichnisstruktur, aber keine inhaltlichen Specs.
   Der erste Change sollte die grundlegenden User Stories fuer das Projekt
   anlegen (-> haengt mit der README-Idee oben zusammen).

2. **Instance-Specs anpassen** — Die vom Setup kopierten Instance-Specs
   (z.B. Release-Prozess, Branching-Strategie) sind generisch und muessen
   auf das konkrete Projekt zugeschnitten werden.

3. **Implement Agent anpassen** — Der generische Implement Agent weiss
   nicht wie das Projekt gebaut wird (Sprache, Build-System, Test-Framework).
   Instance-Level Design Specs fuer den Implement-Workflow fehlen.

4. **Release Agent anpassen** — Generischer Release-Prozess passt selten
   1:1. Versionierung, Changelog-Format, CI/CD Pipeline, Deployment-Ziel
   muessen projektspezifisch konfiguriert werden.

5. **Memory Agent / copilot-instructions.md** — Die initiale
   copilot-instructions.md ist nach Setup minimal. Sollte frueh mit
   projektspezifischen Konventionen gefuellt werden.

**Idee:**
Der Setup Agent gibt am Ende eine strukturierte "Getting Started" Checkliste
aus, z.B.:

```
Setup abgeschlossen! Empfohlene naechste Schritte:

1. @syspilot.change — Erstelle deine ersten User Stories
   (Beschreibe worum es in deinem Projekt geht)

2. @syspilot.change — Passe den Release-Prozess an
   (Versionierung, Branch-Strategie, CI/CD)

3. @syspilot.change — Definiere den Implement-Workflow
   (Sprache, Build-System, Test-Strategie)

4. @syspilot.memory — Aktualisiere copilot-instructions.md
   mit projektspezifischen Konventionen
```

**Offene Fragen:**
- Soll die Checkliste statisch sein oder dynamisch anhand dessen was der
  Setup Agent vorfindet (README, vorhandene CI-Config, package.json etc.)?
- Sollen die naechsten Schritte als Issues angelegt werden oder reicht
  eine Konsolenausgabe?
- Zusammenspiel mit der README-Idee: Wenn Setup den Projektkontext kennt,
  kann er gezieltere naechste Schritte vorschlagen.
- Wie granular? Zu viele Schritte auf einmal ueberfordern, zu wenige
  lassen den User orientierungslos.

**Status:** Fruehe Idee. Eng verknuepft mit der README/Projektkontext-Idee
oben — idealerweise zusammen angehen.

## Idee: Family-Unterverzeichnis bei Kundenprojekten hinterfragen

**Problem:**
Der Setup Agent legt bei einem neuen Projekt die Verzeichnisstruktur
`docs/syspilot/userstories/`, `docs/syspilot/requirements/`, etc. an.
Das `syspilot`-Unterverzeichnis ist der **Family-Name** — das ergibt Sinn
fuer das syspilot-Produkt selbst (multi-family-faehig), aber fuer ein
typisches Kundenprojekt ist das verwirrend und unnoetig.

**Warum es so ist:**
Das Family-Konzept stammt aus der Idee dass ein Repo mehrere Produktfamilien
enthalten koennte (`docs/family_a/`, `docs/family_b/`). Die Methodology
schreibt es so vor, und der Setup Agent setzt es 1:1 um.

**Warum es fuer Kundenprojekte nicht passt:**
- Ein typisches Kundenprojekt hat genau EINE Produktfamilie — das Projekt selbst
- `docs/syspilot/userstories/` suggeriert dass die User Stories fuer syspilot
  sind, nicht fuer das Kundenprojekt
- Der zusaetzliche Ordner-Level (`docs/<family>/`) ist ein Indirection ohne
  Mehrwert wenn es nur eine Family gibt
- Neue User fragen sich sofort: "Warum steht da syspilot?"

**Moegliche Loesungen:**

1. **Family-Name = Projektname** — Setup Agent fragt den Projektnamen und
   legt `docs/<projektname>/` an statt `docs/syspilot/`. Semantisch korrekt,
   aber immer noch ein Extra-Level.

2. **Flache Struktur fuer Single-Family** — Wenn nur eine Family existiert,
   direkt `docs/userstories/`, `docs/requirements/`, `docs/design/` ohne
   Family-Unterverzeichnis. Einfacher, aber bricht mit dem Multi-Family-Konzept.

3. **Family-Level optional machen** — In der Methodology konfigurierbar:
   Single-Family-Projekte nutzen flache Struktur, Multi-Family-Projekte
   nutzen Unterverzeichnisse. Setup Agent fragt oder erkennt es automatisch.

## Idee: Test-Phase zwischen Implement und Verify

**Problem:**
Die aktuelle Handoff-Chain ist: `change -> implement -> verify -> memory`.
Zwischen Implement und Verify fehlt eine explizite **Test-Phase**. Zwar
testet der Implement Agent schon selbst (Unit Tests als Teil der Implementierung),
aber es gibt keinen formalen Schritt fuer:
- Integration Tests
- Build-Validierung (baut das Projekt noch?)
- User/Acceptance Tests
- Ausfuehren eines Testplans gegen alle Changes

**Was heute passiert:**
- Implement Agent schreibt Code und fuehrt ggf. Unit Tests aus
- Verify Agent prueft ob die Implementierung zum Change Document passt
- Aber: Niemand prueft systematisch ob die Changes als Ganzes funktionieren
- Kein formaler Testplan, kein Testbericht

**Was fehlt:**
1. **Testplan erstellen** — Pro Change (oder pro Release?) ein Testplan der
   beschreibt was getestet werden muss. Integrationsszenarien, nicht nur
   Unit-Level. Wer schreibt den? Change Agent? Eigener Test Agent?
2. **Build + Test ausfuehren** — Projekt bauen, Tests laufen lassen,
   Ergebnisse sammeln. Automatisierbar wenn CI/CD vorhanden.
3. **User Test / Acceptance** — Manche Changes brauchen manuelles Testen.
   Agent kann den User durch den Testplan fuehren und Ergebnisse dokumentieren.
4. **Testbericht** — Artefakt das den Teststatus dokumentiert. Analog zum
   Validation Report von Verify.

**Wo im Workflow?**

Option A: **Implement -> Test -> Verify**
- Test prueft ob es funktioniert (funktional korrekt)
- Verify prueft ob es zum Change Document passt (traceability korrekt)
- Verify koennte den erfolgreichen Testlauf als Vorbedingung pruefen
- Saubere Trennung: Test = funktional, Verify = formal

Option B: **Implement -> Verify -> Test**
- Verify prueft zuerst Traceability und Vollstaendigkeit
- Test kommt danach als finaler Quality Gate
- Problem: Wenn Tests fehlschlagen, muss zurueck zu Implement — aber
  Verify hat schon "approved"?

Option C: **Test ist Teil von Verify**
- Verify wird erweitert um Test-Ausfuehrung
- Ein Agent macht beides: formale Pruefung + funktionale Tests
- Einfacher, aber Verify wird sehr gross

**Einschaetzung:** Option A klingt am saubersten. Verify wird zum finalen
Gate das auch den Testbericht prueft. Die Chain waere dann:
`change -> implement -> test -> verify -> memory`

**Offene Fragen:**
- Eigener Test Agent oder Erweiterung von Implement/Verify?
- Testplan-Erstellung: Teil des Change Documents (Level 2 SPEC enthaelt
  Akzeptanzkriterien) oder eigenes Artefakt?
- Wie mit Projekten umgehen die kein Test-Framework haben?
  (Reine Doku-Projekte wie syspilot selbst?)
- Testplan pro Change oder pro Release? Bei Release-Bundling muessten
  alle Changes zusammen getestet werden.
- CI/CD Integration: Agent triggert Pipeline oder fuehrt Tests lokal aus?
- A-SPICE Alignment: SWE.6 (Software Qualification Test) mapt hierauf —
  wie stark wollen wir uns daran orientieren?

**Status:** Fruehe Idee. Grundlegende Workflow-Erweiterung die gut
durchdacht werden muss. Haengt zusammen mit der Agent-Handover-Idee
(formale Vorbedingungen zwischen Agents) und dem A-SPICE Alignment.

**KISS-Warnung:** Ein vollstaendiger Test Agent ist ein Riesenprojekt fuer
sich. Nicht ueberengineeren! Stufenplan:

**Stufe 1 (Minimalstart — eigener Agent, aber simpel):**
- Eigener `@syspilot.test` Agent
- Input: Change Document (was wurde geaendert)
- Output: Kurze Zusammenfassung was manuell getestet werden soll
- User fuehrt den Test manuell durch und bestaetigt Ergebnis
- Agent dokumentiert das Testergebnis (PASS/FAIL + Notizen)
- Kein formaler Testplan, kein Testframework, kein Automatismus
- Einfach: "Hier ist was du testen solltest, hast du's gemacht, hat's geklappt?"

**Stufe 2 (spaeter):**
- Implement Agent fuehrt nach dem Schreiben `build + test` aus
- Test Agent prueft ob Build/Tests erfolgreich waren
- Einfache automatisierte Tests (Unit Tests die Implement schreibt)

**Stufe 3 (viel spaeter):**
- Formale Testplaene, Testrun-Tracking
- Integration Tests
- Automatisierte Testreports

**Stufe 4 (ferne Zukunft):**
- HIL Tests, System-Level Tests
- CI/CD Integration
- A-SPICE SWE.6 Alignment

Schrittweise erweitern, nicht Big Bang. Stufe 1 reicht um die Luecke
zwischen Implement und Verify zu schliessen.

**Erfahrung aus Kundenprojekt (Jarvis):**
Erster manueller Test dort gerade im Aufbau — bestaetigt dass Stufe 1
(manueller Test mit kurzer Beschreibung) der richtige Einstieg ist.

4. **Immer Family-Name, aber korrekt** — Bei `syspilot.setup` den Family-Name
   als Pflichtparameter abfragen. Dann steht wenigstens der richtige Name da.
   Mindest-Aufwand, Konzept bleibt konsistent.

**Zusammenhang mit anderen Ideen:**
- README/Projektkontext-Idee: Wenn der Setup Agent den Projektnamen kennt,
  kann er den Family-Name automatisch setzen (Loesung 1 oder 4)
- Instance-Verzeichnis `docs/inst/syspilot/` hat das gleiche Problem —
  dort steht "syspilot" fuer die Family deren Agents installiert werden,
  das ist eigentlich korrekt (Instance OF syspilot), aber trotzdem verwirrend

**Status:** Fruehe Idee. Beruehrt die Methodology grundlegend — muss gut
durchdacht werden bevor es ein Change wird. Loesung 4 waere der kleinste
sinnvolle Schritt.

**Nachtrag: Betrifft auch Sphinx-Needs ID-Prefixe!**

Das Family-Thema beschraenkt sich nicht auf Verzeichnisse — es betrifft
genauso die Sphinx-Needs IDs. Beobachtet bei einer Jarvis-Installation:
Der Change Agent leitet aus den Naming Conventions ab: `JARVIS_US_EXP_...`,
`JARVIS_REQ_EXP_...`, etc. — Projektname wird zum Family-Prefix.

Das ist *technisch* korrekt (Projektname = Family-Name), aber:
- Es passiert implizit, nicht als bewusste Entscheidung des Users
- Der User wird nie gefragt "Wie soll dein Family-Prefix heissen?"
- Bei Projekten mit langem Namen wird der Prefix unhandlich
  (`HELLO_WORLD_EXPLORER_US_NAV_...`)
- Naming Conventions (namingconventions.md) definieren das Schema
  `<FAMILY>_<TYPE>_<THEME>_<SLUG>` — aber wer setzt `<FAMILY>`?
- Aktuell leitet der Agent es selbst ab, ohne explizite Bestaetigung

**Loesung (gleich wie oben):**
Beim Setup den Family-Name/Prefix explizit abfragen und bestaetigen lassen.
Dann ist sowohl das Verzeichnis (`docs/<family>/`) als auch der ID-Prefix
(`<FAMILY>_US_...`) konsistent und vom User bewusst gewaehlt.

Das verstaerkt Loesung 4 oben: Family-Name als Pflichtparameter im Setup
ist nicht nur "nice to have" fuer Verzeichnisse, sondern **notwendig**
damit die Sphinx-Needs IDs sinnvoll sind.

**Weitergedacht: Family-Prefix ist fuer Kundenprojekte oft ueberfluessig!**

In einem Single-Family-Kundenprojekt braucht man eigentlich gar keinen
Family-Prefix. `US_NAV_SIDEBAR` ist klarer als `JARVIS_US_NAV_SIDEBAR`.
Der Prefix existiert nur um Families in einem Multi-Family-Repo zu
unterscheiden — wenn es nur eine Family gibt, ist er reiner Ballast.

Vorschlag: Der Setup Agent sollte die **Naming Convention interaktiv mit
dem Nutzer festlegen** und das Ergebnis sofort in der
`copilot-instructions.md` dokumentieren. Konkret:

1. Setup Agent fragt: "Moechtest du einen Prefix fuer deine Spec-IDs?"
   - Option A: Kein Prefix → `US_<THEME>_<SLUG>`, `REQ_<THEME>_<SLUG>`
     (empfohlen fuer Single-Family-Projekte)
   - Option B: Projekt-Prefix → `<PREFIX>_US_<THEME>_<SLUG>`
     (fuer Multi-Family oder wenn der Kunde es so will)
2. Setup Agent fragt nach initialen Themes (oder schlaegt welche vor
   basierend auf README/Projektkontext)
3. Setup Agent schreibt die festgelegte Konvention in
   `copilot-instructions.md` → Alle Agents kennen ab sofort das Schema
4. Optional: `docs/namingconventions.md` (oder Instance-Variante) wird
   ebenfalls generiert

**Warum in copilot-instructions.md?**
- Jeder Agent liest diese Datei automatisch
- Naming Conventions sind *die* Information die Agents staendig brauchen
- Kein Agent muss raten oder aus den RSTs reverse-engineeren wie IDs
  aufgebaut sind
- Aenderungen an der Konvention wirken sofort auf alle Agents

**Wie es bei syspilot selbst geloest ist (NICHT 1:1 uebertragbar!):**
- `docs/namingconventions.md` — Framework-Level (ID-Format, Slug-Regeln)
- `docs/syspilot/namingconventions.md` — Family-spezifisch (Themes, Beispiele)
- Diese Zweiteilung existiert weil syspilot selbst multi-family-faehig ist

**Fuer Kundenprojekte:** Nur EINE `docs/namingconventions.md` die alles
enthaelt — ID-Format, Themes, Slug-Regeln, Beispiele. Kein Family-Level
Unterverzeichnis, keine Indirektion. Ein Kundenprojekt hat eine Family,
also eine Naming Convention.

Der Setup Agent sollte:
1. Interaktiv Naming Convention festlegen (Prefix ja/nein, Themes, Slug-Stil)
2. Eine einzige `docs/namingconventions.md` generieren (alles in einem Dokument)
3. Kurzfassung + Verweis in `copilot-instructions.md` eintragen

**Auswirkung auf die Methodology:**
- `<FAMILY>_` Prefix wird optional statt mandatory
- namingconventions.md muss angepasst werden (Prefix als "recommended
  for multi-family, optional for single-family")
- Alle Specs die das ID-Schema hart verdrahten muessen geprueft werden

**Status:** Wichtige Idee — adressiert mehrere Probleme gleichzeitig
(Verzeichnisstruktur, ID-Prefixe, Agent-Kontext). Sollte zusammen mit
README-/Projektkontext-Idee und Getting-Started-Checkliste als ein
kohaerentes "Setup v2" Paket angegangen werden.

## Idee: Learn / Critical Reviewer Agent

**Problem:**
Prozesse und Design-Entscheidungen laufen nicht immer perfekt. Aktuell
gibt es keinen systematischen Feedback-Loop der aus Fehlern lernt und
Verbesserungen vorschlaegt. Wenn ein Workflow holpert, ein Agent-Handoff
nicht sauber laeuft, oder ein Design-Pattern sich als suboptimal herausstellt,
bleibt das Wissen im Kopf des Users — nicht im System.

**Konzept: `@syspilot.review` oder `@syspilot.learn` Agent**

Zwei Facetten, moeglicherweise ein Agent mit zwei Modi:

**1. Prozess-Review (Retrospektive):**
- Input: Ein abgeschlossener Workflow (Change -> Implement -> Verify Zyklus)
- Analysiert: Was hat gut funktioniert? Wo gab es Reibung?
- Liest: Change Document, Validation Report, git log, Agent-Outputs
- Output: Konkrete Verbesserungsvorschlaege fuer Prozess/Agents/Specs
- Beispiel: "Der Change Agent hat bei Level 2 den Kontext verloren weil
  die Traceability-Links noch nicht da waren" -> Verbesserung vorschlagen

**2. Design-Review (Kritische Analyse):**
- Input: Ein bestimmtes Design-Artefakt (Spec, Architecture, Workflow)
- Analysiert: Konsistenz, Vollstaendigkeit, Einfachheit, Skalierbarkeit
- Geht ueber MECE hinaus: MECE prueft Struktur, Review prueft Qualitaet
- Stellt unbequeme Fragen: "Brauchen wir das wirklich?" "Ist das zu komplex?"
- Output: Findings mit Empfehlungen (keep / simplify / rethink / remove)

**Abgrenzung zu existierenden Agents:**
- MECE Agent: Prueft strukturelle Vollstaendigkeit (Luecken, Ueberlappungen)
- Verify Agent: Prueft Implementation gegen Spec (Korrektheit)
- Review Agent: Prueft ob Prozess und Design *gut* sind (Qualitaet, Eleganz)
- Trace Agent: Folgt Links vertikal (Vollstaendigkeit der Kette)
- Review Agent: Hinterfragt ob die Kette *sinnvoll* ist

**Moegliche Trigger:**
- Manuell: User ruft `@syspilot.review` auf nach einem Workflow
- Nach Verify: Automatisch als optionaler Schritt wenn Verify Probleme findet
- Periodisch: Vor einem Release als "Gesundheitscheck"
- Ad-hoc: "Review mal unser Naming-Konzept" oder "Was lief bei Issue #6 schief?"

**Offene Fragen:**
- Ein Agent mit zwei Modi oder zwei separate Agents (process-review vs design-review)?
- Wo speichert der Agent seine Findings? Eigenes Artefakt? ideas.md? Issues?
- Wie vermeidet man Scope Creep? Der Agent soll hinterfragen, nicht umbauen
- Zusammenspiel mit Memory Agent: Review-Findings -> Memory-Updates?
- Manueller Trigger reicht fuer Stufe 1, Automatisierung spaeter

**Status:** Fruehe Idee. Passt zum wachsenden Projekt — je mehr Agents
und Prozesse es gibt, desto wertvoller wird ein systematischer Review.
KISS: Stufe 1 waere ein einfacher Agent der nach einem Workflow 3-5
konkrete Verbesserungsvorschlaege macht. Nicht mehr.

**Konkretes Beispiel aus der Praxis (Jarvis):**
Eine Spec enthielt relevantes Verhalten als "Begleittext" unterhalb der
Acceptance Criteria — aber nicht als eigenstaendige Spec/Need formalisiert.
Ergebnis: Der Change Agent hat die Information nicht gefunden, weil er
nur nach expliziten sphinx-needs Elementen sucht. Das Wissen war da,
aber nicht als traceable Need sichtbar.

Genau das wuerde ein Design-Review Agent finden:
- "Diese Spec enthaelt Implementierungsdetails im Freitext die eigentlich
  eine eigene SPEC sein sollten"
- "Verhaltensanforderung X steht nur als Prosatext, nicht als Need —
  nicht traceable, nicht testbar"
- Pattern: Freitext in RST der sphinx-needs-Elemente enthaltene Details
  beschreibt → Kandidat fuer Extraktion als eigenes Need

Das ist ein Qualitaetsproblem das weder MECE (Struktur) noch Verify
(Implementation) noch Trace (Links) finden wuerden — nur ein inhaltlicher
Review der prueft ob alles was spezifiziert sein sollte auch als Need
formalisiert ist.

## Offene Frage: Wie wird der Critique Agent getriggert?

Haengt eng mit der Learn/Review Agent Idee zusammen. Zwei grundsaetzliche
Ansaetze:

**Option A: Manuell**
- User ruft `@syspilot.critique` auf wenn er will
- Vorteil: Kein Overhead beim normalen Arbeiten
- Nachteil: Wird vergessen, besonders bei Quick Fixes unter Zeitdruck
  (genau dann wenn er am meisten helfen wuerde!)
- Variante: Als Pflichtschritt in der Workflow-Chain — aber dann ist
  es halbautomat nicht manuell

**Option B: Automatisch getriggert**
- Nach jedem git commit? Nach jedem Implement-Lauf?
- Vorteil: Kann nicht vergessen werden
- Nachteil: Nervt bei kleinen/offensichtlichen Aenderungen, verlangsamt
  den Workflow, False Positives
- Variante: Nur triggern wenn bestimmte Dateitypen geaendert wurden
  (z.B. .agent.md ohne zugehoerige .rst Aenderung = Alarm)

**Option C: Heuristik-basiert (smart trigger)**
- Critique Agent wird vorgeschlagen wenn:
  - Agent-Datei geaendert aber kein neues/geaendertes Change Document
  - Prod-Dateien (syspilot/) geaendert aber kein Sphinx-Build danach
  - Verify-Lauf hat Luecken gefunden
  - git commit enthaelt "fix", "patch", "quick" im Message
- Vorteil: Nur wenn es Sinn macht
- Nachteil: Heuristik kann falsch liegen, komplex zu implementieren

**Option D: Post-Commit Hook / CI**
- Als Git Hook oder CI-Step
- Ausserhalb des Agent-Workflows
- Vorteil: Immer ausgefuehrt, unabhaengig vom User
- Nachteil: Technisch aufwaendiger, nicht in VS Code integriert

**Tendenz:** Option C fuer Stufe 1 — smart trigger wenn offensichtliche
Prozessabweichungen erkannt werden. Option A als Fallback ("hab ich was
vergessen?"). Option B/D fuer spaeter wenn Muster sich zeigen.

**Kernerkenntnis:** Der Critique Agent ist am wertvollsten genau dann
wenn man ihn NICHT aufrufen will — unter Zeitdruck, bei Quick Fixes,
bei "das ist nur eine kleine Aenderung". Der Trigger-Mechanismus muss
das abfangen ohne nervig zu sein. Schwieriges Gleichgewicht.

**Framing hilft:** Der Critique Agent IST der nervige QA-Kollege der
immer dann in die Quere kommt wenn man es gerade nicht brauchen kann.
Und GENAU das ist sein Job. Das Framing sollte bewusst so sein —
nicht "helpful assistant" sondern "unbequemer Wachhund".

## Idee: Continuous Improvement Loop (aus Critique Agent Findings)

**Problem:**
Wenn der Critique/Review Agent einen Prozessfehler findet — was passiert
dann? Aktuell: nichts Systematisches. Der User fixt es, und dasselbe
Muster kann beim naechsten Mal wieder passieren.

**Zwei Kategorien von Findings:**

1. **Lokaler Prozessfehler** — "Du hast einen Agent gepatcht ohne
   Change Document." Fix: Prozess nachziehen (Change Doc, Sphinx-Build,
   Verify). Einmalig, kein systemisches Problem.

2. **Systemisches syspilot-Problem** — "Dieser Fehler passiert immer
   wieder weil der Prozess es zu leicht macht ihn zu machen." Beispiel:
   Ein Agent macht Quick Fixes so verlockend dass der formale Weg
   umgangen wird. Fix: syspilot selbst muss verbessert werden.

**Idee: Findings-Klassifikation**
- Critique Agent klassifiziert jeden Fund: LOCAL | SYSTEMIC
- SYSTEMIC-Findings landen automatisch als Issue (oder in ideas.md)
- SYSTEMIC-Pattern ueber mehrere Findings hinweg = starkes Signal fuer
  einen Change an syspilot selbst

**Idee: Retrospektive pro Release**
- Vor jedem Release: Alle Critique-Findings seit letztem Release anschauen
- Pattern: Was wurde immer wieder gefunden? -> syspilot-Change
- Input fuer den PM Agent / Release Planning

**Zusammenhang mit anderen Ideen:**
- Memory Agent koennte Critique-Findings persistent speichern
- PM Agent koennte SYSTEMIC-Issues automatisch in den Backlog aufnehmen
- Review Agent + Continuous Improvement + PM Agent = vollstaendiger
  Feed-Back-Loop: Arbeiten -> Fehler erkennen -> Lernen -> Verbessern

**KISS fuer Stufe 1:**
- Critique Agent gibt am Ende jedes Findings an ob es LOCAL oder SYSTEMIC ist
- SYSTEMIC = Empfehlung "Erwaege ein GitHub Issue zu erstellen"
- Kein Automatismus, kein komplexes Tracking — nur die Klassifikation

**Status:** Fruehe Idee. Haengt komplett am Critique/Review Agent der
selbst noch nicht existiert. Aber das Konzept klar halten fuer wenn
der Agent gebaut wird.

## Issue #16 Nachfolger: Post-Update Review funktioniert nicht zuverlaessig

**Beobachtet (2026-04-08, Dennis Jarvis-Projekt):**
Beim letzten syspilot-Update wurde wieder eine projektspezifische Aenderung
in einer Prozessdatei ueberschrieben — obwohl v0.3.1 genau das verhindern sollte
(Post-Update Extension Review, SYSPILOT_SPEC_INST_POST_UPDATE_REVIEW).

**Was erwartet war:**
Setup Agent sollte nach dem Ersetzen einer methodology-owned Datei die alte
Version mit `git show HEAD:<path>` vergleichen, projektspezifische Ergaenzungen
erkennen und den User warnen/fragen.

**Was passierte:**
Die Erkennung hat nicht oder nicht ausreichend angeschlagen — die
projekteigene Aenderung wurde stillschweigend geloescht.

**Root Cause (konkret ermittelt):**
Datei: `syspilot.verify.agent.md` — enthielt ein projektspezifisches Test-Skript.
Der Post-Update-Review-Vergleich (`git show HEAD:<path>` vs neue Version) hat
CRLF (Windows) vs LF (Unix) Zeilenenden als einzigen Unterschied erkannt und
daraus geschlossen: "keine inhaltliche Aenderung" — und damit die
projektspezifischen Ergaenzungen stillschweigend geloescht.

**Das eigentliche Problem:**
Der Diff-Algorithmus in der Erkennungslogik ist nicht line-ending-agnostisch.
Er behandelt CRLF/LF-Unterschiede als "kein Diff" statt korrekt zu normalisieren
und dann inhaltlich zu vergleichen.

**Fix-Ansatz:**
- Beim Vergleich Line Endings normalisieren (z.B. `git diff --ignore-cr-at-eol`
  oder explizite Normalisierung vor dem Diff)
- Alternativ: `.gitattributes`-bewusster Vergleich
- SYSPILOT_SPEC_INST_POST_UPDATE_REVIEW muss explizit fordern dass der
  Vergleich line-ending-agnostisch erfolgt

**Naechste Schritte:**
- Neues Issue erstellen (oder #16 reopenen mit diesem konkreten Bug)
- SYSPILOT_SPEC_INST_POST_UPDATE_REVIEW anpassen: AC fuer line-ending-agnostischen Diff
- Setup Agent Implementierung fixen

**Prioritaet:** Hoch — betrifft Kundenprojekte direkt

## Idee: Test Engineer Persona + Manual Release Tests

**Beobachtung aus Jarvis-Projekt:**
Statt eines eigenstaendigen Test-Agents wurde eine andere Herangehensweise
ausprobiert: Eine **Test Engineer Persona** die in bestehende Workflows
eingebettet ist, und explizite **Manual Release Tests** als erstes konkretes
Test-Artefakt.

**Was das bedeutet:**

*Test Engineer Persona:*
- Keine eigene Agent-Datei, sondern eine Rolle/Perspektive die ein Agent
  einnehmen kann ("Als Test Engineer betrachte ich diese Aenderung...")
- Kann im Change Agent aktiviert werden: "Schreibe Akzeptanzkriterien aus
  Testperspektive" statt nur aus Entwicklerperspektive
- Oder als separater Copilot Custom Instruction / Prompt der die Perspektive
  einnimmt

*Manual Release Tests:*
- Testplan der pro Release beschreibt was manuell getestet werden muss
- Keine automatisierten Tests, keine Test-Frameworks
- Einfach: "Vor dem Release pruefe diese Szenarien manuell"
- Wird vom Verify Agent oder vom Test Agent ausgefuehrt (fragt User durch)

**Warum das interessant ist:**
- Persona-Ansatz ist leichtgewichtiger als ein eigener Agent
- Manual Release Tests sind das KISS-Aequivalent zu einem Testplan
- Loest das sofortige Problem (was testen wir vor dem Release?)
  ohne Ueberengineering
- Erfahrung in Jarvis: Funktioniert in der Praxis

**Zusammenhang mit Test-Phase Idee (oben):**
- Ergaenzt die "Stufe 1" Idee (manueller Test Agent)
- Persona-Ansatz koennte die Implementierung von Stufe 1 vereinfachen:
  Kein neuer Agent noetig, sondern Persona-Erweiterung bestehender Agents
- Release Tests als erstes konkretes Artefakt, dann iteratively erweitern

**Offene Fragen:**
- Persona als Prompt/Instruction oder als Agent-Erweiterung?
- Wo lebt der Manual Release Test Plan? Im Change Document? Eigene Datei?
- Wie wird die Persona aktiviert — explizit durch User oder automatisch
  bei bestimmten Workflow-Schritten?

**Status:** Praxiserfahrung aus Jarvis bestaetigt den Ansatz. Sollte
als Weiterentwicklung der Test-Phase Idee formalisiert werden — eventuell
direkt als Change fuer den Test-Agent (Stufe 1) aufgreifen.

## Idee: Persona-basiertes Arbeiten in syspilot

**Beobachtung:**
In Jarvis wurden Personas eingefuehrt (User, Developer, Test Engineer)
und sofort war klar: verschiedene Perspektiven erzeugen bessere Ergebnisse.
syspilot hat das implizit (Agents = Rollen) aber nirgends explizit.

**Kern-Erkenntnis: Agent ≠ Persona, aber sie haengen zusammen**

Personas sind Perspektiven/Rollen, Agents sind Werkzeuge. Ein Agent kann
mehrere Personas aktivieren, und eine Persona kann von mehreren Agents
genutzt werden.

**Personas fuer syspilot:**

| Persona | Perspektive | Worauf achtet sie? |
|---------|------------|-------------------|
| User | Endnutzer-Sicht | Verstaendlichkeit, Nutzbarkeit |
| Developer | Implementierungs-Sicht | Machbarkeit, Einfachheit, Testbarkeit |
| Test Engineer | Test-Sicht | Testbarkeit, Akzeptanzkriterien, Edge Cases |
| Validation Engineer | Formale Sicht | Traceability, Vollstaendigkeit, Spec-Konformitaet |
| Release Engineer | Auslieferungs-Sicht | Kompatibilitaet, Migration, Breaking Changes |
| Project Manager | Planungs-Sicht | Prioritaet, Abhaengigkeiten, Roadmap |
| Architect | Struktur-Sicht | Konsistenz, Skalierbarkeit, Einfachheit |
| QA / Critique | Kritische Sicht | Was kann schiefgehen? Was fehlt? |

**Wo Personas verankern — zwei Ebenen:**

1. **In User Stories:** "As a <PERSONA>, I want..." — Die User Stories
   werden ab sofort aus der Perspektive der jeweiligen Persona geschrieben.
   Das ist der natuerlichste Ort, macht die Stories konkreter und zwingt
   zum Perspektivwechsel.

2. **In Agent-Files (Soul):** Jeder Agent bekommt ganz vorne seine
   Persona(s) definiert — "Du bist der Developer. Deine Aufgabe ist..."
   Das ist die "Soul"-Idee: Agenten haben eine Identitaet, nicht nur
   eine Aufgabenliste.

**Implement und Test trennen — Developer ≠ Test Engineer:**

Starkes Argument aus der QA-Welt: Der Tester sollte nicht der
Implementierer sein. Wenn Test und Implement verschiedene Agents sind:
- Implement (Developer Persona): Schreibt Code, Unit Tests, baut das Feature
- Test (Test Engineer Persona): Prueft Akzeptanzkriterien, schreibt
  Testfaelle aus ANDERER Perspektive
- Beide koennen quasi parallel/autonom laufen
- Die Requirements werden automatisch besser weil zwei verschiedene
  Perspektiven sie lesen und validieren
- Der Test Engineer findet Luecken die der Developer nicht sieht
  (und umgekehrt)

**Zusammenhang mit bestehenden Ideen:**
- Test-Phase Idee (oben): Test Engineer Persona ist die Basis fuer
  den Test Agent, egal ob eigener Agent oder Persona-Erweiterung
- Review/Critique Agent: QA Persona, systematisch kritisch
- PM Agent (#14): Project Manager Persona
- Agent-Unifikation: Soul + Sections + projektspezifischer Inhalt =
  einheitliches Agent-Modell

**Moeglicher Einstieg:**
1. Personas in den existierenden User Stories einfuehren (Review + Rewrite)
2. Agent-Files mit Soul-Section versehen (Persona-Definition ganz vorne)
3. Implement/Test-Trennung als naechsten grossen Architektur-Change
4. Projekte koennen eigene Personas definieren (z.B. Safety Engineer
   im Automotive, UX Designer bei Consumer-Produkten)

**Status:** Gute Idee mit Praxisbestaetigung aus Jarvis. Betrifft die
Methodology fundamental — User Story Format, Agent-Struktur, Workflow.
Koennte zusammen mit Agent-Unifikation (v0.4.0?) angegangen werden.
Einstieg ueber User Stories ist der natuerlichste und niedrigschwelligste Weg.

**Artefakt: Persona-Agent Matrix als Doku-Seite**

Neues Dokument (z.B. `docs/personas.md` oder `docs/syspilot/personas.md`)
das die Persona-Landschaft beschreibt:

1. **Persona-Katalog** — Wer sind die Rollen, was ist ihre Perspektive:

| Persona | Perspektive | Worauf achtet sie? |
|---------|------------|-------------------|
| User | Endnutzer-Sicht | Verstaendlichkeit, Nutzbarkeit |
| Developer | Implementierungs-Sicht | Machbarkeit, Einfachheit, Testbarkeit |
| Test Engineer | Test-Sicht | Testbarkeit, Akzeptanzkriterien, Edge Cases |
| Validation Engineer | Formale Sicht | Traceability, Vollstaendigkeit, Spec-Konformitaet |
| Release Engineer | Auslieferungs-Sicht | Kompatibilitaet, Migration, Breaking Changes |
| Project Manager | Planungs-Sicht | Prioritaet, Abhaengigkeiten, Roadmap |
| Architect | Struktur-Sicht | Konsistenz, Skalierbarkeit, Einfachheit |
| QA / Critique | Kritische Sicht | Was kann schiefgehen? Was fehlt? |

2. **Persona-Agent Mapping** — Welche Persona lebt in welchem Agent:

| Agent | Primaere Persona | Sekundaere Persona(s) |
|-------|-----------------|----------------------|
| `@syspilot.change` | Architect | User (US-Level) |
| `@syspilot.implement` | Developer | — |
| `@syspilot.test` (neu) | Test Engineer | — |
| `@syspilot.verify` | Validation Engineer | — |
| `@syspilot.release` | Release Engineer | — |
| `@syspilot.pm` (neu) | Project Manager | — |
| `@syspilot.mece` | Architect | QA / Critique |
| `@syspilot.trace` | Validation Engineer | — |
| `@syspilot.review` (neu) | QA / Critique | Architect |
| `@syspilot.memory` | — (Meta-Agent) | — |
| `@syspilot.setup` | — (Infrastruktur) | — |

3. **Persona im Workflow** — Wann welche Perspektive aktiv ist:

```
User Story:     User + Architect
Requirements:   Architect + Developer + Test Engineer
Design:         Developer + Architect
Implement:      Developer
Test:           Test Engineer
Verify:         Validation Engineer
Release:        Release Engineer
Review:         QA / Critique
```

4. **Projekt-spezifische Personas** — Projekte koennen eigene Personas
   definieren (Safety Engineer, UX Designer, Domain Expert etc.) und
   bestehenden Agents zuordnen.

Dieses Dokument waere die "Personas" Seite in der Doku, verlinkt aus
architecture.md und methodology.md. Agents referenzieren es fuer ihre Soul.

**Wichtig: Change Agent NICHT zerteilen!**

Der Change Agent ist bewusst ein Multi-Persona Agent:
- Requirements Manager (Was brauchen wir?)
- Architect (Wie strukturieren wir es?)
- Designer (Wie sieht die Loesung aus?)

Das ist kein Designfehler — das ist ein Feature. Die Ende-zu-Ende-
Verantwortung im Change Agent hat einen riesigen Vorteil: Kontext bleibt
erhalten ueber die gesamte Session. Die Persona-Wechsel (von US/User-Sicht
zu REQ/Architect-Sicht zu SPEC/Designer-Sicht) sind fliessend, der
Kontextverlust beim Umschalten ist minimal.

Wuerde man den Change Agent in drei Agents zerteilen (Req Manager,
Architect, Designer), muesste man bei jedem Handoff den kompletten
Kontext uebergeben — und genau DAS ist das Problem das wir bei
Implement->Verify schon kennen (Change Document als Bruecke).

**Regel:** Agents zerteilen wenn die PERSPEKTIVE fundamental verschieden
ist (Developer vs. Test Engineer — die SOLLEN anders denken). Agents
NICHT zerteilen wenn es derselbe Denkprozess in verschiedenen
Granularitaetsstufen ist (User Story -> Requirement -> Design = ein
zusammenhaengender analytischer Prozess).

**Multi-Persona Agents (OK):**
- Change Agent: Req Manager + Architect + Designer (ein Analyseprozess)
- MECE Agent: Architect + QA (ein Pruefprozess)

**Getrennte Agents (besser):**
- Implement vs. Test (verschiedene Denkweisen, absichtlich)
- Implement vs. Verify (Macher vs. Pruefer, absichtlich)
