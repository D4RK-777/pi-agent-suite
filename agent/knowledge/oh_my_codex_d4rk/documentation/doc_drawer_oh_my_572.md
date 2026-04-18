aptured"}
```

Snapshot fields are flat JSON at the top level, with nested objects for each section:

```json
{
  "schema_version": 1,
  "authority": {
    "owner": "w1",
    "lease_id": "l1",
    "leased_until": "2026-03-19T02:00:00Z",
    "stale": false,
    "stale_reason": null
  },
  "backlog": {
    "pending": 1,
    "notified": 0,
    "delivered": 0,
    "failed": 0
  },
  "replay": {
    "cursor": null,
    "pending_events": 0,
    "last_replayed_event_id": null,
    "deferred_leader_notification": false
  },
  "readiness": {
    "ready": true,
    "reasons": []
  }
}
```