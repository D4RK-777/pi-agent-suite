---
name: ultrawork
description: Parallel execution engine for high-throughput task completion
---

<Purpose>
Ultrawork is a parallel execution engine that runs multiple agents simultaneously for independent tasks. It is a component, not a standalone persistence mode -- it provides parallelism and smart model routing but not persistence, verification loops, or state management.
</Purpose>

<Use_When>
- Multiple independent tasks can run simultaneously
- User says "ulw", "ultrawork", or wants parallel execution
- You need to delegate work to multiple agents at once
- Task benefits from concurrent execution but the user will manage completion themselves
</Use_When>