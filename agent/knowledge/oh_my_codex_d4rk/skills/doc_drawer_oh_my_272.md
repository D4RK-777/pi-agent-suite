when the next step is materially branching, destructive, or preference-dependent
</Execution_Policy>

<Steps>
0. **Pre-context intake (required before planning/execution loop starts)**:
   - Assemble or load a context snapshot at `.omx/context/{task-slug}-{timestamp}.md` (UTC `YYYYMMDDTHHMMSSZ`).
   - Minimum snapshot fields:
     - task statement
     - desired outcome
     - known facts/evidence
     - constraints
     - unknowns/open questions
     - likely codebase touchpoints
   - If an existing relevant snapshot is available, reuse it and record the path in Ralph state.