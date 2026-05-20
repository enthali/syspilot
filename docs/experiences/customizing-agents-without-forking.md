# Customizing Agents Without Forking

**Topic:** How to adapt agent behavior for your project without touching the agent files

## Versions

| Component | Version |
|-----------|---------|
| VS Code | 1.121 |
| Jarvis | 0.5.11 |
| syspilot | 0.5.5 |

---

## The Temptation

The Change Manager does something I don't like. Maybe it's too verbose. Maybe it skips
a step I care about. Maybe I want it to always use a specific branch prefix.

The natural reflex: open `.github/agents/syspilot.cm.agent.md`, find the line, change it.

That reflex is wrong.

## Why That Hurts Later

syspilot ships agent files. When there's an update — a new workflow step, a fixed prompt,
a vocabulary migration — the Setup Agent writes new files into `.github/agents/`. Your
edits are gone. No merge, no warning.

There's also a subtler problem: you forget what you changed. Six months later, something
behaves differently than expected. You stare at the agent file trying to remember if that
line was always there or if you put it there.

Agent files are not configuration. They are product.

## The Better Way: `context.md`

Every Jarvis session has a `context.md`. It lives at
`.jarvis/sessions/<SessionName>/context.md`.

When a session starts, Jarvis injects this file into the agent's context. The agent reads
it, and if it contains instructions that override the default behavior, the agent follows
them. The agent file itself never changes.

Your `context.md` is yours. syspilot updates never touch it.

## What Jarvis 0.5.11 Added

In the Jarvis panel, clicking the book icon next to a session opens its `context.md`
directly. You can read and edit the agent's project-specific instructions at any time
without leaving VS Code. But you don't have to. you can also ask your agent to maintain it based on your instructions

`.jarvis/` is per-installation private — it belongs in `.gitignore` and it's up to you whether it gets committed. It's your local workspace. Depening on your processes and preferences, you might choose to commit it (for team visibility or auditability) or ignore it (for personal overrides). Either way, it's separate from the agent files that syspilot manages.

## Other Approaches

If you're not using Jarvis, you still have options:

- **VS Code Memory** (`/memories/`) — works well, and the agent reads it automatically.
  Downside: it lives outside your repository. If you work across machines or share a
  project with others, the memory is not there. Matter of taste.
- **`.instructions.md`** — VS Code evaluates these files and injects them as context.
  Good for static project conventions ("always use TypeScript strict mode"). Less suited
  for per-agent behavioral overrides.
- **Custom prompt files** — You can build a wrapper prompt that calls the agent and
  prepends your project context. Works, but puts the maintenance burden on you.

The `context.md` approach via Jarvis is my preference because it keeps the override
close to the session it affects, visible in the UI, and completely separate from the
agent definition.

## The Rule

`.github/agents/` belongs to syspilot. `.jarvis/` belongs to you.

I wouldn't recommend editing the files in `.github/agents/` to adapt behavior for your project. Put your
project-specific instructions where the agent update cycle can't reach them.

## How Do You Actually Do It?

Tell your agent — in its session — what you want changed about the process. Then ask it
to record that in the `context.md`.

That's it.

For example, I once told my Change Manager:

> *"From now on, always create the branch with the prefix `feature/` before you open the Change Document. >Remember that in your context.md."*

The CM wrote the instruction into `.jarvis/sessions/Change Manager/context.md`. Every
subsequent session, it starts with that instruction already loaded. I never touched the
agent file.

The beauty of this: the agent is the one who writes the override, in its own words, in
the right place. You don't have to know the file path or the format. Just ask.
