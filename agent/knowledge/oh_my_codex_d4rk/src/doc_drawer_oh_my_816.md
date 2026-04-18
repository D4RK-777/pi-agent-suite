{ ok: false, error: stderr || stdout || `gh exited ${result.status}` };
  }
  return { ok: true };
}

async function askYesNo(question: string): Promise<boolean> {
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  try {
    const answer = (await rl.question(question)).trim().toLowerCase();
    return answer === '' || answer === 'y' || answer === 'yes';
  } finally {
    rl.close();
  }
}

export async function maybePromptGithubStar(deps: MaybePromptGithubStarDeps = {}): Promise<void> {
  const stdinIsTTY = deps.stdinIsTTY ?? process.stdin.isTTY;
  const stdoutIsTTY = deps.stdoutIsTTY ?? process.stdout.isTTY;
  if (!stdinIsTTY || !stdoutIsTTY) return;