nsole.log(`inspect_worker_shutdown_request_path_${target}: ${workerShutdownRequestPath}`);
    }
  }
  for (const [target, workerShutdownAckPath] of Object.entries(paneStatus.recommended_inspect_worker_shutdown_ack_paths)) {
    if (workerShutdownAckPath) {
      console.log(`inspect_worker_shutdown_ack_path_${target}: ${workerShutdownAckPath}`);
    }
  }
  for (const [target, teamDirPath] of Object.entries(paneStatus.recommended_inspect_team_dir_paths)) {
    if (teamDirPath) {
      console.log(`inspect_team_dir_path_${target}: ${teamDirPath}`);
    }
  }
  for (const [target, teamConfigPath] of Object.entries(paneStatus.recommended_inspect_team_config_paths)) {
    if (teamConfigPath) {
      console.log(`inspect_team_config_path_${target}: ${teamConfigPath}`);
    }
  }