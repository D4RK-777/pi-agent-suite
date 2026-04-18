ILL.md (skill 目录)
    -> ~/.codex/config.toml (功能、通知、MCP)
    -> .omx/ (运行时状态、记忆、计划、日志)
```

## 主要命令

```bash
omx                # 启动 Codex（在 tmux 中附带 HUD）
omx setup          # 按作用域安装 prompt/skill/config + 项目 .omx + 作用域专属 AGENTS.md
omx doctor         # 安装/运行时诊断
omx doctor --team  # Team/swarm 诊断
omx team ...       # 启动/状态/恢复/关闭 tmux 团队 worker
omx status         # 显示活动模式
omx cancel         # 取消活动执行模式
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test（插件扩展工作流）
omx hud ...        # --watch|--json|--preset
omx help
```

## Hooks 扩展（附加表面）

OMX 现在包含用于插件脚手架和验证的 `omx hooks`。

- `omx tmux-hook` 继续支持且未更改。
- `omx hooks` 是附加的，不会替代 tmux-hook 工作流。
- 插件文件位于 `.omx/hooks/*.mjs`。
- 插件默认关闭；使用 `OMX_HOOK_PLUGINS=1` 启用。