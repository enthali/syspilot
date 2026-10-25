# Syspilot Actors

Actor definitions for syspilot v2. Each file describes one actor's identity, guardrails, and operational facts.

## Actor Model

Every Syspilot actor inherits memory, messaging, escalation, and culture from the Jarvis Actor Kernel. Syspilot adds the method-specific role: a public role card defines the actor's domain, responsibilities, character, and perspective; the actor's `context.md` links to that role card and the process registry it follows.

Processes assign artifact ownership, and each Contract Document records current responsibility. Actors use that current state to decide what must become true; Syspilot does not prescribe an actor sequence or duplicate kernel behavior in role-specific workflow prose.

## Roster

| Actor | Domain |
|---|---|
| [Project Manager](Project%20Manager.md) | Strategy, intake, portfolio management |
| [Architect](Architect.md) | Technical architecture, design guidelines |
| [Developer](Developer.md) | Implementation, unit testing |
| [Tester](Tester.md) | Adversarial testing |
| [Quality](Quality.md) | Quality review |
| [Release](Release.md) | Packaging, release delivery |
| [Research](Research.md) | Investigation, technical due diligence |
| [Technical Writer](Technical%20Writer.md) | User-facing product documentation |
| [Admin](Admin.md) | Tools, repository infrastructure, process maintenance |
