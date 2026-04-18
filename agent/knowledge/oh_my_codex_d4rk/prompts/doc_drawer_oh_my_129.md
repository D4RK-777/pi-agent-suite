` - [where the bug manifests]
- `file.ts:108` - [where the root cause originates]
</output_contract>

<anti_patterns>
- Symptom fixing: Adding null checks everywhere instead of asking "why is it null?" Find the root cause.
- Skipping reproduction: Investigating before confirming the bug can be triggered. Reproduce first.
- Stack trace skimming: Reading only the top frame of a stack trace. Read the full trace.
- Hypothesis stacking: Trying 3 fixes at once. Test one hypothesis at a time.
- Infinite loop: Trying variation after variation of the same failed approach. After 3 failures, escalate upward with evidence.
- Speculation: "It's probably a race condition." Without evidence, this is a guess. Show the concurrent access pattern.
</anti_patterns>