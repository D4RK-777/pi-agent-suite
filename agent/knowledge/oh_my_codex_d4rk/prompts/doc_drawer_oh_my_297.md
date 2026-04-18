output.
5) CLEANUP: Kill tmux session, remove artifacts. Always cleanup, even on failure.
</explore>

<execution_loop>
<success_criteria>
- Prerequisites verified before testing (tmux available, ports free, directory exists)
- Each test case has: command sent, expected output, actual output, PASS/FAIL verdict
- All tmux sessions cleaned up after testing (no orphans)
- Evidence captured: actual tmux output for each assertion
- Clear summary: total tests, passed, failed
</success_criteria>