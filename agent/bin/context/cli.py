#!/usr/bin/env python3
"""
D4rk Mind — Context Manager CLI
Quick context retrieval from the command line.

Usage:
  python cli.py "explain the auth system"
  python cli.py "fix the login bug" --wings expert-auth --max-tokens 1500
  python cli.py "build a modal" --stats
"""

import sys
import os
import json
import time
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from __init__ import ContextManager


def main():
    parser = argparse.ArgumentParser(
        description="D4rk Mind Context Manager — Get relevant context for any query",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py "explain the auth system"
  python cli.py "build a modal component" --wings expert-frontend
  python cli.py "fix the bug" --max-tokens 1000
  python cli.py --stats "test query"

Wings:
  expert-frontend, expert-backend, expert-auth, expert-security,
  expert-optimization, expert-orchestration, design-systems,
  components, architecture, all
"""
    )
    
    parser.add_argument('query', nargs='?', help='Query to get context for')
    parser.add_argument('--wings', '-w', help='Comma-separated wings to search')
    parser.add_argument('--max-tokens', '-t', type=int, default=2000, help='Max tokens in context')
    parser.add_argument('--json', '-j', action='store_true', help='JSON output')
    parser.add_argument('--stats', '-s', action='store_true', help='Show performance stats')
    parser.add_argument('--no-cache', '-n', action='store_true', help='Disable cache')
    
    args = parser.parse_args()
    
    # Performance test mode
    if args.stats:
        print("\n" + "="*60)
        print("PERFORMANCE TEST")
        print("="*60 + "\n")
        
        test_queries = [
            "explain the auth system",
            "build a modal component",
            "how does react hooks work",
            "jwt token validation",
            "docker kubernetes deployment",
        ]
        
        cm = ContextManager()
        
        for q in test_queries:
            times = []
            for _ in range(3):
                start = time.time()
                cm.build_context(q, use_cache=False)
                times.append((time.time() - start) * 1000)
            
            avg = sum(times) / len(times)
            print(f"  '{q[:40]}...'")
            print(f"    Avg: {avg:.1f}ms, Min: {min(times):.1f}ms, Max: {max(times):.1f}ms\n")
        
        print("="*60)
        return
    
    if not args.query:
        parser.print_help()
        print("\n" + "="*60)
        print("Quick examples:")
        print("  python cli.py \"explain the auth system\"")
        print("  python cli.py \"build a modal\" --wings expert-frontend")
        print("  python cli.py --stats")
        print("="*60)
        return
    
    # Parse wings
    wings = args.wings.split(',') if args.wings else None
    
    # Build context
    cm = ContextManager()
    response = cm.build_context(
        args.query,
        wings=wings,
        max_tokens=args.max_tokens,
        use_cache=not args.no_cache
    )
    
    # Output
    if args.json:
        print(json.dumps({
            "query": response.query,
            "context": response.context,
            "sources": [
                {
                    "source": r.source,
                    "wing": r.wing,
                    "room": r.room,
                    "similarity": r.similarity,
                    "tokens": r.tokens,
                }
                for r in response.sources
            ],
            "stats": {
                "tokens_used": response.tokens_used,
                "retrieval_time_ms": response.retrieval_time_ms,
                "compression_ratio": response.compression_ratio,
                "wings_searched": response.wings_searched,
            }
        }, indent=2))
    else:
        print("\n" + "="*60)
        print(f"QUERY: {response.query}")
        print("="*60)
        print()
        print(f"  Wings searched: {', '.join(response.wings_searched)}")
        print(f"  Retrieval time: {response.retrieval_time_ms}ms")
        print(f"  Tokens used:    {response.tokens_used}")
        print(f"  Sources:        {len(response.sources)}")
        print()
        print("  Sources:")
        for i, r in enumerate(response.sources, 1):
            print(f"    [{i}] {r.wing}/{r.room} — {r.source} (sim: {r.similarity})")
        print()
        print("="*60)
        print(response.context)
        print("="*60)


if __name__ == "__main__":
    main()
