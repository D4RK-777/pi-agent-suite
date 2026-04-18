es, MCP)
    -> .omx/ (estado en ejecución, memoria, planes, registros)
```

## Comandos principales

```bash
omx                # Lanzar Codex (+ HUD en tmux cuando está disponible)
omx setup          # Instalar prompts/skills/config por alcance + .omx del proyecto + AGENTS.md específico del alcance
omx doctor         # Diagnósticos de instalación/ejecución
omx doctor --team  # Diagnósticos de Team/swarm
omx team ...       # Iniciar/estado/reanudar/apagar workers tmux del equipo
omx status         # Mostrar modos activos
omx cancel         # Cancelar modos de ejecución activos
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (flujo de trabajo de extensión de plugins)