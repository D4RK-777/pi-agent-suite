*15 non-merge commits** (`2026-03-05` to `2026-03-06`)
- **70 files changed** (`+2,300 / -243`)

---

## Verification summary

Release verification evidence is recorded in `docs/qa/release-readiness-0.8.2.md`.

Release gates for the final `main` release candidate:
- `npm run build`
- `npm test`
- `npm run check:no-unused`
- CLI smoke checks (`--help`, `version`, `status`, `doctor`, `setup --dry-run`, `cancel`)

---

Thanks for using **oh-my-codex**. If anything regresses, please open an issue with reproduction steps, logs, and your CLI/runtime details.