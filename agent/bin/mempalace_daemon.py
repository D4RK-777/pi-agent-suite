"""MemPalace HTTP daemon — keeps the palace loaded in memory for fast recall.

Listens on 127.0.0.1:8787. Endpoints:
  GET  /health                          → status dict
  GET  /search?q=...&n=3                → [{similarity, wing, room, source, text}, ...]
  POST /search   {q, wing?, n?}         → same shape
  POST /add      {content, wing, room?, source?}  → {filed: true, wing, chars}

Why it exists:
  Python + mempalace cold-start is 1.5-2s on this Windows box, which blows the
  UserPromptSubmit budget. This daemon amortizes that to one process.

Auto-start: Startup folder shortcut (pythonw.exe, no console window). The
`mempalace_keeper.py` watchdog launches this on login and restarts it if it dies.
"""

from __future__ import annotations

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# Reuse the wrapper so path resolution stays single-sourced.
BIN = Path(__file__).parent
if str(BIN) not in sys.path:
    sys.path.insert(0, str(BIN))
from mempalace_fast import PALACE, search, status  # noqa: E402

# Lazy-imported on first /add to avoid paying the miner import cost if
# nobody files a drawer this run.
_miner_mod = None


def _get_miner():
    global _miner_mod
    if _miner_mod is None:
        from mempalace import miner as _m  # noqa: E402
        _miner_mod = _m
    return _miner_mod


def _format_hits(results: list[dict]) -> list[dict]:
    hits = []
    for r in results or []:
        src = (r.get("source_file") or "") or ""
        # Windows vs POSIX safe basename
        src = src.replace("/", "\\").split("\\")[-1][:80]
        hits.append(
            {
                "similarity": round(r.get("similarity", 0.0), 3),
                "wing": r.get("wing", "") or "",
                "room": r.get("room", "") or "",
                "source": src,
                "text": (r.get("text") or "")[:500],
            }
        )
    return hits


class Handler(BaseHTTPRequestHandler):
    def _json(self, code: int, body: dict | list) -> None:
        data = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *_args, **_kw) -> None:
        # Silence default access logs — this daemon runs in pythonw with no console.
        return

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            s = status()
            self._json(200 if s.get("ok") else 503, s)
            return
        if parsed.path == "/search":
            qs = parse_qs(parsed.query)
            q = (qs.get("q") or [""])[0]
            wing = (qs.get("wing") or [None])[0]
            try:
                n = int((qs.get("n") or ["3"])[0])
            except ValueError:
                n = 3
            if not q:
                self._json(400, {"error": "missing q"})
                return
            try:
                out = search(q, wing=wing, n=n)
                self._json(200, _format_hits(out.get("results", [])))
            except Exception as e:  # keep the daemon alive on any palace error
                self._json(500, {"error": str(e)})
            return
        self._json(404, {"error": "not found"})

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            self._json(400, {"error": "bad json"})
            return
        parsed = urlparse(self.path)
        if parsed.path == "/search":
            q = payload.get("q") or payload.get("query") or ""
            wing = payload.get("wing")
            n = int(payload.get("n", 3))
            if not q:
                self._json(400, {"error": "missing q"})
                return
            try:
                out = search(q, wing=wing, n=n)
                self._json(200, _format_hits(out.get("results", [])))
            except Exception as e:
                self._json(500, {"error": str(e)})
            return
        if parsed.path == "/add":
            content = payload.get("content") or ""
            wing = payload.get("wing") or ""
            room = payload.get("room") or "notes"
            source = payload.get("source") or "pi-daemon-add"
            agent = payload.get("agent") or "pi"
            if not content or not wing:
                self._json(400, {"error": "content and wing required"})
                return
            try:
                miner = _get_miner()
                col = miner.get_collection(PALACE, create=True)
                miner.add_drawer(
                    collection=col,
                    wing=wing,
                    room=room,
                    content=content,
                    source_file=source,
                    chunk_index=0,
                    agent=agent,
                )
                self._json(200, {"filed": True, "wing": wing, "room": room, "chars": len(content)})
            except Exception as e:
                self._json(500, {"error": str(e)})
            return
        self._json(404, {"error": "not found"})


def main(host: str = "127.0.0.1", port: int = 8787) -> None:
    # Warm the palace so the first request is fast too.
    try:
        search("warmup", n=1)
    except Exception:
        pass
    server = ThreadingHTTPServer((host, port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
