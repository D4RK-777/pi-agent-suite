ration.de.md) | [Français](./openclaw-integration.fr.md) | [Italiano](./openclaw-integration.it.md)


Trang này bản địa hóa mục **“Prompt tuning guide (concise + context-aware)”** từ tài liệu tiếng Anh chính.

Để xem tài liệu tích hợp đầy đủ (gateway, hook, xác minh), hãy xem [English guide](./openclaw-integration.md).

## Tinh chỉnh prompt (ngắn gọn + nhận biết ngữ cảnh)

## Vị trí chỉnh sửa mẫu prompt

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Token ngữ cảnh khuyến nghị