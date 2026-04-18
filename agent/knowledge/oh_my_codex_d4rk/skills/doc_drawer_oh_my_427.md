)
- Run quick commands (git status, file reads, simple checks) in the foreground
</Execution_Policy>

<Steps>
1. **Read agent reference**: Load `docs/shared/agent-tiers.md` for tier selection
2. **Classify tasks by independence**: Identify which tasks can run in parallel vs which have dependencies
3. **Route to correct tiers**:
   - Simple lookups/definitions: LOW tier
   - Standard implementation: STANDARD tier
   - Complex analysis/refactoring: THOROUGH tier
4. **Fire independent tasks simultaneously**: Launch all parallel-safe tasks at once
5. **Run dependent tasks sequentially**: Wait for prerequisites before launching dependent work
6. **Background long operations**: Builds, installs, and test suites use `run_in_background: true`
7. **Verify when all tasks complete** (lightweight):