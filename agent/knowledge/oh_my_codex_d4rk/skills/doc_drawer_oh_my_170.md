script/context snapshot for traceability)
- **Invocation:** `$plan --consensus --direct <spec-path>`
- **Consumer Behavior:** Treat the deep-interview spec as the requirements source of truth. Do not repeat the interview by default; refine architecture/feasibility around the clarified intent and boundaries instead.
- **Skipped / Already-Satisfied Stages:** Requirements discovery, ambiguity clarification, and early intent-boundary elicitation
- **Expected Output:** Canonical planning artifacts under `.omx/plans/`, especially `prd-*.md` and `test-spec-*.md`
- **Best When:** Requirements are clear enough to stop interviewing, but architectural validation / consensus planning is still desirable