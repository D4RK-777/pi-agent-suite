h (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    return null;
  }
}

function escapeShellDoubleQuotedValue(value: string): string {
  return value.replace(/["\\$`]/g, "\\$&");
}

function buildDetachedSessionLeaderCommand(
  sessionName: string,
  codexCmd: string,
): string {
  const cleanupTrap = [
    "status=$?;",
    "trap - 0 INT TERM HUP;",
    `tmux kill-session -t "${escapeShellDoubleQuotedValue(sessionName)}" >/dev/null 2>&1 || true;`,
    "exit $status;",
  ].join(" ");
  const wrapped = [`trap '${cleanupTrap}' 0 INT TERM HUP;`, codexCmd].join(" ");
  return `/bin/sh -lc ${quoteShellArg(wrapped)}`;
}