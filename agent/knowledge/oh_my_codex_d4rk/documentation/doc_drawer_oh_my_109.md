ificações, MCP)
    -> .omx/ (estado de execução, memória, planos, logs)
```

## Comandos principais

```bash
omx                # Iniciar Codex (+ HUD no tmux quando disponível)
omx setup          # Instalar prompts/skills/config por escopo + .omx do projeto + AGENTS.md específico do escopo
omx doctor         # Diagnósticos de instalação/execução
omx doctor --team  # Diagnósticos de Team/swarm
omx team ...       # Iniciar/status/retomar/encerrar workers tmux da equipe
omx status         # Mostrar modos ativos
omx cancel         # Cancelar modos de execução ativos
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (fluxo de trabalho de extensão de plugins)
omx hud ...        # --watch|--json|--preset