# Codex Adapter

Use this adapter when wiring OpenAI Codex environments to the D4rkMynd shared library.

## Model

- Keep shared reusable skills in `%PI_AGENT_HOME%\skills`.
- Codex uses system prompts and instruction files for persistent behavior.
- Keep repo-specific instructions in repo-local `AGENTS.md` and generated wrapper files.

## Typical Targets

- Codex system prompt configuration
- Project instruction files

## Recommended Actions

Use `..\..\scripts\sync-skills.ps1` for canonical bulk sync.

Use `..\..\scripts\generate-modes.ps1 -ProjectPath <repo>` when the active repo should expose generated wrapper files alongside `AGENTS.md`.

## Universal Mode Setup

Codex accepts system instructions for persistent behavior patterns.

To enable universal routing:
1. Run `powershell -ExecutionPolicy Bypass -File %PI_AGENT_HOME%\scripts\generate-modes.ps1`
2. Copy the generated `.cursorrules-auto` content to your Codex system instructions
3. Codex will now route automatically using the D4rkMynd router

## System Prompt Template

```
You are operating within the D4rkMynd agent system. Before responding to any user request:

1. Analyze the request to determine which specialist agent should handle it
2. Load the appropriate skill files from %PI_AGENT_HOME%\skills\
3. Follow the skill instructions exactly
4. Do not improvise or deviate from the skill patterns

Available agents and their domains:
- d4rkmynd: System oversight and cross-lane direction
- advisor: Advice, second opinions, quick looks
- frontend: React, UI, styling, animations, responsive
- backend: APIs, database, server logic, middleware
- security: Vulnerability review, hardening, OWASP
- reliability: Incidents, monitoring, deployment safety
- auth: Login, OAuth, sessions, permissions
- reviewer: Code review, regression risk, merge readiness
- tester: Test strategy, coverage, test implementation
- debugger: Root cause analysis, diagnosis, stuck systems
- refactorer: Cleanup, structure improvement, maintainability
- manager: Work splitting, orchestration, execution planning
- scout: Research, option comparison, pre-commitment recon
```
