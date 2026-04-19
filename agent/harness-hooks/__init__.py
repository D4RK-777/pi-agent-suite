#!/usr/bin/env python3
"""
Pi Hooks Runner

Command-line interface for running harness hooks.
Called by the hook-connector extension on lifecycle events.

Usage:
    python hooks.py session_start
    python hooks.py session_end [task] [skill1] [skill2] ...
    python hooks.py extract_patterns [transcript]
"""

from __future__ import annotations

import json
import sys
import subprocess
from dataclasses import dataclass, asdict
from datetime import datetime
import os
from pathlib import Path
from typing import Any

# ============================================================================
# PATHS
# ============================================================================

PI_ROOT = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi"))
AGENT_DIR = PI_ROOT / "agent"
SESSIONS_DIR = PI_ROOT / "sessions"
SKILLS_DIR = AGENT_DIR / "skills"
MEMPALACE_BIN = AGENT_DIR / "bin"

# Ensure directories exist
SESSIONS_DIR.mkdir(exist_ok=True, parents=True)
(AGENT_DIR / "runtime").mkdir(exist_ok=True, parents=True)


# ============================================================================
# UTILITIES
# ============================================================================

def run_command(cmd: list[str], timeout: int = 30) -> tuple[int, str, str]:
    """Run a command and return (code, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "Command timed out"
    except Exception as e:
        return 1, "", str(e)


def log(message: str, level: str = "INFO"):
    """Log a message."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}", file=sys.stderr)


# ============================================================================
# SESSION MEMORY
# ============================================================================

@dataclass
class Session:
    """Represents a session."""
    id: str
    start_time: float
    end_time: float | None
    task: str
    skills: list[str]
    outcome: str
    events: list[dict]

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Session:
        return cls(**data)


class SessionStore:
    """Manages session persistence."""

    def __init__(self):
        self.sessions_dir = SESSIONS_DIR
        self.sessions_dir.mkdir(exist_ok=True, parents=True)

    def save(self, session: Session) -> Path:
        """Save session to disk."""
        filename = f"{session.id}.json"
        filepath = self.sessions_dir / filename
        filepath.write_text(
            json.dumps(session.to_dict(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return filepath

    def load(self, session_id: str) -> Session | None:
        """Load session by ID."""
        filepath = self.sessions_dir / f"{session_id}.json"
        if filepath.exists():
            try:
                data = json.loads(filepath.read_text(encoding="utf-8"))
                return Session.from_dict(data)
            except (json.JSONDecodeError, TypeError):
                return None
        return None

    def get_latest(self) -> Session | None:
        """Get the most recent session."""
        sessions = sorted(
            self.sessions_dir.glob("session-*.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        if sessions:
            return self.load(sessions[0].stem)
        return None

    def list_recent(self, count: int = 5) -> list[Session]:
        """List recent sessions."""
        sessions = sorted(
            self.sessions_dir.glob("session-*.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )[:count]

        result = []
        for path in sessions:
            session = self.load(path.stem)
            if session:
                result.append(session)
        return result


# ============================================================================
# MEMPALACE INTEGRATION
# ============================================================================

def search_mempalace(query: str, wing: str = "governance", n: int = 5) -> list[dict]:
    """Search MemPalace for relevant memories."""
    cmd = [
        sys.executable,
        "-X", "utf8",
        "-m", "mempalace_fast",
        "search",
        query,
        "--wing", wing,
        "--n", str(n),
    ]

    code, stdout, stderr = run_command(cmd, timeout=10)

    if code == 0 and stdout:
        try:
            return json.loads(stdout)
        except json.JSONDecodeError:
            pass

    return []


def mine_to_mempalace(content: str, wing: str = "governance", room: str = "learned") -> bool:
    """Mine content to MemPalace."""
    cmd = [
        sys.executable,
        "-X", "utf8",
        "-c",
        f"""
import sys
sys.path.insert(0, r'{str(MEMPALACE_BIN)}')
from mempalace_fast import mine
result = mine('{content.replace("'", "''")}', wing='{wing}', room='{room}')
print('success' if result else 'failed')
""",
    ]

    code, stdout, stderr = run_command(cmd, timeout=15)
    return code == 0 and "success" in stdout.lower()


# ============================================================================
# PATTERN EXTRACTION
# ============================================================================

def extract_patterns(transcript: str) -> list[dict]:
    """Extract reusable patterns from transcript."""
    patterns = []

    # Success patterns
    if any(kw in transcript.lower() for kw in ["success", "done", "completed", "fixed"]):
        patterns.append({
            "type": "success",
            "content": "Task completed successfully",
            "timestamp": datetime.now().isoformat(),
        })

    # Error patterns
    if "error" in transcript.lower():
        patterns.append({
            "type": "error_encountered",
            "content": "An error was encountered",
            "timestamp": datetime.now().isoformat(),
        })

    # User correction patterns
    if any(kw in transcript.lower() for kw in ["corrected", "wrong", "different", "no,", "instead"]):
        patterns.append({
            "type": "user_correction",
            "content": "User provided a correction",
            "timestamp": datetime.now().isoformat(),
        })

    # Security patterns
    if any(kw in transcript.lower() for kw in ["security", "auth", "permission", "vulnerability"]):
        patterns.append({
            "type": "security_relevant",
            "content": "Task involved security considerations",
            "timestamp": datetime.now().isoformat(),
        })

    return patterns


# ============================================================================
# HOOK HANDLERS
# ============================================================================

def handle_session_start() -> str:
    """Handle session start event."""
    store = SessionStore()
    previous = store.get_latest()

    output = []
    output.append(f"Session store: {SESSIONS_DIR}")

    # Write context file for other systems
    context_file = AGENT_DIR / "runtime" / "session_context.md"
    (AGENT_DIR / "runtime").mkdir(exist_ok=True, parents=True)

    context_lines = ["## Session Context", ""]

    if previous:
        output.append(f"Previous session: {previous.id}")
        output.append(f"Previous task: {previous.task[:100] if previous.task else 'N/A'}...")
        output.append(f"Previous skills: {', '.join(previous.skills[:5])}")
        output.append(f"Outcome: {previous.outcome}")

        # Build context for injection
        context_lines.append(f"**Last session:** {previous.id}")
        context_lines.append(f"**Task:** {previous.task or 'N/A'}")
        if previous.skills:
            context_lines.append(f"**Skills used:** {', '.join(previous.skills)}")
        context_lines.append(f"**Outcome:** {previous.outcome}")
        context_lines.append("")

        # Search for related memories
        if previous.task:
            memories = search_mempalace(previous.task, n=3)
            if memories:
                output.append("\nRelated memories found:")
                context_lines.append("**Related memories:**")
                for mem in memories[:3]:
                    output.append(f"  - {str(mem)[:80]}...")
                    context_lines.append(f"- {str(mem)[:100]}...")
                context_lines.append("")
    else:
        output.append("No previous session found.")
        context_lines.append("No previous sessions found.")
        context_lines.append("")

    # Write context file
    context_file.write_text("\n".join(context_lines), encoding="utf-8")

    return "\n".join(output)


def handle_session_end(task: str = "", skills: list[str] = None) -> str:
    """Handle session end event."""
    skills = skills or []
    store = SessionStore()
    previous = store.get_latest()

    # Create session record
    session = Session(
        id=f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        start_time=previous.end_time if previous else datetime.now().timestamp(),
        end_time=datetime.now().timestamp(),
        task=task or (previous.task if previous else ""),
        skills=skills or (previous.skills if previous else []),
        outcome="completed",
        events=[],
    )

    # Save session
    filepath = store.save(session)
    log(f"Session saved: {session.id}")

    # Extract and mine patterns
    patterns = extract_patterns(task)
    mined = 0
    for pattern in patterns:
        if mine_to_mempalace(json.dumps(pattern)):
            mined += 1

    output = []
    output.append(f"Session ended: {session.id}")
    output.append(f"Task: {task[:100] if task else 'N/A'}")
    output.append(f"Skills: {', '.join(skills) if skills else 'None'}")
    output.append(f"Patterns mined: {mined}")

    return "\n".join(output)


def handle_extract_patterns(transcript: str = "") -> str:
    """Extract patterns from transcript and mine to MemPalace."""
    patterns = extract_patterns(transcript)

    if not patterns:
        return "No patterns extracted."

    mined = 0
    for pattern in patterns:
        if mine_to_mempalace(json.dumps(pattern)):
            mined += 1

    return f"Extracted {len(patterns)} patterns, mined {mined} to MemPalace."


def handle_precompact() -> str:
    """Handle pre-compaction event."""
    store = SessionStore()
    current = store.get_latest()

    if current:
        # Update session with precompact marker
        current.events.append({
            "type": "precompact",
            "timestamp": datetime.now().isoformat(),
        })
        store.save(current)
        return f"Precompact marker added to {current.id}"

    return "No active session to mark."


# ============================================================================
# MAIN
# ============================================================================

def main():
    if len(sys.argv) < 2:
        print("Usage: hooks.py <command> [args...]")
        print("")
        print("Commands:")
        print("  session_start              - Load previous session")
        print("  session_end [task] [skills...]  - End session and mine patterns")
        print("  extract_patterns [text]    - Extract patterns from text")
        print("  precompact                  - Mark before compaction")
        print("  test                        - Test hook system")
        sys.exit(1)

    command = sys.argv[1]

    if command == "session_start":
        print(handle_session_start())

    elif command == "session_end":
        # Parse remaining args: first is task, rest are skills
        args = sys.argv[2:]
        task = args[0] if args and not args[0].startswith("-") else ""
        skills = [a for a in args[1:] if not a.startswith("-")]
        print(handle_session_end(task, skills))

    elif command == "extract_patterns":
        transcript = sys.argv[2] if len(sys.argv) > 2 else ""
        print(handle_extract_patterns(transcript))

    elif command == "precompact":
        print(handle_precompact())

    elif command == "test":
        print("Testing hook system...")
        print(f"PI_ROOT: {PI_ROOT}")
        print(f"SESSIONS_DIR: {SESSIONS_DIR}")
        print(f"SKILLS_DIR: {SKILLS_DIR}")

        # Test session store
        store = SessionStore()
        print(f"Sessions: {len(list(SESSIONS_DIR.glob('*.json')))}")

        # Test MemPalace search
        results = search_mempalace("test query", n=2)
        print(f"MemPalace search: {len(results)} results")

        print("Hook system: OK")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
