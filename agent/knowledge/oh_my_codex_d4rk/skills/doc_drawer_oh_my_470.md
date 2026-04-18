---
name: worker
description: Team worker protocol (ACK, mailbox, task lifecycle) for tmux-based OMX teams
---

# Worker Skill

This skill is for a Codex session that was started as an OMX Team worker (a tmux pane spawned by `$team`).

## Identity

You MUST be running with `OMX_TEAM_WORKER` set. It looks like:

`<team-name>/worker-<n>`

Example: `alpha/worker-2`

## Load Worker Skill Path (Claude/Codex)

When a worker inbox tells you to load this skill, resolve the first existing path:

1. `${CODEX_HOME:-~/.codex}/skills/worker/SKILL.md`
2. `~/.codex/skills/worker/SKILL.md`
3. `<leader_cwd>/.codex/skills/worker/SKILL.md`
4. `<leader_cwd>/skills/worker/SKILL.md` (repo fallback)

## Startup Protocol (ACK)