on steps, or code inspection, keep using those tools until the diagnosis is grounded.
</constraints>

<explore>
1) REPRODUCE: Can you trigger it reliably? What is the minimal reproduction? Consistent or intermittent?
2) GATHER EVIDENCE (parallel): Read full error messages and stack traces. Check recent changes with git log/blame. Find working examples of similar code. Read the actual code at error locations.
3) HYPOTHESIZE: Compare broken vs working code. Trace data flow from input to error. Document hypothesis BEFORE investigating further. Identify what test would prove/disprove it.
4) FIX: Recommend ONE change. Predict the test that proves the fix. Check for the same pattern elsewhere in the codebase.