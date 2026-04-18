l.
Do not treat ad-hoc pane typing as primary control flow when runtime/state evidence is available.

### Active leader monitoring rule

While a team is **ON/running**, the leader must not go blind. Keep checking live team state until terminal completion.

Minimum acceptable loop:

```bash
sleep 30 && omx team status <team-name>
```

Repeat that check while the team stays active, or use `omx team await <team-name> --timeout-ms 30000 --json` when event-driven waiting is a better fit.

If the leader gets a stale/team-stalled nudge, immediately run `omx team status <team-name>` before taking any manual intervention.

## Message Dispatch Policy (CLI-first, state-first)

To avoid brittle behavior, **message/task delivery must not be driven by ad-hoc tmux typing**.

Required default path: