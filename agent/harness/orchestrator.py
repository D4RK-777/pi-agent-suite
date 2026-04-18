"""
Pi Harness Orchestrator — Simplified CLI

Commands:
  route <input>      - Route user input to best agent
  check <agent>      - Run enforcement (loads skills/domain from manifest)
  watcher <agent> <input> <output> - Full watcher pipeline
  compliance <agent> <output>       - Compliance check only
  memory <sub>       - Memory ops (search/context/stats/health)
  info               - Show system info
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HARNESS_DIR = Path(__file__).parent
sys.path.insert(0, str(HARNESS_DIR))

from router import route as router_route, RoutingResult
from enforcement import Enforcer, ComplianceWatcher, MemoryWatcher, WatcherPipeline
from memory import search_memory, search_all_wings, get_memory_stats, build_memory_context, MEMORY_WINGS

PI_ROOT = Path.home() / ".pi" / "agent"
COOKBOOKS_DIR = PI_ROOT / "cookbooks"


# ---------------------------------------------------------------------------
# Formatters
# ---------------------------------------------------------------------------

def format_routing_result(result: RoutingResult) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("🧠 ROUTING RESULT")
    lines.append("=" * 60)
    lines.append(f"  Agent: {result.selected_agent}")
    lines.append(f"  Confidence: {result.confidence} ({result.score:.1f} pts)")
    lines.append(f"  Skills: {', '.join(result.skills_to_load)}")
    if result.suggested_chain:
        lines.append(f"  Chain: {' → '.join(result.suggested_chain)}")
    lines.append(f"  Reasoning: {'; '.join(result.reasoning[:2])}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_route(args: list[str]) -> int:
    if not args:
        print("Usage: route <user input>")
        return 1
    print(format_routing_result(router_route(" ".join(args))))
    return 0


def cmd_check(args: list[str]) -> int:
    if not args:
        print("Usage: check <agent_name> [--stdin]")
        return 1

    agent_name = args[0]
    agents_manifest = json.loads((PI_ROOT / "manifests" / "agents.json").read_text())
    agent_data = next((a for a in agents_manifest.get("agents", []) if a["name"] == agent_name), None)
    if not agent_data:
        print(f"Agent not found: {agent_name}")
        return 1

    use_stdin = "--stdin" in args
    output = sys.stdin.read() if use_stdin else " ".join(args[1:])

    enforcer = Enforcer()
    enforcer.enforce(output, agent_name, agent_data.get("skills", []), agent_data.get("domain"))
    summary = enforcer.get_summary()

    print(f"{'✅ PASS' if summary['pass'] else '❌ FAIL'} | {agent_name}")
    print(f"  Blockers: {summary['blockers']} | Warnings: {summary['warnings']}")
    if enforcer.violations:
        for v in enforcer.violations:
            icon = "🚫" if v.severity == "blocker" else "⚠️"
            print(f"  {icon} [{v.severity}] {v.category}: {v.message}")
    return 0 if summary["pass"] else 1


def cmd_watcher(args: list[str]) -> int:
    if len(args) < 3:
        print("Usage: watcher <agent> <input> <output>")
        return 1
    agent, user_input, output = args[0], args[1], args[2]
    agents_manifest = json.loads((PI_ROOT / "manifests" / "agents.json").read_text())
    agent_data = next((a for a in agents_manifest.get("agents", []) if a["name"] == agent), None)
    result = WatcherPipeline().full_check(
        user_input, output, agent,
        expected_skills=agent_data.get("skills", []) if agent_data else [],
        expected_domain=agent_data.get("domain") if agent_data else None,
    )
    print(json.dumps(result, indent=2))
    return 0 if result["overall"]["pass"] else 1


def cmd_compliance(args: list[str]) -> int:
    if len(args) < 2:
        print("Usage: compliance <agent> <output>")
        return 1
    result = ComplianceWatcher().check(args[1], args[0])
    print(json.dumps(result, indent=2))
    return 0 if result["pass"] else 1


def cmd_memory_search(args: list[str]) -> int:
    if not args:
        print("Usage: memory search <query> [wing]")
        return 1
    query, wing = args[0], args[1] if len(args) > 1 else None
    result = search_memory(query, wing=wing, n=5)
    print(f"Found {result.get('stats', {}).get('count', 0)} results ({result.get('stats', {}).get('query_time_ms', 0):.0f}ms)")
    for r in result.get("results", [])[:3]:
        src = r.get("source", "unknown").split("\\")[-1][:50]
        print(f"  📌 {src} ({r.get('similarity', 0):.2f})")
        print(f"     {r.get('content', '')[:150]}...")
    return 0


def cmd_memory_context(args: list[str]) -> int:
    if not args:
        print("Usage: memory context <query> [wing]")
        return 1
    ctx = build_memory_context(args[0], wing=args[1] if len(args) > 1 else None)
    print(ctx if ctx else "No relevant memories found.")
    return 0


def cmd_memory_stats(args: list[str]) -> int:
    result = get_memory_stats()
    if result.get("status") == "available":
        print("✅ MemPalace available")
        print(result.get("output", "")[:500])
    else:
        print(f"❌ Unavailable: {result.get('error', 'unknown')}")
    return 0


def cmd_memory_health(args: list[str]) -> int:
    result = MemoryWatcher().get_health()
    print(json.dumps(result, indent=2))
    return 0


def cmd_repeat_offenders(args: list[str]) -> int:
    threshold = int(args[0]) if args else 3
    offenders = ComplianceWatcher().get_repeat_offenders(threshold)
    if offenders:
        print("Repeat offenders:")
        for o in offenders:
            print(f"  {o['agent']}: {o['violation']} x{o['count']}")
    else:
        print("No repeat offenders found.")
    return 0


def cmd_info(args: list[str]) -> int:
    skills = json.loads((PI_ROOT / "manifests" / "skills.json").read_text())["skills"]
    agents = json.loads((PI_ROOT / "manifests" / "agents.json").read_text())["agents"]
    domains = json.loads((PI_ROOT / "manifests" / "domains.json").read_text())["domains"]
    cookbooks = [d.name for d in COOKBOOKS_DIR.iterdir() if d.is_dir()] if COOKBOOKS_DIR.exists() else []

    print("=" * 60)
    print("ℹ️  PI HARNESS")
    print("=" * 60)
    print(f"  Skills: {len([s for s in skills if s.get('status') == 'active'])} active / {len(skills)} total")
    print(f"  Agents: {len([a for a in agents if a.get('status') == 'active'])} active / {len(agents)} total")
    print(f"  Domains: {len(domains)}")
    print(f"  Cookbooks: {len(cookbooks)}")
    print(f"  Harness files: {len(list(HARNESS_DIR.glob('*.py')))}")
    print("")
    print("  Commands:")
    print("    route <input>                          - Route to best agent")
    print("    check <agent> [--stdin]                - Run enforcement")
    print("    watcher <agent> <input> <output>       - Full watcher pipeline")
    print("    compliance <agent> <output>            - Compliance check only")
    print("    memory search <query> [wing]           - Search MemPalace")
    print("    memory context <query> [wing]          - Build context")
    print("    memory stats                           - Memory stats")
    print("    memory health                          - ChromaDB health")
    print("    repeat-offenders [threshold]            - Find repeat violators")
    print("    info                                   - This info")
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    if len(sys.argv) < 2:
        cmd_info([])
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    cmds = {
        "route": cmd_route,
        "check": cmd_check,
        "watcher": cmd_watcher,
        "compliance": cmd_compliance,
        "info": cmd_info,
        "repeat-offenders": cmd_repeat_offenders,
        # Memory subcommands
        "memory": cmd_memory_search,
        "memory-search": cmd_memory_search,
        "memory-context": cmd_memory_context,
        "memory-stats": cmd_memory_stats,
        "memory-health": cmd_memory_health,
    }

    if command == "memory" and args:
        sub = args[0]
        sub_cmds = {
            "search": cmd_memory_search,
            "context": cmd_memory_context,
            "stats": cmd_memory_stats,
            "health": cmd_memory_health,
        }
        if sub in sub_cmds:
            sys.exit(sub_cmds[sub](args[1:]))
        else:
            print(f"Unknown memory command: {sub}")
            sys.exit(1)

    if command in cmds:
        sys.exit(cmds[command](args))
    else:
        print(f"Unknown command: {command}")
        print(f"Available: {', '.join(cmds.keys())}")
        sys.exit(1)


if __name__ == "__main__":
    main()