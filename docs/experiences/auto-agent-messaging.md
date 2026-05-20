# Auto Agent Messaging with Jarvis Sessions

**Topic:** How to run messages between agent sessions automatically

## Versions

| Component | Version |
|-----------|---------|
| VS Code | 1.121 |
| Jarvis | 0.5.11 |
| syspilot | 0.5.5 |
| Sphinx | 9.1.0 |
| sphinx-needs | 8.0.0 |

---

## The Situation

When I run multiple AI agent sessions in parallel — a Change Manager, a Quality Manager, a Project Manager — they are isolated by design. Each has its own context window. They can't see each other.

But in a real workflow, they need to talk. QM needs to tell PM that a check failed. CM needs to notify PM that a branch is ready for merge. PM needs to approve or hold.

The naive solution is: I relay messages manually. That works for a demo. It doesn't scale.

## What Jarvis Provides

Jarvis is a VS Code extension that adds a persistent message queue between named chat sessions. Instead of the user playing telephone, an agent can call `jarvis_sendToSession("Quality Manager", "...")` and the message sits in a queue until the QM session picks it up with `jarvis_readMessage("Quality Manager")`.

With **Jarvis 0.5.11**, named sessions are the communication unit. I open a chat, give it a name, and it's addressable. That's it — no extra configuration needed.

One important detail: Jarvis lets me control message delivery **per agent session**. I can choose between two modes:

- **Manual approval** — incoming messages are held in the queue and I release them one by one. Useful when I want to review what an agent is about to receive before it acts on it.
- **Automatic delivery** — messages are delivered immediately when the session is active. The agent processes them without waiting for me.

When I run a change, I keep the PM session on **manual approval** and all other agents on **automatic**. This lets me follow the flow of a change at my own pace and align with the PM on sequencing before the next message is processed.

## How It Works in Practice

I run the syspilot change workflow across three separate VS Code chat sessions:

- **Project Manager** — strategic decisions, CR authoring, merge approval
- **Change Manager** — workflow execution, branch management, engineer delegation
- **Quality Manager** — independent quality checks, findings reports

I send a CR to CM via `jarvis_sendToSession`. CM works, then sends completion + change document path to both PM and QM. QM checks and sends findings to me as PM. I decide fix/defer/accept and send the merge decision back to CM. CM merges and confirms to me.

No manual relay. I only watch the PM session — everything else runs in the background.

## What to Watch Out For

**Cross-talk is real.** When I asked QM for a re-check and QM had already sent the result, both messages arrived in my inbox. The second one said "already sent, messages crossed." I now read until `remaining = 0`, process each message, and ignore confirmed duplicates.

**Sessions must be open.** A message queued to "Quality Manager" sits in the queue indefinitely if no QM session is running. This is intentional (async) but means I need all sessions active before triggering a multi-agent workflow.

**Agent names in messages must match exactly.** `jarvis_sendToSession` uses the session name as-is. "quality manager" ≠ "Quality Manager". I established a naming convention early and stuck to it.

**Direct notification shortcuts cause problems.** In one early run, CM notified QM directly (step 9 in the CM workflow) instead of routing through me as PM. This worked fine for async Jarvis — but it would break entirely for a synchronous (`runSubagent`) variant of the workflow, where only I can block-and-wait on QM results. If I ever want to run synchronously, I need to enforce PM as the single orchestration point from the start, even when async works without it.

## The Payoff

Once it's running, the multi-session async pattern feels surprisingly natural. I see a Jarvis notification, read my inbox, make a decision, reply. The other sessions do their work independently. It feels less like "prompting an AI" and more like managing a small team over a message queue.

The overhead of setting it up — naming conventions, message formats, read loops — is real but one-time. After the first few CRs, it becomes routine.

## Bonus: Running a Multi-Change Sequence Overnight

Working with PM on new ideas generates a backlog fast. One change leads to the next — old concepts need adjusting, new patterns emerge. Before I know it there are nine changes lined up.

One evening, late, backlog at nine, important day ahead, I just typed to the PM:

> *"Hey, I'm going to bed now. You know the process — as soon as you get QM approval, merge and kick off the next change. Have fun, see you tomorrow morning."*

I switched PM to automatic delivery and went to bed.

It works. PM handles it. QM checks each change, PM evaluates findings, approves merges, triggers the next CR. The queue drains while I sleep.

Try it.


