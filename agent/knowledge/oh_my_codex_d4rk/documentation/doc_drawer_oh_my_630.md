ality is partly operator-judged: the summary must preserve the facts that matter, not exact wording.

**Goal**
- Confirm `omx-sparkshell --tmux-pane` preserves operator-critical facts when pane tails are large and noisy.
- Confirm the summary/fallback path still points the operator to the right next action.

**Setup**
1. Start a tmux session with a pane that emits mixed signal + distractor output.
2. Predeclare the must-preserve facts before running the scenario.
3. Capture the pane id.

Suggested must-preserve facts:
- the failing command name,
- the final non-zero exit or failure state,
- the actionable recovery or inspection hint,
- any file/path identifier needed for next action.

**Command shape**

```bash
omx sparkshell --tmux-pane <pane-id> --tail-lines 400
```