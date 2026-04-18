tatus|validate|test（插件擴充工作流程）
omx hud ...          # --watch|--json|--preset
omx help
```

Ask 指令範例：

```bash
omx ask claude "review this diff"
omx ask gemini "brainstorm alternatives"
omx ask claude --agent-prompt executor "implement feature X with tests"
omx ask gemini --agent-prompt=planner --prompt "draft a rollout plan"
# 底層供應商 CLI 說明中的旗標：
# claude -p|--print "<prompt>"
# gemini -p|--prompt "<prompt>"
```

非 tmux 團隊啟動（進階）：

```bash
OMX_TEAM_WORKER_LAUNCH_MODE=prompt omx team 2:executor "task"
```

## Hooks 擴充（附加介面）

OMX 現已包含 `omx hooks`，用於插件鷹架建立與驗證。

- `omx tmux-hook` 持續受支援，行為不變。
- `omx hooks` 屬於附加功能，不會取代 tmux-hook 工作流程。
- 插件檔案位於 `.omx/hooks/*.mjs`。
- 插件預設關閉；使用 `OMX_HOOK_PLUGINS=1` 啟用。

完整的擴充工作流程與事件模型，請參閱 `docs/hooks-extension.md`。

## 啟動旗標