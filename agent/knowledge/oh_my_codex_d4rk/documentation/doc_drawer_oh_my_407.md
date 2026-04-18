ly
- supports packaged native resolution plus source/repo-local fallback paths

### `omx sparkshell`

- adds an operator-facing native shell sidecar
- supports direct command execution
- summarizes long output into compact sections
- supports explicit tmux-pane summarization:

```bash
omx sparkshell --tmux-pane %12 --tail-lines 400
```

### Explore ↔ sparkshell integration

- qualifying read-only shell-native `omx explore` prompts can route through `omx sparkshell`
- fallback behavior remains explicit and hardened
- guidance/docs/tests were aligned around this contract

### Worker follow-through polish