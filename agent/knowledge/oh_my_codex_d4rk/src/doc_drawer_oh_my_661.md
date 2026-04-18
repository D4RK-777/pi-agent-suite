etectLinuxRuntimeLibc(env);
  if (runtime === 'musl') return ['musl'];
  return ['musl', 'glibc'];
}

function detectLinuxRuntimeLibc(env: NodeJS.ProcessEnv = process.env): NativeLibc | undefined {
  if (process.platform !== 'linux') return undefined;

  const lddProbe = spawnPlatformCommandSync('ldd', ['--version'], { encoding: 'utf-8' }, process.platform, env);
  const lddRuntime = inferRuntimeLibcFromText(`${lddProbe.result.stdout || ''}\n${lddProbe.result.stderr || ''}`);
  if (lddRuntime) return lddRuntime;