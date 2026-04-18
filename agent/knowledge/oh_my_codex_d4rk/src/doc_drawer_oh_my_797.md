cal}, and ${nestedRepoLocal}. `
      + `Set ${OMX_SPARKSHELL_BIN_ENV} to override the path.`
  );
}

export async function resolveSparkShellBinaryPathWithHydration(
  options: ResolveSparkShellBinaryPathOptions = {},
): Promise<string> {
  const {
    cwd = process.cwd(),
    env = process.env,
    packageRoot = getPackageRoot(),
    platform = process.platform,
    arch = osArch(),
    linuxLibcPreference,
    exists = existsSync,
  } = options;

  const override = env[OMX_SPARKSHELL_BIN_ENV]?.trim();
  if (override) {
    return isAbsolute(override) ? override : resolve(cwd, override);
  }