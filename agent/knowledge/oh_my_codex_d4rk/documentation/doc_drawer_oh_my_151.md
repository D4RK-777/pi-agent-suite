hutdown handling is no longer a separate public workflow.

Takım çalışanları için Worker CLI seçimi:

```bash
OMX_TEAM_WORKER_CLI=auto    # varsayılan; worker --model "claude" içeriyorsa claude kullanır
OMX_TEAM_WORKER_CLI=codex   # Codex CLI çalışanlarını zorla
OMX_TEAM_WORKER_CLI=claude  # Claude CLI çalışanlarını zorla
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # çalışan başına CLI karışımı (uzunluk=1 veya çalışan sayısı)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # isteğe bağlı: adaptif queue->resend geri dönüşünü devre dışı bırak
```