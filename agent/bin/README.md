# D4rk Mind — Knowledge System

Continuous knowledge mining and cultivation system for AI agents.

## Overview

D4rk Mind keeps your MemPalace growing with fresh, deep domain knowledge from:
- Codebase mining (your projects)
- Component libraries (Radix, shadcn, Chakra, etc.)
- Design systems (Tailwind, Radix Colors, etc.)
- Architecture patterns (12-factor, system design)
- Security patterns (OWASP, security headers)
- Best practices (REST, GraphQL, Node.js)

## Quick Start

```bash
# Start all knowledge daemons
bash ~/.pi/agent/bin/start_knowledge_daemon.sh start

# Check status
bash ~/.pi/agent/bin/start_knowledge_daemon.sh status

# View logs
tail -f ~/.mempalace/logs/knowledge_gardener.log
```

## Tools

### knowledge_gardener.py

Continuously studies curated sources and adds patterns to MemPalace.

```bash
# Run once
python knowledge_gardener.py

# Run forever (checks every 24 hours)
python knowledge_gardener.py --daemon

# List configured sources
python knowledge_gardener.py --sources
```

### mine_agent.py

Watches your codebases and keeps MemPalace updated with your code.

```bash
# Mine current directory once
python mine_agent.py

# Watch for changes (every 60 seconds)
python mine_agent.py --watch

# Auto-detect all projects
python mine_agent.py --auto-detect

# Watch specific projects
python mine_agent.py --project ~/code/myapp --watch
```

### index_projects.py

Deep-index a project structure into MemPalace.

```bash
# Index current project
python index_projects.py

# Index specific project
python index_projects.py ~/code/myapp

# Index all detected projects
python index_projects.py --all
```

### add_knowledge_source.py

Add custom repositories to the knowledge garden.

```bash
# Interactive mode
python add_knowledge_source.py --interactive

# Add a GitHub repo
python add_knowledge_source.py \
    --name "MyComponents" \
    --url "https://github.com/user/components" \
    --wing expert-frontend \
    --room "components/my-lib" \
    --patterns "Button,Modal,Card"

# List all custom sources
python add_knowledge_source.py --list

# Mine all custom sources
python add_knowledge_source.py --mine
```

### mempalace_fast.py

Fast MemPalace search (~20ms queries).

```python
import sys
sys.path.insert(0, '.pi/agent/bin')
from mempalace_fast import search

# Fast search
results = search("react hooks patterns")
for r in results['results']:
    print(f"{r['similarity']}: {r['source']}")
    print(r['content'][:200])
```

## Daemon Management

```bash
# Start all daemons
bash start_knowledge_daemon.sh start

# Stop all daemons
bash start_knowledge_daemon.sh stop

# Check status
bash start_knowledge_daemon.sh status

# Restart
bash start_knowledge_daemon.sh restart
```

## Knowledge Sources

### Pre-configured Sources

| Wing | Source | Patterns |
|------|--------|----------|
| expert-frontend | Radix UI | 22 components |
| expert-frontend | shadcn/ui | 18 components |
| expert-frontend | Headless UI | 9 components |
| expert-frontend | Chakra UI | 13 components |
| expert-frontend | React Aria | 14 hooks |
| design-systems | Tailwind CSS | 18 patterns |
| design-systems | Radix Colors | 14 palettes |
| design-systems | Heroicons | 6 patterns |
| expert-backend | Node.js Best Practices | 11 sections |
| expert-backend | REST API Design | 12 patterns |
| expert-security | OWASP Top 10 | 20 patterns |
| architecture | 12-Factor App | 12 factors |
| architecture | System Design | 12 patterns |

### Custom Sources

Add your own:

```bash
python add_knowledge_source.py --interactive
```

Popular choices:
- Company component library
- Internal design system
- Architecture decision records
- API documentation
- Team coding conventions

## File Structure

```
~/.mempalace/
├── palace/              # Vector database (ChromaDB)
├── custom_sources.json  # Your custom knowledge sources
├── mine_agent_state.json  # Mining state
├── knowledge_gardener_state.json  # Garden state
├── pids/              # Daemon PID files
└── logs/              # Daemon logs
    ├── knowledge_gardener.log
    └── mine_agent.log
```

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     D4RK MIND SYSTEM                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              KNOWLEDGE GARDENER                         │   │
│  │  (Studies curated sources every 24 hours)                │   │
│  │  • Radix UI, shadcn, Chakra                             │   │
│  │  • Tailwind, Radix Colors                               │   │
│  │  • OWASP, 12-Factor, System Design                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                MINE AGENT                                │   │
│  │  (Watches codebases continuously)                        │   │
│  │  • Auto-detects projects                                │   │
│  │  • Indexes structure & content                          │   │
│  │  • Tracks changes                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   MEMPALACE                              │   │
│  │  (27,000+ records, 150MB vector DB)                     │   │
│  │  Wings: expert-frontend, expert-backend, etc.           │   │
│  │  Fast search: ~20ms queries                             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   AI AGENTS                             │   │
│  │  (Use MemPalace for instant knowledge recall)           │   │
│  │  • Claude Code                                          │   │
│  │  • Codex CLI                                            │   │
│  │  • Gemini                                               │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Troubleshooting

### Daemon not starting
```bash
# Check logs
tail -f ~/.mempalace/logs/knowledge_gardener.log

# Verify Python
python --version

# Check dependencies
pip show chromadb httpx
```

### No search results
```bash
# Run gardener manually
python knowledge_gardener.py

# Check palace status
python -X utf8 -m mempalace.cli status
```

### Slow queries
```bash
# Use fast API (already configured in skills)
# Should be ~20ms per query
```

## Cron Setup (Alternative)

If you prefer cron over daemons:

```bash
# Run every hour
0 * * * * cd ~/.pi/agent/bin && python mine_agent.py --auto-detect

# Run every day at midnight
0 0 * * * cd ~/.pi/agent/bin && python knowledge_gardener.py
```

## Contributing

To add a new knowledge source:

1. Add to `knowledge_gardener.py` SOURCES list
2. Or use: `python add_knowledge_source.py --interactive`
3. Restart daemon or run manually

## License

MIT
