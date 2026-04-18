atically; ask only when the next step is materially branching, destructive, or preference-dependent.

You are now in **ULTRAQA** mode - an autonomous QA cycling workflow that runs until your quality goal is met.

**Cycle**: qa-tester → architect verification → fix → repeat

## Goal Parsing

Parse the goal from arguments. Supported formats:

| Invocation | Goal Type | What to Check |
|------------|-----------|---------------|
| `/ultraqa --tests` | tests | All test suites pass |
| `/ultraqa --build` | build | Build succeeds with exit 0 |
| `/ultraqa --lint` | lint | No lint errors |
| `/ultraqa --typecheck` | typecheck | No TypeScript errors |
| `/ultraqa --custom "pattern"` | custom | Custom success pattern in output |