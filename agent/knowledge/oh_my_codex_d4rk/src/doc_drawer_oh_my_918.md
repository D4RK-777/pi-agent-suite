ject.entries(paneStatus.recommended_inspect_turn_counts)) {
    if (typeof turnCount === 'number') {
      console.log(`inspect_turn_count_${target}: ${turnCount}`);
    }
  }
  for (const [target, turnsWithoutProgress] of Object.entries(paneStatus.recommended_inspect_turns_without_progress)) {
    if (typeof turnsWithoutProgress === 'number') {
      console.log(`inspect_turns_without_progress_${target}: ${turnsWithoutProgress}`);
    }
  }
  for (const [target, lastTurnAt] of Object.entries(paneStatus.recommended_inspect_last_turn_at)) {
    if (lastTurnAt) {
      console.log(`inspect_last_turn_at_${target}: ${lastTurnAt}`);
    }
  }
  for (const [target, statusUpdatedAt] of Object.entries(paneStatus.recommended_inspect_status_updated_at)) {
    if (statusUpdatedAt) {