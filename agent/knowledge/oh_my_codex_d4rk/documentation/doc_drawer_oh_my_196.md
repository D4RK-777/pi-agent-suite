），并忽略显式的 `--model` / `--config` / `--effort` 覆盖，使 Claude 使用默认 `settings.json`。

## `omx setup` 写入的内容

- `.omx/setup-scope.json`（持久化的设置作用域）
- 依赖作用域的安装：
  - `user`：`~/.codex/prompts/`、`~/.codex/skills/`、`~/.codex/config.toml`、`~/.omx/agents/`、`~/.codex/AGENTS.md`
  - `project`：`./.codex/prompts/`、`./.codex/skills/`、`./.codex/config.toml`、`./.omx/agents/`、`./AGENTS.md`
- 启动行为：如果持久化的作用域是 `project`，`omx` 启动时自动使用 `CODEX_HOME=./.codex`（除非 `CODEX_HOME` 已设置）。
- 启动指令会合并 `~/.codex/AGENTS.md`（或被覆盖的 `CODEX_HOME/AGENTS.md`）与项目 `./AGENTS.md`，然后附加运行时 overlay。
- 现有 `AGENTS.md` 文件绝不会被静默覆盖：交互式 TTY 下 setup 会先询问是否替换；非交互模式下除非传入 `--force`，否则会跳过替换（活动会话安全检查仍然适用）。
- `config.toml` 更新（两种作用域均适用）：
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`