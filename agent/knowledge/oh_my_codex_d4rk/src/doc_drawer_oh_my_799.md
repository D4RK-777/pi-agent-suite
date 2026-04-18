l = repoLocalSparkShellBinaryPath(packageRoot, platform);
  if (exists(repoLocal)) return repoLocal;

  const nestedRepoLocal = nestedRepoLocalSparkShellBinaryPath(packageRoot, platform);
  if (exists(nestedRepoLocal)) return nestedRepoLocal;

  const hydrated = await hydrateNativeBinary('omx-sparkshell', { packageRoot, env, platform, arch });
  if (hydrated) return hydrated;

  throw new Error(
    `[sparkshell] native binary not found. Checked cached/native candidates under ${packageRoot}, ${repoLocal}, and ${nestedRepoLocal}. `
      + `Reconnect to the network so OMX can fetch the release asset, or set ${OMX_SPARKSHELL_BIN_ENV} to override the path.`
  );
}