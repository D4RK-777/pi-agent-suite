on native Windows${stderr ? ` (${stderr})` : ""}. Continuing without tmux/HUD.`,
      );
    }
  }

  const launchCwd = process.cwd();
  const parsedWorktree = parseWorktreeMode(args);
  const notifyTempResult = resolveNotifyTempContract(
    parsedWorktree.remainingArgs,
    process.env,
  );
  const codexHomeOverride = resolveCodexHomeForLaunch(launchCwd, process.env);
  const launchPolicy = resolveCodexLaunchPolicy(
    process.env,
    process.platform,
    undefined,
    isNativeWindows(),
  );
  const enableNotifyFallbackAuthority = launchPolicy === "direct";
  const workerSparkModel = resolveWorkerSparkModel(
    notifyTempResult.passthroughArgs,
    codexHomeOverride,
  );
  const normalizedArgs = normalizeCodexLaunchArgs(
    notifyTempResult.passthroughArgs,
  );