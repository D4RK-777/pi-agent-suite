the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

從終端機：

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```

## 建議工作流程

1. `$deep-interview` — 當範圍或邊界仍不清楚時，先用它釐清需求。
2. `$ralplan` — 把釐清後的範圍整理成可核准的架構與實作計畫。
3. `$team` 或 `$ralph` — 需要協調平行執行時用 `$team`，需要單一負責人持續推進到完成並驗證時用 `$ralph`。

## 核心模型

OMX 安裝並串接以下各層：

```text
使用者
  -> Codex CLI
    -> AGENTS.md（編排大腦）
    -> ~/.codex/prompts/*.md（代理提示詞目錄）
    -> ~/.codex/skills/*/SKILL.md（技能目錄）
    -> ~/.codex/config.toml（功能、通知、MCP）
    -> .omx/（執行期狀態、記憶、計畫、日誌）
```

## 主要指令