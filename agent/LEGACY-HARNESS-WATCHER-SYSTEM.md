# LEGACY — Pi Harness + Watcher System

> **⚠ ARCHIVED — NOT ACTIVE.**
> This document describes the old D4rkMynd "compliance watcher" enforcement system.
> It is not wired into pi's runtime. `harness-hooks/hooks.json` is not loaded by
> pi-coding-agent (verified against compiled `dist/cli.js` — no references).
> The Python scripts in `harness/` and `harness-hooks/` are orphaned.
> Pi's active harness is built from TypeScript extensions in `extensions/`.
> Kept for historical reference only. Do not re-enable without careful review —
> the BLOCKER checks below caused Obsidian/MemPalace tunnel vision previously.

---

## What Was Built

A complete enforcement system that prevents MiniMax (or any LLM) from ignoring the harness workflow.

## Components

### 1. Harness Compliance Checks (`harness/enforcement.py`)

Three new BLOCKER-level checks added to the enforcer:

| Check | Severity | What It Catches |
|-------|----------|-----------------|
| **Harness Compliance** | BLOCKER | Agent doesn't follow harness workflow or reference expected skills |
| **MemPalace Consultation** | BLOCKER | Agent doesn't consult MemPalace (Egypt of Knowledge) before acting |
| **Context Awareness** | WARNING | Agent doesn't demonstrate awareness of current conversation |

These run BEFORE all other checks. If a blocker is found, the output is REJECTED.

### 2. ChromaDB Server (`bin/start_chroma_server.ps1`)

- **Running**: `http://localhost:8000` with persistent storage at `~\.mempalace\palace`
- **Auto-start**: Windows scheduled task created (runs on login)
- **Status**: ✅ Running with 10,000+ drawers across multiple wings

### 3. Watcher Agents

#### Compliance Watcher (D4rkW4tch3r)
- **File**: `agents/compliance-watcher/AGENT.md`
- **Role**: Autonomous enforcer that monitors every agent output
- **What it watches**: Harness compliance, skill usage, MemPalace consultation, persona, placeholders
- **Actions**: BLOCK (reject output), WARN (flag for review), ESCALATE (repeat offenders → D4rkMynd)

#### Memory Watcher (D4rkM3m0ry)
- **File**: `agents/memory-watcher/AGENT.md`
- **Role**: MemPalace guardian that ensures ChromaDB is consulted before every action
- **What it watches**: Pre-action memory injection, post-action memory verification, ChromaDB health
- **Actions**: Inject context before agent acts, verify agent used it after, report health

### 4. Watcher Pipeline (`harness/watcher.py`)

Python script that runs both watchers in sequence:

```
User Input → Memory Watcher (inject context) → Agent Acts → Compliance Watcher (check output) → Memory Watcher (verify usage) → Result
```

### 5. Updated Hooks (`harness-hooks/hooks.json`)

| Hook | Trigger | What It Does |
|------|---------|--------------|
| `session:memory:load` | SessionStart | Load previous session context |
| `watcher:memory:health` | SessionStart | Check ChromaDB health |
| `harness:route:before:act` | PreToolUse | **Force harness routing before agent acts** |
| `watcher:memory:inject` | PreToolUse | **Memory watcher injects MemPalace context** |
| `quality:gate:edit` | PostToolUse | Run quality gate on edits |
| `watcher:compliance:check` | PostToolUse | **Compliance watcher checks output** |
| `session:memory:save` | Stop | Save session learnings |
| `pattern:extract` | Stop | Extract patterns |
| `watcher:repeat:offenders` | Stop | Check repeat violators |

## How It Works Now

### Before (Agent Ignored Harness)
```
User: "Build a login form"
Agent: *writes from memory, no skills, no MemPalace*
Result: ✅ Output passes (no enforcement)
```

### After (Agent Must Follow Harness)
```
User: "Build a login form"
Hook: Harness routes to 'frontend' agent, loads 6 skills
Hook: Memory watcher injects 3 relevant memories from ChromaDB
Agent: "Routed as frontend. Following frontend-engineering skill guidance..."
Hook: Compliance watcher checks output
  → If no skill references → BLOCKER
  → If no MemPalace mention → BLOCKER
Hook: Memory watcher verifies agent used injected context
Result: ❌ BLOCKED if non-compliant, ✅ PASSES if compliant
```

## Commands

```bash
# Test routing
python .pi/agent/harness/orchestrator.py route "build a login form"

# Test enforcement (non-compliant output)
echo "I'll just write this" | python .pi/agent/harness/enforcement.py frontend "frontend-engineering" "frontend-experience" --stdin

# Test watcher pipeline
python .pi/agent/harness/watcher.py check frontend "build login" "non-compliant output"

# Check ChromaDB health
python .pi/agent/harness/watcher.py health

# Search MemPalace
python .pi/agent/bin/mempalace_fast.py "React patterns"

# View violation history
python .pi/agent/harness/watcher.py repeat-offenders
```

## Test Results

| Test | Result | Details |
|------|--------|---------|
| Harness routing | ✅ PASS | Correctly routes to frontend with 14.5 points |
| Non-compliant enforcement | ✅ BLOCKED | 2 blockers: no harness compliance, no MemPalace |
| Compliant enforcement | ✅ PASS | 0 blockers, 1 warning (context awareness) |
| ChromaDB health | ✅ RUNNING | 10,000+ drawers, multiple wings |
| Watcher pipeline | ✅ WORKING | Full pipeline with memory injection + compliance check |

## Files Changed

| File | Change |
|------|--------|
| `harness/enforcement.py` | Added 3 new checks: harness_compliance, mempalace_consultation, context_awareness |
| `harness/orchestrator.py` | Updated cmd_check to load agent skills/domain from manifest |
| `harness/watcher.py` | NEW: Watcher pipeline with compliance + memory watchers |
| `harness-hooks/hooks.json` | Added PreToolUse hooks for routing + memory injection, PostToolUse for compliance check |
| `manifests/agents.json` | Added compliance-watcher and memory-watcher agents |
| `agents/compliance-watcher/AGENT.md` | NEW: Compliance watcher agent definition |
| `agents/memory-watcher/AGENT.md` | NEW: Memory watcher agent definition |

## Next Steps

1. **Ensure hooks are actually loaded by your LLM agent** — the hook system needs to be integrated into the Claude Code / MiniMax agent's tool execution loop
2. **Consider making blockers harder** — you could add a `PreResponse` hook that blocks the LLM's response before it reaches the user
3. **Add violation tracking** — track which agents violate which rules most often to improve routing
4. **Set up ChromaDB auto-restart** — the startup script has an `--AutoRestart` flag for crash recovery
