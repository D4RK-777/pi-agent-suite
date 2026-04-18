Id && leaderPaneId.startsWith("%")) {
    targets.delete(leaderPaneId);
  }
  return [...targets];
}

export async function main(args: string[]): Promise<void> {
  const knownCommands = new Set([
    "launch",
    "exec",
    "setup",
    "agents",
    "agents-init",
    "deepinit",
    "uninstall",
    "doctor",
    "cleanup",
    "ask",
    "autoresearch",
    "explore",
    "sparkshell",
    "team",
    "ralph",
    "session",
    "resume",
    "version",
    "tmux-hook",
    "hooks",
    "hud",
    "status",
    "cancel",
    "help",
    "--help",
    "-h",
  ]);
  const firstArg = args[0];
  const { command, launchArgs } = resolveCliInvocation(args);
  const flags = new Set(args.filter((a) => a.startsWith("--")));
  const options = {
    force: flags.has("--force"),