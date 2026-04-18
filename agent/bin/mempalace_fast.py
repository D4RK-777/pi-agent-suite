"""Thin wrapper so hooks and scripts can `from mempalace_fast import search`.

Reuses the installed mempalace package — does NOT reimplement search.
Returns dicts (not stdout prints) so callers can process results programmatically.

Install path: ~/.pi/agent/bin/mempalace_fast.py

Usage:
    from mempalace_fast import search, status
    results = search("react hooks typescript", n=3)
    s = status()

CLI usage:
    python mempalace_fast.py                    # status check
    python mempalace_fast.py react hooks        # quick search
"""

from __future__ import annotations

import io
import os
import sys
import time
from pathlib import Path

# Windows: force UTF-8 stdout/stderr so non-ASCII chars don't crash on cp1252 terminals.
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
    except Exception:
        pass

# Allow overriding the palace path via environment variable.
PALACE = os.environ.get(
    "MEMPALACE_PALACE",
    str(Path.home() / ".mempalace" / "palace"),
)

# Resolve mempalace package: prefer pip-installed, fall back to source checkout
# pointed to by PI_AGENT_HOME (useful during development / editable installs).
_pi_home = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi"))
_mempalace_src = _pi_home / "mempalace-src"
if _mempalace_src.is_dir() and str(_mempalace_src) not in sys.path:
    sys.path.insert(0, str(_mempalace_src))

try:
    from mempalace.searcher import search_memories as _search_memories
    from mempalace.backends.chroma import ChromaBackend as _ChromaBackend
    _MEMPALACE_AVAILABLE = True
except ImportError:
    _MEMPALACE_AVAILABLE = False

# Rolling average query time (in-process only, resets on restart).
_query_times_ms: list[float] = []


def search(
    query: str,
    wing: str | None = None,
    room: str | None = None,
    n: int = 5,
    max_distance: float = 0.0,
) -> dict:
    """Hybrid BM25+vector search. Returns a dict with a 'results' list.

    Each result has: text, wing, room, source_file, distance, similarity.
    Distance is cosine (0 = identical). Similarity = max(0, 1 - distance).

    Returns {"results": [], "error": "message"} on failure so callers can
    fail-silent without try/except.
    """
    if not _MEMPALACE_AVAILABLE:
        return {"results": [], "error": "mempalace package not installed — run: pip install mempalace"}

    t0 = time.perf_counter()
    try:
        out = _search_memories(
            query=query,
            palace_path=PALACE,
            wing=wing,
            room=room,
            n_results=n,
            max_distance=max_distance,
        )
    except Exception as e:
        return {"results": [], "error": str(e)}

    elapsed = (time.perf_counter() - t0) * 1000.0
    _query_times_ms.append(elapsed)
    if len(_query_times_ms) > 50:
        _query_times_ms.pop(0)
    return out


def status() -> dict:
    """Return a compact status dict.

    Keys: ok, palace_path, total_records, avg_query_time_ms, error (on failure).
    """
    if not _MEMPALACE_AVAILABLE:
        return {
            "ok": False,
            "error": "mempalace not installed — run: pip install mempalace",
            "total_records": 0,
            "avg_query_time_ms": 0,
        }
    try:
        backend = _ChromaBackend()
        col = backend.get_collection(PALACE, "mempalace_drawers", create=False)
        total = col.count()
    except Exception as e:
        return {
            "ok": False,
            "error": str(e),
            "total_records": 0,
            "avg_query_time_ms": 0,
        }

    avg = round(sum(_query_times_ms) / len(_query_times_ms), 1) if _query_times_ms else 0
    return {
        "ok": True,
        "palace_path": PALACE,
        "total_records": total,
        "avg_query_time_ms": avg,
    }


if __name__ == "__main__":
    s = status()
    if not s.get("ok"):
        print(f"Palace unavailable: {s.get('error')}", file=sys.stderr)
        sys.exit(1)
    print(f"Palace ready: {s['total_records']:,} records at {s['palace_path']}")
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        result = search(q, n=3)
        results = result.get("results", [])
        if not results:
            print("No results.")
        for i, r in enumerate(results, 1):
            sim = r.get("similarity")
            sim_s = f" (sim={sim:.2f})" if sim is not None else ""
            print(f"\n[{i}] {r.get('wing', '?')}/{r.get('room', '?')}{sim_s}")
            print((r.get("text") or "")[:400])
