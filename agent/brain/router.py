"""
Intent Router — The Brain
Automatically identifies and loads relevant skills/knowledge based on natural language requests.
"""

import json
import os
import re
from pathlib import Path
from typing import Optional

_pi_home = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi"))
SKILLS_DIR = _pi_home / "agent" / "skills"

# Skill Registry — maps keywords to skills
SKILL_REGISTRY = {
    # Core domains
    "frontend": ["frontend-engineering", "expert-frontend", "frontend-quality"],
    "backend": ["backend-engineering", "expert-backend", "data-and-persistence"],
    "auth": ["expert-auth", "security-and-auth"],
    "security": ["expert-security", "security-first-pass", "security-and-auth"],
    "database": ["data-and-persistence", "expert-backend"],
    "api": ["backend-engineering", "expert-backend"],
    
    # Infrastructure
    "deploy": ["expert-orchestration"],
    "docker": ["expert-orchestration"],
    "kubernetes": ["expert-orchestration"],
    "ci/cd": ["expert-orchestration"],
    "infrastructure": ["expert-orchestration", "observability-and-monitoring"],
    
    # Quality
    "test": ["delivery-testing"],
    "review": ["delivery-code-review"],
    "performance": ["expert-optimization", "frontend-quality"],
    "optimize": ["expert-optimization"],
    "speed": ["expert-optimization"],
    
    # Research & Extraction
    "scrape": ["firecrawl", "firecrawl-scrape"],
    "search": ["firecrawl-search"],
    "crawl": ["firecrawl-crawl"],
    "extract": ["firecrawl-agent"],
    "browser": ["browser", "firecrawl-browser"],
    "download": ["firecrawl-download"],
    "map": ["firecrawl-map"],
    
    # Design & Creative
    "image": ["image-craft", "higgsfield"],
    "design": ["expert-frontend"],
    "animation": ["gsap"],
    "ascii": ["ascii-animator"],
    "cli animation": ["ascii-animator"],
    "ui": ["expert-frontend", "frontend-engineering"],
    "component": ["frontend-engineering", "expert-frontend"],
    
    # Workflow
    "memory": ["mempalace", "mempalace-workflow"],
    "mempalace": ["mempalace", "mempalace-workflow"],
    "agent": ["agents-cli"],
    "skills": ["skill-creator", "skill-validator", "skill-packager"],
    
    # Analysis
    "analyze": ["analyze-code"],
    "incident": ["incident-and-recovery"],
    "monitor": ["observability-and-monitoring"],
    "problem": ["problem-framing"],
    
    # Writing & Content
    "write": ["writer"],
    "blog": ["writer"],
    "copy": ["writer"],
    "meme": ["memetic-compression"],
    
    # Task Management
    "linear": ["linear"],
    "ticket": ["linear"],
    
    # Meta
    "session": ["sessions"],
}

# Skill descriptions for context
SKILL_DESCRIPTIONS = {
    "frontend-engineering": "React, Next.js, components, hooks, state, forms, responsive layouts",
    "backend-engineering": "API routes, server actions, middleware, validation, business logic",
    "expert-frontend": "UI patterns, CSS, animations, accessibility, design systems",
    "expert-backend": "APIs, databases, caching, queues, microservices, serverless",
    "expert-auth": "OAuth, JWT, sessions, SSO, MFA, RBAC, password hashing",
    "expert-security": "OWASP, vulnerabilities, XSS, SQL injection, CSRF, cryptography",
    "expert-optimization": "Performance, bundle size, latency, caching strategies",
    "expert-orchestration": "Docker, Kubernetes, CI/CD, Terraform, cloud infra",
    "data-and-persistence": "Schemas, queries, migrations, data models, storage",
    "delivery-testing": "Tests, coverage, verification, QA, smoke checks",
    "delivery-code-review": "Code review, PR review, quality gates, risk assessment",
    "frontend-quality": "A11y, performance, responsive, Core Web Vitals, polish",
    "mempalace": "Memory palace, knowledge mining, semantic search",
    "mempalace-workflow": "D4rk workflow, search → read → code → file pattern",
    "firecrawl": "Web search, scraping, crawling, browser automation",
    "firecrawl-scrape": "Extract markdown from URLs, JS-rendered pages",
    "firecrawl-search": "Web search with full page extraction",
    "firecrawl-crawl": "Bulk extract content from entire sites",
    "firecrawl-agent": "Structured data extraction from websites",
    "firecrawl-browser": "Browser automation, form fills, logins, clicks",
    "firecrawl-download": "Download entire websites as local files",
    "firecrawl-map": "Discover all URLs on a website",
    "image-craft": "High-quality image generation for any creative use",
    "higgsfield": "Image/video generation via Higgsfield AI",
    "gsap": "GSAP animations, ScrollTrigger, timelines, motion",
    "ascii-animator": "Create ASCII animations for CLI terminals using the 5x12 grid animator",
    "browser": "Browser automation via agent-browser CLI",
    "analyze-code": "Codebase exploration, pattern finding, understanding",
    "incident-and-recovery": "Incident handling, rollback, recovery, stabilization",
    "observability-and-monitoring": "Logs, metrics, traces, dashboards, alerts",
    "problem-framing": "Task structuring, sanity checks, architecture planning",
    "security-first-pass": "Quick security scan, secrets detection, risk patterns",
    "security-and-auth": "Auth flows, permissions, secrets management",
    "writer": "Product launches, landing pages, blog posts, social copy",
    "memetic-compression": "Viral memes, cultural zeitgeist capture",
    "linear": "Issue tracking, sprint management, project workflow",
    "agents-cli": "Agent CLI management, versions, MCP servers",
    "skill-creator": "Creating and improving AI agent skills",
    "skill-packager": "Scaffolding and packaging D4rkMynd-style skills",
    "skill-validator": "Structural validation of skill files",
    "sessions": "Named sessions across agent versions",
    "recursive-improvement-loop": "Capturing patterns, improving skills/system",
    "findings-synthesis": "Synthesizing reports into priorities and plans",
}


def analyze_task(task: str) -> dict:
    """Analyze a task and return relevant skills with reasoning."""
    task_lower = task.lower()
    words = re.findall(r'\w+', task_lower)
    
    matched_skills = set()
    reasoning = []
    
    # Check each skill trigger
    for keyword, skills in SKILL_REGISTRY.items():
        if keyword in words or keyword in task_lower:
            for skill in skills:
                if skill not in matched_skills:
                    matched_skills.add(skill)
                    reasoning.append(f"'{keyword}' → {skill}")
    
    # Special compound detection
    if any(w in task_lower for w in ["react", "vue", "angular", "jsx", "tsx", "css", "html", "tailwind"]):
        matched_skills.update(["frontend-engineering", "expert-frontend"])
        reasoning.append("frontend framework detected")
    
    if any(w in task_lower for w in ["node", "python", "api", "rest", "graphql", "server"]):
        matched_skills.update(["backend-engineering", "expert-backend"])
        reasoning.append("backend technology detected")
    
    if any(w in task_lower for w in ["security", "vulnerability", "xss", "injection", "auth", "hack"]):
        matched_skills.update(["expert-security", "security-first-pass"])
        reasoning.append("security concern detected")
    
    if any(w in task_lower for w in ["performance", "speed", "optimize", "fast", "latency"]):
        matched_skills.add("expert-optimization")
        reasoning.append("performance concern detected")
    
    if any(w in task_lower for w in ["test", "verify", "qa", "coverage"]):
        matched_skills.add("delivery-testing")
        reasoning.append("testing need detected")
    
    if any(w in task_lower for w in ["review", "audit", "assess"]):
        matched_skills.add("delivery-code-review")
        reasoning.append("review need detected")
    
    # Always include workflow skill
    matched_skills.add("mempalace-workflow")
    
    return {
        "task": task,
        "matched_skills": sorted(list(matched_skills)),
        "reasoning": reasoning,
        "skill_count": len(matched_skills)
    }


def get_skill_path(skill: str) -> Optional[Path]:
    """Get the path to a skill's SKILL.md file."""
    skill_path = SKILLS_DIR / skill / "SKILL.md"
    if skill_path.exists():
        return skill_path
    return None


def load_skill_content(skill: str) -> Optional[str]:
    """Load the content of a skill's SKILL.md file."""
    skill_path = get_skill_path(skill)
    if skill_path:
        with open(skill_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None


def format_router_output(analysis: dict) -> str:
    """Format the router output for display."""
    output = []
    output.append("[BRAIN] INTENT ANALYSIS")
    output.append("=" * 50)
    output.append(f"\nTask: {analysis['task']}")
    output.append(f"\nMatched Skills ({analysis['skill_count']}):")
    
    for skill in analysis['matched_skills']:
        desc = SKILL_DESCRIPTIONS.get(skill, "No description")
        output.append(f"  * {skill} - {desc}")
    
    output.append(f"\nReasoning:")
    for reason in analysis['reasoning']:
        output.append(f"  -> {reason}")
    
    output.append("\n" + "=" * 50)
    return "\n".join(output)


def main():
    """CLI entry point."""
    import sys
    import io
    
    # Fix Windows encoding
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    if len(sys.argv) < 2:
        print("Usage: router.py <task description>")
        print("\nExample:")
        print("  router.py 'build a React login form with JWT auth'")
        sys.exit(1)
    
    task = " ".join(sys.argv[1:])
    analysis = analyze_task(task)
    print(format_router_output(analysis))


if __name__ == "__main__":
    main()
