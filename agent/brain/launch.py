"""
Brain Launcher v2 — With Hooks, Memory, and Continuous Learning

Integrates:
  - SessionStart hooks (load previous context)
  - Memory persistence (save session state)
  - Continuous learning (extract patterns to MemPalace)
  - Quality gates (enforce output)
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Add paths
PI_ROOT = Path.home() / ".pi"
HARNESS_DIR = PI_ROOT / "agent" / "harness"
SKILLS_DIR = PI_ROOT / "agent" / "skills"
SESSIONS_DIR = PI_ROOT / "sessions"
MEMPALACE_BIN = PI_ROOT / "agent" / "bin"

# Add harness to path for imports
if str(HARNESS_DIR) not in sys.path:
    sys.path.insert(0, str(HARNESS_DIR))
if str(PI_ROOT / "agent" / "hooks") not in sys.path:
    sys.path.insert(0, str(PI_ROOT / "agent" / "hooks"))

from router import Router
from enforcement import Enforcer
from memory import search_memory, build_memory_context

def analyze_task(task: str) -> dict:
    """Analyze task using the router."""
    router = Router()
    result = router.route(task)
    return {
        "task": task,
        "matched_skills": result.skills_to_load,
        "skill_count": len(result.skills_to_load),
        "reasoning": result.reasoning,
        "selected_agent": result.selected_agent,
        "confidence": result.confidence
    }


# ---------------------------------------------------------------------------
# Session Memory
# ---------------------------------------------------------------------------

def get_latest_session() -> dict[str, Any] | None:
    """Load the most recent session."""
    sessions = sorted(SESSIONS_DIR.glob("session-*.json"), reverse=True)
    if sessions:
        return json.loads(sessions[0].read_text(encoding="utf-8"))
    return None


def save_session(
    task: str,
    outcome: str,
    patterns: list[str] | None = None,
    skills_used: list[str] | None = None
) -> Path:
    """Save session state for future recall."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filepath = SESSIONS_DIR / f"session-{timestamp}.json"
    
    session = {
        "timestamp": timestamp,
        "task": task,
        "outcome": outcome,
        "patterns": patterns or [],
        "skills_used": skills_used or [],
        "datetime": datetime.now().isoformat()
    }
    
    filepath.write_text(json.dumps(session, indent=2), encoding="utf-8")
    return filepath


def mine_to_mempalace(content: str, wing: str = "governance", room: str = "learned") -> bool:
    """Mine content to MemPalace."""
    try:
        result = subprocess.run(
            [
                "python", "-X", "utf8", "-m", "mempalace.cli", "mine",
                content, "--wing", wing, "--room", room
            ],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(PI_ROOT)
        )
        return result.returncode == 0
    except Exception:
        return False


def extract_and_mine_patterns(task: str, outcome: str) -> list[str]:
    """Extract patterns from session and mine to MemPalace."""
    patterns = []
    
    # Pattern: Task type → Outcome
    if outcome == "success":
        patterns.append(f"Task '{task}' completed successfully")
    
    # Mine patterns
    for pattern in patterns:
        mine_to_mempalace(pattern)
    
    return patterns


# ---------------------------------------------------------------------------
# Session Start Hook
# ---------------------------------------------------------------------------

def run_session_start_hook() -> str:
    """Run on session start - load previous context."""
    output = []
    output.append("\n" + "=" * 60)
    output.append("🧠 SESSION START")
    output.append("=" * 60)
    
    # Load latest session
    latest = get_latest_session()
    if latest:
        output.append(f"\n📋 Previous session ({latest.get('timestamp', 'unknown')}):")
        output.append(f"   Task: {latest.get('task', 'N/A')}")
        output.append(f"   Outcome: {latest.get('outcome', 'N/A')}")
        
        # Search MemPalace for related patterns
        patterns = search_memory(latest.get('task', ''), n=3)
        if patterns.get('results'):
            output.append("\n📌 Related patterns from memory:")
            for r in patterns['results'][:3]:
                source = r.get('source', '').split('/')[-1][:40]
                output.append(f"   - {source}")
    else:
        output.append("\n📋 No previous session found.")
    
    return "\n".join(output)


# ---------------------------------------------------------------------------
# Session End Hook
# ---------------------------------------------------------------------------

def run_session_end_hook(task: str, outcome: str, skills: list[str]) -> str:
    """Run on session end - save learnings and mine patterns."""
    output = []
    
    # Save session
    filepath = save_session(task, outcome, skills_used=skills)
    
    # Extract and mine patterns
    patterns = extract_and_mine_patterns(task, outcome)
    
    output.append("\n" + "=" * 60)
    output.append("💾 SESSION END")
    output.append("=" * 60)
    output.append(f"\n✅ Session saved: {filepath.name}")
    
    if patterns:
        output.append(f"✅ Mined {len(patterns)} patterns to MemPalace")
    else:
        output.append("ℹ️ No new patterns to mine")
    
    return "\n".join(output)


# ---------------------------------------------------------------------------
# Task Launcher
# ---------------------------------------------------------------------------

def launch_task(task: str, auto_load: bool = True) -> dict[str, Any]:
    """Launch a task with automatic skill loading and hooks."""
    
    # === SESSION START ===
    print(run_session_start_hook())
    
    print("\n🧠 **Brain Processing...**")
    print(f"\n📝 Task: {task}")
    
    # === ANALYZE ===
    analysis = analyze_task(task)
    matched_skills = analysis.get('matched_skills', [])
    
    print(f"\n🎯 Matched {len(matched_skills)} skills:")
    
    loaded_content = {}
    
    # === LOAD SKILLS ===
    for skill in matched_skills:
        print(f"  📚 `{skill}`")
        
        if auto_load:
            skill_path = SKILLS_DIR / skill / "SKILL.md"
            if skill_path.exists():
                content = skill_path.read_text(encoding="utf-8")
                loaded_content[skill] = content
                print(f"     ✓ Loaded")
            else:
                print(f"     ✗ Not found")
        else:
            print(f"     (not loaded)")
    
    # === MEMORY CONTEXT ===
    print("\n🧠 Searching memory...")
    memory = build_memory_context(task, n=5)
    if memory:
        print("   Found relevant patterns from previous sessions")
    
    # === BUILD CONTEXT ===
    context = _build_context(task, matched_skills, loaded_content, memory)
    
    # === RUN ===
    print("\n" + "=" * 60)
    print("✅ Context ready. Agent processing...")
    print("=" * 60 + "\n")
    
    return {
        "task": task,
        "analysis": analysis,
        "matched_skills": matched_skills,
        "loaded_content": loaded_content,
        "context": context,
        "memory_context": memory
    }


def _build_context(task: str, skills: list[str], content: dict[str, str], memory: str) -> str:
    """Build full context for agent."""
    parts = []
    
    parts.append(f"# Task: {task}")
    parts.append("")
    
    # Memory patterns
    if memory:
        parts.append("## Related Patterns from Memory")
        parts.append(memory)
        parts.append("")
    
    # Activated skills
    parts.append("## Activated Skills")
    
    for skill in skills:
        parts.append(f"\n### {skill}")
        parts.append("```")
        
        if skill in content:
            # Truncate long content
            skill_content = content[skill]
            if len(skill_content) > 2000:
                skill_content = skill_content[:2000] + "\n... (truncated)"
            parts.append(skill_content)
        else:
            parts.append("(skill content not loaded)")
        
        parts.append("```")
    
    return "\n".join(parts)


def complete_session(task: str, outcome: str = "success"):
    """Complete session - run end hooks."""
    analysis = analyze_task(task)
    skills = analysis.get('matched_skills', [])
    
    print(run_session_end_hook(task, outcome, skills))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    # Fix encoding
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    if len(sys.argv) < 2:
        print("Usage: launch.py <task>")
        print("\nExample:")
        print("  python launch.py 'build a React login form'")
        sys.exit(1)
    
    task = " ".join(sys.argv[1:])
    result = launch_task(task)
    
    print(f"\n📊 Summary:")
    print(f"   Skills loaded: {len(result['loaded_content'])}")
    print(f"   Memory patterns: {'Yes' if result['memory_context'] else 'None'}")


if __name__ == "__main__":
    main()
