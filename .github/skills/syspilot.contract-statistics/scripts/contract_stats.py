"""Usage record of one Contract, from the local Copilot session store and git.

Reads the session store read-only and writes .syspilot/stats/<contract>-stat.md.
Exits non-zero and writes nothing when the store is missing, the window start
cannot be determined, or the window holds no usage.
"""
import argparse
import re
import sqlite3
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

STORE = Path.home() / ".copilot" / "session-store.db"
ACTOR_RE = re.compile(r'Actor "([^"]+)"')
START_GATES = ("Contract release", "Release start")
IDLE_GAP_SECS = 300


class StatsError(Exception):
    """A cause that ends the run without a record."""


def _run_git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8")


def git(repo, *args):
    out = _run_git(repo, *args)
    if out.returncode != 0:
        raise StatsError(f"git {' '.join(args[:2])} failed: {out.stderr.strip()}")
    return out.stdout


def parse_ts(value):
    """Parse ISO or SQLite timestamps into aware UTC datetimes."""
    value = value.strip().replace(" ", "T")
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def locate_contract(repo, name):
    """Newest path of the Contract file, found across all branches."""
    out = git(repo, "log", "--all", "--format=", "--name-only", "--", f"*/{name}.md", f"{name}.md")
    paths = [line for line in out.splitlines() if line.strip()]
    if not paths:
        raise StatsError(f"No file named {name}.md in the git history; pass --start or --contract-file.")
    return paths[0]


def file_history(repo, path):
    """(sha, author time, path at that commit) of the file's commits across all branches, oldest first."""
    out = git(repo, "log", "--all", "--follow", "--name-only", "--format=@@%H\t%aI", "--", path)
    rows = []
    for block in out.split("@@")[1:]:
        head, *names = block.splitlines()
        sha, when = head.split("\t")
        names = [n for n in names if n.strip()]
        rows.append((sha, parse_ts(when), names[0] if names else path))
    return list(reversed(rows))


def version_text(repo, sha, path):
    out = _run_git(repo, "show", f"{sha}:{path}")
    return out.stdout if out.returncode == 0 else ""


def gate_approved(text):
    """True when the start gate row carries a status that starts with `approved`."""
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] in START_GATES and cells[-1].lower().startswith("approved"):
            return True
    return False


def holds_quality(text):
    return bool(re.search(r"^\*\*Current responsibility:\*\*\s*Quality\b", text, re.MULTILINE))


def find_marker(repo, path, predicate):
    """First commit in the file history whose version satisfies the predicate, as (sha, time) or None."""
    for sha, when, path_then in file_history(repo, path):
        if predicate(version_text(repo, sha, path_then)):
            return sha, when
    return None


def active_secs(spans):
    """Gaps between consecutive calls up to IDLE_GAP_SECS, plus the last call's duration."""
    ordered = sorted(spans)
    total = 0.0
    for (a, _), (b, _) in zip(ordered, ordered[1:]):
        gap = (b - a).total_seconds()
        if gap <= IDLE_GAP_SECS:
            total += gap
    return total + ordered[-1][1] / 1000


def fmt_secs(seconds):
    minutes, secs = divmod(int(round(seconds)), 60)
    return f"{minutes}m {secs:02d}s" if minutes else f"{secs}s"


def fmt_int(n):
    return f"{int(n):,}".replace(",", " ")


def norm_path(value):
    return (value or "").lower().replace("/", "\\").rstrip("\\")


def collect(store, repo, start, end, split_at):
    con = sqlite3.connect(f"file:{Path(store).as_posix()}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    repo_key = norm_path(str(repo))
    sessions = {}
    for row in con.execute("SELECT id, cwd, summary FROM sessions"):
        if norm_path(row["cwd"]) != repo_key:
            continue
        match = ACTOR_RE.search(row["summary"] or "")
        sessions[row["id"]] = match.group(1) if match else f"(unnamed {row['id'][:8]})"

    stats = defaultdict(lambda: defaultdict(float))
    models, spans = defaultdict(set), defaultdict(list)
    phases = {}
    for r in con.execute("SELECT * FROM assistant_usage_events"):
        actor = sessions.get(r["session_id"])
        if actor is None:
            continue
        when = parse_ts(r["created_at"])
        if not start <= when <= end:
            continue
        s = stats[actor]
        aiu = (r["total_nano_aiu"] or 0) / 1e9
        s["calls"] += 1
        s["model_ms"] += r["duration_ms"] or 0
        s["aiu"] += aiu
        s["premium"] += r["request_multiplier"] or 0
        s["input"] += r["input_tokens"] or 0
        s["cached"] += r["cache_read_tokens"] or 0
        s["cache_write"] += r["cache_write_tokens"] or 0
        s["output"] += r["output_tokens"] or 0
        s["reasoning"] += r["reasoning_tokens"] or 0
        s["subagent"] += 1 if (r["initiator"] == "sub-agent" or r["parent_tool_call_id"]) else 0
        models[actor].add(f"{r['model']} ({r['reasoning_effort'] or 'default'})")
        spans[actor].append((when, r["duration_ms"] or 0))
        if split_at is None:
            phase = "Whole window"
        elif when < split_at:
            phase = "Before first handover to Quality"
        else:
            phase = "From first handover to Quality"
        p = phases.setdefault(phase, {"calls": 0, "aiu": 0.0})
        p["calls"] += 1
        p["aiu"] += aiu
    if not stats:
        con.close()
        raise StatsError("The window holds no usage events.")

    for r in con.execute("SELECT session_id, timestamp FROM turns"):
        actor = sessions.get(r["session_id"])
        if actor in stats and start <= parse_ts(r["timestamp"]) <= end:
            stats[actor]["turns"] += 1
    for r in con.execute("SELECT session_id, first_seen_at FROM session_files"):
        actor = sessions.get(r["session_id"])
        if actor in stats and start <= parse_ts(r["first_seen_at"]) <= end:
            stats[actor]["files"] += 1
    con.close()
    return stats, models, spans, phases


def render(contract, start, end, start_source, commits, stats, models, spans, phases):
    actors = sorted(stats, key=lambda a: -stats[a]["aiu"])
    total = defaultdict(float)
    for a in actors:
        stats[a]["active"] = active_secs(spans[a])
        for k, v in stats[a].items():
            total[k] += v

    def cached_pct(s):
        return f"{100 * s['cached'] / s['input']:.0f}%" if s["input"] else "-"

    lines = [
        f"# Contract statistics: {contract}",
        "",
        f"- **Window:** {start.astimezone():%Y-%m-%d %H:%M:%S %z} to {end.astimezone():%Y-%m-%d %H:%M:%S %z}"
        f" ({fmt_secs((end - start).total_seconds())} wall clock)",
        f"- **Window start:** {start_source}",
        f"- **Commits in window (all branches):** {commits}",
        f"- **Extracted:** {datetime.now().astimezone():%Y-%m-%d %H:%M %z} from the local Copilot session store",
        "- **Credit:** AIU = `total_nano_aiu` / 1e9. Premium requests = sum of `request_multiplier`.",
        "",
        "## Usage per actor",
        "",
        "| Actor | Calls | Model time | Active time | AIU | Premium requests | Input tokens | Cached | Cache write | Output tokens | Reasoning tokens | Model (effort) |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for a in actors:
        s = stats[a]
        lines.append(
            f"| {a} | {int(s['calls'])} | {fmt_secs(s['model_ms'] / 1000)} | {fmt_secs(s['active'])} | {s['aiu']:.1f}"
            f" | {s['premium']:g} | {fmt_int(s['input'])} | {cached_pct(s)} | {fmt_int(s['cache_write'])}"
            f" | {fmt_int(s['output'])} | {fmt_int(s['reasoning'])} | {', '.join(sorted(models[a]))} |"
        )
    lines.append(
        f"| **Total** | {int(total['calls'])} | {fmt_secs(total['model_ms'] / 1000)} | {fmt_secs(total['active'])} | {total['aiu']:.1f}"
        f" | {total['premium']:g} | {fmt_int(total['input'])} | {cached_pct(total)} | {fmt_int(total['cache_write'])}"
        f" | {fmt_int(total['output'])} | {fmt_int(total['reasoning'])} | |"
    )
    top = actors[0]
    if total["aiu"]:
        summary = (
            f"{len(actors)} actors made {int(total['calls'])} model calls and used {total['aiu']:.1f} AIU"
            f" ({fmt_secs(total['model_ms'] / 1000)} model time, {fmt_secs(total['active'])} active time in total);"
            f" {top} was the largest consumer with {stats[top]['aiu']:.1f} AIU ({100 * stats[top]['aiu'] / total['aiu']:.0f}%)."
        )
    else:
        summary = f"{len(actors)} actors made {int(total['calls'])} model calls; no credits were recorded."
    lines += ["", f"**Summary:** {summary}", "", "## Activity per actor", "",
              "| Actor | Turns | Files changed | Sub-agent calls |", "|---|---|---|---|"]
    for a in actors:
        s = stats[a]
        lines.append(f"| {a} | {int(s['turns'])} | {int(s['files'])} | {int(s['subagent'])} |")
    lines.append(f"| **Total** | {int(total['turns'])} | {int(total['files'])} | {int(total['subagent'])} |")
    if total["files"]:
        summary = (f"{int(total['turns'])} turns across {len(actors)} actors changed {int(total['files'])} files"
                   f" ({total['aiu'] / total['files']:.1f} AIU per changed file).")
    else:
        summary = f"{int(total['turns'])} turns across {len(actors)} actors; no file changes were recorded."
    lines += ["", f"**Summary:** {summary}", "", "## AIU by phase", "", "| Phase | Calls | AIU |", "|---|---|---|"]
    for phase, p in phases.items():
        lines.append(f"| {phase} | {p['calls']} | {p['aiu']:.1f} |")
    if total["aiu"]:
        shares = ", ".join(f"{100 * p['aiu'] / total['aiu']:.0f}% {phase[0].lower() + phase[1:]}" for phase, p in phases.items())
        summary = f"the AIU split is {shares}."
    else:
        summary = "no credits were recorded."
    lines += [
        "",
        f"**Summary:** {summary}",
        "",
        "## Limits",
        "",
        "- The figures are usage, not a judgment of the work.",
        f"- Active time adds the gaps between consecutive model calls of an actor that are at most {IDLE_GAP_SECS // 60} minutes, plus the last call; longer gaps count as idle. It includes tool and wait time, so it approximates how long the actor ran.",
        "- The phase split uses the first commit of the Contract file whose `Current responsibility` is Quality; without that commit, or with an explicit start, the whole window is one phase.",
        "- Per-actor commit counts are not available: the session store holds no commit references. Total commits are in the header.",
        "- Tool calls and tool durations are not in the local store and are not recorded.",
        "- Every session started in this repository counts; a parallel unrelated session inside the window is included.",
        "",
    ]
    return "\n".join(lines)


def run(args):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", args.contract) or ".." in args.contract:
        raise StatsError(f"The Contract name must be a plain file name without .md, not {args.contract!r}.")
    repo = Path(args.repo).resolve()
    store = Path(args.store)
    if not store.is_file():
        raise StatsError(f"Session store not found: {store}")

    path = None
    if args.start:
        start, start_source = parse_ts(args.start), "explicit start"
    else:
        path = args.contract_file or locate_contract(repo, args.contract)
        found = find_marker(repo, path, gate_approved)
        if found is None:
            raise StatsError(
                f"No commit of {path} shows the start gate ({' or '.join(START_GATES)}) as approved; pass --start."
            )
        start, start_source = found[1], f"first commit of {path} with the gate approved: {found[0][:7]}"
    end = parse_ts(args.end) if args.end else datetime.now(timezone.utc)
    if end <= start:
        raise StatsError("The window is empty: the end is not after the start.")

    split_at = None
    if path:
        quality = find_marker(repo, path, holds_quality)
        split_at = quality[1] if quality else None

    stats, models, spans, phases = collect(store, repo, start, end, split_at)
    commits = git(repo, "rev-list", "--all", "--count", f"--since={start.isoformat()}", f"--until={end.isoformat()}").strip()
    text = render(args.contract, start, end, start_source, commits, stats, models, spans, phases)

    target = repo / ".syspilot" / "stats" / f"{args.contract}-stat.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(target)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("contract", help="Contract name, the file name without .md, e.g. impact-artifact-list")
    ap.add_argument("--repo", default=".", help="Repository root")
    ap.add_argument("--start", help="Window start (ISO); overrides the start gate")
    ap.add_argument("--end", help="Window end (ISO); default is now")
    ap.add_argument("--contract-file", help="Path of the Contract file in the repository, when its name does not locate it")
    ap.add_argument("--store", default=str(STORE), help="Copilot session store")
    args = ap.parse_args()
    try:
        run(args)
    except StatsError as error:
        sys.exit(f"contract-statistics: {error}")


if __name__ == "__main__":
    main()
