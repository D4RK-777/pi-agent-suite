ch {
    // ignore invalid persisted scope and fall back to prompt/default
  }
  return undefined;
}

async function promptForSetupScope(
  defaultScope: SetupScope,
): Promise<SetupScope> {
  if (!process.stdin.isTTY || !process.stdout.isTTY) {
    return defaultScope;
  }
  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  try {
    console.log("Select setup scope:");
    console.log(
      `  1) user (default) — installs to ~/.codex (skills default to ~/.codex/skills)`,
    );
    console.log("  2) project — installs to ./.codex (local to project)");
    const answer = (await rl.question("Scope [1-2] (default: 1): "))
      .trim()
      .toLowerCase();
    if (answer === "2" || answer === "project") return "project";
    return defaultScope;