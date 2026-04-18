rially branching, destructive, or preference-dependent.

When user triggers `$team`, the agent must:

1. Invoke OMX runtime directly with `omx team ...`
2. Avoid replacing the flow with in-process `spawn_agent` fanout
3. Verify startup and surface concrete state/pane evidence
4. Keep team state alive until workers are terminal (unless explicit abort)
5. Handle cleanup and stale-pane recovery when needed

If `omx team` is unavailable, stop with a hard error.

## Invocation Contract

```bash
omx team [N:agent-type] "<task description>"
```

Examples:

```bash
omx team 3:executor "analyze feature X and report flaws"
omx team "debug flaky integration tests"
omx team "ship end-to-end fix with verification"
```

### Team-first launch contract