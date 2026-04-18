#!/usr/bin/env python3
"""
D4rk Mind — Context Server
HTTP API for the Context Manager.

Start:
  python server.py

Endpoints:
  POST /context     - Build context for query
  GET  /health     - Health check
  GET  /stats      - Server statistics
  GET  /cache      - Cache status
  POST /cache/clear - Clear cache
"""

import sys
import os
import json
import time
import threading
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))

from __init__ import ContextManager, Wing

# Server config
HOST = "localhost"
PORT = 8766

# Global state
stats = {
    "requests": 0,
    "total_time_ms": 0,
    "cache_hits": 0,
    "start_time": time.time(),
}
stats_lock = threading.Lock()

# Initialize context manager
print("Initializing Context Manager...")
cm = ContextManager()
print("Ready!")


class Handler(BaseHTTPRequestHandler):
    """HTTP request handler."""
    
    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path == "/health":
            self.send_json({"status": "ok", "uptime": time.time() - stats["start_time"]})
            
        elif parsed.path == "/stats":
            with stats_lock:
                avg_time = stats["total_time_ms"] / stats["requests"] if stats["requests"] > 0 else 0
                self.send_json({
                    "requests": stats["requests"],
                    "avg_time_ms": round(avg_time, 1),
                    "cache_hits": stats["cache_hits"],
                    "uptime_seconds": round(time.time() - stats["start_time"], 1),
                })
            
        elif parsed.path == "/cache":
            cache_size = len(cm._cache)
            cache_oldest = 0
            cache_newest = 0
            if cm._cache:
                timestamps = [v["timestamp"] for v in cm._cache.values()]
                cache_oldest = min(timestamps)
                cache_newest = max(timestamps)
            
            self.send_json({
                "size": cache_size,
                "ttl": cm._cache_ttl,
                "oldest_entry": cache_oldest,
                "newest_entry": cache_newest,
            })
            
        else:
            self.send_json({
                "endpoints": [
                    "POST /context - Build context for query",
                    "GET /health - Health check",
                    "GET /stats - Server statistics",
                    "GET /cache - Cache status",
                    "POST /cache/clear - Clear cache",
                ],
                "example": {
                    "method": "POST",
                    "path": "/context",
                    "body": {
                        "query": "explain the auth system",
                        "wings": ["expert-auth"],
                        "max_tokens": 1500,
                    }
                }
            })
    
    def do_POST(self):
        parsed = urlparse(self.path)
        
        if parsed.path == "/context":
            # Read body
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode() if content_length > 0 else "{}"
            
            try:
                data = json.loads(body)
            except:
                self.send_error(400, "Invalid JSON")
                return
            
            query = data.get("query", "")
            wings = data.get("wings", None)
            max_tokens = data.get("max_tokens", 2000)
            
            if not query:
                self.send_error(400, "Missing 'query' parameter")
                return
            
            # Build context
            start = time.time()
            response = cm.build_context(query, wings=wings, max_tokens=max_tokens)
            elapsed = (time.time() - start) * 1000
            
            # Update stats
            with stats_lock:
                stats["requests"] += 1
                stats["total_time_ms"] += elapsed
                # Check if cache hit
                if response.retrieval_time_ms < elapsed * 0.5:
                    stats["cache_hits"] += 1
            
            # Send response
            self.send_json({
                "query": response.query,
                "context": response.context,
                "sources": [
                    {
                        "source": r.source,
                        "wing": r.wing,
                        "room": r.room,
                        "similarity": r.similarity,
                    }
                    for r in response.sources
                ],
                "stats": {
                    "total_time_ms": round(elapsed, 1),
                    "retrieval_time_ms": response.retrieval_time_ms,
                    "tokens_used": response.tokens_used,
                    "compression_ratio": response.compression_ratio,
                    "wings_searched": response.wings_searched,
                    "sources_count": len(response.sources),
                }
            })
            
        elif parsed.path == "/cache/clear":
            cm._cache.clear()
            with stats_lock:
                stats["cache_hits"] = 0
            self.send_json({"status": "cache cleared"})
            
        else:
            self.send_error(404, "Not found")
    
    def send_json(self, data, status=200):
        """Send JSON response."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
    
    def log_message(self, format, *args):
        """Custom logging."""
        print(f"  {args[0]}")
        pass


def run_server(port=PORT):
    """Run the HTTP server."""
    server = HTTPServer((HOST, port), Handler)
    print(f"\n{'='*60}")
    print(f"  D4rk Mind — Context Server")
    print(f"{'='*60}")
    print(f"  Running at: http://{HOST}:{port}")
    print(f"  Endpoints:")
    print(f"    POST /context  - Build context")
    print(f"    GET  /health   - Health check")
    print(f"    GET  /stats    - Statistics")
    print(f"    GET  /cache    - Cache status")
    print(f"  ")
    print(f"  Press Ctrl+C to stop")
    print(f"{'='*60}\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-p", type=int, default=PORT)
    args = parser.parse_args()
    
    run_server(args.port)
