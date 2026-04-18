ageRoot, platform, arch, env, linuxLibcPreference)) {
    if (exists(packaged)) return packaged;
  }

  const repoLocal = repoLocalSparkShellBinaryPath(packageRoot, platform);
  if (exists(repoLocal)) return repoLocal;

  const nestedRepoLocal = nestedRepoLocalSparkShellBinaryPath(packageRoot, platform);
  if (exists(nestedRepoLocal)) return nestedRepoLocal;

  const packagedCandidates = packagedSparkShellBinaryCandidatePaths(packageRoot, platform, arch, env, linuxLibcPreference);
  throw new Error(
    `[sparkshell] native binary not found. Checked ${packagedCandidates.join(', ')}, ${repoLocal}, and ${nestedRepoLocal}. `
      + `Set ${OMX_SPARKSHELL_BIN_ENV} to override the path.`
  );
}