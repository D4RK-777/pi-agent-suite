aths
- Easier onboarding for new users
- Lower chance of config drift between notification providers

### 3) OpenClaw safety + operability improvements

- OpenClaw command timeout is now configurable with bounded safety limits.
- Documentation was expanded with stronger token/command safety guidance and a practical dev runbook.

**Why this matters:**
- Safer operation in automation-heavy environments
- Better operational clarity for development and incident follow-up

---

## Compatibility / migration notes

- If you previously relied on legacy `team_*` MCP workflows, migrate to:
  - `omx team api <operation> ...`
- For notification setup, prefer:
  - `omx configure-notifications` (or skill equivalent)

No breaking package-level API changes were introduced in this patch release.

---