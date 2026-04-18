workspace metadata, and lockfiles

## Verification evidence

### Release-focused verification suite

- `cargo check --workspace` ✅
- `npm run build` ✅
- `npm run lint` ✅
- `node --test dist/cli/__tests__/version-sync-contract.test.js` ✅
- release-workflow inline version-sync check from `.github/workflows/release.yml` ✅
- `npm run test:node:cross-platform` ✅
- `npm run smoke:packed-install` ✅

## Remaining risk

- This release verification is targeted to release integrity plus the post-`0.11.11` runtime/test/doc surfaces; it is not a full CI matrix rerun.
- Future workflow-doc edits should stay anchored on the deep-interview → ralplan → team/ralph progression so release docs do not drift back to older entrypoint guidance.