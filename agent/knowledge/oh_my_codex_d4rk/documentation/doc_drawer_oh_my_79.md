みプランを並列で進めるなら `$team`、1 人の担当者が完了と検証まで粘り強く進めるなら `$ralph` を使います。

## コアモデル

OMXは以下のレイヤーをインストールして接続します：

```text
User
  -> Codex CLI
    -> AGENTS.md (オーケストレーションブレイン)
    -> ~/.codex/prompts/*.md (エージェントプロンプトカタログ)
    -> ~/.codex/skills/*/SKILL.md (スキルカタログ)
    -> ~/.codex/config.toml (機能、通知、MCP)
    -> .omx/ (ランタイム状態、メモリ、計画、ログ)
```

## 主要コマンド

```bash
omx                # Codexを起動（tmuxでHUD付き）
omx setup          # スコープ別にプロンプト/スキル/設定をインストール + プロジェクト .omx + スコープ別 AGENTS.md
omx doctor         # インストール/ランタイム診断
omx doctor --team  # Team/swarm診断
omx team ...       # tmuxチームワーカーの開始/ステータス/再開/シャットダウン
omx status         # アクティブなモードを表示
omx cancel         # アクティブな実行モードをキャンセル
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test