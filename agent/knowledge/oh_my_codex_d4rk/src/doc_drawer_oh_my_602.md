...codexEnvWithSession, [TEAM_WORKER_LAUNCH_ARGS_ENV]: workerLaunchArgs }
    : codexEnvWithSession;
  const codexEnvWithNotify = notifyTempContractRaw
    ? { ...codexEnv, [OMX_NOTIFY_TEMP_CONTRACT_ENV]: notifyTempContractRaw }
    : codexEnv;

  const launchPolicy = resolveCodexLaunchPolicy(
    process.env,
    process.platform,
    undefined,
    nativeWindows,
  );

  if (isCodexVersionRequest(launchArgs)) {
    runCodexBlocking(cwd, launchArgs, codexEnvWithNotify);
    return;
  }