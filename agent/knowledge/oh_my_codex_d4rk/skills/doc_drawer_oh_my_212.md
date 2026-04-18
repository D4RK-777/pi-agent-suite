---
name: "hud"
description: "Show or configure the OMX HUD (two-layer statusline)"
role: "display"
scope: ".omx/**"
---

# HUD Skill

The OMX HUD uses a two-layer architecture:

1. **Layer 1 - Codex built-in statusLine**: Real-time TUI footer showing model, git branch, and context usage. Configured via `[tui] status_line` in `~/.codex/config.toml`. Zero code required.

2. **Layer 2 - `omx hud` CLI command**: Shows OMX-specific orchestration state (ralph, ultrawork, autopilot, team, pipeline, ecomode, turns). Reads `.omx/state/` files.

## Quick Commands