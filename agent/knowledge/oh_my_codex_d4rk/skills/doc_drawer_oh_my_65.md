retrieval, execution, or verification, keep using the relevant tools until the workflow is grounded
- Continue through clear, low-risk, reversible next steps automatically; ask only when the next step is materially branching, destructive, or preference-dependent
</Execution_Policy>

<Steps>
0. **Pre-context Intake (required before Phase 0 starts)**:
   - Derive a task slug from the request.
   - Load the latest relevant snapshot from `.omx/context/{slug}-*.md` when available.
   - If no snapshot exists, create `.omx/context/{slug}-{timestamp}.md` (UTC `YYYYMMDDTHHMMSSZ`) with:
     - Task statement
     - Desired outcome
     - Known facts/evidence
     - Constraints
     - Unknowns/open questions
     - Likely codebase touchpoints