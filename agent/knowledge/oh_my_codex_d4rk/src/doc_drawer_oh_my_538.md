rr.status === "number";
  const hasSignal = typeof err.signal === "string" && err.signal.length > 0;

  if (hasExitStatus || hasSignal) {
    return {
      kind: "exit",
      code,
      message,
      exitCode: hasExitStatus
        ? (err.status as number)
        : resolveSignalExitCode(err.signal),
      signal: hasSignal ? (err.signal as NodeJS.Signals) : undefined,
    };
  }

  return {
    kind: "launch-error",
    code,
    message,
  };
}

function runCodexBlocking(
  cwd: string,
  launchArgs: string[],
  codexEnv: NodeJS.ProcessEnv,
): void {
  const { result } = spawnPlatformCommandSync("codex", launchArgs, {
    cwd,
    stdio: "inherit",
    env: codexEnv,
    encoding: "utf-8",
  });