o
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # только для setup
```

`--madmax` соответствует Codex `--dangerously-bypass-approvals-and-sandbox`.
Используйте только в доверенных/внешних sandbox-окружениях.

### Политика workingDirectory MCP (опциональное усиление)

По умолчанию инструменты MCP state/memory/trace принимают `workingDirectory`, предоставленный вызывающей стороной.
Чтобы ограничить это, задайте список разрешённых корней:

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

При установке значения `workingDirectory` за пределами этих корней будут отклонены.

## Codex-First управление промптами

По умолчанию OMX внедряет:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```