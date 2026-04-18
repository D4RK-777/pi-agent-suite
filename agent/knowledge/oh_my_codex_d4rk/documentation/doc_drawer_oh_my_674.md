seam-hardening gaps, not evidence that the Rust runtime direction was wrong.

## Remaining seam gaps

### 1. Rust runtime ↔ TS team state dual-write

Status: **resolved by issue #1108**

Evidence:

- `src/team/state/dispatch.ts:130-140`
- `src/team/state/mailbox.ts:45-49`

Current state:

- Rust bridge / compat files are now the canonical dispatch and mailbox surface
- legacy TS dispatch/mailbox files remain fallback-only for degraded lanes where the bridge is disabled, unavailable, or unreadable
- watcher/runtime paths were narrowed so bridge-owned success paths no longer semantically dual-write legacy mailbox/dispatch state

Risk: