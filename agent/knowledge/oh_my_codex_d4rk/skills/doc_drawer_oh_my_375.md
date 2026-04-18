sitive. Treat it as an operator workflow, not a generic prompt pattern.

## Team vs Native Subagents

- Use **Codex native subagents** for bounded, in-session parallelism where one leader thread can fan out a few independent subtasks and wait for them directly.
- Use **`omx team`** when you need durable tmux workers, shared task state, mailbox/dispatch coordination, worktrees, explicit lifecycle control, or long-running parallel execution that must survive beyond one local reasoning burst.
- Native subagents can complement team/ralph execution, but they do **not** replace the tmux team runtime's stateful coordination contract.

## What This Skill Must Do

## GPT-5.4 Guidance Alignment