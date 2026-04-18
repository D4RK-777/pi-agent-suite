known facts/evidence
   - constraints
   - unknowns/open questions
   - likely codebase touchpoints
4. If ambiguity remains high, run `explore` first for brownfield facts, then run `$deep-interview --quick <task>` before team launch.

Do not start worker panes until this gate is satisfied; if forced to proceed quickly, state explicit scope/risk limitations in the launch report.

For simple read-only brownfield lookups during intake, follow active session guidance: when `USE_OMX_EXPLORE_CMD` is enabled, prefer `omx explore` with narrow, concrete prompts; otherwise use the richer normal explore path and fall back normally if `omx explore` is unavailable.

## Follow-up Staffing Contract