#!/usr/bin/env python3
"""
D4rk Mind — Continuous Codebase Mining Agent
Watches directories and keeps MemPalace updated with the latest codebase intelligence.

Usage:
    python mine_agent.py                    # Run once
    python mine_agent.py --watch            # Continuous mode
    python mine_agent.py --watch --daemon  # Background daemon
    python mine_agent.py --project ~/code/myapp  # Mine specific project
"""

import os
import sys
import json
import time
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, Set, Dict, List, Tuple

try:
    import mempalace
    MEMPALACE_AVAILABLE = True
except ImportError:
    MEMPALACE_AVAILABLE = False
    print("⚠️  MemPalace not installed. Install: pip install mempalace")

# File patterns to mine
CODE_EXTENSIONS = {
    '.py', '.js', '.ts', '.jsx', '.tsx', '.vue', '.svelte',
    '.java', '.kt', '.go', '.rs', '.c', '.cpp', '.h', '.hpp',
    '.cs', '.rb', '.php', '.swift', '.m', '.sql', '.sh',
    '.yaml', '.yml', '.toml', '.json', '.xml', '.md',
}

# Directories to skip
SKIP_DIRS = {
    'node_modules', '.git', '__pycache__', '.venv', 'venv',
    'dist', 'build', '.next', '.nuxt', 'target', 'out',
    '.cache', '.tmp', '.temp', 'tmp', '.parcel-cache',
    'vendor', 'packages', '.pnpm-store', '.yarn-cache',
}

# Max file size (1MB)
MAX_FILE_SIZE = 1024 * 1024


class MineAgent:
    """Continuous codebase mining agent."""
    
    def __init__(self, watch_paths: Optional[List[Path]] = None):
        self.watch_paths = watch_paths or [Path.cwd()]
        self.state_file = Path.home() / '.mempalace' / 'mine_agent_state.json'
        self.last_mtimes: Dict[str, float] = self._load_state()
        
    def _load_state(self) -> Dict[str, float]:
        """Load last modification times."""
        if self.state_file.exists():
            try:
                return json.loads(self.state_file.read_text())
            except:
                return {}
        return {}
    
    def _save_state(self):
        """Save current state."""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state_file.write_text(json.dumps(self.last_mtimes, indent=2))
    
    def get_file_hash(self, path: Path) -> str:
        """Get quick hash of file for change detection."""
        try:
            return hashlib.md5(path.read_bytes()[:1024]).hexdigest()[:8]
        except:
            return ""
    
    def should_mine_file(self, path: Path) -> bool:
        """Check if file should be mined."""
        # Check extension
        if path.suffix.lower() not in CODE_EXTENSIONS:
            return False
        
        # Check size
        try:
            if path.stat().st_size > MAX_FILE_SIZE:
                return False
        except:
            return False
        
        # Check if changed
        key = str(path)
        try:
            mtime = path.stat().st_mtime
            if key in self.last_mtimes and self.last_mtimes[key] == mtime:
                return False  # Not modified
            self.last_mtimes[key] = mtime
        except:
            return False
        
        return True
    
    def mine_file(self, path: Path) -> Optional[str]:
        """Mine a single file."""
        if not self.should_mine_file(path):
            return None
        
        try:
            content = path.read_text(encoding='utf-8', errors='ignore')
            
            # Skip empty files
            if len(content.strip()) < 10:
                return None
            
            # Build metadata
            rel_path = path
            for wp in self.watch_paths:
                try:
                    rel_path = path.relative_to(wp)
                    break
                except ValueError:
                    continue
            
            wing = str(rel_path.parts[0]) if rel_path.parts else 'unknown'
            room = str(rel_path.parent) if len(rel_path.parts) > 1 else 'root'
            
            # Detect file type
            ext = path.suffix.lower()
            file_type = self._detect_file_type(ext, content)
            
            # Chunk content for better search
            chunks = self._chunk_content(content, max_chunk=2000)
            
            return json.dumps({
                'content': content[:5000],  # First 5KB for mining
                'path': str(path),
                'rel_path': str(rel_path),
                'wing': wing,
                'room': room,
                'file_type': file_type,
                'extension': ext,
                'size': len(content),
                'lines': len(content.split('\n')),
                'chunks': len(chunks),
                'mined_at': datetime.now().isoformat(),
            })
            
        except Exception as e:
            return None
    
    def _detect_file_type(self, ext: str, content: str) -> str:
        """Detect the type of file."""
        type_hints = {
            'component': ['return (', 'function', '=>', 'class ', 'export '],
            'test': ['test(', 'describe(', 'it(', 'expect(', 'def test_'],
            'config': ['=', ':', '{', '['],
            'api': ['router', 'app.', 'def ', 'async ', 'get(', 'post('],
            'style': ['style', 'css', 'color', 'margin', 'padding', '{'],
            'database': ['SELECT', 'INSERT', 'CREATE TABLE', 'prisma', 'schema'],
            'auth': ['auth', 'login', 'password', 'token', 'jwt', 'session'],
            'doc': ['#', '##', '###', '```', '**'],
        }
        
        for file_type, hints in type_hints.items():
            if any(hint in content for hint in hints):
                return file_type
        return 'code'
    
    def _chunk_content(self, content: str, max_chunk: int = 2000) -> List[str]:
        """Split content into searchable chunks."""
        lines = content.split('\n')
        chunks = []
        current = []
        current_len = 0
        
        for line in lines:
            line_len = len(line)
            if current_len + line_len > max_chunk and current:
                chunks.append('\n'.join(current))
                current = [line]
                current_len = line_len
            else:
                current.append(line)
                current_len += line_len
        
        if current:
            chunks.append('\n'.join(current))
        
        return chunks
    
    def mine_directory(self, root: Path, recursive: bool = True) -> Tuple[int, int]:
        """Mine a directory."""
        mined = 0
        skipped = 0
        
        try:
            for item in root.iterdir():
                # Skip unwanted directories
                if item.name in SKIP_DIRS:
                    continue
                
                if item.is_dir() and recursive:
                    sub_mined, sub_skipped = self.mine_directory(item, recursive)
                    mined += sub_mined
                    skipped += sub_skipped
                    
                elif item.is_file():
                    result = self.mine_file(item)
                    if result:
                        self._store_memory(result)
                        mined += 1
                    else:
                        skipped += 1
                        
        except PermissionError:
            pass
        
        return mined, skipped
    
    def _store_memory(self, data: str):
        """Store memory in MemPalace (via subprocess for isolation)."""
        if not MEMPALACE_AVAILABLE:
            return
        
        try:
            import subprocess
            # Use mempalace CLI to store
            result = subprocess.run(
                ['python', '-X', 'utf8', '-m', 'mempalace.cli', 'mine'],
                input=data.encode(),
                capture_output=True,
                timeout=5
            )
        except:
            pass
    
    def run_once(self) -> Dict:
        """Run a single mining pass."""
        results = {
            'projects': 0,
            'files_mined': 0,
            'files_skipped': 0,
            'errors': 0,
            'duration': 0,
        }
        
        start = time.time()
        
        for watch_path in self.watch_paths:
            if not watch_path.exists():
                continue
                
            if watch_path.is_file():
                result = self.mine_file(watch_path)
                if result:
                    self._store_memory(result)
                    results['files_mined'] += 1
                results['projects'] += 1
                
            elif watch_path.is_dir():
                mined, skipped = self.mine_directory(watch_path)
                results['files_mined'] += mined
                results['files_skipped'] += skipped
                results['projects'] += 1
        
        results['duration'] = round(time.time() - start, 2)
        self._save_state()
        
        return results
    
    def watch(self, interval: int = 60):
        """Watch mode - continuously check for changes."""
        print(f"👁️  Watching {len(self.watch_paths)} paths...")
        print(f"   Press Ctrl+C to stop\n")
        
        while True:
            try:
                results = self.run_once()
                if results['files_mined'] > 0:
                    print(f"✓ Mined {results['files_mined']} files in {results['duration']}s")
                time.sleep(interval)
            except KeyboardInterrupt:
                print("\n\n👋 Stopped watching.")
                break


def auto_detect_projects() -> List[Path]:
    """Auto-detect code projects."""
    candidates = []
    
    # Common locations
    locations = [
        Path.home() / 'code',
        Path.home() / 'projects',
        Path.home() / 'dev',
        Path.home() / 'workspace',
        Path.cwd(),
    ]
    
    for loc in locations:
        if not loc.exists():
            continue
            
        for item in loc.iterdir():
            if item.is_dir():
                # Check if it looks like a code project
                if any((item / marker).exists() for marker in [
                    '.git', 'package.json', 'Cargo.toml', 'go.mod',
                    'requirements.txt', 'pyproject.toml', 'pom.xml',
                    'Makefile', '.env.example', 'tsconfig.json',
                ]):
                    candidates.append(item)
    
    return candidates


def main():
    parser = argparse.ArgumentParser(description='D4rk Mind — Continuous Codebase Mining')
    parser.add_argument('--watch', '-w', action='store_true', help='Watch mode')
    parser.add_argument('--daemon', '-d', action='store_true', help='Run as background daemon')
    parser.add_argument('--project', '-p', action='append', help='Project path to mine')
    parser.add_argument('--interval', '-i', type=int, default=60, help='Watch interval (seconds)')
    parser.add_argument('--auto-detect', '-a', action='store_true', help='Auto-detect projects')
    
    args = parser.parse_args()
    
    # Determine paths to mine
    paths = []
    
    if args.project:
        for p in args.project:
            paths.append(Path(p).expanduser().resolve())
    
    if args.auto_detect or not paths:
        detected = auto_detect_projects()
        paths.extend(detected)
    
    if not paths:
        paths = [Path.cwd()]
    
    # Remove duplicates
    paths = list(set(paths))
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║           D4rk Mind — Codebase Mining Agent                  ║")
    print("╠════════════════════════════════════════════════════════════════╣")
    print(f"║  Projects: {len(paths)}                                               ║")
    for p in paths[:3]:
        print(f"║    • {str(p)[:50]:<50}  ║")
    if len(paths) > 3:
        print(f"║    ... and {len(paths) - 3} more                                       ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print()
    
    agent = MineAgent(paths)
    
    if args.daemon:
        # Background daemon mode
        import subprocess
        print("🚀 Starting daemon...")
        subprocess.Popen(
            [sys.executable] + sys.argv,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        print("✅ Daemon started in background")
        
    elif args.watch:
        agent.watch(interval=args.interval)
        
    else:
        # Single run
        results = agent.run_once()
        print(f"\n📊 Results:")
        print(f"   Projects scanned: {results['projects']}")
        print(f"   Files mined:      {results['files_mined']}")
        print(f"   Files skipped:    {results['files_skipped']}")
        print(f"   Duration:         {results['duration']}s")


if __name__ == '__main__':
    main()
