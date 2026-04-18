#!/usr/bin/env python3
"""
D4rk Mind — Context Tracker
Tracks conversation history, offloads to MemPalace, and displays effective context.

Shows: "Effective Context: 2.1M tokens" instead of "2M available"

How it works:
1. Monitor conversation tokens
2. Periodically summarize and offload to MemPalace
3. Calculate effective context = actual tokens + (retrieved patterns)
4. Display the growing effective context to the user
"""

import os
import sys
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict

# MemPalace
PALACE_PATH = str(Path.home() / ".mempalace" / "palace")

try:
    import chromadb
    CHROMA_AVAILABLE = True
except ImportError:
    CHROMA_AVAILABLE = False


@dataclass
class ConversationSegment:
    """A segment of conversation history."""
    id: str
    timestamp: str
    role: str  # 'user' or 'assistant'
    content: str
    tokens: int
    summary: Optional[str] = None
    offloaded: bool = False


@dataclass
class ContextStats:
    """Current context statistics."""
    actual_tokens: int
    max_tokens: int
    offloaded_tokens: int
    retrievable_patterns: int
    effective_context: int
    compression_ratio: float
    segments_stored: int
    retrieval_time_ms: float


class ContextTracker:
    """
    Tracks conversation context and manages effective context window.
    
    Usage:
        tracker = ContextTracker(max_tokens=2000000)  # 2M with compression
        
        # Track messages
        tracker.add_user_message("build me a modal")
        tracker.add_assistant_message("Here's the modal code...")
        
        # Get stats for display
        stats = tracker.get_stats()
        print(f"Effective Context: {stats.effective_context:,} tokens")
        
        # When context gets tight, offload oldest
        if tracker.should_offload():
            tracker.offload_oldest()
    """
    
    def __init__(
        self,
        max_tokens: int = 2000000,  # 2M effective context with MemPalace compression
        offload_threshold: float = 0.7,
        segment_interval: int = 5000,  # Offload every N tokens
    ):
        self.max_tokens = max_tokens
        self.offload_threshold = offload_threshold
        self.segment_interval = segment_interval
        
        # Conversation segments
        self.segments: List[ConversationSegment] = []
        self.current_tokens = 0
        
        # Offloaded segments storage
        self.offload_dir = Path.home() / ".mempalace" / "conversation_offload"
        self.offload_dir.mkdir(parents=True, exist_ok=True)
        
        # ChromaDB for retrieval
        self.collection = None
        if CHROMA_AVAILABLE:
            self._init_storage()
        
        # Stats
        self.retrieval_times: List[float] = []
        
    def _init_storage(self):
        """Initialize ChromaDB storage."""
        try:
            client = chromadb.PersistentClient(path=PALACE_PATH)
            self.collection = client.get_or_create_collection(
                name="conversation_history",
                metadata={"description": "Offloaded conversation segments"}
            )
        except Exception as e:
            print(f"⚠️  Storage init error: {e}")
    
    def _estimate_tokens(self, text: str) -> int:
        """Estimate tokens in text (~4 chars per token)."""
        return len(text) // 4
    
    def _generate_summary(self, content: str) -> str:
        """Generate a summary of conversation segment."""
        # Simple extractive summarization - first 2 sentences
        sentences = content.split('.')
        summary = '.'.join(sentences[:2])
        if len(summary) > 200:
            summary = summary[:200] + '...'
        return summary
    
    def _generate_id(self) -> str:
        """Generate unique ID for segment."""
        return hashlib.md5(f"{time.time()}{len(self.segments)}".encode()).hexdigest()[:12]
    
    def add_user_message(self, content: str) -> ConversationSegment:
        """Add a user message to tracking."""
        return self._add_segment("user", content)
    
    def add_assistant_message(self, content: str) -> ConversationSegment:
        """Add an assistant message to tracking."""
        return self._add_segment("assistant", content)
    
    def _add_segment(self, role: str, content: str) -> ConversationSegment:
        """Add a conversation segment."""
        tokens = self._estimate_tokens(content)
        
        segment = ConversationSegment(
            id=self._generate_id(),
            timestamp=datetime.now().isoformat(),
            role=role,
            content=content,
            tokens=tokens,
            summary=self._generate_summary(content),
        )
        
        self.segments.append(segment)
        self.current_tokens += tokens
        
        return segment
    
    def should_offload(self) -> bool:
        """Check if we should offload oldest segments."""
        # Offload if we're above threshold
        if self.current_tokens > self.max_tokens * self.offload_threshold:
            return True
        
        # Or if segment interval reached
        offloaded = sum(s.tokens for s in self.segments if s.offloaded)
        if self.current_tokens - offloaded > self.segment_interval:
            return True
        
        return False
    
    def offload_oldest(self, keep_segments: int = 2) -> int:
        """
        Offload oldest segments to MemPalace.
        
        Args:
            keep_segments: Number of recent segments to keep in memory
        
        Returns:
            Number of segments offloaded
        """
        if len(self.segments) <= keep_segments:
            return 0
        
        offloaded_count = 0
        offloaded_tokens = 0
        
        # Find oldest non-offloaded segments
        to_offload = [s for s in self.segments if not s.offloaded][:-keep_segments]
        
        for segment in to_offload:
            # Store in MemPalace
            if self.collection:
                try:
                    self.collection.add(
                        documents=[segment.content],
                        metadatas=[{
                            "role": segment.role,
                            "timestamp": segment.timestamp,
                            "summary": segment.summary or "",
                            "tokens": segment.tokens,
                            "conversation_id": "current",  # Could be dynamic
                        }],
                        ids=[f"conv_{segment.id}"]
                    )
                except Exception as e:
                    print(f"⚠️  Offload error: {e}")
            
            # Save locally too
            self._save_offload_locally(segment)
            
            # Mark as offloaded
            segment.offloaded = True
            offloaded_count += 1
            offloaded_tokens += segment.tokens
        
        # Update current tokens
        self.current_tokens -= offloaded_tokens
        
        # Compact segments list (remove oldest offloaded)
        self.segments = [s for s in self.segments if not s.offloaded] + \
                      [s for s in self.segments if s.offloaded][-keep_segments:]
        
        return offloaded_count
    
    def _save_offload_locally(self, segment: ConversationSegment):
        """Save offloaded segment locally."""
        file_path = self.offload_dir / f"{segment.id}.json"
        file_path.write_text(json.dumps(asdict(segment), indent=2))
    
    def retrieve_history(self, query: str, limit: int = 5) -> List[ConversationSegment]:
        """Retrieve relevant conversation history from MemPalace."""
        if not self.collection:
            return []
        
        start = time.time()
        
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=limit,
                include=["documents", "metadatas"]
            )
            
            retrieval_time = (time.time() - start) * 1000
            self.retrieval_times.append(retrieval_time)
            
            segments = []
            for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
                segments.append(ConversationSegment(
                    id=meta.get("id", ""),
                    timestamp=meta.get("timestamp", ""),
                    role=meta.get("role", "unknown"),
                    content=doc,
                    tokens=meta.get("tokens", 0),
                    summary=meta.get("summary", ""),
                    offloaded=True,
                ))
            
            return segments
            
        except Exception as e:
            print(f"⚠️  Retrieval error: {e}")
            return []
    
    def get_stats(self) -> ContextStats:
        """Get current context statistics."""
        # Count offloaded tokens
        offloaded_tokens = sum(s.tokens for s in self.segments if s.offloaded)
        
        # Estimate retrievable patterns (based on collection size)
        retrievable = 0
        if self.collection:
            try:
                retrievable = min(self.collection.count(), 1000)  # Cap at 1000
            except:
                pass
        
        # Calculate effective context
        # effective = actual remaining + (retrievable patterns * avg pattern tokens)
        avg_pattern_tokens = 500  # Assume 500 tokens per pattern
        effective = (self.max_tokens - self.current_tokens) + (retrievable * avg_pattern_tokens)
        
        # Compression ratio
        compression = 1.0
        if retrievable > 0:
            compression = (retrievable * avg_pattern_tokens) / max(1, self.current_tokens)
        
        # Avg retrieval time
        avg_retrieval = sum(self.retrieval_times) / len(self.retrieval_times) if self.retrieval_times else 0
        
        return ContextStats(
            actual_tokens=self.current_tokens,
            max_tokens=self.max_tokens,
            offloaded_tokens=offloaded_tokens,
            retrievable_patterns=retrievable,
            effective_context=effective,
            compression_ratio=compression,
            segments_stored=len([s for s in self.segments if s.offloaded]),
            retrieval_time_ms=round(avg_retrieval, 1),
        )
    
    def get_display(self) -> str:
        """
        Get display string for UI.
        
        Returns formatted string showing effective context.
        """
        stats = self.get_stats()
        
        # Format large numbers
        def fmt(n: int) -> str:
            if n >= 1_000_000:
                return f"{n/1_000_000:.1f}M"
            elif n >= 1_000:
                return f"{n/1_000:.0f}K"
            return str(n)
        
        # Calculate percentages
        used_pct = (stats.actual_tokens / stats.max_tokens) * 100
        remaining = stats.max_tokens - stats.actual_tokens
        
        lines = [
            "",
            "╔════════════════════════════════════════════════════════════════╗",
            "║                 D4RK EFFECTIVE CONTEXT                       ║",
            "╠════════════════════════════════════════════════════════════════╣",
            f"║  Effective Context:     {fmt(stats.effective_context):>10} tokens                  ║",
            f"║  ─────────────────────────────────────────────────────────   ║",
            f"║  Actual in context:    {fmt(stats.actual_tokens):>10} tokens ({used_pct:.0f}% used)   ║",
            f"║  Offloaded:            {fmt(stats.offloaded_tokens):>10} tokens                  ║",
            f"║  Retrievable patterns: {fmt(stats.retrievable_patterns):>10} segments                ║",
            f"║  Compression ratio:    {stats.compression_ratio:>10.1f}x                       ║",
            f"║  Retrieval speed:     {stats.retrieval_time_ms:>10.1f}ms                    ║",
            "╚════════════════════════════════════════════════════════════════╝",
            "",
        ]
        
        return "\n".join(lines)
    
    def get_status_line(self) -> str:
        """Get single-line status for display."""
        stats = self.get_stats()
        
        def fmt(n: int) -> str:
            if n >= 1_000_000:
                return f"{n/1_000_000:.1f}M"
            elif n >= 1_000:
                return f"{n/1_000:.0f}K"
            return str(n)
        
        used_pct = (stats.actual_tokens / stats.max_tokens) * 100
        
        return (
            f"Context: {fmt(stats.effective_context)} "
            f"({100-used_pct:.0f}% | "
            f"{fmt(stats.retrievable_patterns)} patterns | "
            f"{stats.retrieval_time_ms:.0f}ms)"
        )


def demo():
    """Demo the context tracker."""
    print("\n" + "="*60)
    print("D4RK MIND — Context Tracker Demo")
    print("="*60 + "\n")
    
    tracker = ContextTracker(max_tokens=50000)  # Small for demo
    
    # Simulate conversation
    messages = [
        ("user", "I want to build a modal component"),
        ("assistant", "I'll create an accessible modal with Radix UI. It will include keyboard navigation, focus trapping, and ARIA attributes."),
        ("user", "Great! Can you add a backdrop blur effect?"),
        ("assistant", "Added the backdrop blur with backdrop-filter: blur(8px) and a semi-transparent overlay. The modal now has a nice frosted glass effect."),
        ("user", "Perfect. Now add a slide-in animation"),
        ("assistant", "Done! Using Framer Motion's AnimatePresence and slide-in from bottom. Added spring physics for a natural feel."),
    ]
    
    for role, content in messages:
        if role == "user":
            tracker.add_user_message(content)
        else:
            tracker.add_assistant_message(content)
        
        # Check if we need to offload
        if tracker.should_offload():
            offloaded = tracker.offload_oldest()
            print(f"  ↕ Offloaded {offloaded} segments")
    
    # Show stats
    print(tracker.get_display())
    
    # Demo retrieval
    print("\nRetrieving relevant history:")
    history = tracker.retrieve_history("animation slide")
    for h in history:
        print(f"  - [{h.role}] {h.summary[:50]}...")
    
    # Show final status
    print(f"\nStatus: {tracker.get_status_line()}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", "-d", action="store_true", help="Run demo")
    args = parser.parse_args()
    
    if args.demo:
        demo()
    else:
        print(__doc__)
        print("\nRun with --demo to see it in action.")


# Integration helpers for AI coding harness
def create_tracker(max_tokens: int = 2000000) -> ContextTracker:
    """Create a new context tracker."""
    return ContextTracker(max_tokens=max_tokens)


def get_effective_context_display(tracker: ContextTracker) -> str:
    """Get display string for UI."""
    return tracker.get_display()


def get_status_line(tracker: ContextTracker) -> str:
    """Get single-line status."""
    return tracker.get_status_line()
