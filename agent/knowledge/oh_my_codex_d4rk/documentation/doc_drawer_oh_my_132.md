rt -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Операционные команды:

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Важное правило: не завершайте работу, пока задачи находятся в состоянии `in_progress`, если только не прерываете выполнение.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

Выбор Worker CLI для рабочих команды: