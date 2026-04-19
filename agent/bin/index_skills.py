#!/usr/bin/env python3
"""
Index expert skills to MemPalace
Populates the expert wings with curated domain knowledge.
"""

import sys
import os

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from pathlib import Path
from typing import Dict, List

import chromadb

PALACE_PATH = str(Path.home() / ".mempalace" / "palace")

# Expert skill folders to index
EXPERT_SKILLS = {
    "expert-frontend": [
        ("components", "knowledge/components.md"),
        ("react-patterns", "knowledge/react-patterns.md"),
        ("css-architecture", "knowledge/css-architecture.md"),
        ("animation-motion", "knowledge/animation-motion.md"),
        ("accessibility", "knowledge/accessibility.md"),
        ("typography", "knowledge/typography.md"),
        ("recipes/components", "recipes/components.md"),
    ],
    "expert-backend": [
        ("api-design", "knowledge/api-design.md"),
    ],
    "expert-auth": [
        ("auth-patterns", "knowledge/auth-patterns.md"),
    ],
    "expert-security": [
        ("owasp-patterns", "knowledge/owasp-patterns.md"),
        ("security-patterns", "knowledge/security-patterns.md"),
    ],
    "expert-optimization": [
        ("performance-patterns", "knowledge/performance-patterns.md"),
    ],
    "expert-orchestration": [
        ("infra-patterns", "knowledge/infra-patterns.md"),
    ],
}

def index_file(client: chromadb.PersistentClient, wing: str, room: str, file_path: Path) -> int:
    """Index a single knowledge file."""
    collection = client.get_collection("mempalace_drawers")
    
    if not file_path.exists():
        print(f"  [SKIP] {file_path} not found")
        return 0
    
    content = file_path.read_text(encoding='utf-8', errors='replace')
    
    # Split into chunks (~500 chars each)
    chunk_size = 500
    chunks = []
    lines = content.split('\n')
    current = ""
    
    for line in lines:
        if len(current) + len(line) > chunk_size and current:
            chunks.append(current.strip())
            current = ""
        current += "\n" + line
    
    if current.strip():
        chunks.append(current.strip())
    
    # Add to collection
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            metadatas=[{
                "wing": wing,
                "room": room,
                "source_file": str(file_path),
                "chunk": i,
            }],
            ids=[f"{wing}/{room}/{file_path.name}/{i}"]
        )
    
    return len(chunks)


def main():
    print("=== INDEXING EXPERT SKILLS ===")
    print()
    
    client = chromadb.PersistentClient(path=PALACE_PATH)
    collection = client.get_collection("mempalace_drawers")
    
    skills_dir = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi")) / "agent" / "skills"
    
    total_chunks = 0
    
    for wing, files in EXPERT_SKILLS.items():
        print(f"[{wing}]")
        wing_chunks = 0
        
        for room, relative_path in files:
            file_path = skills_dir / wing / relative_path
            count = index_file(client, wing, room, file_path)
            if count > 0:
                print(f"  + {count} chunks from {relative_path}")
            wing_chunks += count
        
        print(f"  = {wing_chunks} total")
        total_chunks += wing_chunks
        print()
    
    print(f"TOTAL: {total_chunks} chunks indexed")
    
    # Verify
    print()
    print("=== VERIFICATION ===")
    for wing in EXPERT_SKILLS.keys():
        r = collection.get(where={"wing": wing}, limit=1000)
        docs = [d for d in r['documents'] if d]
        print(f"{wing}: {len(docs)} documents")


if __name__ == "__main__":
    main()
