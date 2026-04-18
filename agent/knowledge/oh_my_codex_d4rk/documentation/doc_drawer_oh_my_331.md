ration.de.md) | [Français](./openclaw-integration.fr.md) | [Italiano](./openclaw-integration.it.md)


Bu sayfa, İngilizce ana belgede yer alan **“Prompt tuning guide (concise + context-aware)”** bölümünün yerelleştirilmiş sürümüdür.

Tam entegrasyon dokümantasyonu (gateway, hook, doğrulama) için [English guide](./openclaw-integration.md) sayfasına bakın.

## Prompt ayarı (kısa + bağlam farkındalıklı)

## Prompt şablonları nerede düzenlenir

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Önerilen bağlam tokenları