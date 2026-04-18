TS.md`, or other root orchestration guidance, keep the orchestration contract mode-driven and terse:

1. **Mode selection comes first.** Distinguish between `$deep-interview`, `$ralplan`, `$team`, and direct solo execution instead of blending them into one generic flow.
2. **Leader and worker responsibilities stay separate.** Leaders choose the mode, own verification, and integrate work; workers execute assigned slices and report blockers upward.
3. **Stop/escalate rules are explicit.** The prompt should say when to stop, when to escalate to the user, and when workers must escalate back to the leader.