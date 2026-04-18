, and the workflow restarts discovery or stops before the missing verification/evidence is gathered.

<Examples>
<Good>
Correct parallel delegation:
```
delegate(role="executor", tier="LOW", task="Add type export for UserConfig")
delegate(role="executor", tier="STANDARD", task="Implement the caching layer for API responses")
delegate(role="executor", tier="THOROUGH", task="Refactor auth module to support OAuth2 flow")
```
Why good: Three independent tasks fired simultaneously at appropriate tiers.
</Good>