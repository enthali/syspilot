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

## GitHub Issue Lifecycle (Board + Reminder Pattern)

This project tracks work on **GitHub Project "Syspilot" #5** (board fields: Status, Priority).
GitHub Issues are PM-owned end-to-end — no other agent opens, edits, or closes them.

**After PM merges a feature branch into `development` (Step 13):**
- Set the board Status of every tracked issue (`gh project item-edit … --single-select-option-id`) to **"Merged"**.
  Field ID: `PVTSSF_lAHOAFDYiM4Bdr-CzhYLwvE` (Status); option ID for Merged: add this field via the board UI first, then record the option ID here.
- Leave the GitHub Issue **open** — it is not done until released.

**After SEND to Release Agent (Step 15):**
- Set a `jarvis_setReminder` for yourself: `"Check CI on main for release; if green, close issues #X #Y ... with release notes link."`, deliverAt: ~30 min after expected release completion.

**At reminder delivery:**
- Run `gh run list --repo enthali/syspilot --branch main --limit 5` and verify the latest workflow run concluded successfully.
- If green: close each tracked issue with a comment referencing the GitHub Release URL and the `docs/releasenotes.md` version anchor. Closing triggers the board's "Item closed" automation → Status flips to **Done** automatically.
- If red: do not close. Escalate to the user.

**Board field IDs for reference (do not re-query unless project is rebuilt):**
- Project node ID: `PVT_kwHOAFDYiM4Bdr-C`
- Status field ID: `PVTSSF_lAHOAFDYiM4Bdr-CzhYLwvE`
- Priority field ID: `PVTSSF_lAHOAFDYiM4Bdr-CzhYLwvw`
- Priority options: P0=`79628723`, P1=`0a877460`, P2=`da944a9c`
- Status options: Backlog=`f75ad846`, Ready=`61e4505c`, In progress=`47fc9ee4`, In review=`df73e18b`, Merged=`d5c9819d`, Done=`98236657`
- **WIP limit on "In progress": 1** — if a second item needs to go "In progress", something is wrong; resolve the active CR first. Epics are never set to "In progress" — use Backlog as their standing status (progress is visible via sub-issues #54, #55).
- Merged=`d5c9819d`

## Infrastructure Changes

Tooling, CI, Sphinx config, and release pipeline changes are **not spec-driven**.
- PM creates a feature branch + lightweight change document (L0-L2 sections marked "N/A — infrastructure change")
- PM implements directly (does not send to CM)
- QM review is still performed
- PM merges to `experimental` after QM sign-off
