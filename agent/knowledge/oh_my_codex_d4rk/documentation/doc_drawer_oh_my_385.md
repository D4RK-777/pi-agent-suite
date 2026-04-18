ecklist sections normalized. | No intentional functional delta in migration commit. |

## Validation

- Commit diff summary: `30 files changed, 2439 insertions(+), 2511 deletions(-)`
- Spot-checks performed on role-heavy prompts (`planner`, `executor`, `explore`) confirmed semantic parity with formatting normalization.

---

## Orchestration Brain Migration (`AGENTS.md`, `templates/AGENTS.md`)

### Summary

These files are the instruction root that OMX expects Codex to follow across a workspace.
Changes here are primarily about aligning instructions with Codex CLI tool contracts.

### Key Deltas