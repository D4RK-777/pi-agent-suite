red_leader_notification": false
  },
  "readiness": {
    "ready": true,
    "reasons": []
  }
}
```

## Invariants
- Exactly one semantic authority owner may be active at a time.
- Dispatches must move `pending -> notified -> delivered|failed`.
- Replay state must be durable and deduplicated.
- Readiness is derived from Rust-owned truth, not from JS-side inference.