bounds**.

---

## What changed

### 1) Team runtime: CLI-first interop is now the default direction

- Added and finalized team API interop through:
  - `omx team api ...`
- Legacy `team_*` MCP tools are now treated as deprecated paths in favor of the CLI-first contract.

**Why this matters:**
- More predictable behavior across team orchestration flows
- Cleaner compatibility surface for worker/leader interactions
- Better long-term maintainability around team runtime contracts

### 2) Notifications: setup is now unified

- Notification setup guidance has been refactored into a single workflow:
  - `configure-notifications`

**Why this matters:**
- Fewer fragmented setup paths
- Easier onboarding for new users
- Lower chance of config drift between notification providers