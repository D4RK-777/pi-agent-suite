──────
    await postLaunch(cwd, sessionId, codexHomeOverride, enableNotifyFallbackAuthority);
  }
}

export async function execWithOverlay(args: string[]): Promise<void> {
  const launchCwd = process.cwd();
  const parsedWorktree = parseWorktreeMode(args);
  const notifyTempResult = resolveNotifyTempContract(
    parsedWorktree.remainingArgs,
    process.env,
  );
  const codexHomeOverride = resolveCodexHomeForLaunch(launchCwd, process.env);
  const normalizedArgs = normalizeCodexLaunchArgs(
    notifyTempResult.passthroughArgs,
  );
  let cwd = launchCwd;