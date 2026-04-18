ovals-and-sandbox`にマッピングされます。
信頼された/外部のサンドボックス環境でのみ使用してください。

### MCP workingDirectoryポリシー（オプションの強化）

デフォルトでは、MCP state/memory/traceツールは呼び出し元が提供する`workingDirectory`を受け入れます。
これを制限するには、許可されたルートのリストを設定します：

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

設定すると、これらのルート外の`workingDirectory`値は拒否されます。

## Codex-Firstプロンプト制御

デフォルトでは、OMXは以下を注入します：

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

これは`CODEX_HOME`の`AGENTS.md`とプロジェクトの`AGENTS.md`（存在する場合）を結合し、その上にランタイムオーバーレイを追加します。
Codexの動作を拡張しますが、Codexのコアシステムポリシーを置き換えたりバイパスしたりしません。

制御：

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # AGENTS.md注入を無効化
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## チームモード

並列ワーカーが有利な大規模作業にはチームモードを使用します。

ライフサイクル：