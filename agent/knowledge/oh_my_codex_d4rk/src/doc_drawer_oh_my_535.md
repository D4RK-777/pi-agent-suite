OMMANDS.has(command);
}

export type CodexLaunchPolicy = "inside-tmux" | "detached-tmux" | "direct";

export function resolveCodexLaunchPolicy(
  env: NodeJS.ProcessEnv = process.env,
  _platform: NodeJS.Platform = process.platform,
  tmuxAvailable: boolean = isTmuxAvailable(),
  nativeWindows: boolean = isNativeWindows(),
  stdinIsTTY: boolean = Boolean(process.stdin.isTTY),
  stdoutIsTTY: boolean = Boolean(process.stdout.isTTY),
): CodexLaunchPolicy {
  if (env.TMUX) return "inside-tmux";
  if (nativeWindows) return "direct";
  if (!stdinIsTTY || !stdoutIsTTY) return "direct";
  return tmuxAvailable ? "detached-tmux" : "direct";
}

type ExecFileSyncFailure = NodeJS.ErrnoException & {
  status?: number | null;
  signal?: NodeJS.Signals | null;
};