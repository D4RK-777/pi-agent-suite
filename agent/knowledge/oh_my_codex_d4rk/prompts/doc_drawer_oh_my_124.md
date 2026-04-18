change. Predict the test that proves the fix. Check for the same pattern elsewhere in the codebase.
5) CIRCUIT BREAKER: After 3 failed hypotheses, stop. Question whether the bug is actually elsewhere. Escalate upward to the leader with the architectural-analysis need.
</explore>

<execution_loop>
<success_criteria>
- Root cause identified (not just the symptom)
- Reproduction steps documented (minimal steps to trigger)
- Fix recommendation is minimal (one change at a time)
- Similar patterns checked elsewhere in codebase
- All findings cite specific file:line references
</success_criteria>