.toLowerCase();
    return answer === "y" || answer === "yes";
  } finally {
    rl.close();
  }
}

async function resolveSetupScope(
  projectRoot: string,
  requestedScope?: SetupScope,
): Promise<ResolvedSetupScope> {
  if (requestedScope) {
    return { scope: requestedScope, source: "cli" };
  }
  const persisted = await readPersistedSetupPreferences(projectRoot);
  if (persisted?.scope) {
    return { scope: persisted.scope, source: "persisted" };
  }
  if (process.stdin.isTTY && process.stdout.isTTY) {
    const scope = await promptForSetupScope(DEFAULT_SETUP_SCOPE);
    return { scope, source: "prompt" };
  }
  return { scope: DEFAULT_SETUP_SCOPE, source: "default" };
}