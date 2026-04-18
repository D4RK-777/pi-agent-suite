to the test workspace instead of relying on paths that are only valid in the source checkout layout.

Included changes:
- `scripts/smoke-packed-install.mjs`
- `scripts/__tests__/smoke-packed-install.test.mjs`

Source history:
- hotfix commit: `d86165d` — `fix(release): localize smoke hydration assets`
- merged on `dev` via PR [#806](https://github.com/Yeachan-Heo/oh-my-codex/pull/806)

## Release positioning

- Base feature release remains **Spark Initiative** (`0.9.0`).
- Historical note: **`v0.9.0` remains red** because the release smoke hotfix landed only after that tag.
- Clean superseding release: **`v0.9.1`**.

## Recommended release message

Use language that keeps the historical record accurate: