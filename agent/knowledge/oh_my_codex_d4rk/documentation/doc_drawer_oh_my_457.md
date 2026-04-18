cleanup stability and dead-code cleanup surfaced by the strict no-unused gate.

---

## What changed

### 1) Managed OMX artifacts refresh by default

Setup now treats managed OMX artifacts as refreshable outputs rather than one-time drops. Re-running `omx setup` updates shipped artifacts more consistently, helping existing installations stay aligned with current templates and generated assets.

**Why this matters:**
- reduces stale generated files after upgrades
- makes repeat setup runs safer and more useful
- improves consistency between fresh installs and refreshed installs

### 2) Refresh paths preserve backups before overwriting

When setup replaces managed artifacts, it now does so with stronger backup behavior where applicable.