l is refreshed for the `0.11.10` cut

## Verification evidence

### Release-focused regression suite

- `npx biome lint src/planning/__tests__/artifacts.test.ts` ✅
- `npm run build && node --test dist/planning/__tests__/artifacts.test.js` ✅
- `npm run test:sparkshell` ✅
- `npm run test:team:cross-rebase-smoke` ✅
- `npm run smoke:packed-install` ✅
- `npm test` ✅

## Remaining risk

- This release is intentionally narrow and primarily test / metadata focused; it does not introduce production runtime behavior changes.
- Future launch-hint grammar changes should keep alias-form coverage aligned for both Ralph and Team paths.