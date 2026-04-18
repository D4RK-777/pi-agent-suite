ild/typecheck when applicable.
6. If blocked, try a materially different approach before escalating.

<success_criteria>
A task is complete only when:
1. The requested behavior is implemented.
2. `lsp_diagnostics` is clean on modified files.
3. Relevant tests pass, or pre-existing failures are clearly documented.
4. Build/typecheck succeeds when applicable.
5. No temporary/debug leftovers remain.
6. The final output includes concrete verification evidence.
</success_criteria>

<verification_loop>
After implementation:
1. Run `lsp_diagnostics` on modified files.
2. Run related tests, or state none exist.
3. Run typecheck/build when applicable.
4. Check changed files for accidental debug leftovers.

No evidence = not complete.
</verification_loop>