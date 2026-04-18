validate|test (workflow estensione plugin)
omx hud ...        # --watch|--json|--preset
omx help
```

## Estensione Hooks (Superficie additiva)

OMX ora include `omx hooks` per lo scaffolding e la validazione dei plugin.

- `omx tmux-hook` resta supportato e invariato.
- `omx hooks` è additivo e non sostituisce i workflow tmux-hook.
- I file dei plugin si trovano in `.omx/hooks/*.mjs`.
- I plugin sono disattivati per impostazione predefinita; abilitali con `OMX_HOOK_PLUGINS=1`.

Consulta `docs/hooks-extension.md` per il workflow completo di estensione e il modello degli eventi.

## Flag di avvio

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # solo per setup
```