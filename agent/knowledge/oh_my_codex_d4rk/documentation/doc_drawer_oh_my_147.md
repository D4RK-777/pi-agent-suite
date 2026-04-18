tı iş akışı)
omx hud ...        # --watch|--json|--preset
omx help
```

## Hooks Uzantısı (Ek Yüzey)

OMX artık eklenti iskelesi ve doğrulaması için `omx hooks` içerir.

- `omx tmux-hook` desteklenmeye devam eder ve değişmemiştir.
- `omx hooks` ek niteliktedir ve tmux-hook iş akışlarını değiştirmez.
- Eklenti dosyaları `.omx/hooks/*.mjs` konumunda bulunur.
- Eklentiler varsayılan olarak kapalıdır; `OMX_HOOK_PLUGINS=1` ile etkinleştirin.

Tam uzantı iş akışı ve olay modeli için `docs/hooks-extension.md` dosyasına bakın.

## Başlatma Bayrakları

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # yalnızca setup
```

`--madmax`, Codex `--dangerously-bypass-approvals-and-sandbox` ile eşlenir.
Yalnızca güvenilir/harici sandbox ortamlarında kullanın.