icit opt-in and captures a larger pane tail before applying raw-vs-summary behavior.',
].join('\n');

export interface ResolveSparkShellBinaryPathOptions {
  cwd?: string;
  env?: NodeJS.ProcessEnv;
  packageRoot?: string;
  platform?: NodeJS.Platform;
  arch?: string;
  linuxLibcPreference?: readonly ('musl' | 'glibc')[];
  exists?: (path: string) => boolean;
}

export interface RunSparkShellBinaryOptions {
  cwd?: string;
  env?: NodeJS.ProcessEnv;
  spawnImpl?: typeof spawnSync;
}

function resolveSignalExitCode(signal: NodeJS.Signals | null): number {
  if (!signal) return 1;
  const signalNumber = osConstants.signals[signal];
  if (typeof signalNumber === 'number' && Number.isFinite(signalNumber)) {
    return 128 + signalNumber;
  }
  return 1;
}