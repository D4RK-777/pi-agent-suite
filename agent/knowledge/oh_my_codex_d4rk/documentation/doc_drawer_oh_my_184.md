notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - MCP 伺服器項目（`omx_state`、`omx_memory`、`omx_code_intel`、`omx_trace`）
  - `[tui] status_line`
- 範圍專屬 `AGENTS.md`
- `.omx/` 執行期目錄與 HUD 設定

## 代理與技能

- 提示詞：`prompts/*.md`（`user` 安裝至 `~/.codex/prompts/`，`project` 安裝至 `./.codex/prompts/`）
- 技能：`skills/*/SKILL.md`（`user` 安裝至 `~/.codex/skills/`，`project` 安裝至 `./.codex/skills/`）

範例：
- 代理：`architect`、`planner`、`executor`、`debugger`、`verifier`、`security-reviewer`
- 技能：`deep-interview`、`ralplan`、`team`、`ralph`、`plan`、`cancel`

### 視覺品管迴圈（`$visual-verdict`）

當任務需要視覺保真度驗證（參考圖片 + 生成截圖）時，請使用 `$visual-verdict`。