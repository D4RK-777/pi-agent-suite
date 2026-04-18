# Qwen Code Adapter

Use this adapter when wiring Qwen Code environments to the D4rkMynd shared library.

## Model

- Keep shared reusable skills in `%PI_AGENT_HOME%\skills`.
- Link the canonical skills into `%USERPROFILE%\.qwen\skills` instead of copying them.
- Keep repo-specific instructions in repo-local `AGENTS.md` and generated wrapper files.

## Typical Targets

- `%USERPROFILE%\.qwen\skills`
- repo-local `.qwen\skills`

## Recommended Actions

Use `..\..\scripts\sync-skills.ps1` for canonical bulk sync.

Use `..\..\scripts\install-links.ps1 -QwenSkillsPath "%USERPROFILE%\.qwen\skills"` for an explicit one-surface install.

Use `..\..\scripts\generate-modes.ps1 -ProjectPath <repo>` when the active repo should expose generated wrapper files alongside `AGENTS.md`.

## Universal Mode Setup

Qwen Code reads `.qwen/CLAUDE.md` or `.qwen/instructions.md` for persistent instructions.

To enable universal routing:
1. Run `powershell -ExecutionPolicy Bypass -File %PI_AGENT_HOME%\scripts\generate-modes.ps1`
2. Copy the generated `.cursorrules-auto` content to `.qwen/CLAUDE.md`
3. Qwen will now route automatically using the D4rkMynd router
