licit worker-role matches, and falls back to load balancing with lighter-lane bias for blocked work.
- Atomic tasks still fan out into the fixed aspect trio: implement, test, review/document, but each lane now carries an `allocation_reason` for traceability before CLI output strips the internal field.

### Runtime monitoring
- `monitorTeam()` already gathers the signals needed for rebalance decisions: task inventory, lease expiry, worker liveness, worker status, heartbeat turn counts, and verification evidence gaps (`src/team/runtime.ts:1212-1420`).
- The runtime currently turns those signals into recommendations such as:
  - reassign work from dead workers (`src/team/runtime.ts:1288-1294`)
  - remind non-reporting workers (`src/team/runtime.ts:1297-1300`)