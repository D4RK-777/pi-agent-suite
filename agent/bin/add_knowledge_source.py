#!/usr/bin/env python3
"""
D4rk Mind — Add Custom Knowledge Source
Add your own repositories to the knowledge garden.

Usage:
    python add_source.py                    # Interactive mode
    python add_source.py --name "MyLib" \
                          --url "https://github.com/user/mylib" \
                          --wing expert-frontend \
                          --room "components/mylib" \
                          --patterns "button modal card"
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass, asdict

try:
    import chromadb
except ImportError:
    chromadb = None

PALACE_PATH = str(Path.home() / ".mempalace" / "palace")
CUSTOM_SOURCES_FILE = Path.home() / ".mempalace" / "custom_sources.json"


@dataclass
class CustomSource:
    name: str
    url: str
    wing: str
    room: str
    description: str
    patterns: List[str]
    source_type: str = "github"  # github, web, local
    local_path: Optional[str] = None


class SourceManager:
    """Manage custom knowledge sources."""
    
    WINGS = [
        "expert-frontend",
        "expert-backend", 
        "expert-auth",
        "expert-security",
        "expert-optimization",
        "expert-orchestration",
        "design-systems",
        "components",
        "architecture",
    ]
    
    def __init__(self):
        self.sources = self._load_sources()
    
    def _load_sources(self) -> List[dict]:
        """Load custom sources."""
        if CUSTOM_SOURCES_FILE.exists():
            try:
                return json.loads(CUSTOM_SOURCES_FILE.read_text())
            except:
                pass
        return []
    
    def _save_sources(self):
        """Save custom sources."""
        CUSTOM_SOURCES_FILE.parent.mkdir(parents=True, exist_ok=True)
        CUSTOM_SOURCES_FILE.write_text(json.dumps(self.sources, indent=2))
    
    def add_source(self, source: CustomSource):
        """Add a new knowledge source."""
        # Check for duplicates
        for s in self.sources:
            if s['name'] == source.name:
                print(f"⚠️  Source '{source.name}' already exists, updating...")
                s.update(asdict(source))
                self._save_sources()
                return
        
        self.sources.append(asdict(source))
        self._save_sources()
        print(f"✅ Added source: {source.name}")
    
    def remove_source(self, name: str):
        """Remove a knowledge source."""
        before = len(self.sources)
        self.sources = [s for s in self.sources if s['name'] != name]
        
        if len(self.sources) < before:
            self._save_sources()
            print(f"✅ Removed source: {name}")
        else:
            print(f"⚠️  Source '{name}' not found")
    
    def list_sources(self):
        """List all custom sources."""
        if not self.sources:
            print("\n📭 No custom sources configured.")
            print("   Run with --add to add one.")
            return
        
        print("\n" + "=" * 60)
        print("CUSTOM KNOWLEDGE SOURCES")
        print("=" * 60)
        
        for source in self.sources:
            print(f"\n  📦 {source['name']}")
            print(f"     Wing: {source['wing']}")
            print(f"     Room: {source['room']}")
            print(f"     Type: {source['source_type']}")
            print(f"     URL:  {source['url']}")
            print(f"     Patterns: {len(source['patterns'])}")
            if source['description']:
                print(f"     {source['description']}")
        
        print("\n" + "=" * 60)
    
    def mine_all(self):
        """Mine all custom sources."""
        if not self.sources:
            print("No custom sources to mine.")
            return
        
        if not chromadb:
            print("⚠️  ChromaDB not available, skipping mining")
            return
        
        client = chromadb.PersistentClient(path=PALACE_PATH)
        collection = client.get_or_create_collection(
            name="custom_knowledge",
            metadata={"description": "Custom knowledge sources"}
        )
        
        total_stored = 0
        
        for source in self.sources:
            print(f"\n🌱 Mining: {source['name']}")
            
            try:
                if source['source_type'] == 'local' and source.get('local_path'):
                    stored = self._mine_local(collection, source)
                elif source['source_type'] == 'github':
                    stored = self._mine_github(collection, source)
                else:
                    stored = self._mine_web(collection, source)
                
                total_stored += stored
                print(f"   ✓ Stored {stored} patterns")
                
            except Exception as e:
                print(f"   ✗ Error: {e}")
        
        print(f"\n✅ Total patterns stored: {total_stored}")
    
    def _mine_local(self, collection, source: dict) -> int:
        """Mine from local directory."""
        import hashlib
        
        local_path = Path(source['local_path'])
        if not local_path.exists():
            return 0
        
        stored = 0
        patterns = source['patterns']
        
        for file_path in local_path.rglob('*'):
            if not file_path.is_file():
                continue
            
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                
                # Check if any pattern matches
                for pattern in patterns:
                    if pattern.lower() in content.lower():
                        doc_id = hashlib.md5(f"{source['name']}_{file_path.name}".encode()).hexdigest()[:16]
                        
                        collection.upsert(
                            documents=[content[:5000]],
                            metadatas=[{
                                'source': source['name'],
                                'wing': source['wing'],
                                'room': source['room'],
                                'pattern': pattern,
                                'file': str(file_path),
                            }],
                            ids=[doc_id]
                        )
                        stored += 1
                        break
                        
            except Exception:
                pass
        
        return stored
    
    def _mine_github(self, collection, source: dict) -> int:
        """Mine from GitHub."""
        import hashlib
        import httpx
        
        try:
            # Parse GitHub URL
            url = source['url']
            
            # Try to get repository content
            headers = {"Accept": "application/vnd.github.v3+json"}
            if os.environ.get("GITHUB_TOKEN"):
                headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
            
            response = httpx.get(url, headers=headers, timeout=30)
            
            if response.status_code != 200:
                return 0
            
            content = response.text
            stored = 0
            
            for pattern in source['patterns']:
                if pattern.lower() in content.lower():
                    doc_id = hashlib.md5(f"{source['name']}_{pattern}".encode()).hexdigest()[:16]
                    
                    collection.upsert(
                        documents=[content[:5000]],
                        metadatas=[{
                            'source': source['name'],
                            'wing': source['wing'],
                            'room': source['room'],
                            'pattern': pattern,
                            'url': url,
                        }],
                        ids=[doc_id]
                    )
                    stored += 1
            
            return stored
            
        except Exception as e:
            print(f"   ⚠️  GitHub fetch error: {e}")
            return 0
    
    def _mine_web(self, collection, source: dict) -> int:
        """Mine from web."""
        import hashlib
        import httpx
        
        try:
            response = httpx.get(source['url'], timeout=30, follow_redirects=True)
            
            if response.status_code != 200:
                return 0
            
            content = response.text[:10000]
            stored = 0
            
            for pattern in source['patterns']:
                if pattern.lower() in content.lower():
                    doc_id = hashlib.md5(f"{source['name']}_{pattern}".encode()).hexdigest()[:16]
                    
                    collection.upsert(
                        documents=[content],
                        metadatas=[{
                            'source': source['name'],
                            'wing': source['wing'],
                            'room': source['room'],
                            'pattern': pattern,
                            'url': source['url'],
                        }],
                        ids=[doc_id]
                    )
                    stored += 1
            
            return stored
            
        except Exception as e:
            print(f"   ⚠️  Web fetch error: {e}")
            return 0


def interactive_add():
    """Interactively add a new source."""
    print("\n" + "=" * 60)
    print("ADD KNOWLEDGE SOURCE")
    print("=" * 60)
    
    manager = SourceManager()
    
    # Get source details
    name = input("\n  Source name: ").strip()
    if not name:
        return
    
    url = input("  URL (GitHub repo, website, or local path): ").strip()
    
    print("\n  Wing (domain):")
    for i, wing in enumerate(SourceManager.WINGS, 1):
        print(f"    {i}. {wing}")
    wing_choice = input(f"  Choice [1-{len(SourceManager.WINGS)}]: ").strip()
    
    try:
        wing = SourceManager.WINGS[int(wing_choice) - 1]
    except:
        wing = SourceManager.WINGS[0]
    
    room = input("  Room (sub-folder, e.g., 'components/buttons'): ").strip() or "general"
    
    description = input("  Description: ").strip()
    
    print("\n  Patterns (keywords to search for, comma-separated):")
    print("  e.g., Button, Modal, Card, Form, Input, Dropdown...")
    patterns_str = input("  Patterns: ").strip()
    patterns = [p.strip() for p in patterns_str.split(',') if p.strip()]
    
    if not patterns:
        print("⚠️  At least one pattern required")
        return
    
    source_type = "github"
    if url.startswith('/') or (Path(url).exists() if url else False):
        source_type = "local"
    elif not 'github.com' in url:
        source_type = "web"
    
    source = CustomSource(
        name=name,
        url=url,
        wing=wing,
        room=room,
        description=description,
        patterns=patterns,
        source_type=source_type,
        local_path=url if source_type == "local" else None,
    )
    
    manager.add_source(source)
    
    # Offer to mine now
    print("\n" + "=" * 60)
    mine_now = input("  Mine this source now? (y/N): ").strip().lower()
    if mine_now == 'y':
        print()
        manager.mine_all()


def main():
    parser = argparse.ArgumentParser(description='Add knowledge source to D4rk Mind')
    parser.add_argument('--name', '-n', help='Source name')
    parser.add_argument('--url', '-u', help='URL or local path')
    parser.add_argument('--wing', '-w', help=f"Wing ({', '.join(SourceManager.WINGS)})")
    parser.add_argument('--room', '-r', help='Room/sub-folder')
    parser.add_argument('--patterns', '-p', help='Comma-separated patterns')
    parser.add_argument('--description', '-d', help='Description')
    parser.add_argument('--list', '-l', action='store_true', help='List all sources')
    parser.add_argument('--mine', '-m', action='store_true', help='Mine all sources')
    parser.add_argument('--remove', help='Remove a source by name')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')
    
    args = parser.parse_args()
    
    manager = SourceManager()
    
    if args.interactive:
        interactive_add()
    elif args.list:
        manager.list_sources()
    elif args.mine:
        manager.mine_all()
    elif args.remove:
        manager.remove_source(args.remove)
    elif args.name:
        if not args.url or not args.patterns:
            print("⚠️  --url and --patterns are required")
            return
        
        patterns = [p.strip() for p in args.patterns.split(',')]
        
        source = CustomSource(
            name=args.name,
            url=args.url,
            wing=args.wing or "expert-frontend",
            room=args.room or "general",
            description=args.description or "",
            patterns=patterns,
        )
        
        manager.add_source(source)
        
        # Offer to mine
        mine = input("\nMine this source now? (y/N): ").strip().lower()
        if mine == 'y':
            manager.mine_all()
    else:
        parser.print_help()
        print("\n" + "=" * 60)
        print("EXAMPLES:")
        print("  # Interactive mode")
        print("  python add_source.py --interactive")
        print()
        print("  # Add a GitHub repo")
        print("  python add_source.py -n 'MyLib' -u 'https://github.com/user/mylib' \\")
        print("    -w expert-frontend -r 'components/mylib' \\")
        print("    -p 'Button,Modal,Card'")
        print()
        print("  # Add a local directory")
        print("  python add_source.py -n 'LocalLib' -u '~/code/mylib' \\")
        print("    -w expert-frontend -r 'components' \\")
        print("    -p 'Button,Input,Select'")
        print("=" * 60)


if __name__ == '__main__':
    main()
