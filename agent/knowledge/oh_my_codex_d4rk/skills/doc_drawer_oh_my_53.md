serve earlier non-conflicting workflow constraints and apply the update locally.

## Execution steps

1. **Identify the analysis type**: Architecture, bug investigation, performance, or dependency analysis
2. **Gather relevant context**: Read or identify the key files involved
3. **Generate hypotheses**: At least 2-3 competing explanations
4. **Route to analyzer**:
   - For simple cases: investigate directly with file reads and reasoning
   - For complex cases: use `$team` with tracer lanes
   - Use `ask_codex` with `agent_role: "architect"` when available
5. **Falsify**: Try to break your own best hypothesis
6. **Return structured findings**: Present with evidence, file references, and actionable recommendations

## Output format

### Observed Result
[What happened]