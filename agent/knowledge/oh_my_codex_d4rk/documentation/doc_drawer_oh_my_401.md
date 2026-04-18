thin cooldown window: verify no duplicate notification spam.
- Verify event/log entries are emitted.

### B. Auto-nudge pattern detection
- Feed outputs containing new phrases (e.g., "say go", "next I can", "keep driving").
- Verify stall detection triggers in the last-lines hot zone.
- Verify unrelated text does not false-trigger.

### C. Tmux input reliability + mouse scrolling
- In team mode, verify mouse wheel scrolls pane history.
- Confirm arrow keys still work for CLI input history.
- Send repeated worker prompts and verify submission consistency.
- Set `OMX_TEAM_MOUSE=0`, restart session, verify mouse mode is not forcibly enabled.