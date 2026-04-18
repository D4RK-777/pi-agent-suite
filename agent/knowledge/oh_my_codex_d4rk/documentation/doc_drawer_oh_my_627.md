ore` separately only if you specifically want the debug cargo build path during local investigation.

Use a clean throwaway workspace when possible. If you need tmux-pane coverage, run inside tmux and confirm the target pane id first.

## Verified command baseline

The following command forms were verified during this doc pass:

| Command | Result |
|---|---|
| `node bin/omx.js explore --help` | PASS |
| `node bin/omx.js sparkshell --help` | PASS |
| `node bin/omx.js sparkshell git --version` | PASS |
| `node bin/omx.js version` | PASS |
| `for i in $(seq 1 20); do node bin/omx.js sparkshell git --version; done` | PASS (bounded sample verified locally) |
| `seq 1 5 | xargs -I{} -P5 node bin/omx.js sparkshell git --version` | PASS (bounded sample verified locally) |