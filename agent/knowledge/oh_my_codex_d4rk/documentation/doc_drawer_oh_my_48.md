assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Commandes opérationnelles :

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Règle importante : n'arrêtez pas tant que des tâches sont encore `in_progress`, sauf en cas d'abandon.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

Sélection du CLI worker pour les workers d'équipe :