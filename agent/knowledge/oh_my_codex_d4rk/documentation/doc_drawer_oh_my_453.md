ehavior for prompt-launched Gemini workers
- translation behavior when default models are non-Gemini

### 4) Full-suite verification was stabilized

Release validation also hardened a flaky watcher test so the full suite reliably waits for watcher readiness before asserting streaming EOF-tail behavior.

**Why this matters:**
- keeps release verification deterministic under heavy suite load
- preserves the intended watcher behavior instead of relying on fixed sleeps
- does not change shipped Gemini runtime behavior

---

## Related PRs and issues

### Merged PRs in this release
- #585 — fix(team): seed gemini workers with prompt-interactive launch