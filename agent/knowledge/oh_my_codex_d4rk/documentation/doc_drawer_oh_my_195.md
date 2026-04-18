linked-Ralph shutdown handling is no longer a separate public workflow.

团队 worker 的 Worker CLI 选择：

```bash
OMX_TEAM_WORKER_CLI=auto    # 默认；当 worker --model 包含 "claude" 时使用 claude
OMX_TEAM_WORKER_CLI=codex   # 强制 Codex CLI worker
OMX_TEAM_WORKER_CLI=claude  # 强制 Claude CLI worker
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # 每个 worker 的 CLI 混合（长度=1 或 worker 数量）
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # 可选：禁用自适应 queue->resend 回退
```

注意：
- Worker 启动参数仍通过 `OMX_TEAM_WORKER_LAUNCH_ARGS` 共享。
- `OMX_TEAM_WORKER_CLI_MAP` 覆盖 `OMX_TEAM_WORKER_CLI` 以实现每个 worker 的选择。
- 触发器提交默认使用自适应重试（queue/submit，需要时使用安全的 clear-line+resend 回退）。
- 在 Claude worker 模式下，OMX 以普通 `claude` 启动 worker（无额外启动参数），并忽略显式的 `--model` / `--config` / `--effort` 覆盖，使 Claude 使用默认 `settings.json`。

## `omx setup` 写入的内容