current home directory dynamically
- updated tests for newly surfaced claim-lock inspection metadata

## Local verification
- `npm run lint`
- `npm run check:no-unused`
- `npm run build:full`
- `cargo test --manifest-path native/omx-sparkshell/Cargo.toml`
- `node scripts/build-sparkshell.mjs`
- `node scripts/test-sparkshell.mjs`
- `node bin/omx.js sparkshell cargo --version`
- `node bin/omx.js sparkshell npm --version`
- `node bin/omx.js sparkshell git log --oneline -3`
- `npm test`

## Notes
- `npm test` removes the staged packaged sparkshell binary as part of packaging cleanup; I restored the tracked binary afterward.
- Native Rust build artifacts under `native/omx-sparkshell/target/` were removed after verification.