fects
   - **Missing tests** — behavior not locked, weak regression coverage, gaps around edge cases

4. **Execute passes one smell at a time**
   - **Pass 1: Dead code deletion**
   - **Pass 2: Duplicate removal**
   - **Pass 3: Naming/error handling cleanup**
   - **Pass 4: Test reinforcement**
   - Re-run targeted verification after each pass
   - Avoid bundling unrelated refactors into the same edit set

5. **Run quality gates**
   - Regression tests stay green
   - Lint passes
   - Typecheck passes
   - Relevant unit/integration tests pass
   - Static/security scan passes when available
   - Diff stays minimal and scoped
   - No new abstractions or dependencies unless explicitly required