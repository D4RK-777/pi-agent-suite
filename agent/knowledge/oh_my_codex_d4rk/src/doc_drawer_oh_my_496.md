ss.arch, env)) {
    if (existsSync(cached)) {
      return { command: cached, args: [] };
    }
  }

  const packaged = resolvePackagedExploreHarnessCommand(packageRoot);
  if (packaged) return packaged;

  const repoBuilt = repoBuiltExploreHarnessCommand(packageRoot);
  if (repoBuilt) return repoBuilt;

  if (!isRepositoryCheckout(packageRoot)) {
    const hydrated = await hydrateNativeBinary('omx-explore-harness', { packageRoot, env });
    if (hydrated) return { command: hydrated, args: [] };
    throw new Error('[explore] no compatible native harness is available for this install. Reconnect to the network so OMX can fetch the release asset, or set OMX_EXPLORE_BIN to a prebuilt harness binary.');
  }

  return resolveExploreHarnessCommand(packageRoot, env);
}