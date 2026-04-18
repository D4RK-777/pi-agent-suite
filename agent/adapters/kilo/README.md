# Kilo Code Adapter

Use this adapter when wiring Kilo Code environments to the D4rkMynd shared library.

## Model

- Keep shared reusable skills in `%PI_AGENT_HOME%\skills`.
- Link the canonical skills into `%USERPROFILE%\.kilocodemodes` instead of copying them.
- Keep repo-specific instructions in repo-local `AGENTS.md` and generated wrapper files.

## Typical Targets

- `%USERPROFILE%\.kilocodemodes`
- repo-local `.kilocodemodes`

## Recommended Actions

Use `..\..\scripts\sync-skills.ps1` for canonical bulk sync.

Use `..\..\scripts\generate-modes.ps1 -ProjectPath <repo>` when the active repo should expose generated wrapper files alongside `AGENTS.md`.

## Universal Mode Setup

The universal auto-mode is generated automatically when you run `generate-modes.ps1`. It adds the "D4rkMynd Auto" mode to your `.kilocodemodes` file.

To use:
1. Run `powershell -ExecutionPolicy Bypass -File %PI_AGENT_HOME%\scripts\generate-modes.ps1`
2. Switch to "D4rkMynd Auto" mode in Kilo
3. Just talk naturally — the system routes automatically
