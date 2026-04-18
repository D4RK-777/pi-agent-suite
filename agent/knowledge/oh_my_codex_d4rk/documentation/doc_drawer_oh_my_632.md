can be environment-sensitive.
- Useful signal comes from aggregate stability, not one isolated run.

**Goal**
- Confirm repeated runs do not degrade fallback reliability or guidance quality.
- Confirm concurrent direct-command use does not produce confusing or unusable operator output.

**Setup**
1. Choose a stable direct command and one fallback-oriented command.
2. Run the direct command repeatedly.
3. Run a bounded burst of concurrent invocations.

Verified direct-command example:

```bash
node bin/omx.js sparkshell git --version
```

Suggested repeated-run shape:

```bash
for i in $(seq 1 20); do node bin/omx.js sparkshell git --version; done
```

Suggested concurrent-run shape:

```bash
seq 1 5 | xargs -I{} -P5 node bin/omx.js sparkshell git --version
```