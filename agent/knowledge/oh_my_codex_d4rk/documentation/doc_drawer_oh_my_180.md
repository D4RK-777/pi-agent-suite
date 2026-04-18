*.mjs`。
- 插件預設關閉；使用 `OMX_HOOK_PLUGINS=1` 啟用。

完整的擴充工作流程與事件模型，請參閱 `docs/hooks-extension.md`。

## 啟動旗標

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # 僅用於 setup
```

`--madmax` 對應 Codex 的 `--dangerously-bypass-approvals-and-sandbox`。
僅在信任環境或外部沙箱環境中使用。

### MCP workingDirectory 策略（選用強化）

預設情況下，MCP 狀態/記憶/追蹤工具接受呼叫方提供的 `workingDirectory`。
若要限制此行為，請設定允許的根目錄清單：

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

設定後，超出這些根目錄的 `workingDirectory` 值將被拒絕。

## Codex 優先的提示詞控制

預設情況下，OMX 注入：

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

這會將 `CODEX_HOME` 中的 `AGENTS.md` 與專案的 `AGENTS.md`（若存在）合併，然後再附加執行期 overlay。
此舉擴充了 Codex 的行為，但不會取代或繞過 Codex 核心系統策略。

控制方式：