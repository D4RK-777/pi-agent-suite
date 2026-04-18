dirimler, MCP)
    -> .omx/ (çalışma zamanı durumu, bellek, planlar, günlükler)
```

## Ana Komutlar

```bash
omx                # Codex'i başlat (tmux'ta HUD ile birlikte)
omx setup          # Prompt/skill/config'i kapsama göre kur + proje .omx + kapsama özel AGENTS.md
omx doctor         # Kurulum/çalışma zamanı tanılamaları
omx doctor --team  # Team/swarm tanılamaları
omx team ...       # tmux takım çalışanlarını başlat/durum/devam et/kapat
omx status         # Aktif modları göster
omx cancel         # Aktif çalışma modlarını iptal et
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (eklenti uzantı iş akışı)
omx hud ...        # --watch|--json|--preset
omx help
```

## Hooks Uzantısı (Ek Yüzey)