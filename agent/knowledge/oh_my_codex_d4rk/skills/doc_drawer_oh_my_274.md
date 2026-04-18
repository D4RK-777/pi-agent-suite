list and any prior iteration state
2. **Continue from where you left off**: Pick up incomplete tasks
3. **Delegate in parallel**: Route tasks to specialist agents at appropriate tiers
   - Simple lookups: LOW tier -- "What does this function return?"
   - Standard work: STANDARD tier -- "Add error handling to this module"
   - Complex analysis: THOROUGH tier -- "Debug this race condition"
   - When Ralph is entered as a ralplan follow-up, start from the approved **available-agent-types roster** and make the delegation plan explicit: implementation lane, evidence/regression lane, and final sign-off lane using only known agent types
4. **Run long operations in background**: Builds, installs, test suites use `run_in_background: true`