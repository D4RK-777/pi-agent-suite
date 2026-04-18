quipo

Usa el modo equipo para trabajo amplio que se beneficia de workers paralelos.

Ciclo de vida:

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Comandos operacionales:

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Regla importante: no apagues mientras las tareas estén en estado `in_progress` a menos que estés abortando.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

Selección de Worker CLI para los workers del equipo: