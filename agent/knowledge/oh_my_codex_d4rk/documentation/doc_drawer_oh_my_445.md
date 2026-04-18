odel updates
- cleaner test and config semantics

### 3) Setup/install behavior is cleaner and safer

Setup now respects the catalog manifest and current Codex compatibility more strictly:
- installs only `active` / `internal` skills
- canonically ships `configure-notifications`
- skips deprecated / merged / alias entries
- removes stale shipped / legacy notification skill directories during `--force` cleanup
- skips writing the deprecated `[tui]` section when Codex CLI is `>= 0.107.0`

**Why this matters:**
- cleaner installs and upgrades
- fewer stale shipped assets after upgrades
- fewer setup/config issues on newer Codex CLI versions
- lower chance of confusing doctor/setup results

### 4) Patch fixes

Two additional correctness fixes landed in this release: