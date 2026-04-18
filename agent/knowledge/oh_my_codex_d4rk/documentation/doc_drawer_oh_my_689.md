6d9dd55a78ae9edf192fa36ab8370cb5f2dee4958fc458432429a36000917`

## Semantics extracted from baseline

1. **Iteration semantics**
   - Ralph is an iterative loop with persisted lifecycle state (`iteration`, `max_iterations`, `current_phase`).
   - Iteration progress is updated on each pass and moves between execute/verify/fix phases.

2. **Retry semantics**
   - If verification rejects completion, Ralph keeps running and re-enters fix/verify rather than exiting early.
   - Ralph is explicitly persistence-first (do not stop at partial completion).

3. **Completion semantics**
   - Completion requires fresh verification evidence and explicit architect approval.
   - Terminal success sets `active=false`, `current_phase=complete`, and writes `completed_at`.