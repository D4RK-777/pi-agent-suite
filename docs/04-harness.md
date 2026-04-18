# 04 — The Pi Harness

The task routing and orchestration engine at the heart of Pi Agent Suite.

---

## Overview

The harness is a deterministic multi-agent router. When given a task, it scores all available agents using six signals and routes the task to the best match. It does not rely on LLM calls for routing — scoring is pure keyword matching, which makes it fast and predictable.

```
Task description
     │
     ▼
brain/router.py
  ├── score each agent with 6 signals
  └── pick winner (or fall back to advisor)
     │
     ▼
harness/orchestrator.py
  ├── load agent manifest
  ├── inject system prompt + skills
  └── launch session via brain/launch.py
     │
     ▼
Agent runs with full context:
  - specialist system prompt
  - relevant skills
  - MemPalace context (from hooks)
  - conversation history
```

---

## Running the harness

```bash
# Set up Python path first
cd ~/.pi/agent
# or: export PYTHONPATH="$PI_AGENT_HOME/agent:$PYTHONPATH"

# Route a task to the best agent
python -m harness route "build a REST API for user auth"

# Get a multi-agent plan
python -m harness plan "full-stack user registration feature"

# Check compliance
python -m harness check "my code changes"

# Memory stats
python -m harness memory

# System info
python -m harness info

# Run routing tests
python -m harness test
```

**Via pi-harness.ps1 (Windows/cross-platform launcher):**
```powershell
.\pi-harness.ps1 route "build a REST API for user auth"
.\pi-harness.ps1 plan "full-stack user registration feature"
.\pi-harness.ps1 search "react hooks patterns"
.\pi-harness.ps1 stats
```

---

## The 6-signal scoring system

From `brain/router.py`, agents are scored on these signals (higher = stronger match):

| Signal | Points | Example |
|---|---|---|
| Explicit name | 10.0 | "use the backend agent" |
| Skill keyword match | 1.5–2.0 | "API", "database", "endpoint" → backend agent |
| Skill tag match | 1.0 | task contains agent's tag words |
| Domain focus | 0.5/word | task domain matches agent's focus domain |
| Role/note match | 0.25–0.5/word | task words appear in agent's role description |
| Intent keywords | 0.5–1.0 | "build", "debug", "review", "research" |

**Example routing:**
```
Task: "debug the authentication middleware throwing 401 errors"
  - intent keyword "debug" → +1.0 to debugger agent
  - "authentication" → backend skill keyword → +1.5 to backend
  - "401 errors" → debugging keywords → +1.5 to debugger
  - "middleware" → backend domain → +0.5 to backend
  → Debugger agent wins (3.0) over backend (2.0)
```

---

## Agents

Eight specialist agents, each with a focused role:

### advisor
General-purpose strategic advisor. **Default fallback** when no specialist is a strong match. Handles: architecture decisions, tech stack choices, trade-off analysis, roadmap planning.

### backend
Server-side engineering specialist. Handles: REST/GraphQL APIs, databases (SQL + NoSQL), authentication, background jobs, microservices, performance.

### debugger
Root cause analysis specialist. Handles: error diagnosis, stack trace reading, log analysis, performance profiling, fixing flaky tests.

### frontend
UI/UX engineering specialist. Handles: React, TypeScript, state management, CSS, accessibility (WCAG 2.2 AA), responsive design, web performance.

### librarian
Knowledge retrieval specialist. Handles: documentation research, MemPalace queries, Obsidian vault operations, pattern retrieval. Routes knowledge requests to memory stores.

### reviewer
Code quality specialist. Handles: code review, security audit (OWASP), performance review, test coverage analysis, refactoring suggestions.

### scout
Research and discovery specialist. Handles: exploring unfamiliar codebases, technology research, dependency audits, finding relevant libraries.

### _template
Starter template for creating new agents. Not routed to directly.

---

## Agent manifests

Each agent has a JSON manifest in `agent/manifests/` that declares its capabilities:

```json
{
  "name": "backend",
  "aliases": ["server", "api", "database"],
  "role": "Backend engineering specialist",
  "domain_focus": ["API", "server", "database", "auth", "microservices"],
  "skill_keywords": ["endpoint", "REST", "GraphQL", "SQL", "migration"],
  "tags": ["backend", "server", "api", "database"],
  "skills": ["auto-memory", "mempalace-tools", "pi-tasks"],
  "system_prompt_file": "agents/backend/AGENT.md"
}
```

---

## Skills

Skills are composable capability modules that agents can use. They're defined in `agent/skills/` and referenced in manifests.

Core skills (always available):

| Skill | Description |
|---|---|
| `auto-memory` | Persist decisions and patterns to MemPalace automatically |
| `mempalace-tools` | Direct MemPalace search and retrieval |
| `obsidian-tools` | Read/write Obsidian vault |
| `pi-tasks` | Create and track tasks across sessions |
| `pi-spawn-agent` | Launch specialist sub-agents |
| `pi-plan-mode` | Enter structured planning mode |
| `adaptive-recovery` | Recover from errors without losing progress |
| `hook-connector` | Wire custom events to MemPalace |

---

## Bundles

Pre-configured collections of skills for common use cases:

| Bundle | Skills included |
|---|---|
| `essentials` | auto-memory, mempalace-tools, pi-tasks |
| `frontend` | essentials + obsidian-tools, accessibility-checker |
| `backend` | essentials + pi-spawn-agent, hook-connector |
| `fullstack` | frontend + backend |
| `security` | essentials + security-audit, owasp-checker |
| `testing` | essentials + test-writer, coverage-analyzer |
| `operations` | essentials + pi-plan-mode, adaptive-recovery |

Load a bundle:
```bash
python -m harness route "build a login form" --bundle frontend
```

---

## Cookbooks

Multi-step workflow templates for complex tasks. Stored in `agent/cookbooks/`.

Each cookbook defines:
- Step sequence with agent assignments
- Handoff protocols between agents
- Success criteria
- Rollback procedures

Example cookbooks:
- `full-stack-feature.md` — end-to-end feature from design to deployment
- `debug-session.md` — systematic debugging workflow
- `code-review.md` — structured review process
- `api-design.md` — API-first design workflow

---

## Session lifecycle

`brain/launch.py` manages each session:

```python
# Session start
run_session_start_hook(task, agent)  # logs session, injects context

# Task execution (handled by AI client)
...

# Session end
mine_to_mempalace(transcript)  # saves conversation to palace
save_session(session_id, task, agent, outcome)  # saves session record
run_session_end_hook(session_id)  # cleanup
```

Sessions are saved to `agent/sessions/` (excluded from the distributed package).

---

## Enforcement and compliance

`harness/enforcement.py` provides optional compliance watching:

- **Enforcer** — validates agent outputs against rules
- **ComplianceWatcher** — monitors for policy violations
- **MemoryWatcher** — ensures memory operations are correct
- **WatcherPipeline** — chains multiple watchers

Run compliance check:
```bash
python -m harness compliance --agent backend --task "auth implementation"
```

---

## Extending the harness

See [docs/07-customization.md](07-customization.md) for:
- Adding new agents
- Creating custom skills
- Building new bundles
- Writing cookbooks
