can overlap with `${CODEX_HOME:-~/.codex}/skills/` and cause duplicate Enable/Disable Skills entries

Look for files like:
- `architect.md`, `researcher.md`, `explore.md`, `executor.md`, etc. in agents/
- `ultrawork.md`, `deepsearch.md`, etc. in commands/
- Any oh-my-codex-related `.md` files in skills/

---

## Report Format

After running all checks, output a report:

```
## OMX Doctor Report

### Summary
[HEALTHY / ISSUES FOUND]

### Checks