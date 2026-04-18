known facts/evidence
   - constraints
   - unknowns/open questions
   - likely codebase touchpoints
4. If ambiguity remains high, gather brownfield facts first. When session guidance enables `USE_OMX_EXPLORE_CMD`, prefer `omx explore` for simple read-only repository lookups with narrow, concrete prompts; otherwise use the richer normal explore path. Then run `$deep-interview --quick <task>` before continuing.

Do not hand off to execution modes until this intake is complete; if urgency forces progress, explicitly document the risk tradeoffs.

## Pre-Execution Gate

### Why the Gate Exists