r next action.

**Command shape**

```bash
omx sparkshell --tmux-pane <pane-id> --tail-lines 400
```

**Evidence to capture**
- raw pane tail sample,
- summarized output,
- must-preserve fact checklist,
- whether the next-step command in the output is actually sufficient.

**Failure signal**
- any must-preserve fact is missing,
- the output suggests the wrong next command,
- the output hides the actual failure source under noise.

## Scenario 2: repeated / concurrent invocation stress

**Why excluded from default CI**
- Repetition and concurrency are more expensive and can be environment-sensitive.
- Useful signal comes from aggregate stability, not one isolated run.