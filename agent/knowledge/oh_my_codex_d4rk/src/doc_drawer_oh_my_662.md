dProbe.result.stdout || ''}\n${lddProbe.result.stderr || ''}`);
  if (lddRuntime) return lddRuntime;

  const getconfProbe = spawnPlatformCommandSync('getconf', ['GNU_LIBC_VERSION'], { encoding: 'utf-8' }, process.platform, env);
  const getconfRuntime = inferRuntimeLibcFromText(`${getconfProbe.result.stdout || ''}\n${getconfProbe.result.stderr || ''}`);
  if (getconfRuntime) return getconfRuntime;

  for (const directory of MUSL_LOADER_DIRS) {
    if (!existsSync(directory)) continue;
    try {
      if (readdirSync(directory).some((entry) => MUSL_LOADER_PATTERN.test(entry))) {
        return 'musl';
      }
    } catch {
      // Ignore unreadable loader directories.
    }
  }

  return undefined;
}