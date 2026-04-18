ations, MCP)
    -> .omx/ (état d'exécution, mémoire, plans, journaux)
```

## Commandes principales

```bash
omx                # Lancer Codex (+ HUD dans tmux si disponible)
omx setup          # Installer prompts/skills/config par scope + .omx du projet + AGENTS.md propre au scope
omx doctor         # Diagnostics d'installation/exécution
omx doctor --team  # Diagnostics Team/Swarm
omx team ...       # Démarrer/statut/reprendre/arrêter les workers d'équipe tmux
omx status         # Afficher les modes actifs
omx cancel         # Annuler les modes d'exécution actifs
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (workflow d'extension de plugins)
omx hud ...        # --watch|--json|--preset
omx help