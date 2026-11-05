# Example Actors

Generic role cards of the nine persistent Syspilot actors. Setup copies them into an adopting project's `docs/Syspilot Actors/`, where the project owns and adapts them. This file serves the Syspilot documentation build and is not installed, because Setup generates the registry of the adopting project.

Each card here is identical to its counterpart in `docs/Syspilot Actors/` after line-ending normalization, unless the table below declares a deviation with its reason. A test fails on an undeclared difference and on a declared deviation whose cards do not differ.

## Deviations

| Card | Reason |
|---|---|
| Technical Writer | The example-maintenance duty exists only where the example folders exist; an adopting project has neither folder nor an `Example sync` row |

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

```{toctree}
:hidden:

Project Manager
Architect
Developer
Tester
Quality
Release
Research
Technical Writer
Admin
```
