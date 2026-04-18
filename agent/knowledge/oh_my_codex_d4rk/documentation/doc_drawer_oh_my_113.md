t -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Comandos operacionais:

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Regra importante: não encerre enquanto tarefas estiverem em estado `in_progress`, a menos que esteja abortando.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

Seleção de Worker CLI para workers da equipe: