"""
MemPalace Project Wing Manager
=============================
Manages project-specific memory wings for all your repos.
Each project gets:
- Live documentation index
- Architecture summaries
- Code patterns
- Decision tracking
- Auto-updates on file changes

Usage:
    project_wing_manager.py init <path> <name>    # Add project
    project_wing_manager.py list                    # List all projects
    project_wing_manager.py sync <name>           # Sync project
    project_wing_manager.py context <name>       # Get project context
    project_wing_manager.py watch                  # Start auto-sync daemon
"""

import os
import sys
import json
import time
import logging
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Optional

# Config
PROJECTS_FILE = Path.home() / ".mempalace" / "project_wings.json"
LOG_FILE = Path.home() / ".mempalace" / "logs" / "project_wing_manager.log"
WATCH_INTERVAL = 300  # 5 minutes

# Setup logging
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


def load_projects() -> dict:
    """Load project configurations."""
    if PROJECTS_FILE.exists():
        return json.loads(PROJECTS_FILE.read_text())
    return {}


def save_projects(projects: dict):
    """Save project configurations."""
    PROJECTS_FILE.write_text(json.dumps(projects, indent=2))


def detect_project_type(path: Path) -> str:
    """Detect project type from package.json, requirements.txt, etc."""
    if (path / "package.json").exists():
        try:
            pkg = json.loads((path / "package.json").read_text())
            return pkg.get("type", "node")  # react, next, node, etc
        except:
            return "node"
    elif (path / "requirements.txt").exists() or (path / "pyproject.toml").exists():
        return "python"
    elif (path / "Cargo.toml").exists():
        return "rust"
    elif (path / "go.mod").exists():
        return "go"
    elif (path / "*.sln").exists() or (path / "*.csproj").exists():
        return "dotnet"
    return "unknown"


def extract_readme(path: Path) -> dict:
    """Extract and summarize README content."""
    for readme in ["README.md", "README.txt", "README.rst"]:
        readme_path = path / readme
        if readme_path.exists():
            content = readme_path.read_text(encoding="utf-8", errors="ignore")
            # Get first section (usually overview)
            first_lines = "\n".join(content.split("\n")[:50])
            return {
                "exists": True,
                "name": readme,
                "preview": first_lines[:2000],
                "size": len(content)
            }
    return {"exists": False}


def extract_docs(path: Path) -> list[dict]:
    """Extract documentation files."""
    docs = []
    docs_dir = path / "docs"
    
    if docs_dir.exists():
        for doc in docs_dir.rglob("*.md"):
            content = doc.read_text(encoding="utf-8", errors="ignore")
            docs.append({
                "file": str(doc.relative_to(path)),
                "name": doc.stem,
                "preview": content[:1000],
                "size": len(content)
            })
    
    return docs


def detect_architecture(path: Path) -> dict:
    """Detect project architecture patterns."""
    arch = {
        "dirs": [],
        "patterns": [],
        "has_api": False,
        "has_frontend": False,
        "has_database": False
    }
    
    # Scan directory structure
    for item in path.iterdir():
        if item.is_dir():
            name = item.name.lower()
            arch["dirs"].append(name)
            
            if name in {"api", "routes", "endpoints", "controllers"}:
                arch["has_api"] = True
            if name in {"frontend", "client", "ui", "components", "pages"}:
                arch["has_frontend"] = True
            if name in {"db", "database", "models", "migrations"}:
                arch["has_database"] = True
    
    # Detect patterns
    if (path / "next.config.js").exists() or (path / "next.config.mjs").exists():
        arch["patterns"].append("nextjs")
    if (path / "astro.config.mjs").exists():
        arch["patterns"].append("astro")
    if (path / "docker-compose.yml").exists() or (path / "docker-compose.yaml").exists():
        arch["patterns"].append("docker")
    if (path / "kubernetes").exists() or (path / "k8s").exists():
        arch["patterns"].append("kubernetes")
    
    return arch


def extract_dependencies(path: Path) -> dict:
    """Extract dependency information."""
    deps = {"production": [], "development": []}
    
    # Node.js
    pkg_json = path / "package.json"
    if pkg_json.exists():
        try:
            pkg = json.loads(pkg_json.read_text())
            deps["production"] = list(pkg.get("dependencies", {}).keys())
            deps["development"] = list(pkg.get("devDependencies", {}).keys())
            return deps
        except:
            pass
    
    # Python
    req_txt = path / "requirements.txt"
    if req_txt.exists():
        deps["production"] = [l.strip() for l in req_txt.read_text().split("\n") if l.strip() and not l.startswith("#")]
    
    return deps


def extract_stakeholders(path: Path) -> dict:
    """Extract team/owner information from package.json, setup.py, etc."""
    info = {}
    
    pkg_json = path / "package.json"
    if pkg_json.exists():
        try:
            pkg = json.loads(pkg_json.read_text())
            info["author"] = pkg.get("author", "")
            info["version"] = pkg.get("version", "")
            info["license"] = pkg.get("license", "")
            info["name"] = pkg.get("name", path.name)
        except:
            pass
    
    return info


def compute_file_hash(filepath: Path) -> str:
    """Compute MD5 hash of file."""
    return hashlib.md5(filepath.read_bytes()).hexdigest()[:8]


def build_project_profile(project_path: Path) -> dict:
    """Build comprehensive project profile."""
    logger.info(f"Building profile for: {project_path}")
    
    profile = {
        "name": project_path.name,
        "path": str(project_path),
        "type": detect_project_type(project_path),
        "last_synced": datetime.now().isoformat(),
        "file_hashes": {}
    }
    
    # README
    profile["readme"] = extract_readme(project_path)
    
    # Architecture
    profile["architecture"] = detect_architecture(project_path)
    
    # Dependencies
    profile["dependencies"] = extract_dependencies(project_path)
    
    # Stakeholders
    profile["stakeholders"] = extract_stakeholders(project_path)
    
    # Docs
    profile["docs"] = extract_docs(project_path)
    
    # Key files with hashes
    key_patterns = ["*.md", "*.json", "*.toml", "*.yaml", "*.yml"]
    for pattern in key_patterns:
        for f in project_path.rglob(pattern):
            if f.is_file():
                rel_path = str(f.relative_to(project_path))
                profile["file_hashes"][rel_path] = compute_file_hash(f)
    
    return profile


def sync_project(name: str) -> dict:
    """Sync a project's wing."""
    projects = load_projects()
    
    if name not in projects:
        logger.error(f"Project not found: {name}")
        return {"error": f"Project '{name}' not found"}
    
    project_path = Path(projects[name]["path"])
    if not project_path.exists():
        logger.error(f"Project path not found: {project_path}")
        return {"error": f"Path not found: {project_path}"}
    
    # Build fresh profile
    profile = build_project_profile(project_path)
    
    # Update stored profile
    projects[name]["profile"] = profile
    projects[name]["last_sync"] = datetime.now().isoformat()
    save_projects(projects)
    
    logger.info(f"Synced project: {name}")
    return profile


def get_project_context(name: str) -> str:
    """Get project context for AI agents."""
    projects = load_projects()
    
    if name not in projects:
        return f"Project '{name}' not found"
    
    project = projects[name]
    profile = project.get("profile", {})
    
    lines = []
    lines.append(f"# {profile.get('name', name)}")
    lines.append("")
    
    # Overview
    if profile.get("readme", {}).get("exists"):
        lines.append("## Overview")
        lines.append(profile["readme"]["preview"][:500])
        lines.append("")
    
    # Architecture
    arch = profile.get("architecture", {})
    if arch.get("patterns"):
        lines.append("## Architecture")
        lines.append(f"Patterns: {', '.join(arch['patterns'])}")
        lines.append(f"Has API: {arch.get('has_api', False)}")
        lines.append(f"Has Frontend: {arch.get('has_frontend', False)}")
        lines.append(f"Has Database: {arch.get('has_database', False)}")
        lines.append("")
    
    # Key directories
    if arch.get("dirs"):
        lines.append("## Directory Structure")
        lines.append(f"Key dirs: {', '.join(arch['dirs'][:10])}")
        lines.append("")
    
    # Type
    lines.append(f"## Project Type")
    lines.append(f"Language/Framework: {profile.get('type', 'unknown')}")
    lines.append("")
    
    # Dependencies count
    deps = profile.get("dependencies", {})
    prod_deps = len(deps.get("production", []))
    dev_deps = len(deps.get("development", []))
    lines.append(f"## Dependencies")
    lines.append(f"Production: {prod_deps}, Development: {dev_deps}")
    lines.append("")
    
    # Docs
    docs = profile.get("docs", [])
    if docs:
        lines.append(f"## Documentation ({len(docs)} files)")
        for doc in docs[:5]:
            lines.append(f"- {doc['name']}: {doc['preview'][:100]}...")
        lines.append("")
    
    # Last sync
    lines.append(f"*Last synced: {project.get('last_sync', 'Never')}*")
    
    return "\n".join(lines)


def add_project(name: str, path: str) -> dict:
    """Add a new project to track."""
    projects = load_projects()
    project_path = Path(path).resolve()
    
    if not project_path.exists():
        return {"error": f"Path not found: {project_path}"}
    
    # Build initial profile
    profile = build_project_profile(project_path)
    
    projects[name] = {
        "name": name,
        "path": str(project_path),
        "type": profile["type"],
        "added_at": datetime.now().isoformat(),
        "last_sync": None,
        "profile": profile
    }
    
    save_projects(projects)
    logger.info(f"Added project: {name} ({project_path})")
    
    return {"success": True, "name": name, "profile": profile}


def list_projects() -> list:
    """List all tracked projects."""
    projects = load_projects()
    return [
        {
            "name": name,
            "path": info["path"],
            "type": info.get("type", "unknown"),
            "last_sync": info.get("last_sync"),
        }
        for name, info in projects.items()
    ]


def sync_all_projects():
    """Sync all projects."""
    projects = load_projects()
    results = []
    
    for name in projects:
        result = sync_project(name)
        results.append({"name": name, "result": result})
    
    return results


def watch_daemon():
    """Run as daemon, syncing projects periodically."""
    logger.info("Starting Project Wing Manager daemon")
    
    while True:
        try:
            projects = load_projects()
            
            for name, info in projects.items():
                project_path = Path(info["path"])
                
                # Check if project directory was modified
                last_sync = info.get("last_sync")
                if not last_sync:
                    logger.info(f"Never synced: {name}")
                    sync_project(name)
                    continue
                
                # Compare file hashes
                last_profile = info.get("profile", {}).get("file_hashes", {})
                current_hashes = {}
                
                for rel_path in last_profile:
                    current_file = project_path / rel_path
                    if current_file.exists():
                        current_hashes[rel_path] = compute_file_hash(current_file)
                
                # Check for changes
                changed = set(last_profile.keys()) ^ set(current_hashes.keys())
                for key in set(last_profile.keys()) & set(current_hashes.keys()):
                    if last_profile[key] != current_hashes[key]:
                        changed.add(key)
                
                if changed:
                    logger.info(f"Changes detected in {name}: {len(changed)} files")
                    sync_project(name)
                else:
                    logger.debug(f"No changes in {name}")
            
        except Exception as e:
            logger.error(f"Watch error: {e}")
        
        time.sleep(WATCH_INTERVAL)


def add_to_mempalace(name: str):
    """Add project context to MemPalace for semantic search."""
    try:
        from mempalace_fast import search
        
        context = get_project_context(name)
        # In a full implementation, this would add to MemPalace
        # For now, the profile is stored in project_wings.json
        
        logger.info(f"Would add {name} context to MemPalace")
        
    except Exception as e:
        logger.error(f"Failed to add to MemPalace: {e}")


# CLI Commands
def cmd_init(args):
    """Initialize a new project wing."""
    name = args[0] if args else None
    path = args[1] if len(args) > 1 else None
    
    if not name or not path:
        print("Usage: project_wing_manager.py init <name> <path>")
        return
    
    result = add_project(name, path)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Added project: {name}")
        print(f"Type: {result['profile']['type']}")


def cmd_list():
    """List all projects."""
    projects = list_projects()
    
    if not projects:
        print("No projects tracked.")
        print("\nAdd one:")
        print("  project_wing_manager.py init <name> <path>")
        return
    
    print()
    print("=" * 60)
    print("  Tracked Projects")
    print("=" * 60)
    print()
    
    for p in projects:
        status = f"Last sync: {p['last_sync'][:16] if p['last_sync'] else 'Never'}"
        print(f"  {p['name']}")
        print(f"    Path: {p['path']}")
        print(f"    Type: {p['type']}")
        print(f"    {status}")
        print()


def cmd_sync(name: Optional[str] = None):
    """Sync project(s)."""
    if name:
        result = sync_project(name)
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Synced: {name}")
            print(f"Type: {result.get('type', 'unknown')}")
            if result.get("readme", {}).get("exists"):
                print("README: Found")
            print(f"Dependencies: {len(result.get('dependencies', {}).get('production', []))}")
    else:
        print("Syncing all projects...")
        results = sync_all_projects()
        print(f"Synced {len(results)} projects")


def cmd_context(name: str):
    """Get project context for AI."""
    if not name:
        print("Usage: project_wing_manager.py context <name>")
        return
    
    context = get_project_context(name)
    print(context)


def cmd_watch():
    """Start watch daemon."""
    print("Starting watch daemon... (Ctrl+C to stop)")
    watch_daemon()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        cmd_list()
    else:
        cmd = sys.argv[1].lower()
        args = sys.argv[2:]
        
        if cmd == "init":
            cmd_init(args)
        elif cmd == "list":
            cmd_list()
        elif cmd == "sync":
            cmd_sync(args[0] if args else None)
        elif cmd == "context":
            cmd_context(args[0] if args else None)
        elif cmd == "watch":
            cmd_watch()
        else:
            print(f"Unknown command: {cmd}")
            print("Commands: init, list, sync, context, watch")
