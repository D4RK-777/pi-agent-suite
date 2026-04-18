えをスキップします（アクティブセッションの安全チェックは引き続き適用されます）。
- `config.toml`の更新（両スコープ共通）：
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - MCPサーバーエントリ（`omx_state`、`omx_memory`、`omx_code_intel`、`omx_trace`）
  - `[tui] status_line`
- スコープ別`AGENTS.md`
- `.omx/`ランタイムディレクトリとHUD設定

## エージェントとスキル

- プロンプト：`prompts/*.md`（`user`は`~/.codex/prompts/`に、`project`は`./.codex/prompts/`にインストール）
- スキル：`skills/*/SKILL.md`（`user`は`~/.codex/skills/`に、`project`は`./.codex/skills/`にインストール）

例：
- エージェント：`architect`、`planner`、`executor`、`debugger`、`verifier`、`security-reviewer`
- スキル：`deep-interview`、`ralplan`、`team`、`ralph`、`plan`、`cancel`

## プロジェクト構成