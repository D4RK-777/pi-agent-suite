- Write full assignment to worker `inbox.md`
- Send short trigger (<200 chars) with `tmux send-keys`

Worker-to-leader:

- Send ACK to `leader-fixed` mailbox via `omx team api send-message --json`
- Claim/transition/release task lifecycle via `omx team api <operation> --json`

Worker commit protocol (critical for incremental integration):

- After completing task work and before reporting completion, workers MUST commit:
  `git add -A && git commit -m "task: <task-subject>"`
- This ensures changes are available for incremental integration into the leader branch
- If a worker forgets to commit, the runtime auto-commits as a fallback, but explicit commits are preferred

Task ID rule (critical):