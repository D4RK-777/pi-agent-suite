so bridge-owned success paths no longer semantically dual-write legacy mailbox/dispatch state

Risk:

- residual regressions are now more likely to come from incorrect fallback activation than from active dual-write divergence
- future refactors could accidentally widen fallback behavior unless tests/docs keep the canonical-owner rule explicit

Desired end state:

- Rust owns the semantic transition
- TS stores only adapter-local or presentation-local metadata

### 2. Team metadata resolution still spans multiple files

Evidence:

- `src/team/api-interop.ts:423-438`

Current state:

- worker identity metadata is checked first
- then `manifest.v2.json`
- then `config.json`

Risk:

- working-directory or state-root resolution can depend on fallback order instead of one canonical source