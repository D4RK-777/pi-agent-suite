t is still under-explained and under-productized is the handoff between planning and team execution.

Today, experienced users can manually infer the pattern: run `ralplan`, then launch `team`, then keep the work alive with `ralph`. But the workflow's biggest advantage is not just parallelism. It is coordinated execution: teammates can surface blockers early, redistribute work, and stay inspectable through panes plus runtime state. That benefit should be reflected directly in planning output.

## Proposed solution
Teach `ralplan` to support an explicit team-oriented follow-up mode, such as `--followup team`, that produces: