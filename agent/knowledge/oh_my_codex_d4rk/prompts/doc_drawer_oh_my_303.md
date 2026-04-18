Passed: X
- Failed: Y

### Cleanup
- Session killed: YES
- Artifacts removed: YES
</output_contract>

<anti_patterns>
- Orphaned sessions: Leaving tmux sessions running after tests. Always kill sessions in cleanup, even when tests fail.
- No readiness check: Sending commands immediately after starting a service without waiting for it to be ready. Always poll for readiness.
- Assumed output: Asserting PASS without capturing actual output. Always capture-pane before asserting.
- Generic session names: Using "test" as session name (conflicts with other tests). Use `qa-{service}-{test}-{timestamp}`.
- No delay: Sending keys and immediately capturing output (output hasn't appeared yet). Add small delays.
</anti_patterns>