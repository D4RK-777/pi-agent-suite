## Merged PRs in this release
- #585 — fix(team): seed gemini workers with prompt-interactive launch

### Scope note
- Functional release scope is centered on PR `#585`, the Gemini worker startup hotfix after the `0.8.2` dev release line.
- Release validation also includes a small test-only stabilization in `src/hooks/__tests__/notify-fallback-watcher.test.ts` so the full suite remains reliable under load.
- Final tracked change set for the release branch: `package.json`, `package-lock.json`, `CHANGELOG.md`, and the watcher test hardening.

---

## Verification summary

Release verification evidence is recorded in `docs/qa/release-readiness-0.8.3.md`.