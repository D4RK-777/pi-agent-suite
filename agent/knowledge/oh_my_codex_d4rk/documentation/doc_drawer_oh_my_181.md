`AGENTS.md` 與專案的 `AGENTS.md`（若存在）合併，然後再附加執行期 overlay。
此舉擴充了 Codex 的行為，但不會取代或繞過 Codex 核心系統策略。

控制方式：

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # 停用 AGENTS.md 注入
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## 團隊模式

對於能從平行工作進程獲益的大規模工作，請使用團隊模式。

生命週期：

```text
啟動 -> 分配有界通道 -> 監控 -> 驗證終端任務 -> 關閉
```

作業指令：

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

重要規則：除非要中止，否則請勿在任務仍處於 `in_progress` 狀態時關閉。

### Ralph 後續流程

若協調式 Team 執行之後仍需要單一負責人的持續修正 / 驗證迴圈，
請在 Team 工作完成後另外執行 `omx ralph ...`。舊的 linked-Ralph 團隊路徑已不再是建議或支援的標準路徑。

團隊工作進程的 Worker CLI 選擇：