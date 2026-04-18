#!/usr/bin/env python3
"""
D4rk Mind — Project Indexer
Deep-index a project into MemPalace with structure awareness.

Usage:
    python index_projects.py                          # Index current dir
    python index_projects.py ~/code/myapp            # Index specific project
    python index_projects.py --all                   # Index all detected projects
    python index_projects.py --watch                 # Continuous mode
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

try:
    import chromadb
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False

# MemPalace config
PALACE_PATH = str(Path.home() / ".mempalace" / "palace")

# File patterns
CODE_EXTENSIONS = {
    '.py', '.js', '.ts', '.jsx', '.tsx', '.vue', '.svelte',
    '.java', '.kt', '.go', '.rs', '.c', '.cpp', '.h', '.hpp',
    '.cs', '.rb', '.php', '.swift', '.m', '.sql', '.sh',
    '.yaml', '.yml', '.toml', '.json', '.xml', '.md',
}

SKIP_DIRS = {
    'node_modules', '.git', '__pycache__', '.venv', 'venv',
    'dist', 'build', '.next', '.nuxt', 'target', 'out',
    '.cache', '.tmp', '.temp', 'tmp', '.parcel-cache',
    'vendor', 'packages', '.pnpm-store', '.yarn-cache',
    '.idea', '.vscode', '.DS_Store', '.env', '.env.local',
}


class ProjectIndexer:
    """Deep project indexer for MemPalace."""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path.resolve()
        self.project_name = self.project_path.name
        self.wing = f"project_{self.project_name}"
        self.files_indexed = 0
        self.errors = 0
        self.start_time = time.time()
        
        # ChromaDB client
        self.client = None
        self.collection = None
        
        if CHROMADB_AVAILABLE:
            try:
                self.client = chromadb.PersistentClient(path=PALACE_PATH)
                self.collection = self.client.get_or_create_collection(
                    name="project_index",
                    metadata={"description": "Codebase structure index"}
                )
            except Exception as e:
                print(f"⚠️  Could not initialize ChromaDB: {e}")
    
    def index_project(self) -> Dict:
        """Index an entire project."""
        print(f"\n📁 Indexing: {self.project_path}")
        print(f"   Wing: {self.wing}")
        print()
        
        # Index project structure first
        self._index_structure()
        
        # Index all code files
        self._index_files()
        
        # Index README and docs
        self._index_docs()
        
        # Index dependencies
        self._index_dependencies()
        
        duration = time.time() - self.start_time
        
        return {
            'project': self.project_name,
            'path': str(self.project_path),
            'wing': self.wing,
            'files_indexed': self.files_indexed,
            'errors': self.errors,
            'duration': round(duration, 2),
        }
    
    def _index_structure(self):
        """Index the directory structure."""
        print("  📊 Mapping structure...")
        
        structure = self._get_directory_tree(self.project_path, max_depth=3)
        
        if self.collection:
            try:
                self.collection.add(
                    documents=[json.dumps(structure)],
                    metadatas=[{
                        'wing': self.wing,
                        'room': 'structure',
                        'source_file': 'PROJECT_STRUCTURE',
                        'file_type': 'structure',
                    }],
                    ids=[f"{self.wing}_structure"]
                )
                print("    ✓ Structure indexed")
            except Exception as e:
                print(f"    ✗ Structure error: {e}")
    
    def _get_directory_tree(self, root: Path, max_depth: int = 3, current_depth: int = 0) -> Dict:
        """Get directory tree structure."""
        if current_depth >= max_depth:
            return {'_truncated': True}
        
        tree = {
            'type': 'directory',
            'name': root.name,
            'children': []
        }
        
        try:
            for item in sorted(root.iterdir()):
                name = item.name
                
                # Skip certain items
                if name.startswith('.') or name in SKIP_DIRS:
                    continue
                
                if item.is_dir():
                    tree['children'].append(
                        self._get_directory_tree(item, max_depth, current_depth + 1)
                    )
                elif item.is_file() and item.suffix.lower() in CODE_EXTENSIONS:
                    tree['children'].append({
                        'type': 'file',
                        'name': item.name,
                        'ext': item.suffix.lower(),
                    })
        except PermissionError:
            pass
        
        return tree
    
    def _index_files(self):
        """Index all code files."""
        print("  📝 Indexing files...")
        
        files = list(self.project_path.rglob('*'))
        code_files = [f for f in files if f.is_file() and f.suffix.lower() in CODE_EXTENSIONS]
        
        print(f"    Found {len(code_files)} code files")
        
        for i, file_path in enumerate(code_files):
            # Skip unwanted directories
            if any(skip in file_path.parts for skip in SKIP_DIRS):
                continue
            
            try:
                # Get relative path for room
                rel_path = file_path.relative_to(self.project_path)
                room = str(rel_path.parent) if len(rel_path.parts) > 1 else 'root'
                
                # Read content (limit to 10KB)
                content = file_path.read_text(encoding='utf-8', errors='ignore')[:10000]
                
                # Skip empty files
                if len(content.strip()) < 10:
                    continue
                
                # Detect file type
                file_type = self._detect_file_type(file_path, content)
                
                # Generate ID
                file_id = f"{self.wing}_{rel_path}".replace('/', '_').replace('\\', '_')
                
                if self.collection:
                    try:
                        self.collection.add(
                            documents=[content],
                            metadatas=[{
                                'wing': self.wing,
                                'room': room,
                                'source_file': str(rel_path),
                                'file_type': file_type,
                                'extension': file_path.suffix.lower(),
                                'project': self.project_name,
                            }],
                            ids=[file_id]
                        )
                        self.files_indexed += 1
                    except Exception as e:
                        self.errors += 1
                
                if (i + 1) % 100 == 0:
                    print(f"    Progress: {i + 1}/{len(code_files)}")
                    
            except Exception as e:
                self.errors += 1
        
        print(f"    ✓ Indexed {self.files_indexed} files")
    
    def _detect_file_type(self, path: Path, content: str) -> str:
        """Detect file type."""
        name = path.name.lower()
        
        if 'test' in name or 'spec' in name:
            return 'test'
        if name in ('package.json', 'requirements.txt', 'go.mod', 'Cargo.toml'):
            return 'dependency'
        if name in ('dockerfile', 'docker-compose'):
            return 'docker'
        if name in ('.env.example', '.env.template'):
            return 'config'
        if path.suffix.lower() in ('.yaml', '.yml', '.toml', '.json'):
            return 'config'
        if path.suffix.lower() in ('.md', '.txt', '.rst'):
            return 'documentation'
        if path.suffix.lower() in ('.css', '.scss', '.less'):
            return 'style'
        
        # Content-based detection
        if 'def ' in content or 'import ' in content:
            if 'class ' in content or 'React' in content:
                return 'component'
            return 'api'
        
        return 'code'
    
    def _index_docs(self):
        """Index README and documentation."""
        print("  📚 Indexing documentation...")
        
        doc_files = []
        for pattern in ['README*', 'CHANGELOG*', 'CONTRIBUTING*', '*.md']:
            doc_files.extend(self.project_path.glob(pattern))
        
        for doc in doc_files[:5]:  # Limit to 5 docs
            try:
                content = doc.read_text(encoding='utf-8', errors='ignore')[:5000]
                doc_id = f"{self.wing}_{doc.stem}".replace(' ', '_')
                
                if self.collection:
                    self.collection.add(
                        documents=[content],
                        metadatas=[{
                            'wing': self.wing,
                            'room': 'docs',
                            'source_file': doc.name,
                            'file_type': 'documentation',
                            'project': self.project_name,
                        }],
                        ids=[doc_id]
                    )
            except:
                pass
        
        print("    ✓ Documentation indexed")
    
    def _index_dependencies(self):
        """Index package dependencies."""
        print("  📦 Indexing dependencies...")
        
        dep_files = [
            ('package.json', 'npm'),
            ('requirements.txt', 'python'),
            ('go.mod', 'go'),
            ('Cargo.toml', 'rust'),
            ('pom.xml', 'java'),
            ('composer.json', 'php'),
        ]
        
        deps = {}
        for filename, pkg_mgr in dep_files:
            for match in self.project_path.rglob(filename):
                try:
                    content = match.read_text(encoding='utf-8', errors='ignore')
                    deps[pkg_mgr] = content[:1000]
                except:
                    pass
        
        if deps and self.collection:
            try:
                self.collection.add(
                    documents=[json.dumps(deps)],
                    metadatas=[{
                        'wing': self.wing,
                        'room': 'dependencies',
                        'source_file': 'DEPENDENCIES',
                        'file_type': 'dependency',
                        'project': self.project_name,
                    }],
                    ids=[f"{self.wing}_dependencies"]
                )
            except:
                pass
        
        print(f"    ✓ Dependencies indexed ({len(deps)} package managers)")


def auto_detect_projects() -> List[Path]:
    """Auto-detect code projects."""
    candidates = []
    
    locations = [
        Path.home() / 'code',
        Path.home() / 'projects',
        Path.home() / 'dev',
        Path.home() / 'workspace',
        Path.home() / 'github',
        Path.home() / 'git',
    ]
    
    markers = ['.git', 'package.json', 'Cargo.toml', 'go.mod',
               'requirements.txt', 'pyproject.toml', 'pom.xml',
               'Makefile', 'tsconfig.json']
    
    for loc in locations:
        if not loc.exists():
            continue
        
        try:
            for item in loc.iterdir():
                if item.is_dir() and any((item / m).exists() for m in markers):
                    candidates.append(item)
        except PermissionError:
            continue
    
    return candidates


def main():
    import argparse
    parser = argparse.ArgumentParser(description='D4rk Mind — Project Indexer')
    parser.add_argument('path', nargs='?', help='Project path')
    parser.add_argument('--all', '-a', action='store_true', help='Index all detected projects')
    parser.add_argument('--watch', '-w', action='store_true', help='Watch mode')
    parser.add_argument('--skip-existing', '-s', action='store_true', help='Skip if already indexed')
    
    args = parser.parse_args()
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║           D4rk Mind — Project Indexer                        ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    # Determine paths
    paths = []
    
    if args.path:
        paths.append(Path(args.path).expanduser().resolve())
    elif args.all:
        paths = auto_detect_projects()
        print(f"\n📁 Auto-detected {len(paths)} projects")
    
    if not paths:
        paths = [Path.cwd()]
    
    # Index each project
    results = []
    for path in paths:
        if not path.exists():
            print(f"\n⚠️  Path not found: {path}")
            continue
        
        indexer = ProjectIndexer(path)
        result = indexer.index_project()
        results.append(result)
        
        print(f"\n  ✓ Indexed in {result['duration']}s")
    
    # Summary
    print("\n" + "=" * 60)
    print("INDEXING COMPLETE")
    print("=" * 60)
    
    for r in results:
        print(f"\n  {r['project']}")
        print(f"    Files: {r['files_indexed']}")
        print(f"    Wing:  {r['wing']}")
        print(f"    Time:  {r['duration']}s")
    
    total_files = sum(r['files_indexed'] for r in results)
    total_time = sum(r['duration'] for r in results)
    
    print(f"\n  TOTAL: {total_files} files in {total_time}s")
    print("=" * 60)


if __name__ == '__main__':
    main()
