ern without forcing silent rewrites

### 4) Regression coverage expanded for refresh and idempotency

This release adds/extends tests and validation hardening around:
- setup refresh behavior
- scoped overwrite handling
- uninstall compatibility during setup-managed refreshes
- config generator idempotency and notify-aware generation flows
- watcher shutdown/cleanup synchronization during streaming fallback tests

---

## Included commits

- `fed035b` — feat(setup): refresh managed OMX artifacts by default with backups
- `6aa577d` — feat(setup): prompt before upgrading gpt-5.3-codex to gpt-5.4

---

## Verification summary

Release verification evidence is recorded in `docs/qa/release-readiness-0.8.4.md`.