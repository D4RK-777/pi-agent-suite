onfig(s)`,
    );
  }
  if (summary.agentsMdRemoved) {
    console.log(`  ${prefix} AGENTS.md`);
  }
  if (summary.cacheDirectoryRemoved) {
    console.log(`  ${prefix} .omx/ cache directory`);
  }

  const totalActions =
    (summary.configCleaned ? 1 : 0) +
    summary.promptsRemoved +
    summary.skillsRemoved +
    summary.agentConfigsRemoved +
    (summary.agentsMdRemoved ? 1 : 0) +
    (summary.cacheDirectoryRemoved ? 1 : 0);

  if (totalActions === 0) {
    console.log(
      "  Nothing to remove. oh-my-codex does not appear to be installed.",
    );
  }
}

export async function uninstall(options: UninstallOptions = {}): Promise<void> {
  const {
    dryRun = false,
    keepConfig = false,
    verbose = false,
    purge = false,
  } = options;