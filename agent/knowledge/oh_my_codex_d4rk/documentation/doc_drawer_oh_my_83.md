gacy linked-Ralph shutdown handling is no longer a separate public workflow.

チームワーカー用のWorker CLI選択：

```bash
OMX_TEAM_WORKER_CLI=auto    # デフォルト；worker --modelに"claude"が含まれる場合claudeを使用
OMX_TEAM_WORKER_CLI=codex   # Codex CLIワーカーを強制
OMX_TEAM_WORKER_CLI=claude  # Claude CLIワーカーを強制
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # ワーカーごとのCLIミックス（長さ=1またはワーカー数）
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # オプション：適応型queue->resendフォールバックを無効化
```

注意：
- ワーカー起動引数は引き続き`OMX_TEAM_WORKER_LAUNCH_ARGS`を通じて共有されます。
- `OMX_TEAM_WORKER_CLI_MAP`はワーカーごとの選択で`OMX_TEAM_WORKER_CLI`をオーバーライドします。
- トリガー送信はデフォルトで適応型リトライを使用します（queue/submit、必要に応じて安全なclear-line+resendフォールバック）。
- Claude workerモードでは、OMXはワーカーをプレーンな`claude`として起動し（追加の起動引数なし）、明示的な`--model` / `--config` / `--effort`オーバーライドを無視して、Claudeがデフォルトの`settings.json`を使用します。