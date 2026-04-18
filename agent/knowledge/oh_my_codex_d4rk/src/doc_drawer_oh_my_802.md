0) === 0) return false;
  return SPARKSHELL_GLIBC_INCOMPATIBLE_PATTERN.test(result.stderr || '');
}

interface SparkShellFallbackInvocation {
  argv: string[];
  kind: 'command' | 'tmux-pane';
}

interface RunSparkShellFallbackOptions {
  announce?: boolean;
}

export function parseSparkShellFallbackInvocation(args: readonly string[]): SparkShellFallbackInvocation {
  if (args.length === 0) {
    throw new Error(`Missing command to run.\n${SPARKSHELL_USAGE}`);
  }

  if (args[0] !== '--tmux-pane' && !args[0]?.startsWith('--tmux-pane=')) {
    return { kind: 'command', argv: [...args] };
  }

  let paneId: string | undefined;
  let tailLines = 200;
  let sawTailLines = false;