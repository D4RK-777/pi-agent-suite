notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - MCP 服务器条目（`omx_state`、`omx_memory`、`omx_code_intel`、`omx_trace`）
  - `[tui] status_line`
- 作用域专属 `AGENTS.md`
- `.omx/` 运行时目录和 HUD 配置

## 代理和技能

- Prompt：`prompts/*.md`（`user` 安装到 `~/.codex/prompts/`，`project` 安装到 `./.codex/prompts/`）
- Skill：`skills/*/SKILL.md`（`user` 安装到 `~/.codex/skills/`，`project` 安装到 `./.codex/skills/`）

示例：
- 代理：`architect`、`planner`、`executor`、`debugger`、`verifier`、`security-reviewer`
- 技能：`deep-interview`、`ralplan`、`team`、`ralph`、`plan`、`cancel`

## 项目结构