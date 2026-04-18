h (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }
}

/**
 * runCodex: Launch Codex CLI (blocks until exit).
 * All 3 paths (new tmux, existing tmux, no tmux) block via execSync/execFileSync.
 */
function runCodex(
  cwd: string,
  args: string[],
  sessionId: string,
  workerDefaultModel?: string,
  codexHomeOverride?: string,
  notifyTempContractRaw?: string | null,
): void {
  const launchArgs = injectModelInstructionsBypassArgs(
    cwd,
    args,
    process.env,
    sessionModelInstructionsPath(cwd, sessionId),
  );
  const nativeWindows = isNativeWindows();
  const omxBin = process.argv[1];
  const hudCmd = nativeWindows
    ? buildWindowsPromptCommand("node", [omxBin, "hud", "--watch"])