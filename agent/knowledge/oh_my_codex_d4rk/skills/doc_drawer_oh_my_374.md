---
name: team
description: N coordinated agents on shared task list using tmux-based orchestration
---

# Team Skill

`$team` is the tmux-based parallel execution mode for OMX. It starts real worker Codex and/or Claude CLI sessions in split panes and coordinates them through `.omx/state/team/...` files plus CLI team interop (`omx team api ...`) and state files.

This skill is operationally sensitive. Treat it as an operator workflow, not a generic prompt pattern.

## Team vs Native Subagents