gressions.
- Ralph CLI task parsing option-value leakage.
- Skills canonical OMX path normalization.

### Reverts
- Revert for opt-in dedicated tmux-session hint change (#432) followed by corrected fix.
- Revert for visual-verdict guidance restoration change followed by path normalization fix.

### Verification for release readiness
- [x] `npm run build` passes
- [x] `npm test` passes
- [x] `npm run check:no-unused` passes
- [x] smoke checks from `DEMO.md` pass (or are documented if environment-limited)

### Smoke verification evidence (2026-03-02)