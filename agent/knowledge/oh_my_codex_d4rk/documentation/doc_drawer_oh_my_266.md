"--scope|project"
  ```
- [ ] Validate team/tmux health checks:
  ```bash
  omx doctor --team
  ```
- [ ] If using spark worker routing, verify flags are available:
  ```bash
  omx --help | rg "spark|madmax-spark"
  ```

## Related docs

- Release notes: [CHANGELOG.md](../CHANGELOG.md)
- Main overview: [README.md](../README.md)