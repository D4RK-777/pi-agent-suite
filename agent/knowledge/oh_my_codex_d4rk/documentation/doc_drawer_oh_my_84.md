し（追加の起動引数なし）、明示的な`--model` / `--config` / `--effort`オーバーライドを無視して、Claudeがデフォルトの`settings.json`を使用します。

## `omx setup`が書き込む内容

- `.omx/setup-scope.json`（永続化されたセットアップスコープ）
- スコープ依存のインストール：
  - `user`：`~/.codex/prompts/`、`~/.codex/skills/`、`~/.codex/config.toml`、`~/.omx/agents/`、`~/.codex/AGENTS.md`
  - `project`：`./.codex/prompts/`、`./.codex/skills/`、`./.codex/config.toml`、`./.omx/agents/`、`./AGENTS.md`
- 起動動作：永続化されたスコープが`project`の場合、`omx`起動時に自動的に`CODEX_HOME=./.codex`を使用（`CODEX_HOME`が既に設定されている場合を除く）。
- 起動命令は`~/.codex/AGENTS.md`（または上書きされた`CODEX_HOME/AGENTS.md`）とプロジェクトの`./AGENTS.md`を結合し、その後ランタイムオーバーレイを追加して使用します。
- 既存の`AGENTS.md`は黙って上書きされません。インタラクティブTTYでは置き換え前に確認し、非インタラクティブ実行では`--force`がない限り置き換えをスキップします（アクティブセッションの安全チェックは引き続き適用されます）。
- `config.toml`の更新（両スコープ共通）：
  - `notify = ["node", "..."]`