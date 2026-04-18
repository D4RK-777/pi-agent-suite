ードをキャンセル
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test（プラグイン拡張ワークフロー）
omx hud ...        # --watch|--json|--preset
omx help
```

## Hooks拡張（追加サーフェス）

OMXにはプラグインのスキャフォールディングとバリデーション用の`omx hooks`が含まれるようになりました。

- `omx tmux-hook`は引き続きサポートされ、変更されていません。
- `omx hooks`は追加的であり、tmux-hookワークフローを置き換えません。
- プラグインファイルは`.omx/hooks/*.mjs`に配置されます。
- プラグインはデフォルトで無効です；`OMX_HOOK_PLUGINS=1`で有効にします。

完全な拡張ワークフローとイベントモデルについては`docs/hooks-extension.md`を参照してください。

## 起動フラグ

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # setupのみ
```

`--madmax`はCodexの`--dangerously-bypass-approvals-and-sandbox`にマッピングされます。
信頼された/外部のサンドボックス環境でのみ使用してください。

### MCP workingDirectoryポリシー（オプションの強化）