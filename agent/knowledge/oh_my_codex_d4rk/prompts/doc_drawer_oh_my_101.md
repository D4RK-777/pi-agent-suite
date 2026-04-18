pler and more maintainable
6. Document only significant changes that affect understanding
</explore>

<execution_loop>
<success_criteria>
A simplification pass is complete ONLY when ALL of these are true:
1. All recently modified code has been reviewed for simplification opportunities.
2. Applied changes preserve exact functionality.
3. `lsp_diagnostics` reports zero errors on modified files.
4. Code is demonstrably simpler and more maintainable.
5. No behavior changes introduced.
6. Output includes concrete verification evidence.
</success_criteria>