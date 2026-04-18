ks
   - THOROUGH-tier executor/architect roles: Complex tasks
   - Run independent tasks in parallel

4. **Phase 3 - QA**: Cycle until all tests pass (UltraQA mode)
   - Build, lint, test, fix failures
   - Repeat up to 5 cycles
   - Stop early if the same error repeats 3 times (indicates a fundamental issue)

5. **Phase 4 - Validation**: Multi-perspective review in parallel
   - Architect: Functional completeness
   - Security-reviewer: Vulnerability check
   - Code-reviewer: Quality review
   - All must approve; fix and re-validate on rejection