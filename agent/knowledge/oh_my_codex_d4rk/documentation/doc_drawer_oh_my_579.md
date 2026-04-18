ders must treat these files as read-only; the Rust engine is the sole writer.

## Thin-adapter rules

1. Compatibility readers must ignore unknown fields and preserve their current
   JSON envelopes.
2. Legacy tmux typing is delivery only; it does not establish semantic truth.
3. If Rust-authored compatibility files and legacy JS defaults disagree, the
   Rust-authored file wins.
4. JS file writes remain fallback-only for lanes where the bridge is disabled or
   unavailable; they are not canonical when the Rust bridge succeeds.
5. Unknown delivery failures are surfaced as adapter failures, not as semantic
   owner changes.

## Consumer matrix