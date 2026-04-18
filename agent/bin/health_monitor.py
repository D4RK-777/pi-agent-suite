"""
MemPalace Health Monitor
========================
Runs permanently in background, monitors:
- ChromaDB server (keeps it warm)
- Startup services
- Disk space
- Auto-restarts if anything crashes

Usage:
    python health_monitor.py          # Start daemon
    python health_monitor.py status   # Check status
    python health_monitor.py stop     # Stop daemon
"""

import time
import sys
import logging
import urllib.request
from pathlib import Path
from datetime import datetime
import json

# Config
CHECK_INTERVAL = 30  # seconds
LOG_DIR = Path.home() / ".mempalace" / "logs"
LOG_FILE = LOG_DIR / "health_monitor.log"
PID_FILE = Path.home() / ".mempalace" / "pids" / "health_monitor.pid"
CHROMA_URL = "http://127.0.0.1:8000/api/v1/heartbeat"

# Setup logging
LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def is_chroma_running():
    """Check if ChromaDB server is responding."""
    try:
        resp = urllib.request.urlopen(CHROMA_URL, timeout=5)
        data = json.loads(resp.read().decode())
        return True, data.get("nanosecond heartbeat", "unknown")
    except Exception as e:
        return False, str(e)


def start_chroma():
    """Start ChromaDB server if not running."""
    logger.info("Starting ChromaDB...")
    
    chroma_script = 'import sys;sys.path.insert(0,"C:/Python313/Lib/site-packages");import uvicorn;import chromadb.app;uvicorn.run(chromadb.app.app,host="127.0.0.1",port=8000,log_level="warning")'
    
    import subprocess
    subprocess.Popen(
        [sys.executable, "-X utf8", "-c", chroma_script],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
    )
    
    # Wait for startup
    for i in range(10):
        time.sleep(2)
        running, _ = is_chroma_running()
        if running:
            logger.info("ChromaDB started successfully")
            return True
    
    logger.error("Failed to start ChromaDB")
    return False


def check_disk_space():
    """Check available disk space."""
    import shutil
    total, used, free = shutil.disk_usage(Path.home())
    free_gb = free // (2**30)
    return free_gb, (free / total) * 100


def run_health_check():
    """Perform health check and return status."""
    status = {
        "timestamp": datetime.now().isoformat(),
        "chroma": {},
        "system": {}
    }
    
    # Check ChromaDB
    running, detail = is_chroma_running()
    status["chroma"]["running"] = running
    status["chroma"]["detail"] = detail if running else None
    
    if not running:
        status["chroma"]["action"] = "restarting"
        start_chroma()
        running_after, _ = is_chroma_running()
        status["chroma"]["restored"] = running_after
    else:
        status["chroma"]["action"] = "ok"
    
    # Check disk space
    free_gb, pct = check_disk_space()
    status["system"]["disk_free_gb"] = free_gb
    status["system"]["disk_free_pct"] = round(pct, 1)
    
    if free_gb < 5:
        logger.warning(f"Low disk space: {free_gb}GB remaining")
        status["system"]["disk_warning"] = True
    
    return status


def status_command():
    """Show current status."""
    print()
    print("=" * 50)
    print("  MemPalace Health Monitor Status")
    print("=" * 50)
    print()
    
    # Check ChromaDB
    running, detail = is_chroma_running()
    if running:
        print(f"  [ONLINE]  ChromaDB Vector DB")
        print(f"           Heartbeat: {str(detail)[:20]}...")
    else:
        print(f"  [OFFLINE] ChromaDB Vector DB")
        print(f"           Error: {detail}")
    
    # Check disk
    free_gb, pct = check_disk_space()
    if free_gb < 5:
        print(f"  [WARN]   Disk Space: {free_gb}GB ({pct:.1f}%)")
    else:
        print(f"  [OK]     Disk Space: {free_gb}GB ({pct:.1f}%)")
    
    # Check if monitor is running
    if PID_FILE.exists():
        pid = PID_FILE.read_text().strip()
        print(f"  [OK]     Monitor PID: {pid}")
    else:
        print(f"  [INFO]   Monitor not running as daemon")
    
    print()
    print(f"  Log file: {LOG_FILE}")
    print()


def stop_command():
    """Stop the health monitor daemon."""
    if PID_FILE.exists():
        import os
        import signal
        pid = int(PID_FILE.read_text().strip())
        try:
            os.kill(pid, signal.SIGTERM)
            PID_FILE.unlink()
            print("Health monitor stopped.")
        except:
            print("Could not stop process. May need admin.")
    else:
        print("Health monitor not running.")


def daemon_loop():
    """Main daemon loop."""
    logger.info("=" * 50)
    logger.info("MemPalace Health Monitor Started")
    logger.info(f"Check interval: {CHECK_INTERVAL}s")
    logger.info("=" * 50)
    
    # Save PID
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(str(os.getpid()))
    
    consecutive_failures = 0
    
    while True:
        try:
            status = run_health_check()
            
            if status["chroma"]["running"]:
                consecutive_failures = 0
                logger.debug(f"Health OK - ChromaDB responding")
            else:
                consecutive_failures += 1
                if consecutive_failures >= 3:
                    logger.warning(f"ChromaDB down for {consecutive_failures} checks")
            
            time.sleep(CHECK_INTERVAL)
            
        except KeyboardInterrupt:
            logger.info("Health monitor stopped by user")
            break
        except Exception as e:
            logger.error(f"Health check error: {e}")
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    import os
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "status":
            status_command()
        elif cmd == "stop":
            stop_command()
        elif cmd == "restart":
            stop_command()
            time.sleep(1)
            daemon_loop()
        else:
            print(f"Unknown command: {cmd}")
            print("Usage: health_monitor.py [status|stop]")
    else:
        daemon_loop()
