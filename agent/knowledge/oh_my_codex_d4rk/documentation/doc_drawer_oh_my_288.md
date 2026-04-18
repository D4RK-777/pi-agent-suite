on.it.md)


このページは英語版ドキュメントの **「Prompt tuning guide (concise + context-aware)」** セクションをローカライズしたものです。

統合全体（gateway / hooks / 検証手順）は [English guide](./openclaw-integration.md) を参照してください。

## プロンプト調整（簡潔 + コンテキスト重視）

## プロンプトテンプレートの編集箇所

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## 推奨コンテキストトークン

- 常時含める: `{{sessionId}}`, `{{tmuxSession}}`
- イベント依存: `{{projectName}}`, `{{question}}`, `{{reason}}`

## 詳細度（verbosity）戦略

- `minimal`: きわめて短い通知
- `session`: 簡潔な運用文脈（推奨）
- `verbose`: 状態・アクション・リスクを詳細化

## クイック更新コマンド（jq）