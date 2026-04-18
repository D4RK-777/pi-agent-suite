}
  if (firstArg === "launch") {
    return { command: "launch", launchArgs: args.slice(1) };
  }
  if (firstArg === "exec") {
    return { command: "exec", launchArgs: args.slice(1) };
  }
  if (firstArg === "resume") {
    return { command: "resume", launchArgs: args.slice(1) };
  }
  return { command: firstArg, launchArgs: [] };
}

export function resolveNotifyTempContract(
  args: string[],
  env: NodeJS.ProcessEnv = process.env,
): ParseNotifyTempContractResult {
  return parseNotifyTempContractFromArgs(args, env);
}

export function commandOwnsLocalHelp(command: CliCommand): boolean {
  return NESTED_HELP_COMMANDS.has(command);
}

export type CodexLaunchPolicy = "inside-tmux" | "detached-tmux" | "direct";