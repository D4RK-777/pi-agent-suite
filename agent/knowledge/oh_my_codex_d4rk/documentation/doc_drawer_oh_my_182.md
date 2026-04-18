驗證迴圈，
請在 Team 工作完成後另外執行 `omx ralph ...`。舊的 linked-Ralph 團隊路徑已不再是建議或支援的標準路徑。

團隊工作進程的 Worker CLI 選擇：

```bash
OMX_TEAM_WORKER_CLI=auto    # 預設；當 worker --model 包含 "claude" 時使用 claude
OMX_TEAM_WORKER_CLI=codex   # 強制使用 Codex CLI 工作進程
OMX_TEAM_WORKER_CLI=claude  # 強制使用 Claude CLI 工作進程
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # 每個工作進程的 CLI 混合（長度為 1 或等於工作進程數量）
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # 選用：停用自適應 queue->resend 回退機制
```

注意事項：
- 工作進程啟動參數仍透過 `OMX_TEAM_WORKER_LAUNCH_ARGS` 共享。
- `OMX_TEAM_WORKER_CLI_MAP` 會覆寫 `OMX_TEAM_WORKER_CLI`，以實現每個工作進程的個別選擇。
- 觸發提交預設使用自適應重試（queue/submit，必要時採用安全的清除行 + 重傳回退）。
- 在 Claude 工作進程模式下，OMX 以純 `claude` 啟動工作進程（無額外啟動參數），並忽略明確的 `--model` / `--config` / `--effort` 覆寫，讓 Claude 使用預設的 `settings.json`。

## `omx setup` 寫入的內容