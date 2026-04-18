release cut from `main` with that fix applied.

## Included fix

### Localize smoke hydration assets

The packed-install smoke workflow now copies and resolves hydration assets from the local smoke workspace so release verification matches packaged-install behavior more reliably.

Changed files:
- `scripts/smoke-packed-install.mjs`
- `scripts/__tests__/smoke-packed-install.test.mjs`

## Local release verification summary

Planned local release-critical validation for `0.9.1`:

- `node scripts/check-version-sync.mjs --tag v0.9.1`
- `npm run lint`
- `npx tsc --noEmit`
- `npm run check:no-unused`
- `npm test`
- `node --test scripts/__tests__/smoke-packed-install.test.mjs`
- `npm run build:full`
- `npm run smoke:packed-install`
- `npm pack --dry-run`

## Historical note