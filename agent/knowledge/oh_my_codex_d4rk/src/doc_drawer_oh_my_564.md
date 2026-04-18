sole.error(
      `[omx] preLaunch warning: ${err instanceof Error ? err.message : err}`,
    );
  }

  try {
    const notifyTempContractRaw = notifyTempResult.contract.active
      ? serializeNotifyTempContract(notifyTempResult.contract)
      : null;
    const codexArgs = injectModelInstructionsBypassArgs(
      cwd,
      ["exec", ...normalizedArgs],
      process.env,
      sessionModelInstructionsPath(cwd, sessionId),
    );
    const codexEnvBase = codexHomeOverride
      ? { ...process.env, CODEX_HOME: codexHomeOverride }
      : process.env;
    const codexEnv = notifyTempContractRaw
      ? {
          ...codexEnvBase,
          [OMX_NOTIFY_TEMP_CONTRACT_ENV]: notifyTempContractRaw,
        }
      : codexEnvBase;
    runCodexBlocking(cwd, codexArgs, codexEnv);
  } finally {