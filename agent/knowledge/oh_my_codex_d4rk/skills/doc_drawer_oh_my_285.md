bad: Uses "should" and "look good" -- no fresh test/build output, no architect verification.
</Bad>

<Bad>
Sequential execution of independent tasks:
```
delegate(executor, LOW, "Add type export") → wait →
delegate(executor, STANDARD, "Implement caching") → wait →
delegate(executor, THOROUGH, "Refactor auth")
```
Why bad: These are independent tasks that should run in parallel, not sequentially.
</Bad>
</Examples>