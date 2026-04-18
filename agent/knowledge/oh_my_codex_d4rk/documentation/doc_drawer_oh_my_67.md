start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Comandi operativi:

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Regola importante: non arrestare mentre i task sono ancora `in_progress`, a meno che non si stia abortendo.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

Selezione CLI worker per i worker del team: