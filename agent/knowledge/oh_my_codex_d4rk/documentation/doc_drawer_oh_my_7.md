lidate|test (Plugin-Erweiterungs-Workflow)
omx hud ...        # --watch|--json|--preset
omx help
```

## Hooks-Erweiterung (Additive Oberfläche)

OMX enthält jetzt `omx hooks` für Plugin-Gerüstbau und -Validierung.

- `omx tmux-hook` wird weiterhin unterstützt und ist unverändert.
- `omx hooks` ist additiv und ersetzt keine tmux-hook-Workflows.
- Plugin-Dateien befinden sich unter `.omx/hooks/*.mjs`.
- Plugins sind standardmäßig deaktiviert; aktivieren mit `OMX_HOOK_PLUGINS=1`.

Siehe `docs/hooks-extension.md` für den vollständigen Erweiterungs-Workflow und das Ereignismodell.

## Start-Flags

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # nur bei setup
```