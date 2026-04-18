mConfigPath) {
      console.log(`inspect_team_config_path_${target}: ${teamConfigPath}`);
    }
  }
  for (const [target, teamManifestPath] of Object.entries(paneStatus.recommended_inspect_team_manifest_paths)) {
    if (teamManifestPath) {
      console.log(`inspect_team_manifest_path_${target}: ${teamManifestPath}`);
    }
  }
  for (const [target, teamEventsPath] of Object.entries(paneStatus.recommended_inspect_team_events_paths)) {
    if (teamEventsPath) {
      console.log(`inspect_team_events_path_${target}: ${teamEventsPath}`);
    }
  }
  for (const [target, teamDispatchPath] of Object.entries(paneStatus.recommended_inspect_team_dispatch_paths)) {
    if (teamDispatchPath) {
      console.log(`inspect_team_dispatch_path_${target}: ${teamDispatchPath}`);
    }
  }