# Syspilot Actors

Actor definitions for syspilot v2. Each file describes one actor's identity, guardrails, and operational facts.

## Actor Model

Every Syspilot actor inherits memory, messaging, escalation, and culture from the Jarvis Actor Kernel. Syspilot adds the method-specific role: a public role card defines the actor's domain, responsibilities, character, and perspective; the actor's `context.md` links to that role card and the process registry it follows.

Processes assign artifact ownership, and each Contract Document records current responsibility. Actors use that current state to decide what must become true; Syspilot does not prescribe an actor sequence or duplicate kernel behavior in role-specific workflow prose.

## Roster

| Actor | Domain |
|---|---|
| [Syspilot Project Manager](Syspilot%20Project%20Manager.md) | Strategy, intake, portfolio management |
| [Syspilot Architect](Syspilot%20Architect.md) | Technical architecture, design guidelines |
| [Syspilot Developer](Syspilot%20Developer.md) | Implementation, unit testing |
| [Syspilot Tester](Syspilot%20Tester.md) | Adversarial testing |
| [Syspilot Quality](Syspilot%20Quality.md) | Quality review |
| [Syspilot Release](Syspilot%20Release.md) | Packaging, release delivery |
| [Syspilot Research](Syspilot%20Research.md) | Investigation, technical due diligence |
| [Syspilot Technical Writer](Syspilot%20Technical%20Writer.md) | User-facing product documentation |
