mx hooks` 是附加的，不会替代 tmux-hook 工作流。
- 插件文件位于 `.omx/hooks/*.mjs`。
- 插件默认关闭；使用 `OMX_HOOK_PLUGINS=1` 启用。

完整的扩展工作流和事件模型请参阅 `docs/hooks-extension.md`。

## 启动标志

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # 仅用于 setup
```

`--madmax` 映射到 Codex `--dangerously-bypass-approvals-and-sandbox`。
仅在可信/外部沙箱环境中使用。

### MCP workingDirectory 策略（可选加固）

默认情况下，MCP state/memory/trace 工具接受调用方提供的 `workingDirectory`。
要限制此行为，请设置允许的根目录列表：

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

设置后，超出这些根目录的 `workingDirectory` 值将被拒绝。

## Codex-First Prompt 控制

默认情况下，OMX 注入：

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

这会将 `CODEX_HOME` 中的 `AGENTS.md` 与项目 `AGENTS.md`（如果存在）合并，然后再附加运行时 overlay。
扩展 Codex 行为，但不会替换/绕过 Codex 核心系统策略。