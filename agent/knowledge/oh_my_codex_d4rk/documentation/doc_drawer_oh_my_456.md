# oh-my-codex v0.8.4

Released: **2026-03-06**

This is a **setup-flow patch release** focused on making `omx setup` refresh behavior safer, more predictable, and easier to rerun.

---

## TL;DR

- `omx setup` now refreshes managed OMX artifacts by default instead of leaving stale generated content behind.
- Managed refresh paths now preserve backups where applicable before overwriting files.
- Setup prompts before upgrading managed Codex model references from `gpt-5.3-codex` to `gpt-5.4`.
- Added deeper refresh/idempotency regression coverage for setup and config generation paths.
- Includes small release-validation hardening: watcher shutdown cleanup stability and dead-code cleanup surfaced by the strict no-unused gate.

---

## What changed