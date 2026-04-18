s` comment wording from legacy alias names to low/medium/high reasoning wording.

## Expected effect

After rebuilding and rerunning `omx setup --force`, spawned-agent metadata should stop surfacing `haiku` / `sonnet` / `opus` as if they were active runtime models for Codex-based OMX runs.

## Re-test steps

```bash
npm run build   # TypeScript build
node bin/omx.js setup --scope project --force
```

Then rerun the fork benchmark and watch for any remaining `Model: sonnet` lines. If they still appear after this cleanup, the remaining source is likely outside prompt/skill/runtime metadata generation and should be investigated in Codex display integration or cached/generated config artifacts.