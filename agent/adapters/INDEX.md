# Adapter Index

All D4rkMynd adapters for different AI coding environments.

## Available Adapters

| Platform | Adapter | Target Files |
|---|---|---|
| **Claude Code** | `adapters/claude/` | `CLAUDE.md`, `.claude/skills` |
| **Kilo Code** | `adapters/kilo/` | `.kilocodemodes` |
| **Cline** | `adapters/cline/` | `.clinerules`, `.cline/skills` |
| **Qwen Code** | `adapters/qwen/` | `.qwen/CLAUDE.md`, `.qwen/skills` |
| **VS Code** | `adapters/vscode/` | `.github/copilot-instructions.md` |
| **Antigravity** | `adapters/antigravity/` | Project instruction files |
| **Google AI Studio** | `adapters/google/` | System prompt |
| **Codex** | `adapters/codex/` | System prompt |
| **D4rkCloud** | `adapters/d4rkcloud/` | `d4rkcloud/skills/` |
| **Generic** | `adapters/generic/` | Any instruction file |

## Quick Setup

For any platform:

1. Run `powershell -ExecutionPolicy Bypass -File %PI_AGENT_HOME%\scripts\generate-modes.ps1`
2. Copy the generated `.cursorrules-auto` content to your platform's instruction file
3. Your AI tool will now route automatically using the D4rkMynd router

For the full cross-tool setup map, read `docs/SURFACE_SETUP_MAP.md`.

## Per-Platform Setup

See each adapter's README.md for platform-specific setup instructions.
