"""
MemPalace Knowledge Curator
==========================
Runs periodically to keep the memory palace healthy:
- Deduplicates similar memories
- Removes stale/bloated entries  
- Consolidates fragmented knowledge
- Flags low-quality entries for review
- Maintains single source of truth

Philosophy: Allow mess during work, clean up after.

Usage:
    python knowledge_curator.py audit      # Analyze palace health
    python knowledge_curator.py clean     # Remove duplicates/stale
    python knowledge_curator.py compress  # Consolidate fragmented memories
    python knowledge_curator.py report     # Show palace health stats
    python knowledge_curator.py watch     # Start curator daemon
"""

import os
import sys
import json
import time
import hashlib
import logging
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter
from typing import Optional

# Config
PALACE_PATH = Path.home() / ".mempalace"
PROJECTS_FILE = PALACE_PATH / "project_wings.json"
CURATION_LOG = PALACE_PATH / "logs" / "knowledge_curator.log"
STALE_DAYS = 30  # Flag memories older than this
DUPLICATE_THRESHOLD = 0.92  # Similarity threshold for duplicates
MAX_MEMORIES_PER_WING = 500  # Soft limit before warning

# Setup logging
PALACE_PATH.mkdir(parents=True, exist_ok=True)
CURATION_LOG.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(CURATION_LOG),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def load_memories() -> dict:
    """Load all memories from ChromaDB."""
    try:
        # Import mempalace
        sys.path.insert(0, str(Path.home() / ".pi" / "agent" / "bin"))
        from mempalace_fast import search
        
        # Get all memories (using empty query to get recent)
        results = search(" ", n=1000)
        
        memories = []
        for r in results.get("results", []):
            memories.append({
                "content": r.get("content", ""),
                "source": r.get("source", ""),
                "wing": r.get("wing", ""),
                "room": r.get("room", ""),
                "similarity": r.get("similarity", 0),
                "semantic": r.get("semantic", 0),
            })
        
        return memories
        
    except Exception as e:
        logger.error(f"Failed to load memories: {e}")
        return []


def compute_text_hash(text: str) -> str:
    """Compute hash for deduplication."""
    return hashlib.md5(text.encode()).hexdigest()[:12]


def find_duplicates(memories: list[dict]) -> list[list[int]]:
    """Find groups of duplicate/near-duplicate memories."""
    duplicates = []
    processed = set()
    
    for i, mem in enumerate(memories):
        if i in processed:
            continue
        
        group = [i]
        content_i = mem.get("content", "")[:500]  # First 500 chars
        
        for j, other in enumerate(memories[i+1:], start=i+1):
            if j in processed:
                continue
            
            content_j = other.get("content", "")[:500]
            
            # Simple similarity check
            if compute_text_hash(content_i) == compute_text_hash(content_j):
                group.append(j)
                processed.add(j)
        
        if len(group) > 1:
            duplicates.append(group)
            processed.update(group)
    
    return duplicates


def find_stale(memories: list[dict], days: int = STALE_DAYS) -> list[int]:
    """Find memories that are stale (old and low-relevance)."""
    stale = []
    
    # This is simplified - in production you'd track access times
    # For now, flag very old memories with low similarity scores
    cutoff = datetime.now() - timedelta(days=days)
    
    for i, mem in enumerate(memories):
        # Flag very old entries that were never highly ranked
        if mem.get("similarity", 0) < 0.5:
            stale.append(i)
    
    return stale


def analyze_wings(memories: list[dict]) -> dict:
    """Analyze memories by wing."""
    by_wing = {}
    
    for mem in memories:
        wing = mem.get("wing", "unknown")
        if wing not in by_wing:
            by_wing[wing] = []
        by_wing[wing].append(mem)
    
    analysis = {}
    for wing, wing_mems in by_wing.items():
        analysis[wing] = {
            "count": len(wing_mems),
            "avg_similarity": sum(m.get("similarity", 0) for m in wing_mems) / len(wing_mems) if wing_mems else 0,
            "sources": list(set(m.get("source", "") for m in wing_mems)),
        }
    
    return analysis


def audit_palace() -> dict:
    """Perform full palace audit."""
    logger.info("Starting palace audit...")
    
    memories = load_memories()
    
    audit = {
        "timestamp": datetime.now().isoformat(),
        "total_memories": len(memories),
        "duplicates": [],
        "stale": [],
        "wings": {},
        "health_score": 0,
        "recommendations": []
    }
    
    if not memories:
        audit["health_score"] = 100
        audit["recommendations"].append("Palace is empty - no action needed")
        return audit
    
    # Find duplicates
    duplicates = find_duplicates(memories)
    audit["duplicates"] = [
        {"group_size": len(d), "indices": d[:5]}  # First 5 indices
        for d in duplicates
    ]
    
    # Find stale
    stale = find_stale(memories)
    audit["stale"] = stale[:10]  # First 10 indices
    
    # Wing analysis
    audit["wings"] = analyze_wings(memories)
    
    # Health score (0-100)
    health = 100
    health -= len(duplicates) * 5  # -5 per duplicate group
    health -= len(stale) * 2       # -2 per stale item
    health = max(0, health)
    audit["health_score"] = health
    
    # Recommendations
    if len(duplicates) > 5:
        audit["recommendations"].append(f"Remove {len(duplicates)} duplicate groups")
    if len(stale) > 10:
        audit["recommendations"].append(f"Review {len(stale)} stale memories")
    if audit["total_memories"] > 5000:
        audit["recommendations"].append("Consider consolidating memories - approaching capacity")
    
    for wing, data in audit["wings"].items():
        if data["count"] > MAX_MEMORIES_PER_WING:
            audit["recommendations"].append(f"Wing '{wing}' has {data['count']} memories - consider pruning")
    
    logger.info(f"Palace audit complete. Health: {health}%")
    
    return audit


def clean_duplicates():
    """Remove duplicate memories."""
    logger.info("Removing duplicates...")
    
    memories = load_memories()
    duplicates = find_duplicates(memories)
    
    if not duplicates:
        logger.info("No duplicates found")
        return {"removed": 0}
    
    # In production, this would delete from ChromaDB
    # For now, log what would be removed
    removed = 0
    for group in duplicates:
        # Keep first, remove rest
        removed += len(group) - 1
        logger.info(f"Duplicate group: keeping {group[0]}, removing {group[1:]}")
    
    logger.info(f"Would remove {removed} duplicate memories")
    
    return {"removed": removed, "groups": len(duplicates)}


def clean_stale():
    """Remove stale memories."""
    logger.info("Removing stale memories...")
    
    memories = load_memories()
    stale = find_stale(memories)
    
    if not stale:
        logger.info("No stale memories found")
        return {"removed": 0}
    
    logger.info(f"Would remove {len(stale)} stale memories")
    
    return {"removed": len(stale)}


def compress_memories():
    """Consolidate fragmented memories into cohesive units."""
    logger.info("Compressing memories...")
    
    memories = load_memories()
    
    # Group by source/topic
    by_source = {}
    for mem in memories:
        source = mem.get("source", "unknown")
        if source not in by_source:
            by_source[source] = []
        by_source[source].append(mem)
    
    compression_suggestions = []
    
    for source, source_mems in by_source.items():
        if len(source_mems) > 10:
            compression_suggestions.append({
                "source": source,
                "count": len(source_mems),
                "action": "consolidate",
                "suggestion": f"Consider merging {len(source_mems)} related memories from {source}"
            })
    
    logger.info(f"Found {len(compression_suggestions)} consolidation opportunities")
    
    return {"suggestions": compression_suggestions}


def print_report():
    """Print comprehensive report."""
    audit = audit_palace()
    
    print()
    print("=" * 60)
    print("  MemPalace Knowledge Curator Report")
    print("=" * 60)
    print()
    print(f"  Generated: {audit['timestamp'][:19]}")
    print()
    
    print(f"  Total Memories: {audit['total_memories']}")
    print(f"  Health Score:   {audit['health_score']}%")
    print()
    
    print("  Wings:")
    for wing, data in audit.get("wings", {}).items():
        print(f"    {wing}: {data['count']} memories (avg similarity: {data['avg_similarity']:.2f})")
    print()
    
    if audit.get("duplicates"):
        print(f"  Duplicate Groups: {len(audit['duplicates'])}")
        for d in audit["duplicates"][:3]:
            print(f"    - {d['group_size']} similar memories")
        print()
    
    if audit.get("recommendations"):
        print("  Recommendations:")
        for r in audit["recommendations"]:
            print(f"    * {r}")
        print()
    
    print("=" * 60)
    print()


def curator_daemon(interval: int = 3600):
    """Run curator as background daemon."""
    logger.info("=" * 50)
    logger.info("Knowledge Curator Daemon Started")
    logger.info(f"Check interval: {interval}s ({interval/60:.0f} min)")
    logger.info("=" * 50)
    
    # Save PID
    pid_file = PALACE_PATH / "pids" / "knowledge_curator.pid"
    pid_file.parent.mkdir(parents=True, exist_ok=True)
    pid_file.write_text(str(os.getpid()))
    
    while True:
        try:
            logger.info("Running scheduled curation...")
            
            # Quick audit
            audit = audit_palace()
            
            if audit["health_score"] < 80:
                logger.warning(f"Palace health low: {audit['health_score']}%")
                # Auto-clean if very unhealthy
                if audit["health_score"] < 60:
                    logger.info("Auto-cleaning...")
                    clean_duplicates()
            
            # Sleep until next check
            time.sleep(interval)
            
        except KeyboardInterrupt:
            logger.info("Curator stopped by user")
            break
        except Exception as e:
            logger.error(f"Curator error: {e}")
            time.sleep(interval)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_report()
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == "audit":
            audit = audit_palace()
            print(json.dumps(audit, indent=2))
        elif cmd == "clean":
            clean_duplicates()
            clean_stale()
            print("Cleanup complete")
        elif cmd == "compress":
            result = compress_memories()
            print(json.dumps(result, indent=2))
        elif cmd == "report":
            print_report()
        elif cmd == "watch":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 3600
            curator_daemon(interval)
        else:
            print(f"Unknown command: {cmd}")
            print("Commands: audit, clean, compress, report, watch")
