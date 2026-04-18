g doctor/setup results

### 4) Patch fixes

Two additional correctness fixes landed in this release:

- **OpenClaw template safety:** unresolved placeholders in hook instruction templates now fall back safely instead of leaking literal placeholders into instructions (`#581`, closes `#578`).
- **Keyword detection hardening:** explicit multi-skill order is preserved left-to-right, missing keyword aliases were restored, and direct `/prompts:<name>` invocations are protected from unintended implicit keyword activation (`#582`).

---

## Related PRs and issues