command")]` — the variant name becomes the `"command"` field, remaining fields are flattened inline:

```json
{"command":"AcquireAuthority","owner":"w1","lease_id":"l1","leased_until":"2026-03-19T02:00:00Z"}
{"command":"RenewAuthority","owner":"w1","lease_id":"l2","leased_until":"2026-03-19T03:00:00Z"}
{"command":"QueueDispatch","request_id":"req-1","target":"worker-2"}
{"command":"MarkNotified","request_id":"req-1","channel":"tmux"}
{"command":"MarkDelivered","request_id":"req-1"}
{"command":"MarkFailed","request_id":"req-1","reason":"timeout"}
{"command":"RequestReplay","cursor":"cursor-1"}
{"command":"CaptureSnapshot"}
```

Events use `#[serde(tag = "event")]` — the variant name becomes the `"event"` field, remaining fields are flattened inline: