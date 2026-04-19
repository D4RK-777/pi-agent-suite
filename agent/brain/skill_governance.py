"""
Pi Skill Governance

Prevents skill bloat through:
  - Skill audits (quarterly review)
  - Duplicate detection
  - Usage tracking
  - Merge recommendations
  - Bundle assignments
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
import os
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

PI_ROOT = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi"))
SKILLS_DIR = PI_ROOT / "agent" / "skills"
BUNDLES_DIR = PI_ROOT / "agent" / "bundles"
MANIFEST = PI_ROOT / "agent" / "manifests" / "skills.json"


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class SkillInfo:
    """Information about a skill."""
    name: str
    path: Path
    size: int
    tags: list[str]
    description: str
    in_bundles: list[str]


@dataclass
class AuditResult:
    """Result of skill audit."""
    category: str
    severity: str  # error, warning, info
    skills: list[str]
    message: str


# ---------------------------------------------------------------------------
# Skill Analyzer
# ---------------------------------------------------------------------------

def analyze_skills() -> list[SkillInfo]:
    """Analyze all skills in the skills directory."""
    skills = []
    
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        
        content = skill_md.read_text(encoding="utf-8")
        
        # Parse frontmatter
        name = skill_dir.name
        tags = []
        description = ""
        
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                rest = parts[2]
                
                for line in fm.split("\n"):
                    if line.startswith("tags:"):
                        # Parse tags
                        import re
                        tags = re.findall(r'-?\s*(\w+)', line)
                    elif line.startswith("description:"):
                        desc = line.split(":", 1)[1].strip()
                        description = desc.strip('"\'')
        
        # Check bundles
        in_bundles = []
        for bundle_file in BUNDLES_DIR.glob("*.json"):
            bundle = json.loads(bundle_file.read_text(encoding="utf-8"))
            if name in bundle.get("skills", []):
                in_bundles.append(bundle["name"])
        
        skills.append(SkillInfo(
            name=name,
            path=skill_md,
            size=len(content),
            tags=tags,
            description=description,
            in_bundles=in_bundles
        ))
    
    return skills


def find_duplicates(skills: list[SkillInfo]) -> list[AuditResult]:
    """Find duplicate or very similar skills."""
    results = []
    
    # Group by similar names
    name_groups: dict[str, list[str]] = {}
    for skill in skills:
        # Normalize name
        normalized = skill.name.lower().replace("-", " ").replace("_", " ")
        
        # Find similar names
        for existing_norm, group in name_groups.items():
            if normalized in existing_norm or existing_norm in normalized:
                group.append(skill.name)
                break
        else:
            name_groups[normalized] = [skill.name]
    
    # Find groups with duplicates
    for norm, group in name_groups.items():
        if len(group) > 1:
            results.append(AuditResult(
                category="duplicate",
                severity="warning",
                skills=group,
                message=f"Similar names: {', '.join(group)}"
            ))
    
    # Check for empty skills
    for skill in skills:
        if skill.size < 100:
            results.append(AuditResult(
                category="empty",
                severity="error",
                skills=[skill.name],
                message=f"Skill is too small ({skill.size} bytes)"
            ))
        
        if not skill.description:
            results.append(AuditResult(
                category="missing_description",
                severity="warning",
                skills=[skill.name],
                message="Skill missing description"
            ))
    
    return results


def find_unused_skills(skills: list[SkillInfo]) -> list[AuditResult]:
    """Find skills not in any bundle."""
    results = []
    
    for skill in skills:
        if not skill.in_bundles:
            results.append(AuditResult(
                category="unused",
                severity="info",
                skills=[skill.name],
                message=f"Skill not in any bundle"
            ))
    
    return results


def find_similar_by_tags(skills: list[SkillInfo]) -> list[AuditResult]:
    """Find skills with very similar tag sets."""
    results = []
    
    # Group by tag similarity
    tag_groups: dict[str, list[str]] = {}
    
    for skill in skills:
        # Create tag signature
        tags_key = ",".join(sorted(skill.tags[:5])) if skill.tags else "none"
        
        if tags_key in tag_groups:
            tag_groups[tags_key].append(skill.name)
        else:
            tag_groups[tags_key] = [skill.name]
    
    # Report groups with 3+ skills (possible overlap)
    for tags_key, group in tag_groups.items():
        if len(group) > 2:
            results.append(AuditResult(
                category="tag_overlap",
                severity="info",
                skills=group,
                message=f"Skills with similar tags: {', '.join(group[:5])}"
            ))
    
    return results


# ---------------------------------------------------------------------------
# Bundle Analysis
# ---------------------------------------------------------------------------

def analyze_bundles() -> dict[str, Any]:
    """Analyze bundle coverage."""
    bundles = {}
    
    for bundle_file in BUNDLES_DIR.glob("*.json"):
        bundle = json.loads(bundle_file.read_text(encoding="utf-8"))
        bundle_skills = []
        
        for skill_name in bundle.get("skills", []):
            skill_path = SKILLS_DIR / skill_name / "SKILL.md"
            bundle_skills.append({
                "name": skill_name,
                "exists": skill_path.exists()
            })
        
        bundles[bundle["name"]] = {
            "label": bundle.get("label", bundle["name"]),
            "skills": bundle_skills,
            "skill_count": len(bundle_skills),
            "missing": [s["name"] for s in bundle_skills if not s["exists"]]
        }
    
    return bundles


# ---------------------------------------------------------------------------
# Full Audit
# ---------------------------------------------------------------------------

def run_audit() -> dict[str, Any]:
    """Run full skill audit."""
    skills = analyze_skills()
    duplicates = find_duplicates(skills)
    unused = find_unused_skills(skills)
    similar = find_similar_by_tags(skills)
    bundles = analyze_bundles()
    
    return {
        "total_skills": len(skills),
        "skills": [
            {"name": s.name, "size": s.size, "tags": s.tags, "bundles": s.in_bundles}
            for s in skills
        ],
        "audit_results": {
            "duplicates": [d.__dict__ for d in duplicates],
            "unused": [u.__dict__ for u in unused],
            "similar": [s.__dict__ for s in similar]
        },
        "bundles": bundles,
        "summary": {
            "errors": len([d for d in duplicates if d.severity == "error"]),
            "warnings": len([d for d in duplicates if d.severity == "warning"]),
            "info": len(unused) + len(similar),
            "bundle_count": len(bundles),
            "covered_by_bundles": len([s for s in skills if s.in_bundles]),
            "uncovered": len([s for s in skills if not s.in_bundles])
        }
    }


def format_audit_report(audit: dict[str, Any]) -> str:
    """Format audit as readable report."""
    lines = []
    
    lines.append("=" * 60)
    lines.append("📋 SKILL GOVERNANCE AUDIT")
    lines.append("=" * 60)
    lines.append("")
    
    summary = audit["summary"]
    lines.append(f"**Total Skills:** {audit['total_skills']}")
    lines.append(f"**Bundles:** {summary['bundle_count']}")
    lines.append(f"**Covered by Bundles:** {summary['covered_by_bundles']}")
    lines.append(f"**Uncovered:** {summary['uncovered']}")
    lines.append("")
    
    # Errors
    if summary["errors"] > 0:
        lines.append("## 🚫 Errors")
        lines.append("")
        for result in audit["audit_results"]["duplicates"]:
            if result["severity"] == "error":
                lines.append(f"- **{result['message']}**")
                lines.append(f"  Skills: {', '.join(result['skills'])}")
        lines.append("")
    
    # Warnings
    if summary["warnings"] > 0:
        lines.append("## ⚠️ Warnings")
        lines.append("")
        for result in audit["audit_results"]["duplicates"]:
            if result["severity"] == "warning":
                lines.append(f"- **{result['message']}**")
                lines.append(f"  Skills: {', '.join(result['skills'])}")
        lines.append("")
    
    # Bundle coverage
    lines.append("## 📦 Bundle Coverage")
    lines.append("")
    for bundle_name, bundle_data in audit["bundles"].items():
        status = "✅" if not bundle_data["missing"] else "❌"
        lines.append(f"  {status} **{bundle_data['label']}** ({bundle_data['skill_count']} skills)")
        if bundle_data["missing"]:
            lines.append(f"     Missing: {', '.join(bundle_data['missing'])}")
    lines.append("")
    
    # Recommendations
    lines.append("## 💡 Recommendations")
    lines.append("")
    
    uncovered = audit["skills"][:5] if summary["uncovered"] > 0 else []
    if uncovered:
        lines.append("- Add uncovered skills to bundles:")
        for s in uncovered[:3]:
            lines.append(f"  - {s['name']}")
    
    if summary["warnings"] > 0:
        lines.append("- Review duplicate/near-duplicate skills")
    
    lines.append("- Run audit quarterly to prevent bloat")
    lines.append("")
    
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import sys
    audit = run_audit()
    
    if "--json" in sys.argv:
        print(json.dumps(audit, indent=2))
    else:
        print(format_audit_report(audit))


if __name__ == "__main__":
    main()
