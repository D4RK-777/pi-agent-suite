alidate|test (workflow d'extension de plugins)
omx hud ...        # --watch|--json|--preset
omx help
```

## Extension Hooks (Surface additive)

OMX inclut désormais `omx hooks` pour l'échafaudage et la validation de plugins.

- `omx tmux-hook` reste supporté et inchangé.
- `omx hooks` est additif et ne remplace pas les workflows tmux-hook.
- Les fichiers de plugins se trouvent dans `.omx/hooks/*.mjs`.
- Les plugins sont désactivés par défaut ; activez-les avec `OMX_HOOK_PLUGINS=1`.

Consultez `docs/hooks-extension.md` pour le workflow d'extension complet et le modèle d'événements.

## Flags de lancement

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # uniquement pour setup
```