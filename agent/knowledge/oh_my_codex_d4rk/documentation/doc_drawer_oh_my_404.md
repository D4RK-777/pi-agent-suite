omated QA

Command executed:

```bash
npm test
```

Result:
- PASS — `664` tests passed, `0` failed.

Notes:
- `npm run test:run` is referenced in the QA plan but is not a script in current `package.json`.

## Release-Metadata Checks

- `package.json` version: `0.4.2`
- `package-lock.json` version: `0.4.2`
- `CHANGELOG.md` contains `## [0.4.2] - 2026-02-18`

## Manual QA Checklist (A–E)

- A/B/C/E require interactive runtime validation and were only partially validated through automated tests + code-path checks in this execution.
- D (config migration) covered by automated tests (`generator-notify` + config generator suite) and passed.

## Overall