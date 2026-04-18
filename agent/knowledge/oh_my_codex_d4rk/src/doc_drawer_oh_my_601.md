;
  const hudCmd = nativeWindows
    ? buildWindowsPromptCommand("node", [omxBin, "hud", "--watch"])
    : buildTmuxPaneCommand("node", [omxBin, "hud", "--watch"]);
  const inheritLeaderFlags = process.env[TEAM_INHERIT_LEADER_FLAGS_ENV] !== "0";
  const workerLaunchArgs = resolveTeamWorkerLaunchArgsEnv(
    process.env[TEAM_WORKER_LAUNCH_ARGS_ENV],
    launchArgs,
    inheritLeaderFlags,
    workerDefaultModel,
  );
  const codexBaseEnv = codexHomeOverride
    ? { ...process.env, CODEX_HOME: codexHomeOverride }
    : process.env;
  const codexEnvWithSession = { ...codexBaseEnv, OMX_SESSION_ID: sessionId };
  const codexEnv = workerLaunchArgs
    ? { ...codexEnvWithSession, [TEAM_WORKER_LAUNCH_ARGS_ENV]: workerLaunchArgs }
    : codexEnvWithSession;