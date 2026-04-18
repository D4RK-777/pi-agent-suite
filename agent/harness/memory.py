"""Pi Memory Integration — MemPalace connector for the Pi Harness.

Provides fast recall of patterns, decisions, and expertise from the local
ChromaDB palace. No CLI subprocess — queries ChromaDB directly.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

# ─── Config ──────────────────────────────────────────────────────────────────

PI_ROOT = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi")) / "agent"
SKILLS_DIR = PI_ROOT / "skills"
PALACE_PATH = os.environ.get("MEMPALACE_PALACE", str(Path.home() / ".mempalace" / "palace"))

MEMORY_WINGS = {
    "frontend": ["components", "css", "react", "animation", "accessibility", "patterns"],
    "backend": ["api", "database", "middleware", "validation", "architecture"],
    "security": ["auth", "vulnerabilities", "encryption", "owasp"],
    "optimization": ["performance", "bundle", "caching", "latency"],
    "orchestration": ["docker", "kubernetes", "ci-cd", "deployment"],
    "governance": ["skills", "workflows", "patterns", "decisions"],
}

# ─── Direct ChromaDB access ────────────────────────────────────────────────

_client = None
_collection = None


def _get_collection():
    """Warm ChromaDB connection — reused across calls."""
    global _client, _collection
    if _collection is None:
        import chromadb
        _client = chromadb.PersistentClient(path=PALACE_PATH)
        _collection = _client.get_collection("mempalace_drawers")
    return _collection


def search_memory(query: str, wing: str | None = None, n: int = 5) -> dict[str, Any]:
    """Search MemPalace directly via ChromaDB."""
    try:
        col = _get_collection()
        where = {"wing": wing} if wing else None
        kwargs: dict = {
            "query_texts": [query],
            "n_results": n,
            "include": ["documents", "metadatas", "distances"],
        }
        if where:
            kwargs["where"] = where

        results = col.query(**kwargs)
        items = []
        for doc, m, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            items.append({
                "content": doc.strip(),
                "source": Path(m.get("source_file", "?")).name,
                "wing": m.get("wing", "?"),
                "room": m.get("room", "?"),
                "similarity": round(1 - dist, 3),
            })
        return {"query": query, "results": items}
    except Exception as e:
        return {"query": query, "error": str(e), "results": []}


def build_memory_context(query: str, wing: str | None = None, n: int = 5) -> str:
    """Build a markdown memory context block for injection into agent prompts."""
    result = search_memory(query, wing=wing, n=n)
    if not result.get("results"):
        return ""
    parts = ["## Related Patterns from Memory", ""]
    for r in result["results"]:
        parts.append(f"**From: {r.get('source', 'unknown')}**")
        parts.append((r.get("content") or "")[:500])
        parts.append("")
    return "\n".join(parts)


def search_all_wings(query: str, n: int = 3) -> dict[str, Any]:
    """Search all wings and return aggregated results."""
    all_results = {}
    for wing in MEMORY_WINGS:
        all_results[wing] = search_memory(query, wing=wing, n=n)
    return {"query": query, "wings_searched": list(MEMORY_WINGS), "results": all_results}


# ─── Mining ────────────────────────────────────────────────────────────────

def mine_memory(content: str, wing: str, room: str | None = None) -> dict[str, Any]:
    """Add knowledge to MemPalace via the CLI."""
    try:
        cmd = [sys.executable, "-m", "mempalace.cli", "mine", content, "--wing", wing]
        if room:
            cmd += ["--room", room]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return {
            "success": result.returncode == 0,
            "wing": wing,
            "room": room,
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None,
        }
    except Exception as e:
        return {"success": False, "wing": wing, "error": str(e)}


# ─── Stats ─────────────────────────────────────────────────────────────────

def get_memory_stats() -> dict[str, Any]:
    """Return MemPalace status via the installed CLI."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "mempalace", "status"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return {
            "status": "available" if result.returncode == 0 else "unavailable",
            "output": result.stdout if result.returncode == 0 else result.stderr,
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


# ─── CLI ───────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: memory.py <command> [args]")
        print("\nCommands:")
        print("  search <query> [wing]     — Search memory")
        print("  search-all <query>        — Search all wings")
        print("  stats                     — Memory statistics")
        print("  mine <content> <wing>     — Add to memory")
        print("  context <query> [wing]    — Build context for agent")
        sys.exit(1)

    command = sys.argv[1]

    if command == "search":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        wing = sys.argv[3] if len(sys.argv) > 3 else None
        print(json.dumps(search_memory(query, wing=wing), indent=2))
    elif command == "search-all":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        print(json.dumps(search_all_wings(query), indent=2))
    elif command == "stats":
        print(json.dumps(get_memory_stats(), indent=2))
    elif command == "mine":
        content = sys.argv[2] if len(sys.argv) > 2 else ""
        wing = sys.argv[3] if len(sys.argv) > 3 else "governance"
        print(json.dumps(mine_memory(content, wing=wing), indent=2))
    elif command == "context":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        wing = sys.argv[3] if len(sys.argv) > 3 else None
        print(build_memory_context(query, wing=wing))
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
