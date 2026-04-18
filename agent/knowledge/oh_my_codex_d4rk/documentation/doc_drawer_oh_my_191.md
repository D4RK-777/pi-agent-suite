the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

从终端：

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```

## 推荐工作流

1. `$deep-interview` — 当范围或边界还不清楚时，先用它澄清需求。
2. `$ralplan` — 把澄清后的范围整理成可批准的架构与实施计划。
3. `$team` 或 `$ralph` — 需要协调并行执行时用 `$team`，需要单一负责人持续推进到完成并验证时用 `$ralph`。

## 核心模型

OMX 安装并连接以下层：

```text
User
  -> Codex CLI
    -> AGENTS.md (编排大脑)
    -> ~/.codex/prompts/*.md (代理 prompt 目录)
    -> ~/.codex/skills/*/SKILL.md (skill 目录)
    -> ~/.codex/config.toml (功能、通知、MCP)
    -> .omx/ (运行时状态、记忆、计划、日志)
```

## 主要命令