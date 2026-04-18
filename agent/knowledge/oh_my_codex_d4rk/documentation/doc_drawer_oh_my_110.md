alidate|test (fluxo de trabalho de extensão de plugins)
omx hud ...        # --watch|--json|--preset
omx help
```

## Extensão de Hooks (Superfície adicional)

OMX agora inclui `omx hooks` para scaffolding e validação de plugins.

- `omx tmux-hook` continua sendo suportado e não foi alterado.
- `omx hooks` é aditivo e não substitui os fluxos de trabalho do tmux-hook.
- Arquivos de plugins ficam em `.omx/hooks/*.mjs`.
- Plugins estão desativados por padrão; ative com `OMX_HOOK_PLUGINS=1`.

Consulte `docs/hooks-extension.md` para o fluxo de trabalho completo de extensões e modelo de eventos.

## Flags de inicialização

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # apenas para setup
```