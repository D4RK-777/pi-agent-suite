ns-path: .../.omx/team/continue-from-clean-commit-810/worktrees/worker-3/AGENTS.md`

Interpretation:

- The test expects the `omx exec` path to always use a generated session-scoped overlay file.
- Inside the active team worker pane, the invocation instead surfaces the worker worktree `AGENTS.md` path.
- This looks like a **test/contract expectation drift for worker-session execution context**, not evidence of a new product regression in the main clean-commit lane.

Evidence excerpt:

```text
expected: /instructions-path:.*\/\.omx\/state\/sessions\/omx-.*\/AGENTS\.md/
actual: fake-codex:exec --model gpt-5 say hi -c model_instructions_file="/home/.../.omx/team/continue-from-clean-commit-810/worktrees/worker-3/AGENTS.md"
```

### 2. `dist/hooks/__tests__/codebase-map.test.js`