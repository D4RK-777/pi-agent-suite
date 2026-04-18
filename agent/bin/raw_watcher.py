#!/usr/bin/env python3
"""
raw_watcher.py — Passive ingest for your Obsidian vault's raw/ directory.

Watches $OBSIDIAN_VAULT/raw/ on a polling loop. When a new or changed file
appears, runs mempalace.miner.mine() against the vault (incremental — only
changed files are re-filed). Dropping a file into raw/articles/ is enough
to get it into MemPalace without any manual action.

Usage:
    python raw_watcher.py                 # Run forever (poll every 30s)
    python raw_watcher.py --once          # One pass, exit
    python raw_watcher.py --interval 60   # Custom poll interval
    python raw_watcher.py --force         # Re-mine everything (ignore cached state)

Environment variables:
    OBSIDIAN_VAULT      — Path to your Obsidian vault (required)
    PI_AGENT_HOME       — Pi install root (default: ~/.pi)
    MEMPALACE_PALACE    — ChromaDB palace path (default: ~/.mempalace/palace)

Logs to:  ~/.mempalace/logs/raw_watcher.log
State:    ~/.mempalace/raw_watcher_state.json
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

_pi_home = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi"))
_mempalace_src = _pi_home / "mempalace-src"
if _mempalace_src.is_dir() and str(_mempalace_src) not in sys.path:
    sys.path.insert(0, str(_mempalace_src))

from mempalace import miner  # noqa: E402

_vault_env = os.environ.get("OBSIDIAN_VAULT", "")
VAULT = Path(_vault_env).expanduser() if _vault_env else None
RAW = VAULT / "raw" if VAULT else None
PALACE = os.environ.get("MEMPALACE_PALACE", str(Path.home() / ".mempalace" / "palace"))
STATE_FILE = Path.home() / ".mempalace" / "raw_watcher_state.json"
LOG_FILE = Path.home() / ".mempalace" / "logs" / "raw_watcher.log"

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE, encoding="utf-8"), logging.StreamHandler()],
)
log = logging.getLogger("raw_watcher")


def _scan_mtimes() -> dict[str, float]:
    out: dict[str, float] = {}
    if not RAW or not RAW.is_dir():
        return out
    for p in RAW.rglob("*"):
        if p.is_file():
            try:
                out[str(p.relative_to(VAULT))] = p.stat().st_mtime
            except OSError:
                pass
    return out


def _load_state() -> dict[str, float]:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save_state(state: dict[str, float]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def run_once() -> int:
    if not VAULT:
        log.error("OBSIDIAN_VAULT env var not set — cannot watch. Set it and restart.")
        return 0
    if not RAW.is_dir():
        log.warning("raw/ not found at %s — nothing to watch", RAW)
        return 0

    prev = _load_state()
    current = _scan_mtimes()

    changed = [p for p, m in current.items() if p not in prev or prev[p] != m]
    if not changed:
        return 0

    log.info("Detected %d new/changed files under raw/:", len(changed))
    for p in changed[:10]:
        log.info("  + %s", p)
    if len(changed) > 10:
        log.info("  ... and %d more", len(changed) - 10)

    try:
        miner.mine(
            project_dir=str(VAULT),
            palace_path=PALACE,
            wing_override="knowledge",
            agent="raw-watcher",
            respect_gitignore=False,
        )
    except SystemExit:
        log.exception("miner.mine exited")
        return 0
    except Exception:
        log.exception("miner.mine failed")
        return 0

    _save_state(current)
    log.info("Watcher pass complete.")
    return len(changed)


def watch_forever(interval: int) -> None:
    log.info("Starting raw_watcher on %s (every %ds)", RAW, interval)
    if not STATE_FILE.exists():
        log.info("First run — priming state without mining (picks up future changes).")
        _save_state(_scan_mtimes())
    while True:
        try:
            run_once()
        except KeyboardInterrupt:
            log.info("Stopped by user.")
            return
        except Exception:
            log.exception("Watcher loop error; sleeping and retrying.")
        time.sleep(interval)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true", help="Run a single pass and exit")
    ap.add_argument("--interval", type=int, default=30, help="Poll interval in seconds")
    ap.add_argument("--force", action="store_true", help="Re-mine ignoring cached state")
    args = ap.parse_args()

    if args.force and STATE_FILE.exists():
        STATE_FILE.unlink()
        log.info("State cleared; next pass will treat all files as new.")

    if args.once:
        n = run_once()
        log.info("Done. Changes handled: %d", n)
        return 0

    watch_forever(args.interval)
    return 0


if __name__ == "__main__":
    sys.exit(main())
