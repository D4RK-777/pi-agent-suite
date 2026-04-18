before allowing completion, and using tiered architect review to confirm quality.
</Why_This_Exists>

<Execution_Policy>
- Fire independent agent calls simultaneously -- never wait sequentially for independent work
- Use `run_in_background: true` for long operations (installs, builds, test suites)
- Always pass the `model` parameter explicitly when delegating to agents
- Read `docs/shared/agent-tiers.md` before first delegation to select correct agent tiers
- Deliver the full implementation: no scope reduction, no partial completion, no deleting tests to make them pass
- Default to concise, evidence-dense progress and completion reporting unless the user or risk level requires more detail