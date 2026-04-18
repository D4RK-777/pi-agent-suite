，並忽略明確的 `--model` / `--config` / `--effort` 覆寫，讓 Claude 使用預設的 `settings.json`。

## `omx setup` 寫入的內容

- `.omx/setup-scope.json`（持久化的設定範圍）
- 依範圍的安裝內容：
  - `user`：`~/.codex/prompts/`、`~/.codex/skills/`、`~/.codex/config.toml`、`~/.omx/agents/`、`~/.codex/AGENTS.md`
  - `project`：`./.codex/prompts/`、`./.codex/skills/`、`./.codex/config.toml`、`./.omx/agents/`、`./AGENTS.md`
- 啟動行為：若持久化範圍為 `project`，`omx` 啟動時自動使用 `CODEX_HOME=./.codex`（除非已設定 `CODEX_HOME`）。
- 啟動指令會合併 `~/.codex/AGENTS.md`（或覆寫後的 `CODEX_HOME/AGENTS.md`）與專案 `./AGENTS.md`，然後再附加執行期 overlay。
- 現有的 `AGENTS.md` 檔案絕不會被靜默覆寫：互動式 TTY 執行時 setup 會先詢問；非互動執行時若沒有 `--force` 就會跳過替換（仍適用活動會話安全檢查）。
- `config.toml` 更新（兩種範圍均適用）：
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`