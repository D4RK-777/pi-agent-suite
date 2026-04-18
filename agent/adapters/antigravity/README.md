# Antigravity Adapter

Use this adapter when wiring Antigravity environments to the D4rkMynd shared library.

## Model

- Keep shared reusable skills in `%PI_AGENT_HOME%\skills`.
- Link the canonical skills into the Antigravity skills directory instead of copying them.
- Keep repo-specific instructions in repo-local `AGENTS.md` and generated wrapper files.

## Typical Targets

- Antigravity skills directory
- repo-local skill files

## Recommended Actions

Use `..\..\scripts\sync-skills.ps1` for canonical bulk sync.

Use `..\..\scripts\generate-modes.ps1 -ProjectPath <repo>` when the active repo should expose generated wrapper files alongside `AGENTS.md`.

## Universal Mode Setup

Antigravity reads project-local instruction files for persistent AI behavior.

To enable universal routing:
1. Run `powershell -ExecutionPolicy Bypass -File %PI_AGENT_HOME%\scripts\generate-modes.ps1`
2. Copy the generated `.cursorrules-auto` content to your Antigravity instructions file
3. Antigravity will now route automatically using the D4rkMynd router
