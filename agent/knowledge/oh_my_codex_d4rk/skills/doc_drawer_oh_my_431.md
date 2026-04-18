e auth middleware")
```
Why good: Independent tasks at appropriate tiers, all fired at once.
</Good>

<Good>
Correct use of background execution:
```
delegate(role="executor", tier="STANDARD", task="npm install && npm run build", run_in_background=true)
delegate(role="writer", tier="LOW", task="Update the README with new API endpoints")
```
Why good: Long build runs in background while short task runs in foreground.
</Good>

<Bad>
Sequential execution of independent work:
```
result1 = delegate(executor, LOW, "Add type export")  # wait...
result2 = delegate(executor, STANDARD, "Implement endpoint")     # wait...
result3 = delegate(test-engineer, STANDARD, "Add tests")              # wait...
```
Why bad: These tasks are independent. Running them sequentially wastes time.
</Bad>