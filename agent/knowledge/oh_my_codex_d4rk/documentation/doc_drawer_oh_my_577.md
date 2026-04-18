me-core/src/engine.rs`) writes the following files via `persist()` and `write_compatibility_view()`:

| File | Written by | Content |
|---|---|---|
| `snapshot.json` | `persist()` | Full `RuntimeSnapshot` — `schema_version`, `authority`, `backlog`, `replay`, `readiness` |
| `events.json` | `persist()` | Append-only event log — array of `RuntimeEvent` values in `#[serde(tag = "event")]` format |
| `authority.json` | `write_compatibility_view()` | `AuthoritySnapshot` section for TS readers |
| `backlog.json` | `write_compatibility_view()` | `BacklogSnapshot` counts (`pending`, `notified`, `delivered`, `failed`) for TS readers |
| `readiness.json` | `write_compatibility_view()` | `ReadinessSnapshot` (`ready`, `reasons`) for TS readers |