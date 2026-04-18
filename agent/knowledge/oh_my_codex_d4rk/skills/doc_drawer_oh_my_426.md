t is designed as a composable component that ralph and autopilot layer on top of.
</Why_This_Exists>

<Execution_Policy>
- Fire all independent agent calls simultaneously -- never serialize independent work
- Always pass the `model` parameter explicitly when delegating
- Read `docs/shared/agent-tiers.md` before first delegation for agent selection guidance
- Use `run_in_background: true` for operations over ~30 seconds (installs, builds, tests)
- Run quick commands (git status, file reads, simple checks) in the foreground
</Execution_Policy>