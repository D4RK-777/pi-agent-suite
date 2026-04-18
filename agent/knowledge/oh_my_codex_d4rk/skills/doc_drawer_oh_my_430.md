`
- **On cancellation/cleanup**:
  run `$cancel` (which should call `state_clear(mode="ultrawork")`)

<Examples>
<Good>
Three independent tasks fired simultaneously:
```
delegate(role="executor", tier="LOW", task="Add missing type export for Config interface")
delegate(role="executor", tier="STANDARD", task="Implement the /api/users endpoint with validation")
delegate(role="test-engineer", tier="STANDARD", task="Add integration tests for the auth middleware")
```
Why good: Independent tasks at appropriate tiers, all fired at once.
</Good>