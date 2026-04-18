n consistency.
- Set `OMX_TEAM_MOUSE=0`, restart session, verify mouse mode is not forcibly enabled.

### D. Config generator migration
- Run setup/generator path on fresh and existing configs.
- Verify `[features]` includes `multi_agent = true` and `child_agents_md = true`.
- Verify deprecated `collab` key is not reintroduced.

### E. `/exit` process termination
- Launch `omx` and invoke `/exit`.
- Verify process exits cleanly without hanging.

## 5) Release Gate

Release is approved only if:
- [ ] Automated tests pass.
- [ ] Manual checklist A–E passes.
- [ ] Changelog entry matches shipped behavior.
- [ ] Version is bumped consistently (`package.json`, `package-lock.json`).