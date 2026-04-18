E/AGENTS.md`, если путь переопределён) с проектным `./AGENTS.md`, а затем добавляют runtime-overlay.
- Существующие файлы `AGENTS.md` никогда не перезаписываются молча: в интерактивном TTY setup спрашивает перед заменой, а в неинтерактивном режиме пропускает замену без `--force` (проверки безопасности активных сессий остаются в силе).
- Обновления `config.toml` (для обеих областей):
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - Записи MCP-серверов (`omx_state`, `omx_memory`, `omx_code_intel`, `omx_trace`)
  - `[tui] status_line`
- `AGENTS.md` для выбранной области
- Директории `.omx/` и конфигурация HUD

## Агенты и навыки