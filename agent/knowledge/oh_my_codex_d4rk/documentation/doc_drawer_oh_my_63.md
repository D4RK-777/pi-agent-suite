, notifiche, MCP)
    -> .omx/ (stato di esecuzione, memoria, piani, log)
```

## Comandi principali

```bash
omx                # Avvia Codex (+ HUD in tmux se disponibile)
omx setup          # Installa prompt/skill/config per scope + .omx del progetto + AGENTS.md specifico dello scope
omx doctor         # Diagnostica installazione/esecuzione
omx doctor --team  # Diagnostica Team/Swarm
omx team ...       # Avvia/stato/riprendi/arresta i worker del team tmux
omx status         # Mostra le modalità attive
omx cancel         # Annulla le modalità di esecuzione attive
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (workflow estensione plugin)
omx hud ...        # --watch|--json|--preset
omx help
```