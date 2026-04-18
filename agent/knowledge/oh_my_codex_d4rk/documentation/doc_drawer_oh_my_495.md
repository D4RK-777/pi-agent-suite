operations

The sparkshell line is not just a hidden backend. It is now part of the operator story.

This release:
- exposes `omx sparkshell --tmux-pane <pane-id> --tail-lines <100-1000>` for explicit pane summarization
- surfaces sparkshell inspection metadata in team status flows
- makes long-output summarization more predictable
- adds stress coverage for noisy and adversarial output

Representative changes:
- `71858c3` — feat: add omx sparkshell and team inspection metadata
- `b890123` — fix: force low reasoning for sparkshell summaries (#781)
- `a653376` — test: add explore and sparkshell stress coverage

### Supporting runtime and operator polish

Alongside the spark-focused work, `dev` also picked up supporting improvements that make the release feel more complete: