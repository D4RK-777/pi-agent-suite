# D4rkCloud Adapter

Use this adapter when wiring D4rkCloud environments to the D4rkMynd shared library.

## Model

- Keep shared reusable skills in `%PI_AGENT_HOME%\skills`.
- D4rkCloud uses plugin-based skill loading from `d4rkcloud/skills/`.
- Keep repo-specific instructions in repo-local `AGENTS.md` and generated wrapper files.

## Typical Targets

- `d4rkcloud/skills/`
- `d4rkcloud/plugins/`

## Recommended Actions

Use `..\..\scripts\sync-skills.ps1` for canonical bulk sync.

Use `..\..\scripts\export-d4rkcloud.ps1` to export skills to D4rkCloud format.

Use `..\..\scripts\generate-modes.ps1 -ProjectPath <repo>` when the active repo should expose generated wrapper files alongside `AGENTS.md`.

## Universal Mode Setup

D4rkCloud reads skill definitions from `d4rkcloud/skills/` directories.

To enable universal routing:
1. Run `powershell -ExecutionPolicy Bypass -File %PI_AGENT_HOME%\scripts\export-d4rkcloud.ps1`
2. This exports all canonical skills to D4rkCloud format
3. D4rkCloud will now have access to all D4rkMynd skills

## Plugin Configuration

```json
{
  "name": "d4rkmynd",
  "version": "1.0.0",
  "description": "D4rkMynd canonical skills for D4rkCloud",
  "skills": [
    "frontend-engineering",
    "backend-engineering",
    "security-and-auth",
    "delivery-code-review",
    "delivery-testing",
    "adaptive-error-recovery",
    "observability-and-monitoring",
    "incident-and-recovery",
    "problem-framing",
    "findings-synthesis",
    "recursive-improvement-loop",
    "skill-validator",
    "skill-packager",
    "security-first-pass"
  ]
}
```
