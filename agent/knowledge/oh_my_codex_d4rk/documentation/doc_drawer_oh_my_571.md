= "event")]` — the variant name becomes the `"event"` field, remaining fields are flattened inline:

```json
{"event":"AuthorityAcquired","owner":"w1","lease_id":"l1","leased_until":"2026-03-19T02:00:00Z"}
{"event":"AuthorityRenewed","owner":"w1","lease_id":"l2","leased_until":"2026-03-19T03:00:00Z"}
{"event":"DispatchQueued","request_id":"req-1","target":"worker-2"}
{"event":"DispatchNotified","request_id":"req-1","channel":"tmux"}
{"event":"DispatchDelivered","request_id":"req-1"}
{"event":"DispatchFailed","request_id":"req-1","reason":"timeout"}
{"event":"ReplayRequested","cursor":"cursor-1"}
{"event":"SnapshotCaptured"}
```

Snapshot fields are flat JSON at the top level, with nested objects for each section: