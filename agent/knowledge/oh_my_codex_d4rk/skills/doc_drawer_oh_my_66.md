facts/evidence
     - Constraints
     - Unknowns/open questions
     - Likely codebase touchpoints
   - If ambiguity remains high, run `explore` first for brownfield facts, then run `$deep-interview --quick <task>` before proceeding.
   - Carry the snapshot path into autopilot artifacts/state so all phases share grounded context.

1. **Phase 0 - Expansion**: Turn the user's idea into a detailed spec
   - If `.omx/specs/deep-interview-*.md` exists for this task: reuse it and skip redundant expansion work
   - If prompt is highly vague: route to `$deep-interview` for Socratic ambiguity-gated clarification
   - Analyst (THOROUGH tier): Extract requirements
   - Architect (THOROUGH tier): Create technical specification
   - Output: `.omx/plans/autopilot-spec.md`