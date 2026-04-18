tup --force --scope project
```

after upgrading so managed config/native-agent paths are refreshed.

## Local release verification summary

Validated locally on `dev` before tagging:

- `node scripts/check-version-sync.mjs --tag v0.9.0`
- `npm run lint`
- `npx tsc --noEmit`
- `npm run check:no-unused`
- `npm test`
- `npm run build:full`
- `npm run test:explore`
- `npm run test:sparkshell`
- `node bin/omx.js doctor`
- `node bin/omx.js setup --dry-run`
- `npm pack --dry-run`

## Notable PRs