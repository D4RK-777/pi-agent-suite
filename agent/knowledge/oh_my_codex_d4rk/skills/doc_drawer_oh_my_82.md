O architectural changes
   - NO performance optimizations
   - ONLY what's needed to make build pass

4. **Verify**
   - Run the project's type check command after each fix
   - Ensure no new errors introduced
   - Stop when build passes

## Command Guidance

- Prefer `omx sparkshell` for noisy build/typecheck runs, repository search/listing, and bounded read-only inspection when summary output is enough.
- Use raw shell when exact stdout/stderr, shell composition, dependency installation, or low-level debugging fidelity is required.
- If `omx sparkshell` returns incomplete, ambiguous, or `summary unavailable` output, retry with a more precise command or the raw shell immediately.

## Agent Delegation

```
delegate(
  role="build-fixer",
  tier="STANDARD",
  prompt="BUILD FIX TASK