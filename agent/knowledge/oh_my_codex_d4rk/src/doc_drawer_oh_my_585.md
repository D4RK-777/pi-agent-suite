nupTrap}' 0 INT TERM HUP;`, codexCmd].join(" ");
  return `/bin/sh -lc ${quoteShellArg(wrapped)}`;
}

export function buildDetachedSessionBootstrapSteps(
  sessionName: string,
  cwd: string,
  codexCmd: string,
  hudCmd: string,
  workerLaunchArgs: string | null,
  codexHomeOverride?: string,
  notifyTempContractRaw?: string | null,
  nativeWindows = false,
  sessionId?: string,
): DetachedSessionTmuxStep[] {
  const detachedLeaderCmd = nativeWindows
    ? "powershell.exe"
    : buildDetachedSessionLeaderCommand(sessionName, codexCmd);
  const newSessionArgs: string[] = [
    "new-session",
    "-d",
    "-P",
    "-F",
    "#{pane_id}",
    "-s",
    sessionName,
    "-c",
    cwd,
    ...(workerLaunchArgs
      ? ["-e", `${TEAM_WORKER_LAUNCH_ARGS_ENV}=${workerLaunchArgs}`]
      : []),