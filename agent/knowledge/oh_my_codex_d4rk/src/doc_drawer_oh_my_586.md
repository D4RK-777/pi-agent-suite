.(workerLaunchArgs
      ? ["-e", `${TEAM_WORKER_LAUNCH_ARGS_ENV}=${workerLaunchArgs}`]
      : []),
    ...(sessionId ? ["-e", `OMX_SESSION_ID=${sessionId}`] : []),
    ...(codexHomeOverride ? ["-e", `CODEX_HOME=${codexHomeOverride}`] : []),
    ...(notifyTempContractRaw
      ? ["-e", `${OMX_NOTIFY_TEMP_CONTRACT_ENV}=${notifyTempContractRaw}`]
      : []),
    detachedLeaderCmd,
  ];
  const splitCaptureArgs: string[] = [
    "split-window",
    "-v",
    "-l",
    String(HUD_TMUX_HEIGHT_LINES),
    "-d",
    "-t",
    sessionName,
    "-c",
    cwd,
    "-P",
    "-F",
    "#{pane_id}",
    hudCmd,
  ];
  return [
    { name: "new-session", args: newSessionArgs },
    { name: "split-and-capture-hud-pane", args: splitCaptureArgs },
  ];
}