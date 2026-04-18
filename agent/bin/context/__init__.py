#!/usr/bin/env python3
"""
D4rk Mind — Context Manager
Gives AI agents effectively unlimited context via semantic retrieval.

Architecture:
  User Query → Query Analyzer → Semantic Search → Compression → Model Context
                    ↓                ↓               ↓            ↓
               Keywords      MemPalace (~20ms)   Token Budget   ~2000 tokens

Usage:
  from context import ContextManager
  
  ctx = ContextManager()
  context = ctx.build_context("explain the auth system")
  print(context)  # Relevant patterns, compressed to fit
"""

import os
import sys
import json
import time
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache

# MemPalace integration
PALACE_PATH = str(Path.home() / ".mempalace" / "palace")

try:
    import chromadb
    CHROMA_AVAILABLE = True
except ImportError:
    CHROMA_AVAILABLE = False
    print("⚠️  ChromaDB not available")

try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    HTTPX_AVAILABLE = False


class Wing(Enum):
    """Knowledge wings."""
    FRONTEND = "expert-frontend"
    BACKEND = "expert-backend"
    AUTH = "expert-auth"
    SECURITY = "expert-security"
    OPTIMIZATION = "expert-optimization"
    ORCHESTRATION = "expert-orchestration"
    DESIGN_SYSTEMS = "design-systems"
    COMPONENTS = "components"
    ARCHITECTURE = "architecture"
    ALL = "all"


@dataclass
class ContextResult:
    """A retrieved context snippet."""
    content: str
    source: str
    wing: str
    room: str
    similarity: float
    tokens: int
    metadata: Dict = field(default_factory=dict)


@dataclass
class ContextResponse:
    """Complete context response."""
    query: str
    context: str
    sources: List[ContextResult]
    tokens_used: int
    retrieval_time_ms: float
    compression_ratio: float
    wings_searched: List[str]


class QueryAnalyzer:
    """Analyzes user queries to extract search intent."""
    
    # Keyword weights
    WEIGHTS = {
        'noun': 2.0,      # Main subject
        'verb': 1.5,      # Action
        'adj': 1.0,       # Modifier
        'tech': 3.0,     # Technical term (high value)
    }
    
    # Wing triggers
    WING_KEYWORDS = {
        'expert-frontend': [
            'ui', 'component', 'react', 'vue', 'angular', 'css', 'style',
            'button', 'modal', 'form', 'input', 'layout', 'animation',
            'accessibility', 'aria', 'responsive', 'tailwind', 'design'
        ],
        'expert-backend': [
            'api', 'endpoint', 'server', 'database', 'db', 'cache',
            'rest', 'graphql', 'microservice', 'queue', 'worker'
        ],
        'expert-auth': [
            'auth', 'login', 'jwt', 'oauth', 'session', 'token',
            'password', 'mfa', 'sso', 'permission', 'role'
        ],
        'expert-security': [
            'security', 'vulnerability', 'xss', 'csrf', 'injection',
            'encrypt', 'hash', 'secret', 'owasp'
        ],
        'expert-optimization': [
            'performance', 'optimize', 'speed', 'latency', 'cache',
            'bundle', 'algorithm', 'memory', 'profiling'
        ],
        'expert-orchestration': [
            'docker', 'kubernetes', 'deploy', 'ci', 'cd', 'pipeline',
            'infrastructure', 'terraform', 'aws', 'cloud'
        ],
    }
    
    def analyze(self, query: str) -> Dict[str, Any]:
        """Analyze query and return search parameters."""
        words = query.lower().split()
        
        # Extract technical terms
        tech_terms = self._extract_tech_terms(query)
        
        # Determine relevant wings
        wings = self._detect_wings(query)
        
        # Expand query with related terms
        expanded = self._expand_query(query, tech_terms)
        
        return {
            'original': query,
            'keywords': tech_terms,
            'wings': wings,
            'expanded_query': expanded,
            'intent': self._detect_intent(query),
        }
    
    def _extract_tech_terms(self, query: str) -> List[str]:
        """Extract technical terms from query."""
        # Common technical patterns
        tech_patterns = [
            r'\b(react|vue|angular|svelte|next|nuxt)\b',
            r'\b(api|rest|graphql|grpc|websocket)\b',
            r'\b(jwt|oauth|sso|mfa|auth)\b',
            r'\b(sql|mysql|postgres|mongodb|redis)\b',
            r'\b(docker|kubernetes|k8s|helm)\b',
            r'\b(aws|azure|gcp|terraform)\b',
            r'\b(ts|tsx|js|jsx|py|go|rs|java)\b',
            r'\b(modal|dialog|form|input|button|dropdown)\b',
            r'\b(hook|context|state|redux|zustand)\b',
            r'\b(middleware|proxy|load.?balanc)\b',
        ]
        
        import re
        terms = []
        for pattern in tech_patterns:
            matches = re.findall(pattern, query.lower())
            terms.extend(matches)
        
        return list(set(terms)) if terms else query.lower().split()[:3]
    
    def _detect_wings(self, query: str) -> List[str]:
        """Detect which knowledge wings to search."""
        query_lower = query.lower()
        matched_wings = []
        
        for wing, keywords in self.WING_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw in query_lower)
            if score > 0:
                matched_wings.append((wing, score))
        
        # Sort by score, return wings
        matched_wings.sort(key=lambda x: -x[1])
        return [w[0] for w in matched_wings[:3]] if matched_wings else ['expert-frontend']
    
    def _expand_query(self, query: str, tech_terms: List[str]) -> str:
        """Expand query with related terms."""
        # Simple expansion - in production, use word embeddings
        expanded = [query] + tech_terms
        return ' '.join(expanded)
    
    def _detect_intent(self, query: str) -> str:
        """Detect user intent."""
        query_lower = query.lower()
        
        if any(w in query_lower for w in ['how', 'what', 'why', 'explain']):
            return 'explanation'
        if any(w in query_lower for w in ['fix', 'bug', 'error', 'issue']):
            return 'debugging'
        if any(w in query_lower for w in ['build', 'create', 'implement', 'add']):
            return 'implementation'
        if any(w in query_lower for w in ['test', 'spec', 'verify']):
            return 'testing'
        if any(w in query_lower for w in ['optimize', 'improve', 'refactor']):
            return 'optimization'
        
        return 'general'


class ContextRetriever:
    """Fast MemPalace retrieval with connection pooling."""
    
    def __init__(self):
        self.client = None
        self.collection = None
        self._init_connection()
    
    def _init_connection(self):
        """Initialize ChromaDB connection."""
        if not CHROMA_AVAILABLE:
            return
        
        try:
            self.client = chromadb.PersistentClient(path=PALACE_PATH)
            self.collection = self.client.get_collection("mempalace_drawers")
        except Exception as e:
            print(f"⚠️  MemPalace init error: {e}")
    
    def retrieve(
        self,
        query: str,
        wings: Optional[List[str]] = None,
        n_results: int = 10
    ) -> List[ContextResult]:
        """Retrieve relevant context from MemPalace."""
        if not self.collection:
            return []
        
        # Build where filter
        where = {}
        if wings and 'all' not in wings:
            if len(wings) == 1:
                where = {"wing": wings[0]}
            else:
                where = {"$or": [{"wing": w} for w in wings]}
        
        try:
            kwargs = {
                "query_texts": [query],
                "n_results": n_results,
                "include": ["documents", "metadatas", "distances"],
            }
            if where:
                kwargs["where"] = where
            
            results = self.collection.query(**kwargs)
            
            contexts = []
            docs = results["documents"][0]
            metas = results["metadatas"][0]
            dists = results["distances"][0]
            
            for doc, meta, dist in zip(docs, metas, dists):
                contexts.append(ContextResult(
                    content=doc.strip()[:2000],  # Limit content
                    source=meta.get("source_file", "unknown"),
                    wing=meta.get("wing", "unknown"),
                    room=meta.get("room", "unknown"),
                    similarity=round(1 - dist, 3),
                    tokens=self._estimate_tokens(doc),
                    metadata=meta,
                ))
            
            return contexts
            
        except Exception as e:
            print(f"⚠️  Retrieval error: {e}")
            return []
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation (~4 chars per token)."""
        return len(text) // 4


class Compressor:
    """Smart context compression."""
    
    def __init__(self, max_tokens: int = 2000):
        self.max_tokens = max_tokens
    
    def compress(
        self,
        results: List[ContextResult],
        max_tokens: Optional[int] = None
    ) -> Tuple[str, List[ContextResult], float]:
        """
        Compress results to fit token budget.
        
        Returns:
            (compressed_context, used_results, compression_ratio)
        """
        max_tokens = max_tokens or self.max_tokens
        
        if not results:
            return "", [], 1.0
        
        # Sort by relevance
        sorted_results = sorted(results, key=lambda x: -x.similarity)
        
        # Greedy selection - pick highest relevance first
        selected = []
        total_tokens = 0
        
        for result in sorted_results:
            if total_tokens + result.tokens <= max_tokens:
                selected.append(result)
                total_tokens += result.tokens
            elif total_tokens < max_tokens * 0.8:
                # Try to fit partial content
                remaining = max_tokens - total_tokens
                partial_content = result.content[:remaining * 4]  # rough chars
                result.content = partial_content
                result.tokens = remaining
                selected.append(result)
                total_tokens = max_tokens
                break
        
        # Build context string
        context = self._build_context(selected)
        
        compression = len(results) / len(selected) if selected else 1.0
        
        return context, selected, compression
    
    def _build_context(self, results: List[ContextResult]) -> str:
        """Build context string from results."""
        parts = []
        
        for i, result in enumerate(results, 1):
            parts.append(f"\n{'='*60}")
            parts.append(f"[{i}] {result.wing}/{result.room}")
            parts.append(f"Source: {result.source} (relevance: {result.similarity})")
            parts.append(f"{'='*60}")
            parts.append(result.content)
            parts.append("")
        
        return "\n".join(parts)


class ContextManager:
    """
    Main context manager - builds relevant context from MemPalace.
    
    Usage:
        ctx = ContextManager()
        response = ctx.build_context("explain the auth system")
        print(response.context)
    """
    
    def __init__(self, max_tokens: int = 2000):
        self.query_analyzer = QueryAnalyzer()
        self.retriever = ContextRetriever()
        self.compressor = Compressor(max_tokens)
        self.max_tokens = max_tokens
        
        # Cache
        self._cache = {}
        self._cache_ttl = 300  # 5 minutes
    
    def build_context(
        self,
        query: str,
        wings: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        use_cache: bool = True
    ) -> ContextResponse:
        """
        Build relevant context for a query.
        
        Args:
            query: User query
            wings: Specific wings to search (auto-detected if None)
            max_tokens: Max tokens in output
            use_cache: Use cached results
        
        Returns:
            ContextResponse with context and metadata
        """
        start_time = time.time()
        
        # Check cache
        cache_key = hashlib.md5(query.encode()).hexdigest()
        if use_cache and cache_key in self._cache:
            cached = self._cache[cache_key]
            if time.time() - cached['timestamp'] < self._cache_ttl:
                return cached['response']
        
        # Step 1: Analyze query
        analysis = self.query_analyzer.analyze(query)
        
        # Step 2: Determine wings
        search_wings = wings or analysis['wings']
        
        # Step 3: Retrieve from MemPalace
        results = self.retriever.retrieve(
            query=analysis['expanded_query'],
            wings=search_wings,
            n_results=15
        )
        
        # Step 4: Compress to token budget
        max_tok = max_tokens or self.max_tokens
        context, used_results, compression = self.compressor.compress(
            results, max_tok
        )
        
        # Build response
        response = ContextResponse(
            query=query,
            context=context,
            sources=used_results,
            tokens_used=sum(r.tokens for r in used_results),
            retrieval_time_ms=round((time.time() - start_time) * 1000, 1),
            compression_ratio=round(compression, 2),
            wings_searched=search_wings,
        )
        
        # Cache
        if use_cache:
            self._cache[cache_key] = {
                'response': response,
                'timestamp': time.time(),
            }
        
        return response
    
    def build_prompt(
        self,
        query: str,
        system_prompt: str = "",
        max_context_tokens: int = 1500
    ) -> str:
        """
        Build a complete prompt with context.
        
        Args:
            query: User query
            system_prompt: Optional system instructions
            max_context_tokens: Max tokens for context
        
        Returns:
            Complete prompt string
        """
        response = self.build_context(query, max_tokens=max_context_tokens)
        
        parts = []
        
        # System prompt
        if system_prompt:
            parts.append(f"<system>\n{system_prompt}\n</system>")
        
        # Context
        if response.context:
            parts.append(f"<context>\n{response.context}\n</context>")
        
        # Sources info
        parts.append(f"<!-- Context: {len(response.sources)} sources, {response.retrieval_time_ms}ms retrieval -->")
        
        # Query
        parts.append(f"<query>\n{query}\n</query>")
        
        return "\n\n".join(parts)


# CLI interface
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='D4rk Mind — Context Manager')
    parser.add_argument('query', nargs='?', help='Query to get context for')
    parser.add_argument('--wings', '-w', help='Comma-separated wings to search')
    parser.add_argument('--max-tokens', '-t', type=int, default=2000, help='Max tokens')
    parser.add_argument('--json', '-j', action='store_true', help='JSON output')
    parser.add_argument('--stats', '-s', action='store_true', help='Show stats only')
    
    args = parser.parse_args()
    
    if not args.query:
        parser.print_help()
        return
    
    ctx = ContextManager(max_tokens=args.max_tokens)
    
    wings = args.wings.split(',') if args.wings else None
    
    if args.stats:
        # Just measure performance
        import time
        times = []
        for _ in range(5):
            start = time.time()
            ctx.build_context(args.query, wings=wings)
            times.append((time.time() - start) * 1000)
        
        print(f"\nPerformance ({len(times)} runs):")
        print(f"  Avg: {sum(times)/len(times):.1f}ms")
        print(f"  Min: {min(times):.1f}ms")
        print(f"  Max: {max(times):.1f}ms")
        return
    
    response = ctx.build_context(args.query, wings=wings)
    
    if args.json:
        print(json.dumps({
            'query': response.query,
            'context': response.context,
            'sources': [
                {
                    'source': r.source,
                    'wing': r.wing,
                    'room': r.room,
                    'similarity': r.similarity,
                    'tokens': r.tokens,
                }
                for r in response.sources
            ],
            'stats': {
                'tokens_used': response.tokens_used,
                'retrieval_time_ms': response.retrieval_time_ms,
                'compression_ratio': response.compression_ratio,
                'wings_searched': response.wings_searched,
            }
        }, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"CONTEXT: {args.query}")
        print(f"{'='*60}")
        print(f"\nWings searched: {', '.join(response.wings_searched)}")
        print(f"Retrieval time: {response.retrieval_time_ms}ms")
        print(f"Tokens used: {response.tokens_used}")
        print(f"Sources: {len(response.sources)}")
        print(f"\n{'='*60}")
        print(response.context)
        print(f"{'='*60}")


if __name__ == '__main__':
    main()
