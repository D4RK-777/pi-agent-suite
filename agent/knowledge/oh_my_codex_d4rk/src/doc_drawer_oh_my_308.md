);
    if (existsSync(path)) return path;
  }
  throw new Error(`agent not found: ${normalized}`);
}

async function confirmRemove(path: string): Promise<boolean> {
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  try {
    const answer = (await rl.question(`Delete native agent ${path}? [y/N]: `)).trim().toLowerCase();
    return answer === 'y' || answer === 'yes';
  } finally {
    rl.close();
  }
}

function ensureInteractiveRemove(force: boolean): void {
  if (force) return;
  if (process.stdin.isTTY && process.stdout.isTTY) return;
  throw new Error('remove requires an interactive terminal; rerun with --force in non-interactive environments');
}