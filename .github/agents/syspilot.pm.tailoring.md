# syspilot.pm — Tailoring for the syspilot project

## Deviation Detection

If you detect a contradiction between the pm.agent.md standard workflow, this
tailoring document, and observed current practice — stop and clarify with the
user before proceeding. Do not silently adopt the current practice as the new
norm.

## Backlog

GitHub Issues (enthali/syspilot) is the single source of truth for the backlog.
No separate backlog file.

## One CR at a Time

Send one CR to CM, wait for merge confirmation, then send the next.
CM is a change executor — planning and sequencing stay in the PM session.

## QM Sign-off

Wait for a **direct message from Quality Manager** before merging.
Do not accept CM-relayed QM clearance — only a direct QM inbox message counts.

## Post-Release Distribution

After the Release Agent completes its work (version bump, changelog, tag), PM
triggers the **syspilot Setup Agent** to install the latest release into this
repository. Releases are active pull operations — there is no automatic CD push.

## Change Document Location

Change documents are placed in `docs/changes/<version>/` where `<version>` is
the target release version. The directory must exist before committing the
change document. Create it if needed.

## Infrastructure Changes

Tooling, CI, Sphinx config, and release pipeline changes are **not spec-driven**.
- PM creates a feature branch + lightweight change document (L0-L2 sections marked "N/A — infrastructure change")
- PM implements directly (does not send to CM)
- QM review is still performed
- PM merges to `experimental` after QM sign-off
