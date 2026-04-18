# VS Code Adapter

Use this adapter when wiring VS Code environments to the D4rkMynd shared library.

## Model

- Keep shared reusable skills in `%PI_AGENT_HOME%\skills`.
- VS Code uses `.vscode/settings.json` and `.vscode/extensions.json` for project configuration.
- Keep repo-specific instructions in repo-local `AGENTS.md` and generated wrapper files.

## Typical Targets

- `.vscode/settings.json`
- `.vscode/extensions.json`
- repo-local `.vscode/`

## Recommended Actions

Use `..\..\scripts\sync-skills.ps1` for canonical bulk sync.

Use `..\..\scripts\generate-modes.ps1 -ProjectPath <repo>` when the active repo should expose generated wrapper files alongside `AGENTS.md`.

## Universal Mode Setup

VS Code with Copilot or other AI extensions reads `.github/copilot-instructions.md` or `.vscode/ai-instructions.md`.

To enable universal routing:
1. Run `powershell -ExecutionPolicy Bypass -File %PI_AGENT_HOME%\scripts\generate-modes.ps1`
2. Copy the generated `.cursorrules-auto` content to `.github/copilot-instructions.md`
3. VS Code AI will now route automatically using the D4rkMynd router

## VS Code Settings

```json
{
  "files.associations": {
    "*.module.css": "css",
    "*.skill.md": "markdown"
  },
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "files.exclude": {
    "**/.git": true,
    "**/.DS_Store": true
  }
}
```
