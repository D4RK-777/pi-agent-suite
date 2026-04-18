|
| **Environment Error** | Exit: "ULTRAQA ERROR: [tmux/port/dependency issue]" |

## Observability

Output progress each cycle:
```
[ULTRAQA Cycle 1/5] Running tests...
[ULTRAQA Cycle 1/5] FAILED - 3 tests failing
[ULTRAQA Cycle 1/5] Architect diagnosing...
[ULTRAQA Cycle 1/5] Fixing: auth.test.ts - missing mock
[ULTRAQA Cycle 2/5] Running tests...
[ULTRAQA Cycle 2/5] PASSED - All 47 tests pass
[ULTRAQA COMPLETE] Goal met after 2 cycles
```

## State Tracking

Use `omx_state` MCP tools for UltraQA lifecycle state.