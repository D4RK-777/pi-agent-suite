t -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Operationelle Befehle:

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Wichtige Regel: Fahren Sie nicht herunter, während Aufgaben noch `in_progress` sind, es sei denn, Sie brechen ab.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

Worker-CLI-Auswahl für Team-Worker: