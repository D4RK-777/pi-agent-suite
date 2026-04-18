y`, `slug`, `launchReady`, and `blockedReasons` fields so `omx autoresearch` can consume it directly
- **Confirmation bridge:** after artifact generation, offer at least `refine further` and `launch`; do not launch detached tmux until the user explicitly confirms `launch`
- **Handoff rule:** downstream execution must preserve the clarified mission intent, evaluator expectations, decision boundaries, and launch-readiness status from this artifact rather than bypassing the draft review step

## Phase 5: Execution Bridge