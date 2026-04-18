едомления, MCP)
    -> .omx/ (состояние выполнения, память, планы, журналы)
```

## Основные команды

```bash
omx                # Запустить Codex (+ HUD в tmux при наличии)
omx setup          # Установить промпты/навыки/конфиг по области + .omx проекта + AGENTS.md для выбранной области
omx doctor         # Диагностика установки/среды выполнения
omx doctor --team  # Диагностика Team/swarm
omx team ...       # Запуск/статус/возобновление/завершение рабочих tmux
omx status         # Показать активные режимы
omx cancel         # Отменить активные режимы выполнения
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (рабочий процесс расширений плагинов)
omx hud ...        # --watch|--json|--preset
omx help