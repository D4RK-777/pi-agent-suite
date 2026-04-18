(`src/team/runtime.ts:1288-1294`)
  - remind non-reporting workers (`src/team/runtime.ts:1297-1300`)
  - surface missing PASS/FAIL verification evidence (`src/team/runtime.ts:1313-1321`)
  - note reclaimed expired claims (`src/team/runtime.ts:1343-1345`)
- `assignTask()` remains the claim + dispatch gateway, including approval checks and post-claim rollback when worker notification fails (`src/team/runtime.ts:1426-1527`).