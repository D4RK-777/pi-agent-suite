#!/usr/bin/env python3
"""
D4rk Mind — Quick Onboarding
Gives any agent instant context about a project in ONE LINE.

Usage:
    python onboard_project.py /path/to/project
    
    # Output example:
    # "Search konekt_nextjs: search('query', wing='konekt_nextjs')"
"""

import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import chromadb

PALACE_PATH = str(Path.home() / ".mempalace" / "palace")


def quick_onboard(project_path: Path) -> str:
    """Get one-line context for any project."""
    client = chromadb.PersistentClient(path=PALACE_PATH)
    col = client.get_collection("mempalace_drawers")
    
    project_name = project_path.name
    
    # Check if project exists as a wing
    data = col.get(include=['metadatas'])
    for m in data['metadatas']:
        if m and project_name.lower() in m.get('wing', '').lower():
            wing = m['wing']
            # Count records
            count = sum(1 for x in data['metadatas'] if x and x.get('wing') == wing)
            return f'Search wing \"{wing}\" ({count:,} records): search("query", wing="{wing}")'
    
    return f'No data for {project_name}. Run: mine_agent.py --project {project_path}'


def main():
    if len(sys.argv) < 2:
        print("Usage: python onboard_project.py /path/to/project")
        sys.exit(1)
    
    project_path = Path(sys.argv[1]).resolve()
    result = quick_onboard(project_path)
    
    print(result)


if __name__ == "__main__":
    main()
