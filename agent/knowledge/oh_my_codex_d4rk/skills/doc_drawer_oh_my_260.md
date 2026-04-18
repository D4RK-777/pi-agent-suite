hy good: Answers its own codebase question first, then asks an informed preference question.
</Good>

<Good>
Single question at a time:
```
Q1: "What's the main goal?"
A1: "Improve performance"
Q2: "For performance, what matters more -- latency or throughput?"
A2: "Latency"
Q3: "For latency, are we optimizing for p50 or p99?"
```
Why good: Each question builds on the previous answer. Focused and progressive.
</Good>

<Bad>
Asking about things you could look up:
```
Planner: "Where is authentication implemented in your codebase?"
User: "Uh, somewhere in src/auth I think?"
```
Why bad: The planner should spawn an explore agent to find this, not ask the user.
</Bad>