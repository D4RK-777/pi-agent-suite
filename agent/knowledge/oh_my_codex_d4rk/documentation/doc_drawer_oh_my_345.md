enclaw-integration.it.md)


此页面是英文主文档中 **“Prompt tuning guide (concise + context-aware)”** 章节的本地化版本。

完整集成文档（gateway、hooks、验证）请参阅 [English guide](./openclaw-integration.md)。

## 提示词调优（简洁 + 上下文感知）

## 提示词模板编辑位置

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## 推荐上下文令牌

- 始终包含：`{{sessionId}}`、`{{tmuxSession}}`
- 按事件选择：`{{projectName}}`、`{{question}}`、`{{reason}}`

## 详细度（verbosity）策略

- `minimal`：超短通知
- `session`：简洁的会话运营上下文（推荐）
- `verbose`：更丰富的状态/动作/风险信息

## 快速更新命令（jq）

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"