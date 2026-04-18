in/omx.js setup --dry-run` | PASS |
| Explore help smoke | `node bin/omx.js explore --help` | PASS |
| Explore prompt-file smoke | `node bin/omx.js explore --prompt-file /tmp/omx-explore-smoke.txt` | PASS |
| Explore→sparkshell routing smoke | `OMX_SPARKSHELL_LINES=1 node bin/omx.js explore --prompt 'git log --oneline -10'` | PASS (summary output emitted) |
| Sparkshell help smoke | `node bin/omx.js sparkshell --help` | PASS |
| Sparkshell direct smoke | `node bin/omx.js sparkshell git --version` | PASS (`git version 2.34.1`) |
| Sparkshell summary smoke | `OMX_SPARKSHELL_LINES=1 node bin/omx.js sparkshell git log --oneline -10` | PASS (summary output emitted) |
| Sparkshell tmux-pane smoke | `node bin/omx.js sparkshell --tmux-pane %2141 --tail-lines 120` | PASS |