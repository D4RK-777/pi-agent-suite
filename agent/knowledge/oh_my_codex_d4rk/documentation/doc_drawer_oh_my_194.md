EX_HOME` 中的 `AGENTS.md` 与项目 `AGENTS.md`（如果存在）合并，然后再附加运行时 overlay。
扩展 Codex 行为，但不会替换/绕过 Codex 核心系统策略。

控制：

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # 禁用 AGENTS.md 注入
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## 团队模式

对于受益于并行 worker 的大规模工作，使用团队模式。

生命周期：

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

操作命令：

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

重要规则：除非中止，否则不要在任务仍处于 `in_progress` 状态时关闭。

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

团队 worker 的 Worker CLI 选择：