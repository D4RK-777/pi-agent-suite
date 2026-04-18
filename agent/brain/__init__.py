"""
Brain Launcher — Auto-loads skills based on task analysis
Run with: python brain/launch.py "your task here"
"""

import subprocess
import sys
from pathlib import Path

# Add brain to path
sys.path.insert(0, str(Path(__file__).parent))

from router import analyze_task, load_skill_content, SKILL_DESCRIPTIONS


def launch_task(task: str, auto_load: bool = True) -> dict:
    """Launch a task with automatic skill loading."""
    print("🧠 **Brain Processing...**")
    print()
    
    # Analyze the task
    analysis = analyze_task(task)
    
    # Display analysis
    print(f"**Task:** {task}")
    print(f"\n**Matched {analysis['skill_count']} skills:**")
    
    loaded_skills = []
    loaded_content = {}
    
    for skill in analysis['matched_skills']:
        print(f"  📚 `{skill}`")
        
        if auto_load:
            content = load_skill_content(skill)
            if content:
                loaded_skills.append(skill)
                loaded_content[skill] = content
                print(f"     ✓ Loaded")
            else:
                print(f"     ✗ Not found")
        else:
            desc = SKILL_DESCRIPTIONS.get(skill, "")
            print(f"     {desc}")
    
    print()
    
    # Return context for agent
    return {
        "task": task,
        "analysis": analysis,
        "loaded_skills": loaded_skills,
        "loaded_content": loaded_content,
        "context_for_agent": build_agent_context(task, analysis, loaded_skills, loaded_content)
    }


def build_agent_context(task: str, analysis: dict, loaded_skills: list, content: dict) -> str:
    """Build context string for the agent."""
    ctx = []
    ctx.append(f"# Task: {task}")
    ctx.append("")
    ctx.append("## Activated Skills")
    
    for skill in loaded_skills:
        ctx.append(f"\n### {skill}")
        ctx.append("```")
        ctx.append(content[skill][:500] + "..." if len(content[skill]) > 500 else content[skill])
        ctx.append("```")
    
    return "\n".join(ctx)


def main():
    task = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("What would you like to do?\n> ")
    
    if not task:
        print("No task provided")
        sys.exit(1)
    
    result = launch_task(task)
    print("\n" + "=" * 60)
    print("Context ready for agent. Skills auto-loaded.")


if __name__ == "__main__":
    main()
