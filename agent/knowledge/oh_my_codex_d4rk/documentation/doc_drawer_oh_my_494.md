lback order explicit across env overrides, hydrated cache, packaged artifacts, and repo-local builds

Representative changes:
- `23d1cf5` — feat(release): unify cross-platform native publishing
- `559089f` — ci(release): add packed install smoke gate
- `99ce264` — ci: validate build:full in workflow
- `d12e5f4` — build: add build:full and document full vs TS-only builds
- `7aee91d` — fix(native-assets): soften missing manifest fallback

### Sparkshell is useful both directly and inside team operations

The sparkshell line is not just a hidden backend. It is now part of the operator story.