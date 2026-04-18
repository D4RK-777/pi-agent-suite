"""
Pi Enforcement Module

Validates LLM output against routing decisions.
Catches persona mismatches, skill avoidance, hardcoded values, debug leftovers,
harness compliance, and MemPalace consultation.

Also includes watcher pipeline for pre/post action monitoring.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Violation Types
# ---------------------------------------------------------------------------

@dataclass
class Violation:
    category: str
    severity: str  # "blocker" | "warning"
    message: str
    line_hint: str | None = None


# ---------------------------------------------------------------------------
# Enforcer
# ---------------------------------------------------------------------------

class Enforcer:
    """Validates LLM output against routing and quality standards."""

    def __init__(self) -> None:
        self.violations: list[Violation] = []

    def enforce(
        self,
        output: str,
        routed_agent: str,
        expected_skills: list[str],
        expected_domain: str | None = None
    ) -> list[Violation]:
        """Run all enforcement checks on LLM output."""
        self.violations = []

        # Check 1: HARNESS COMPLIANCE (BLOCKER - runs first)
        self._check_harness_compliance(output, routed_agent, expected_skills)

        # Check 2: MemPalace consultation (BLOCKER)
        self._check_mempalace_consultation(output, routed_agent)

        # Check 3: Context awareness (BLOCKER)
        self._check_context_awareness(output, routed_agent)

        # Check 4: Persona mismatch
        self._check_persona(output, routed_agent)

        # Check 5: Skill avoidance
        self._check_skill_avoidance(output, expected_skills)

        # Check 6: Hardcoded colors
        self._check_hardcoded_colors(output)

        # Check 7: Debug leftovers
        self._check_debug_leftovers(output)

        # Check 8: Placeholder text
        self._check_placeholders(output)

        # Check 9: Boundary violations (frontend shouldn't write backend logic)
        if expected_domain:
            self._check_boundary_violations(output, expected_domain)

        # Check 10: Generic error handling
        self._check_generic_error_handling(output)

        return self.violations

    def _check_harness_compliance(self, output: str, routed_agent: str, expected_skills: list[str]) -> None:
        """BLOCKER: Check if agent actually followed the harness workflow."""
        output_lower = output.lower()

        # Signals that agent consulted the harness routing decision
        harness_signals = [
            r'routed\s+as', r'routing\s+decided', r'agent.*selected',
            r'harness', r'skill.*load', r'skill.*guidance',
            r'following.*skill', r'according to.*skill',
            r'per.*best practice', r'best practice.*from',
        ]

        has_harness_signal = any(re.search(p, output, re.IGNORECASE) for p in harness_signals)

        # Check if skills were mentioned/used
        skill_usage_count = 0
        for skill in expected_skills:
            skill_lower = skill.lower().replace('-', ' ')
            if skill_lower in output_lower:
                skill_usage_count += 1

        # BLOCKER: No harness compliance AND no skill usage
        if not has_harness_signal and skill_usage_count == 0 and expected_skills:
            self.violations.append(Violation(
                category="harness_compliance",
                severity="blocker",
                message=f"Agent '{routed_agent}' did not follow harness workflow. Expected to reference skills: {expected_skills[:3]}..."
            ))
        elif not has_harness_signal and expected_skills:
            self.violations.append(Violation(
                category="harness_compliance",
                severity="warning",
                message=f"Agent '{routed_agent}' used skills but didn't acknowledge harness routing decision"
            ))

    def _check_mempalace_consultation(self, output: str, routed_agent: str) -> None:
        """BLOCKER: Check if agent consulted MemPalace before acting."""
        # MemPalace consultation signals
        mempalace_signals = [
            r'mempalace', r'MemPalace', r'mempalace',
            r'search.*pattern', r'pattern.*search',
            r'Egypt of Knowledge', r'source of truth',
            r'knowledge.*base', r'pattern.*mining',
            r'retrieved.*context', r'context.*retrieved',
            r'according to.*memor', r'memor.*suggest',
            r'previous.*session', r'session.*learn',
        ]

        has_mempalace = any(re.search(p, output, re.IGNORECASE) for p in mempalace_signals)

        # BLOCKER: No MemPalace consultation
        if not has_mempalace:
            self.violations.append(Violation(
                category="mempalace_consultation",
                severity="blocker",
                message=f"Agent '{routed_agent}' did not consult MemPalace (Egypt of Knowledge) before acting. MemPalace is the single source of truth."
            ))

    def _check_context_awareness(self, output: str, routed_agent: str) -> None:
        """BLOCKER: Check if agent demonstrates awareness of current conversation context."""
        # Signals that agent is aware of current context
        context_signals = [
            r'you mentioned', r'you said', r'you.*ask', r'currently.*work',
            r'we.*discuss', r'about.*speak', r'current.*conver',
            r'regard.*your', r'your.*problem', r'your.*issue',
            r'let me check', r'let me look', r'let me search',
        ]

        has_context = any(re.search(p, output, re.IGNORECASE) for p in context_signals)

        # This is a warning, not a blocker - context awareness is harder to enforce
        if not has_context and len(output) > 100:
            self.violations.append(Violation(
                category="context_awareness",
                severity="warning",
                message=f"Agent '{routed_agent}' output doesn't demonstrate awareness of current conversation context"
            ))

    def _check_persona(self, output: str, routed_agent: str) -> None:
        """Check for persona mismatch - LLM claims to be a different agent."""
        persona_claims = [
            r"I am a (?:senior|lead|expert|principal)",
            r"as a (?:senior|lead|expert|principal) (?:developer|engineer|architect)",
            r"(?:you should consult|speak with|ask) (?:another|a different)",
            r"this is outside my expertise",
        ]
        
        for claim in persona_claims:
            if re.search(claim, output, re.IGNORECASE):
                self.violations.append(Violation(
                    category="persona_mismatch",
                    severity="warning",
                    message=f"Output claims different persona while routed as '{routed_agent}'"
                ))

    def _check_skill_avoidance(self, output: str, expected_skills: list[str]) -> None:
        """Check for skill avoidance - LLM says it'll improvise instead of following skills."""
        avoidance_phrases = [
            r"I don't (?:have access to|know|remember|see) the",
            r"without access to the",
            r"I'll (?:just|simply) improvise",
            r"I don't need the skill",
            r"skill file",
            r"let me (?:just|simply) write",
            r"(?:TODO|FIXME|HACK) without guidance",
        ]
        
        output_lower = output.lower()
        for phrase in avoidance_phrases:
            if re.search(phrase, output_lower):
                self.violations.append(Violation(
                    category="skill_avoidance",
                    severity="warning",
                    message=f"Output appears to avoid following expected skills: {expected_skills}"
                ))

    def _check_hardcoded_colors(self, output: str) -> None:
        """Check for hardcoded color values instead of design tokens."""
        # Common hardcoded color patterns
        color_patterns = [
            r'#[0-9A-Fa-f]{6}',  # Hex colors
            r'#[0-9A-Fa-f]{3}',  # Short hex
            r'rgb\s*\(',
            r'rgba\s*\(',
            r'hsl\s*\(',
            r'hsla\s*\(',
        ]
        
        # Common "safe" colors that might be intentional (but still should use tokens)
        safe_colors = {
            '#000000', '#ffffff', '#000', '#fff',  # Black/white
            '#00000000',  # Transparent
        }
        
        for pattern in color_patterns:
            matches = re.findall(pattern, output)
            for match in matches:
                if match.lower() not in safe_colors:
                    self.violations.append(Violation(
                        category="hardcoded_color",
                        severity="warning",
                        message=f"Found hardcoded color: {match}. Use design tokens instead."
                    ))

    def _check_debug_leftovers(self, output: str) -> None:
        """Check for debug leftovers like console.log."""
        debug_patterns = [
            (r'console\.(?:log|debug|info|warn|error)\s*\(', "console.log"),
            (r'print\s*\(', "print() statement"),
            (r'debugger\s*;', "debugger statement"),
            (r'console\.table\s*\(', "console.table"),
            (r'/\s*console\.', "commented console"),
            (r'//.*console\.', "commented console"),
        ]
        
        for pattern, name in debug_patterns:
            if re.search(pattern, output):
                self.violations.append(Violation(
                    category="debug_leftover",
                    severity="warning",
                    message=f"Found debug leftover: {name}"
                ))

    def _check_placeholders(self, output: str) -> None:
        """Check for placeholder text."""
        placeholder_patterns = [
            (r'\bTODO\b', "TODO comment"),
            (r'\bFIXME\b', "FIXME comment"),
            (r'\bHACK\b', "HACK comment"),
            (r'\bXXX\b', "XXX comment"),
            (r'lorem\s+ipsum', "lorem ipsum"),
            (r'insert\s+here', "insert here"),
            (r'your\s+(?:name|email|content)', "your name/email placeholder"),
            (r'\[Your\s+\w+\]', "bracketed placeholder"),
            (r'\{\{\s*\w+\s*\}\}', "double-brace placeholder"),
        ]
        
        for pattern, name in placeholder_patterns:
            if re.search(pattern, output, re.IGNORECASE):
                self.violations.append(Violation(
                    category="placeholder",
                    severity="blocker",
                    message=f"Found placeholder: {name}"
                ))

    def _check_boundary_violations(self, output: str, expected_domain: str) -> None:
        """Check for boundary violations - agent doing work outside its domain."""
        # Frontend domain shouldn't be writing backend code
        if expected_domain == "frontend-experience":
            backend_signals = [
                r'CREATE TABLE',
                r'CREATE INDEX',
                r'ALTER TABLE',
                r'INSERT INTO.*VALUES',
                r'\.env\s*=',  # Env vars being set
                r'server\s*\.\s*(?:listen|use|get|post|put|delete)',
                r'@app\.(?:route|get|post)',
                r'def\s+\w+.*:.*database',
            ]
            
            for signal in backend_signals:
                if re.search(signal, output, re.IGNORECASE):
                    self.violations.append(Violation(
                        category="boundary_violation",
                        severity="warning",
                        message=f"Frontend agent wrote backend code: {signal}"
                    ))

        # Backend domain shouldn't be writing frontend components
        elif expected_domain == "backend-platform":
            frontend_signals = [
                r'return\s+<[A-Z]',  # JSX component
                r'export\s+default\s+function\s+\w+Component',
                r'useState\s*\(',
                r'useEffect\s*\(',
                r'import\s+.*from\s+["\']@/components',
            ]
            
            for signal in frontend_signals:
                if re.search(signal, output):
                    self.violations.append(Violation(
                        category="boundary_violation",
                        severity="warning",
                        message=f"Backend agent wrote frontend code: {signal}"
                    ))

    def _check_generic_error_handling(self, output: str) -> None:
        """Check for overly generic error handling."""
        generic_patterns = [
            (r'try\s*{[^}]*}\s*catch\s*\([^)]*\)\s*{[^}]*}', "Empty catch block"),
            (r'catch\s*\([^)]*\)\s*{\s*}', "Empty catch block"),
            (r'catch\s*\([^)]*\)\s*{\s*//\s*}', "Empty catch block"),
            (r'console\.(?:log|error)\s*\(\s*e\s*\)', "Generic error logging"),
        ]
        
        for pattern, name in generic_patterns:
            if re.search(pattern, output, re.DOTALL):
                self.violations.append(Violation(
                    category="generic_error_handling",
                    severity="warning",
                    message=f"Found {name}"
                ))

    def get_summary(self) -> dict[str, Any]:
        """Get a summary of enforcement results."""
        blockers = [v for v in self.violations if v.severity == "blocker"]
        warnings = [v for v in self.violations if v.severity == "warning"]
        
        return {
            "total_violations": len(self.violations),
            "blockers": len(blockers),
            "warnings": len(warnings),
            "pass": len(blockers) == 0,
            "violations_by_category": self._group_by_category()
        }

    def _group_by_category(self) -> dict[str, int]:
        """Group violations by category."""
        groups = {}
        for v in self.violations:
            groups[v.category] = groups.get(v.category, 0) + 1
        return groups


# ---------------------------------------------------------------------------
# Watcher Pipeline (merged from watcher.py)
# ---------------------------------------------------------------------------

PI_ROOT_WATCHER = Path.home() / ".pi" / "agent"

class ComplianceWatcher:
    """Monitors agent output for harness compliance."""

    def __init__(self):
        self.enforcer = Enforcer()
        self.violation_history: list[dict] = []

    def check(
        self,
        output: str,
        agent_name: str,
        expected_skills: list[str] = None,
        expected_domain: str = None
    ) -> dict:
        """Run compliance check on agent output."""
        violations = self.enforcer.enforce(
            output, agent_name, expected_skills or [], expected_domain
        )
        summary = self.enforcer.get_summary()

        result = {
            "watcher": "compliance",
            "agent": agent_name,
            "pass": summary["pass"],
            "blockers": summary["blockers"],
            "warnings": summary["warnings"],
            "violations": [
                {
                    "category": v.category,
                    "severity": v.severity,
                    "message": v.message,
                }
                for v in violations
            ],
        }

        if violations:
            self.violation_history.append({
                "agent": agent_name,
                "violations": [(v.category, v.severity) for v in violations],
            })

        return result

    def get_repeat_offenders(self, threshold: int = 3) -> list[dict]:
        """Find agents that violated same rule repeatedly."""
        offender_counts: dict[str, dict[str, int]] = {}

        for entry in self.violation_history:
            agent = entry["agent"]
            if agent not in offender_counts:
                offender_counts[agent] = {}
            for category, _ in entry["violations"]:
                offender_counts[agent][category] = offender_counts[agent].get(category, 0) + 1

        repeat_offenders = []
        for agent, counts in offender_counts.items():
            for category, count in counts.items():
                if count >= threshold:
                    repeat_offenders.append({
                        "agent": agent,
                        "violation": category,
                        "count": count,
                    })

        return repeat_offenders


class MemoryWatcher:
    """Ensures agents consult MemPalace before acting."""

    def __init__(self):
        self.injection_history: list[dict] = []

    def pre_action_inject(self, user_input: str, agent_name: str) -> dict:
        """Search MemPalace and inject context before agent acts."""
        try:
            import sys as _sys
            _sys.path.insert(0, str(PI_ROOT_WATCHER / "bin"))
            from mempalace import search as fast_search

            results = fast_search(user_input, n=3)
            context_parts = []

            for r in results.get("results", [])[:3]:
                source = r.get("source", "unknown").split("\\")[-1][:60]
                content = r.get("content", "")[:300]
                context_parts.append(f"**From: {source}**\n{content}")

            context = "\n\n".join(context_parts) if context_parts else "No relevant memories found — agent will create new knowledge"

            return {
                "watcher": "memory",
                "agent": agent_name,
                "phase": "pre_action",
                "memories_found": bool(context_parts),
                "context": context[:2000],
                "action_required": "Agent MUST reference at least one injected memory in output",
            }
        except Exception:
            return {
                "watcher": "memory",
                "agent": agent_name,
                "phase": "pre_action",
                "memories_found": False,
                "context": "MemPalace unavailable — agent should create new knowledge",
                "action_required": "Agent MUST reference at least one injected memory in output",
            }

    def post_action_verify(self, output: str, agent_name: str) -> dict:
        """Verify agent actually used the injected MemPalace context."""
        mempalace_signals = [
            r'mempalace', r'MemPalace', r'mempalace',
            r'Egypt of Knowledge', r'source of truth',
            r'pattern.*found', r'found.*pattern',
            r'previous.*decid', r'we.*decided',
            r'according to.*memor', r'memor.*suggest',
        ]

        has_reference = any(re.search(p, output, re.IGNORECASE) for p in mempalace_signals)

        return {
            "watcher": "memory",
            "agent": agent_name,
            "phase": "post_action",
            "memPalace_consulted": has_reference,
            "verdict": "PASS" if has_reference else "FAIL",
            "message": (
                "Agent referenced MemPalace ✅" if has_reference
                else "Agent did NOT reference MemPalace ❌ — BLOCKER"
            ),
        }

    def get_health(self) -> dict:
        """Check ChromaDB/MemPalace health."""
        try:
            import sys as _sys
            _sys.path.insert(0, str(PI_ROOT_WATCHER / "bin"))
            from mempalace import search as fast_search
            fast_search("test", n=1)
            return {"watcher": "memory", "phase": "health_check", "status": "available"}
        except Exception as e:
            return {"watcher": "memory", "phase": "health_check", "status": "error", "error": str(e)}


class WatcherPipeline:
    """Runs both watchers in sequence."""

    def __init__(self):
        self.compliance = ComplianceWatcher()
        self.memory = MemoryWatcher()

    def full_check(
        self,
        user_input: str,
        output: str,
        agent_name: str,
        expected_skills: list[str] = None,
        expected_domain: str = None
    ) -> dict:
        """Run full watcher pipeline."""
        memory_injection = self.memory.pre_action_inject(user_input, agent_name)
        memory_verify = self.memory.post_action_verify(output, agent_name)
        compliance_check = self.compliance.check(
            output, agent_name, expected_skills, expected_domain
        )

        blockers = compliance_check["blockers"]
        if not memory_verify["memPalace_consulted"]:
            blockers += 1

        return {
            "overall": {
                "pass": blockers == 0,
                "blockers": blockers,
                "warnings": compliance_check["warnings"],
            },
            "memory_injection": memory_injection,
            "memory_verify": memory_verify,
            "compliance": compliance_check,
        }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: enforcement.py <command> [args]")
        print("\nCommands:")
        print("  check <agent> <skills> [domain] [--stdin]  - Run enforcement")
        print("  watcher <agent> <input> <output>           - Full watcher pipeline")
        print("  compliance <agent> <output>                - Compliance check only")
        print("  memory <agent> <input>                     - Pre-action memory injection")
        print("  health                                     - Check ChromaDB health")
        print("  repeat-offenders [threshold]               - Find repeat violators")
        sys.exit(1)

    command = sys.argv[1]

    # Watcher commands
    if command == "watcher":
        if len(sys.argv) < 5:
            print("Usage: watcher <agent> <input> <output>")
            sys.exit(1)
        agent, user_input, output = sys.argv[2], sys.argv[3], sys.argv[4]
        pipeline = WatcherPipeline()
        result = pipeline.full_check(user_input, output, agent)
        print(json.dumps(result, indent=2))

    elif command == "compliance":
        if len(sys.argv) < 4:
            print("Usage: compliance <agent> <output>")
            sys.exit(1)
        agent, output = sys.argv[2], sys.argv[3]
        cw = ComplianceWatcher()
        print(json.dumps(cw.check(output, agent), indent=2))

    elif command == "memory":
        if len(sys.argv) < 4:
            print("Usage: memory <agent> <input>")
            sys.exit(1)
        agent, user_input = sys.argv[2], sys.argv[3]
        mw = MemoryWatcher()
        print(json.dumps(mw.pre_action_inject(user_input, agent), indent=2))

    elif command == "health":
        mw = MemoryWatcher()
        print(json.dumps(mw.get_health(), indent=2))

    elif command == "repeat-offenders":
        threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        cw = ComplianceWatcher()
        print(json.dumps(cw.get_repeat_offenders(threshold), indent=2))

    # Standard enforcement command
    elif command == "check":
        agent_name = sys.argv[2]
        skills = sys.argv[3].split(",") if len(sys.argv) > 3 and sys.argv[3] else []
        domain = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] and not sys.argv[4].startswith("--") else None
        use_stdin = "--stdin" in sys.argv
        stdin_start = 5 if domain else 4

        if use_stdin:
            output = sys.stdin.read()
        else:
            output = " ".join(sys.argv[stdin_start:]) if len(sys.argv) > stdin_start else ""

        enforcer = Enforcer()
        violations = enforcer.enforce(output, agent_name, skills, domain)
        summary = enforcer.get_summary()

        print("=" * 60)
        print(f"ENFORCEMENT RESULTS for '{agent_name}'")
        print("=" * 60)
        print(f"\n{'✅ PASS' if summary['pass'] else '❌ FAIL'}")
        print(f"Blockers: {summary['blockers']}")
        print(f"Warnings: {summary['warnings']}")

        if violations:
            print("\nVIOLATIONS:")
            for v in violations:
                icon = "🚫" if v.severity == "blocker" else "⚠️"
                print(f"  {icon} [{v.severity}] {v.category}: {v.message}")
        print()

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
