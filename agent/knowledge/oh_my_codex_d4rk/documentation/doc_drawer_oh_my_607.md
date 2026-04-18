# PR Draft: Document the `ralplan -> team -> ralph` workflow

## Target branch
`dev`

## Summary
This PR documents one of OMX's strongest high-control workflows: `ralplan -> team -> ralph`. The goal is to make the README explain not only that team mode exists, but why it matters even when `$ultrawork` already provides parallel execution.

The key point is that team mode is not just fanout. It is coordinated, inspectable, runtime-aware execution. Workers can share blocker awareness, execution stays visible through tmux panes plus durable state, and the leader retains stronger control over recovery and lifecycle commands. Pairing that with `ralplan` up front and `ralph` at the back creates a workflow that is both fast and operationally disciplined.