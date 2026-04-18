rsionOutput);
  if (!parsed) return true;
  return !semverGte(parsed, TUI_OWNED_BY_CODEX_VERSION);
}

async function promptForAgentsOverwrite(
  destinationPath: string,
): Promise<boolean> {
  if (!process.stdin.isTTY || !process.stdout.isTTY) {
    return false;
  }
  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  try {
    const answer = (
      await rl.question(
        `Overwrite existing AGENTS.md at "${destinationPath}"? [y/N]: `,
      )
    )
      .trim()
      .toLowerCase();
    return answer === "y" || answer === "yes";
  } finally {
    rl.close();
  }
}