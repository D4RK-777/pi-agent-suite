.

## Phase 4: Crystallize Artifacts

When threshold is met (or user exits with warning / hard cap):

1. Write interview transcript summary to:
   - `.omx/interviews/{slug}-{timestamp}.md`  
     (kept for ralph PRD compatibility)
2. Write execution-ready spec to:
   - `.omx/specs/deep-interview-{slug}.md`

Spec should include:
- Metadata (profile, rounds, final ambiguity, threshold, context type)
- Context snapshot reference/path (for ralplan/team reuse)
- Clarity breakdown table
- Intent (why the user wants this)
- Desired Outcome
- In-Scope
- Out-of-Scope / Non-goals
- Decision Boundaries (what OMX may decide without confirmation)
- Constraints
- Testable acceptance criteria
- Assumptions exposed + resolutions
- Pressure-pass findings (which answer was revisited, and what changed)