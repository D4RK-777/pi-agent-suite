p candidates
   - If behavior is currently untested, create the narrowest test coverage needed first

2. **Create a cleanup plan before code**
   - List the specific smells to remove
   - Bound the pass to the requested files/scope
   - If a file list scope is provided, keep the pass restricted to that changed-files list
   - Order fixes from safest/highest-signal to riskiest
   - Do not start coding until the cleanup plan is explicit