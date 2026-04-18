"""UserPromptSubmit hook — inject top MemPalace hits as context.

Reads Claude Code's hook JSON from stdin, does a ~20ms MemPalace search
over the user's prompt, and prints verbatim drawers to stdout so Claude
sees them before reasoning.

Install path: wherever you put your hook scripts (referenced in settings.json).

DESIGN CONSTRAINTS (non-negotiable):
- Must fail silent. If MemPalace is broken, slow, or missing, exit 0
  with no output. NEVER block the user's prompt.
- Budget: <500ms end-to-end. A hard timeout is set on POSIX systems.
  On Windows, the `timeout` setting in settings.json (recommended: 2s) is
  the hard limit instead.
- Verbatim: emit the drawer text as-is (no paraphrase).
- Idempotent: same prompt twice yields the same output (no state writes).

Output format (appears in Claude's context as extra injected text):
    <mempalace-context>
    [1] wing/room | source.md | sim=0.82
    <drawer text>
    </mempalace-context>

If no results, emit nothing (not even the wrapper tags).

Setup:
    In ~/.claude/settings.json:
    {
      "hooks": {
        "UserPromptSubmit": [{
          "matcher": "",
          "hooks": [{
            "type": "command",
            "command": "python /path/to/mempalace_prompt_hook.py",
            "timeout": 2
          }]
        }]
      }
    }
"""

from __future__ import annotations

import hashlib
import json
import os
import signal
import sys
from datetime import datetime
from pathlib import Path

# Allow environment variable override for recall log location.
_palace_dir = Path(os.environ.get("MEMPALACE_PALACE", Path.home() / ".mempalace" / "palace"))
RECALL_LOG = _palace_dir.parent / "hook_state" / "recalls.jsonl"

# Locate the bin directory containing mempalace_fast.py.
# Priority: PI_AGENT_HOME env var → default ~/.pi/agent/bin → same dir as this script.
_pi_home = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi"))
_bin_dir = _pi_home / "agent" / "bin"
if not _bin_dir.is_dir():
    _bin_dir = Path(__file__).parent  # fallback: same directory as this file


def _recall_key(wing: str, room: str, text: str) -> str:
    """Stable per-drawer key used by auto_dream.py deadweight detection."""
    h = hashlib.sha1(f"{wing}::{room}::{text[:200]}".encode("utf-8")).hexdigest()
    return h[:16]


def _log_recall(prompt: str, results: list[dict]) -> None:
    """Append one JSONL line per prompt for recall analytics. Fail-silent."""
    try:
        RECALL_LOG.parent.mkdir(parents=True, exist_ok=True)
        entry = {
            "ts": datetime.now().isoformat(),
            "prompt_len": len(prompt),
            "keys": [
                _recall_key(r.get("wing", "?"), r.get("room", "?"), r.get("text", ""))
                for r in results
            ],
        }
        with RECALL_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        pass


# Everything below is wrapped in fail-silent try/except.
try:
    # 500ms hard budget. SIGALRM only works on POSIX / WSL.
    # On Windows, rely on the hook `timeout` in settings.json (set to 2s).
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, lambda *_: sys.exit(0))
        signal.setitimer(signal.ITIMER_REAL, 0.5)

    # Read hook payload (JSON on stdin — Claude Code sends this automatically).
    try:
        payload = json.load(sys.stdin) if not sys.stdin.isatty() else {}
    except Exception:
        payload = {}

    prompt = (payload.get("prompt") or payload.get("user_prompt") or "").strip()
    if not prompt or len(prompt) < 6:
        sys.exit(0)

    # Import the fast wrapper (adds _bin_dir to path so mempalace_fast resolves).
    if str(_bin_dir) not in sys.path:
        sys.path.insert(0, str(_bin_dir))
    from mempalace_fast import search  # type: ignore

    out = search(prompt, n=3)
    results = (out or {}).get("results") or []
    if not results:
        sys.exit(0)

    # Force UTF-8 on stdout to survive Windows cp1252 terminals.
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass

    # Log recall before emitting (so analytics still work even if stdout fails).
    _log_recall(prompt, results)

    palace_path = os.environ.get("MEMPALACE_PALACE", str(Path.home() / ".mempalace" / "palace"))
    print("<mempalace-context>")
    print(f"<!-- {len(results)} drawers from {palace_path} -->")
    for i, r in enumerate(results, 1):
        wing = r.get("wing", "?")
        room = r.get("room", "?")
        src = Path(r.get("source_file") or "?").name
        sim = r.get("similarity")
        sim_s = f" | sim={sim:.2f}" if sim is not None else ""
        print(f"\n[{i}] {wing}/{room} | {src}{sim_s}")
        text = (r.get("text") or "").strip()
        # Cap each drawer at 1200 chars to keep injection small.
        if len(text) > 1200:
            text = text[:1200] + "\n... (truncated)"
        print(text)
    print("</mempalace-context>")

except SystemExit:
    raise
except Exception:
    # Any failure is silent — the hook must never block a prompt.
    pass

sys.exit(0)
