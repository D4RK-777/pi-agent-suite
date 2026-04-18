penclaw-integration.it.md)


此頁為英文主文件中 **「Prompt tuning guide (concise + context-aware)」** 章節的在地化版本。

完整整合文件（gateway、hooks、驗證）請參考 [English guide](./openclaw-integration.md)。

## 提示詞調校（精簡 + 情境感知）

## 提示詞模板編輯位置

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## 建議的情境 Token

- 建議固定包含：`{{sessionId}}`、`{{tmuxSession}}`
- 依事件補充：`{{projectName}}`、`{{question}}`、`{{reason}}`

## 詳細度（verbosity）策略

- `minimal`：極短通知
- `session`：精簡的作業情境（建議）
- `verbose`：提供更完整的狀態/動作/風險資訊

## 快速更新指令（jq）

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"