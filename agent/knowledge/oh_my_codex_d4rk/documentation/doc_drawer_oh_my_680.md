# Rust Runtime Thin-Adapter Release Gate

This checklist is a hard gate for the Rust-core + thin-adapter cutover.
CI/release validation MUST fail when any required scenario below is missing or
failing.

## Verification matrix gate

| ID | Scenario | Required evidence | Status |
|---|---|---|---|
| G1 | Team status reads the manifest-authored compatibility view | `src/compat/__tests__/rust-runtime-compat.test.ts` | [x] |
| G2 | Doctor preserves manifest-first tmux/session precedence | `src/compat/__tests__/rust-runtime-compat.test.ts` | [x] |
| G3 | HUD preserves session-scoped state precedence over root fallback | `src/compat/__tests__/rust-runtime-compat.test.ts` | [x] |