ce/fallback behavior
- pass/fail result
- residual notes

## Exit criteria for the heavy/manual lane

A manual scenario passes only when all of the following are true:
1. the required setup was followed,
2. the expected evidence was captured,
3. the failure signal did **not** appear,
4. the deterministic lane still passes afterward.

Final deterministic recheck (required for the later Ralph verification sweep; not re-run in this doc-only pass):

```bash
npm run test:explore
npm run test:sparkshell
```

## Scenario 1: large noisy tmux-pane captures

**Why excluded from default CI**
- Depends on a live tmux server and realistic pane noise.
- Evidence quality is partly operator-judged: the summary must preserve the facts that matter, not exact wording.