status from this artifact rather than bypassing the draft review step

## Phase 5: Execution Bridge

Present execution options after artifact generation using explicit handoff contracts. Treat the deep-interview spec as the current requirements source of truth and preserve intent, non-goals, decision boundaries, acceptance criteria, and any residual-risk warnings across the handoff.

### 1. **`$ralplan` (Recommended)**
- **Input Artifact:** `.omx/specs/deep-interview-{slug}.md` (optionally accompanied by the transcript/context snapshot for traceability)
- **Invocation:** `$plan --consensus --direct <spec-path>`