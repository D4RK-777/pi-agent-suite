nts
   - If an existing relevant snapshot is available, reuse it and record the path in Ralph state.
   - If request ambiguity is high, gather brownfield facts first. When session guidance enables `USE_OMX_EXPLORE_CMD`, prefer `omx explore` for simple read-only repository lookups with narrow, concrete prompts; otherwise use the richer normal explore path. Then run `$deep-interview --quick <task>` to close critical gaps.
   - Do not begin Ralph execution work (delegation, implementation, or verification loops) until snapshot grounding exists. If forced to proceed quickly, note explicit risk tradeoffs.
1. **Review progress**: Check TODO list and any prior iteration state
2. **Continue from where you left off**: Pick up incomplete tasks