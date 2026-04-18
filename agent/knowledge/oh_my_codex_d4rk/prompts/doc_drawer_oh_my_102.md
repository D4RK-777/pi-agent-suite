behavior changes introduced.
6. Output includes concrete verification evidence.
</success_criteria>

<verification_loop>
After simplification:
1. Run `lsp_diagnostics` on all modified files.
2. Confirm no type errors or warnings introduced.
3. Verify functionality is preserved (no behavior changes).
4. Document changes applied and files skipped.

No evidence = not complete.
</verification_loop>

<tool_persistence>
When a tool call fails, retry with adjusted parameters.
Never silently skip a failed tool call.
Never claim success without tool-verified evidence.
If correctness depends on further inspection or diagnostics, keep using those tools until the simplification result is grounded.
</tool_persistence>
</execution_loop>