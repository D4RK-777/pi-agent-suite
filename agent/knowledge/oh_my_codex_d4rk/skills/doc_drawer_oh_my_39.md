- Diff stays minimal and scoped
   - No new abstractions or dependencies unless explicitly required

6. **Finish with an evidence-dense report**
   - Changed files
   - Simplifications made
   - Tests/diagnostics/build checks run
   - Remaining risks
   - Residual follow-ups or consciously deferred cleanup

## Output Format

```text
AI SLOP CLEANUP REPORT
======================

Scope: [files or feature area]
Behavior Lock: [targeted regression tests added/run]
Cleanup Plan: [bounded smells and order]

Passes Completed:
1. Pass 1: Dead code deletion - [concise fix]
2. Pass 2: Duplicate removal - [concise fix]
3. Pass 3: Naming/error handling cleanup - [concise fix]
4. Pass 4: Test reinforcement - [concise fix]