es(paneStatus.recommended_inspect_team_summary_snapshot_paths)) {
    if (teamSummarySnapshotPath) {
      console.log(`inspect_team_summary_snapshot_path_${target}: ${teamSummarySnapshotPath}`);
    }
  }
  for (const [target, paneId] of Object.entries(paneStatus.recommended_inspect_panes)) {
    if (paneId) {
      console.log(`inspect_pane_${target}: ${paneId}`);
    }
  }
  if (paneStatus.recommended_inspect_command) {
    console.log(`inspect_next: ${paneStatus.recommended_inspect_command}`);
  }
  if (paneStatus.recommended_inspect_summary) {
    console.log(`inspect_summary: ${paneStatus.recommended_inspect_summary}`);
  }
  for (const [index, command] of paneStatus.recommended_inspect_commands.entries()) {
    console.log(`inspect_priority_${index + 1}: ${command}`);
  }