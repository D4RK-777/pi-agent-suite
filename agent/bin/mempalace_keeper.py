"""MemPalace Keeper — watchdog that keeps the daemon alive.

Runs as a background pythonw process (via Startup folder shortcut).
Every HEALTH_INTERVAL_S seconds it pings the daemon's /health endpoint.
If it's dead (network error, non-200, or timeout), respawns it.

Why this exists:
  Without a keeper, a daemon crash means no semantic memory until next login.
  With the keeper, recovery is <30s.

Logs restarts + health pings to ~/.mempalace/logs/keeper.log.

Run manually:
    python mempalace_keeper.py                 # foreground, with console logs
    pythonw mempalace_keeper.py                # background, logs to file only

Override the interval/endpoint via env:
    PI_KEEPER_INTERVAL_S=60   (default 30)
    PI_KEEPER_URL=http://127.0.0.1:8787/health
    PI_KEEPER_DAEMON_SCRIPT=<path to mempalace_daemon.py>
"""

from __future__ import annotations

import json
import logging
import logging.handlers
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BIN = Path(__file__).parent
DAEMON_SCRIPT = Path(os.environ.get("PI_KEEPER_DAEMON_SCRIPT", str(BIN / "mempalace_daemon.py")))
HEALTH_URL = os.environ.get("PI_KEEPER_URL", "http://127.0.0.1:8787/health")
HEALTH_INTERVAL_S = int(os.environ.get("PI_KEEPER_INTERVAL_S", "30"))
HEALTH_TIMEOUT_S = 3
RESTART_BACKOFF_S = 5  # Wait after spawning before next health check
MAX_CONSECUTIVE_FAILS = 3  # Health-check misses before declaring dead

LOG_DIR = Path.home() / ".mempalace" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "keeper.log"

# Rotating log so a long-running keeper can't fill the disk.
_handler = logging.handlers.RotatingFileHandler(
    LOG_FILE, maxBytes=512_000, backupCount=3, encoding="utf-8"
)
_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
log = logging.getLogger("mempalace-keeper")
log.setLevel(logging.INFO)
log.addHandler(_handler)
# Also log to stderr so foreground runs show activity.
_stderr = logging.StreamHandler(sys.stderr)
_stderr.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
log.addHandler(_stderr)


def _ping_health() -> tuple[bool, str]:
    """Returns (alive, reason)."""
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=HEALTH_TIMEOUT_S) as r:
            if r.status != 200:
                return False, f"http {r.status}"
            body = json.loads(r.read().decode("utf-8"))
            if not body.get("ok"):
                return False, f"status says ok=false: {body}"
            return True, f"total={body.get('total_records', '?')}"
    except urllib.error.URLError as e:
        return False, f"url error: {e}"
    except (TimeoutError, OSError) as e:
        return False, f"network: {e}"
    except Exception as e:  # any unexpected parse error
        return False, f"parse: {e}"


def _spawn_daemon() -> subprocess.Popen:
    """Spawn the daemon detached (no parent-kill on exit, no console window)."""
    # pythonw on Windows hides the console. On non-Windows, use python.
    pythonw = _find_pythonw()
    creationflags = 0
    if os.name == "nt":
        # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP — survives parent exit,
        # doesn't propagate ctrl+c.
        creationflags = 0x00000008 | 0x00000200

    proc = subprocess.Popen(
        [pythonw, "-X", "utf8", str(DAEMON_SCRIPT)],
        creationflags=creationflags,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        close_fds=True,
    )
    log.info("spawned daemon pid=%s", proc.pid)
    return proc


def _find_pythonw() -> str:
    """Prefer pythonw.exe (no console) on Windows, fall back to current executable."""
    if os.name == "nt":
        # Try to derive pythonw from the running python.exe
        candidate = Path(sys.executable).with_name("pythonw.exe")
        if candidate.exists():
            return str(candidate)
    return sys.executable


def main() -> None:
    log.info(
        "keeper starting; daemon=%s url=%s interval=%ss",
        DAEMON_SCRIPT,
        HEALTH_URL,
        HEALTH_INTERVAL_S,
    )
    consecutive_fails = 0
    last_restart = 0.0

    # Initial probe: if the daemon is already up (startup-folder shortcut launched
    # it earlier), don't spawn a duplicate. Otherwise spawn fresh.
    alive, reason = _ping_health()
    if alive:
        log.info("daemon already healthy on startup: %s", reason)
    else:
        log.info("daemon down on startup (%s) — spawning", reason)
        _spawn_daemon()
        last_restart = time.time()
        time.sleep(RESTART_BACKOFF_S)

    while True:
        time.sleep(HEALTH_INTERVAL_S)
        alive, reason = _ping_health()
        if alive:
            if consecutive_fails:
                log.info("daemon recovered after %d fails (%s)", consecutive_fails, reason)
            consecutive_fails = 0
            continue

        consecutive_fails += 1
        log.warning("health check miss %d/%d: %s", consecutive_fails, MAX_CONSECUTIVE_FAILS, reason)

        if consecutive_fails >= MAX_CONSECUTIVE_FAILS:
            # Rate-limit restarts so we don't hot-spin if the daemon is broken.
            since_last = time.time() - last_restart
            if since_last < 60:
                log.error("refusing to respawn — only %.0fs since last restart", since_last)
                time.sleep(30)
                consecutive_fails = 0
                continue
            log.error("daemon dead — respawning")
            try:
                _spawn_daemon()
                last_restart = time.time()
            except Exception as e:
                log.exception("spawn failed: %s", e)
            consecutive_fails = 0
            time.sleep(RESTART_BACKOFF_S)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.info("keeper stopped by ctrl+c")
    except Exception:
        log.exception("keeper crashed")
        raise
