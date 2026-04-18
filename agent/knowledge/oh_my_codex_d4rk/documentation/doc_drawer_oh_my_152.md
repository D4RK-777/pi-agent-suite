EAM_AUTO_INTERRUPT_RETRY=0  # isteğe bağlı: adaptif queue->resend geri dönüşünü devre dışı bırak
```

Notlar:
- Worker başlatma argümanları hâlâ `OMX_TEAM_WORKER_LAUNCH_ARGS` aracılığıyla paylaşılır.
- `OMX_TEAM_WORKER_CLI_MAP`, çalışan başına seçim için `OMX_TEAM_WORKER_CLI`'yi geçersiz kılar.
- Tetikleyici gönderimi varsayılan olarak adaptif yeniden denemeler kullanır (queue/submit, ardından gerektiğinde güvenli clear-line+resend geri dönüşü).
- Claude worker modunda, OMX çalışanları düz `claude` olarak başlatır (ekstra başlatma argümanı yok) ve açık `--model` / `--config` / `--effort` geçersiz kılmalarını yok sayar, böylece Claude varsayılan `settings.json` kullanır.

## `omx setup` Ne Yazar