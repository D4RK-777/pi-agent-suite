- previous iteration outcome
- bounded recent ledger summary
- keep policy

## Verification targets

Parity-aligned implementation should prove:
1. fresh launches create distinct run-tagged lanes
2. repo-root active-run lock rejects concurrent launches
3. candidate handoff artifact drives keep/discard/reset decisions
4. discarded candidates reset to `last_kept_commit`
5. `--resume <run-id>` reloads authoritative manifest/worktree state
6. README/help/contracts describe the thin-supervisor parity loop