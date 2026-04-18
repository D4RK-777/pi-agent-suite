idate|test
omx hooks ...      # init|status|validate|test (flujo de trabajo de extensión de plugins)
omx hud ...        # --watch|--json|--preset
omx help
```

## Extensión de Hooks (Superficie adicional)

OMX ahora incluye `omx hooks` para scaffolding y validación de plugins.

- `omx tmux-hook` sigue siendo compatible y no ha cambiado.
- `omx hooks` es aditivo y no reemplaza los flujos de trabajo de tmux-hook.
- Los archivos de plugins se encuentran en `.omx/hooks/*.mjs`.
- Los plugins están desactivados por defecto; actívalos con `OMX_HOOK_PLUGINS=1`.

Consulta `docs/hooks-extension.md` para el flujo de trabajo completo de extensiones y el modelo de eventos.

## Flags de inicio