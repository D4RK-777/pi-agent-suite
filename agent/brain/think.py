#!/usr/bin/env python3
"""
Think — One command to rule them all.
Usage: think "your task"

Automatically analyzes your task, loads relevant skills,
and shows you exactly what's ready to use.
"""

import sys
import os
from pathlib import Path

# Fix Windows encoding
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, str(Path(__file__).parent))
from router import analyze_task, load_skill_content, SKILL_DESCRIPTIONS

def think(task: str):
    """Process task and load all relevant skills."""
    print()
    print("=" * 60)
    print(f"🧠 BRAIN: Analyzing task...")
    print("=" * 60)
    print()
    
    # Analyze
    analysis = analyze_task(task)
    
    print(f"📋 Task: {task}")
    print()
    print(f"📚 MATCHED {analysis['skill_count']} SKILLS:")
    print("-" * 40)
    
    loaded = []
    for skill in analysis['matched_skills']:
        desc = SKILL_DESCRIPTIONS.get(skill, "")
        content = load_skill_content(skill)
        
        if content:
            print(f"  ✓ {skill}")
            print(f"    {desc}")
            loaded.append((skill, content))
        else:
            print(f"  ? {skill} (not found)")
    
    print()
    print("=" * 60)
    print("ACTIVATED SKILLS:")
    print("=" * 60)
    
    for skill, content in loaded:
        print()
        print(f"[{skill}]")
        # Show first 200 chars of each skill
        preview = content[:300].replace('\n', ' ')
        print(f"  {preview}...")
    
    print()
    print("=" * 60)
    print("✓ All relevant knowledge loaded and ready.")
    print("=" * 60)
    
    return loaded

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: think \"your task description\"")
        print()
        print("Examples:")
        print('  think "build a secure login with JWT"')
        print('  think "scrape product data from a website"')
        print('  think "optimize slow API endpoints"')
        sys.exit(1)
    
    task = " ".join(sys.argv[1:])
    think(task)
