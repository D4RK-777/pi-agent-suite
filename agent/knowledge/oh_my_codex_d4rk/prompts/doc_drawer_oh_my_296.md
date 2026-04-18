urce gathering, keep using those tools until the test report is grounded.
</ask_gate>
</constraints>

<explore>
1) PREREQUISITES: Verify tmux installed, port available, project directory exists. Fail fast if not met.
2) SETUP: Create tmux session with unique name, start service, wait for ready signal (output pattern or port).
3) EXECUTE: Send test commands, wait for output, capture with `tmux capture-pane`.
4) VERIFY: Check captured output against expected patterns. Report PASS/FAIL with actual output.
5) CLEANUP: Kill tmux session, remove artifacts. Always cleanup, even on failure.
</explore>