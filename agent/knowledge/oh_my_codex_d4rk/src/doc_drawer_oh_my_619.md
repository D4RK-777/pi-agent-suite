}

function quotePowerShellArg(value: string): string {
  return `'${value.replace(/'/g, "''")}'`;
}

function buildDetachedWindowsBootstrapScript(
  sessionName: string,
  commandText: string,
  delayMs: number = WINDOWS_DETACHED_BOOTSTRAP_DELAY_MS,
): string {
  const delay =
    Number.isFinite(delayMs) && delayMs > 0
      ? Math.floor(delayMs)
      : WINDOWS_DETACHED_BOOTSTRAP_DELAY_MS;
  const targetLiteral = JSON.stringify(`${sessionName}:0.0`);
  const commandLiteral = JSON.stringify(commandText);