ls/*/SKILL.md（技能目錄）
    -> ~/.codex/config.toml（功能、通知、MCP）
    -> .omx/（執行期狀態、記憶、計畫、日誌）
```

## 主要指令

```bash
omx                  # 啟動 Codex（可用時在 tmux 中附帶 HUD）
omx setup            # 依範圍安裝提示詞/技能/設定 + 專案 .omx + 範圍專屬 AGENTS.md
omx doctor           # 安裝/執行期診斷
omx doctor --team    # 團隊/群集診斷
omx ask ...          # 詢問本地供應商顧問（claude|gemini），結果寫入 .omx/artifacts/*
omx team ...         # 啟動/狀態/恢復/關閉團隊工作進程（預設為互動式 tmux）
omx status           # 顯示目前活動模式
omx cancel           # 取消活動中的執行模式
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...    # init|status|validate|test
omx hooks ...        # init|status|validate|test（插件擴充工作流程）
omx hud ...          # --watch|--json|--preset
omx help
```

Ask 指令範例：