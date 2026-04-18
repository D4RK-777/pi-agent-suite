tchPath) {
      console.log(`inspect_team_dispatch_path_${target}: ${teamDispatchPath}`);
    }
  }
  for (const [target, teamPhasePath] of Object.entries(paneStatus.recommended_inspect_team_phase_paths)) {
    if (teamPhasePath) {
      console.log(`inspect_team_phase_path_${target}: ${teamPhasePath}`);
    }
  }
  for (const [target, teamMonitorSnapshotPath] of Object.entries(paneStatus.recommended_inspect_team_monitor_snapshot_paths)) {
    if (teamMonitorSnapshotPath) {
      console.log(`inspect_team_monitor_snapshot_path_${target}: ${teamMonitorSnapshotPath}`);
    }
  }
  for (const [target, teamSummarySnapshotPath] of Object.entries(paneStatus.recommended_inspect_team_summary_snapshot_paths)) {
    if (teamSummarySnapshotPath) {