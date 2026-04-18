#!/usr/bin/env python3
"""
project_sync.py — Mine any project directory into MemPalace incrementally.

Drop this in your project or schedule it via cron/Task Scheduler to keep
MemPalace fresh as your codebase evolves. Mining is incremental — already-filed
files are skipped — so it's safe to run frequently.

Usage:
    python project_sync.py --dir ~/your-project
    python project_sync.py --dir ~/your-project --wing code --limit 50
    python project_sync.py --dir ~/your-project --wing myproject

Environment variables:
    PI_AGENT_HOME       — Pi install root (default: ~/.pi)
    MEMPALACE_PALACE    — ChromaDB palace path (default: ~/.mempalace/palace)
    PROJECT_DIR         — Project directory to mine (override --dir)
    PROJECT_WING        — MemPalace wing to mine into (override --wing)
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path

_pi_home = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi"))
_mempalace_src = _pi_home / "mempalace-src"
if _mempalace_src.is_dir() and str(_mempalace_src) not in sys.path:
    sys.path.insert(0, str(_mempalace_src))

from mempalace import miner  # noqa: E402

PALACE = os.environ.get("MEMPALACE_PALACE", str(Path.home() / ".mempalace" / "palace"))
LOG_FILE = Path.home() / ".mempalace" / "logs" / "project_sync.log"

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE, encoding="utf-8"), logging.StreamHandler()],
)
log = logging.getLogger("project_sync")


def main() -> int:
    ap = argparse.ArgumentParser(description="Incrementally mine a project into MemPalace")
    ap.add_argument("--dir", default=os.environ.get("PROJECT_DIR", ""),
                    help="Project directory to mine")
    ap.add_argument("--wing", default=os.environ.get("PROJECT_WING", "code"),
                    help="MemPalace wing to store in (default: code)")
    ap.add_argument("--limit", type=int, default=0,
                    help="Cap number of files mined, 0 = no cap (default: 0)")
    ap.add_argument("--exclude", default="node_modules,.obsidian,__pycache__,.git,*.pyc",
                    help="Comma-separated patterns to exclude")
    args = ap.parse_args()

    if not args.dir:
        log.error("No project directory specified. Use --dir or set PROJECT_DIR env var.")
        return 2

    project = Path(args.dir).expanduser().resolve()
    if not project.is_dir():
        log.error("Project directory not found: %s", project)
        return 2

    log.info("Mining %s into MemPalace wing=%s ...", project, args.wing)
    try:
        miner.mine(
            project_dir=str(project),
            palace_path=PALACE,
            wing_override=args.wing,
            agent="project-sync",
            limit=args.limit,
            respect_gitignore=True,
        )
    except SystemExit as e:
        log.error("miner.mine exited: %s", e)
        return int(getattr(e, "code", 1) or 1)
    except Exception:
        log.exception("miner.mine failed")
        return 1

    log.info("Sync complete: %s → wing=%s", project, args.wing)
    return 0


if __name__ == "__main__":
    sys.exit(main())
