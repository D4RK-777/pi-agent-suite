car
- allows qualifying read-only shell-native `omx explore` tasks to route through `omx sparkshell`
- keeps the explore path intentionally constrained: shell-only, read-only, and allowlisted

Representative changes:
- `fb07c3c` — feat: add omx explore harness and packaging flow
- `71858c3` — feat: add omx sparkshell and team inspection metadata
- `e8e7594` — feat(explore): route qualifying read-only shell tasks via sparkshell
- `dc83dfd` — fix(explore): harden sparkshell fallback paths
- `25bdd23` — docs(guidance): refine explore and sparkshell usage

### Important Spark Initiative notes

For `0.9.0`, the important distribution contract is: