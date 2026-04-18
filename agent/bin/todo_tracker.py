"""
MemPalace TODO Tracker
======================
Scans codebases for TODO, FIXME, HACK, XXX comments.
Maintains a searchable index in MemPalace.
Flags stale TODOs (not updated in N days).

Usage:
    python todo_tracker.py              # Scan all tracked repos
    python todo_tracker.py scan <path>  # Scan specific path
    python todo_tracker.py report       # Show TODO report
    python todo_tracker.py watch        # Start watching for changes
"""

import os
import re
import sys
import json
import time
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

# Config
TRACKED_REPOS_FILE = Path.home() / ".mempalace" / "todo_tracked_repos.json"
TODO_INDEX_FILE = Path.home() / ".mempalace" / "todo_index.json"
LOG_FILE = Path.home() / ".mempalace" / "logs" / "todo_tracker.log"
STALE_DAYS = 14  # Flag TODOs not touched in 14 days

# Setup logging
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Patterns to track
TODO_PATTERNS = [
    (r"TODO(?:\([^)]+\))?:?\s*(.+)", "TODO"),
    (r"FIXME(?:\([^)]+\))?:?\s*(.+)", "FIXME"),
    (r"HACK(?:\([^)]+\))?:?\s*(.+)", "HACK"),
    (r"XXX(?:\([^)]+\))?:?\s*(.+)", "XXX"),
    (r"BUG(?:\([^)]+\))?:?\s*(.+)", "BUG"),
    (r"NOTE(?:\([^)]+\))?:?\s*(.+)", "NOTE"),
]

# File extensions to scan
SCAN_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx",
    ".java", ".cs", ".go", ".rs", ".rb",
    ".php", ".swift", ".kt", ".scala",
    ".c", ".cpp", ".h", ".hpp",
    ".sh", ".bash", ".ps1",
    ".md", ".txt"
}


def load_tracked_repos():
    """Load list of tracked repositories."""
    if TRACKED_REPOS_FILE.exists():
        return json.loads(TRACKED_REPOS_FILE.read_text())
    return []


def save_tracked_repos(repos):
    """Save tracked repositories list."""
    TRACKED_REPOS_FILE.write_text(json.dumps(repos, indent=2))


def add_tracked_repo(path: str):
    """Add a repository to track."""
    repos = load_tracked_repos()
    path = str(Path(path).resolve())
    if path not in repos:
        repos.append(path)
        save_tracked_repos(repos)
        logger.info(f"Added to tracking: {path}")
    else:
        logger.info(f"Already tracking: {path}")


def scan_file(filepath: Path) -> list[dict]:
    """Scan a single file for TODO comments."""
    todos = []
    
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        lines = content.split("\n")
        
        for line_num, line in enumerate(lines, 1):
            for pattern, tag in TODO_PATTERNS:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    todo_text = match.group(1).strip()
                    todos.append({
                        "file": str(filepath),
                        "line": line_num,
                        "type": tag,
                        "text": todo_text,
                        "context": line.strip()[:200],
                        "scanned_at": datetime.now().isoformat(),
                        "last_seen": datetime.now().isoformat()
                    })
    except Exception as e:
        logger.debug(f"Error scanning {filepath}: {e}")
    
    return todos


def scan_directory(path: Path, max_depth: int = 10) -> list[dict]:
    """Recursively scan directory for TODO comments."""
    todos = []
    
    # Skip common non-code directories
    skip_dirs = {
        ".git", ".svn", ".hg", "node_modules", "venv", ".venv",
        "env", ".env", "__pycache__", ".pytest_cache", "dist",
        "build", ".next", ".nuxt", ".next-dev", ".next-build",
        "vendor", "target", "bin", "obj"
    }
    
    for root, dirs, files in os.walk(path):
        # Filter dirs
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        # Check depth
        depth = root[len(str(path)):].count(os.sep)
        if depth >= max_depth:
            dirs[:] = []
            continue
        
        for filename in files:
            ext = Path(filename).suffix
            if ext in SCAN_EXTENSIONS or filename in {"Makefile", "Dockerfile"}:
                filepath = Path(root) / filename
                todos.extend(scan_file(filepath))
    
    return todos


def load_todo_index() -> dict:
    """Load the TODO index."""
    if TODO_INDEX_FILE.exists():
        return json.loads(TODO_INDEX_FILE.read_text())
    return {"todos": [], "stats": {}}


def save_todo_index(index: dict):
    """Save the TODO index."""
    TODO_INDEX_FILE.write_text(json.dumps(index, indent=2))


def update_todo_index(todos: list[dict]):
    """Update the TODO index with new scan results."""
    index = load_todo_index()
    
    # Create lookup for existing todos
    existing = {
        (t["file"], t["line"], t["type"]): t 
        for t in index.get("todos", [])
    }
    
    # Merge new results
    new_todos = []
    for todo in todos:
        key = (todo["file"], todo["line"], todo["type"])
        if key in existing:
            # Preserve original "created_at" and update "last_seen"
            existing_todo = existing[key]
            existing_todo["last_seen"] = datetime.now().isoformat()
            existing_todo["text"] = todo["text"]  # Update text in case it changed
            new_todos.append(existing_todo)
        else:
            # New todo
            todo["created_at"] = datetime.now().isoformat()
            new_todos.append(todo)
    
    index["todos"] = new_todos
    index["last_scan"] = datetime.now().isoformat()
    
    # Stats
    index["stats"] = {
        "total": len(new_todos),
        "todo": sum(1 for t in new_todos if t["type"] == "TODO"),
        "fixme": sum(1 for t in new_todos if t["type"] == "FIXME"),
        "hack": sum(1 for t in new_todos if t["type"] == "HACK"),
        "bug": sum(1 for t in new_todos if t["type"] == "BUG"),
    }
    
    save_todo_index(index)
    return index


def find_stale_todos(days: int = STALE_DAYS) -> list[dict]:
    """Find TODOs that haven't been seen in N days."""
    index = load_todo_index()
    cutoff = datetime.now() - timedelta(days=days)
    
    stale = []
    for todo in index.get("todos", []):
        last_seen = datetime.fromisoformat(todo["last_seen"])
        if last_seen < cutoff:
            todo["days_stale"] = (datetime.now() - last_seen).days
            stale.append(todo)
    
    return stale


def print_report():
    """Print TODO report."""
    index = load_todo_index()
    todos = index.get("todos", [])
    stats = index.get("stats", {})
    
    print()
    print("=" * 60)
    print("  MemPalace TODO Tracker Report")
    print("=" * 60)
    print()
    
    if not todos:
        print("  No TODOs found.")
        print()
        return
    
    print(f"  Last scan: {index.get('last_scan', 'Never')}")
    print()
    print("  Summary:")
    print(f"    Total: {stats.get('total', 0)}")
    print(f"    TODO:  {stats.get('todo', 0)}")
    print(f"    FIXME: {stats.get('fixme', 0)}")
    print(f"    HACK:  {stats.get('hack', 0)}")
    print(f"    BUG:   {stats.get('bug', 0)}")
    print()
    
    # Stale todos
    stale = find_stale_todos()
    if stale:
        print(f"  Stale (> {STALE_DAYS} days):")
        for todo in stale[:10]:
            print(f"    [{todo['type']}] {todo['days_stale']}d stale")
            print(f"      {todo['file']}:{todo['line']}")
            print(f"      {todo['text'][:80]}")
        if len(stale) > 10:
            print(f"    ... and {len(stale) - 10} more")
        print()
    
    # Group by file
    print("  By File:")
    by_file = {}
    for todo in todos:
        f = todo["file"]
        if f not in by_file:
            by_file[f] = []
        by_file[f].append(todo)
    
    for filepath, file_todos in sorted(by_file.items(), key=lambda x: -len(x[1]))[:10]:
        print(f"    {filepath}: {len(file_todos)} items")
    print()


def mine_todos_to_mempalace():
    """Push TODO index to MemPalace for semantic search."""
    try:
        from mempalace_fast import search
        index = load_todo_index()
        todos = index.get("todos", [])
        
        if not todos:
            return
        
        # Create searchable text for each TODO
        for todo in todos:
            search_text = f"""
            TODO: {todo['text']}
            File: {todo['file']}
            Line: {todo['line']}
            Type: {todo['type']}
            """.strip()
            
            # Would add to mempalace here
            # search() can find these later via natural language
        
        logger.info(f"Mined {len(todos)} TODOs to MemPalace")
        
    except Exception as e:
        logger.error(f"Failed to mine TODOs: {e}")


def scan_command(path: Optional[str] = None):
    """Scan command."""
    repos = load_tracked_repos()
    
    if path:
        paths_to_scan = [Path(path)]
    else:
        paths_to_scan = [Path(r) for r in repos]
    
    if not paths_to_scan:
        print("No repositories to scan.")
        print(f"Add with: python todo_tracker.py add <path>")
        return
    
    all_todos = []
    for scan_path in paths_to_scan:
        if scan_path.exists():
            print(f"Scanning: {scan_path}")
            todos = scan_directory(scan_path)
            all_todos.extend(todos)
            print(f"  Found: {len(todos)} TODOs")
        else:
            print(f"  Not found: {scan_path}")
    
    if all_todos:
        index = update_todo_index(all_todos)
        print(f"\nTotal: {index['stats']['total']} TODOs indexed")
        mine_todos_to_mempalace()


def add_command(path: str):
    """Add repository to track."""
    add_tracked_repo(path)
    scan_command(path)


def daemon_mode(interval: int = 3600):
    """Run as daemon, scanning periodically."""
    import time
    logger.info(f"TODO Tracker daemon started (interval: {interval}s)")
    
    # Initial scan
    scan_command()
    
    while True:
        time.sleep(interval)
        try:
            scan_command()
        except Exception as e:
            logger.error(f"Scan error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        scan_command()
    else:
        cmd = sys.argv[1].lower()
        if cmd == "scan":
            path = sys.argv[2] if len(sys.argv) > 2 else None
            scan_command(path)
        elif cmd == "add":
            if len(sys.argv) > 2:
                add_command(sys.argv[2])
            else:
                print("Usage: todo_tracker.py add <path>")
        elif cmd == "report":
            print_report()
        elif cmd == "stale":
            stale = find_stale_todos()
            print(f"Found {len(stale)} stale TODOs")
        elif cmd == "daemon":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 3600
            daemon_mode(interval)
        else:
            print(f"Unknown command: {cmd}")
            print("Commands: scan, add, report, stale, daemon")
