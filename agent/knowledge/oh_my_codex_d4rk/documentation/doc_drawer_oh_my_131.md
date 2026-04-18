ение промптами

По умолчанию OMX внедряет:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

Это объединяет `AGENTS.md` из `CODEX_HOME` с проектным `AGENTS.md` (если он есть), а затем добавляет runtime-overlay.
Расширяет поведение Codex, но не заменяет/обходит основные системные политики Codex.

Управление:

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # отключить внедрение AGENTS.md
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## Командный режим

Используйте командный режим для масштабной работы, которая выигрывает от параллельных исполнителей.

Жизненный цикл:

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Операционные команды: