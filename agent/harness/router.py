"""
Pi Router — Simplified deterministic agent routing.

6-signal scoring: explicit name/alias (10pts), skill keywords (1.5-2pts),
skill tags (1pt), domain focus (0.5/word), role/note (0.25-0.5/word),
intent keywords (0.5-1pt). Same input → same output.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PI_ROOT = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi")) / "agent"
MANIFESTS = {k: json.loads((PI_ROOT / "manifests" / f"{k}.json").read_text()) for k in ("skills", "agents", "domains")}

INTENT_KEYWORDS = {
    "director": ["oversee", "direct", "orchestrate", "coordinate", "plan", "architect", "system design"],
    "advisor": ["advice", "help", "research", "explore", "analyze", "understand", "documentation", "knowledge", "gather", "architecture", "best practices", "study"],
    "frontend": ["build", "create", "component", "page", "ui", "button", "form", "modal", "navbar", "responsive", "tailwind", "css", "style", "animation", "motion", "react", "nextjs", "gsap", "scroll", "accessible", "dropdown", "header", "footer", "card", "list", "grid", "hero", "section"],
    "backend": ["api", "endpoint", "server", "database", "query", "model", "schema", "migration", "auth", "login", "security", "deploy", "monitor", "docker", "kubernetes", "oauth", "jwt", "session", "route", "validation", "middleware", "token", "crud", "rate limit", "vulnerability", "xss", "injection", "csrf", "password", "encrypt", "alert", "incident", "rollback", "uptime", "ci/cd", "register", "signup", "signin", "sso", "mfa", "permission", "rbac"],
    "reviewer": ["review", "pr", "test", "qa", "verify", "cleanup", "refactor", "quality", "coverage", "audit", "pull request", "assess", "risk", "code quality", "lint", "testing", "unit", "integration", "e2e", "test suite", "coverage"],
    "debugger": ["debug", "error", "crash", "bug", "broken", "issue", "problem", "not working", "won't close", "fix"],
}


@dataclass
class RoutingResult:
    selected_agent: str
    agent_data: dict[str, Any]
    skills_to_load: list[str]
    score: float
    reasoning: list[str]
    all_scores: list[dict[str, Any]]
    confidence: str
    multi_domain: bool
    suggested_chain: list[str] | None = None


def _words(text: str) -> set:
    return set(re.findall(r'\w+', text.lower()))


def route(user_input: str) -> RoutingResult:
    agents = [a for a in MANIFESTS["agents"]["agents"] if a.get("status") == "active"]
    skills = [s for s in MANIFESTS["skills"]["skills"] if s.get("status") == "active"]
    domains = MANIFESTS["domains"]["domains"]
    ul = user_input.lower()
    uwords = _words(user_input)

    scores: dict[str, float] = {a["name"]: 0.0 for a in agents}
    reasoning: list[str] = []

    # Signal 1: explicit name/alias (10pts)
    for a in agents:
        if a["name"].lower() in ul or any(al.lower() in ul for al in a.get("aliases", [])):
            scores[a["name"]] += 10.0
    s1 = {k: v for k, v in scores.items() if v >= 10}
    if s1:
        reasoning.append(f"explicit: {s1}")

    # Signal 2+3: skill keywords + tags
    skill_map = {s["name"]: s for s in skills}
    for a in agents:
        for sn in a.get("skills", []):
            s = skill_map.get(sn)
            if not s:
                continue
            if sn.lower().replace("-", " ") in ul:
                scores[a["name"]] += 2.0
            for tag in s.get("tags", []):
                if tag in ul:
                    scores[a["name"]] += 1.5
                if tag in uwords:
                    scores[a["name"]] += 1.0

    # Signal 4: domain focus
    for d in domains:
        dw = _words(d.get("focus", ""))
        overlap = dw & uwords
        if overlap:
            lead = d.get("leadAgent")
            if lead and lead in scores:
                scores[lead] += len(overlap) * 0.5

    # Signal 5: agent role/note
    for a in agents:
        role = a.get("role", "").lower()
        if role in ul:
            scores[a["name"]] += 0.5
        note_words = _words(a.get("note", ""))
        overlap = note_words & uwords
        if overlap:
            scores[a["name"]] += len(overlap) * 0.25

    # Signal 6: intent keywords
    for agent_name, keywords in INTENT_KEYWORDS.items():
        if agent_name in scores:
            for kw in keywords:
                scores[agent_name] += (1.0 if kw in ul else 0.5) if kw in uwords else 0

    # Pick winner
    max_score = max(scores.values()) if scores else 0
    winner = max(scores, key=scores.get) if max_score > 0 else "pi"
    agent_data = next((a for a in agents if a["name"] == winner), agents[0])
    confidence = "high" if max_score >= 10 else "medium" if max_score >= 5 else "low"

    # Multi-domain detection
    multi_domains = [d["name"] for d in domains if len(_words(d.get("focus", "")) & uwords) >= 2]
    chain = [d["leadAgent"] for dn in multi_domains for d in domains if d["name"] == dn] if len(multi_domains) > 1 else None
    if chain:
        reasoning.append(f"multi-domain: {multi_domains} → {' → '.join(chain)}")

    return RoutingResult(
        selected_agent=winner,
        agent_data=agent_data,
        skills_to_load=agent_data.get("skills", []),
        score=max_score,
        reasoning=reasoning,
        all_scores=[{"agent": k, "score": v} for k, v in sorted(scores.items(), key=lambda x: -x[1]) if v > 0],
        confidence=confidence,
        multi_domain=len(multi_domains) > 1,
        suggested_chain=chain,
    )
