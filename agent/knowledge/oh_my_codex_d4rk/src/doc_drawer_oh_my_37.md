agent, resolvedModel),
    model: resolvedModel,
    reasoningEffort: agent.reasoningEffort,
  });
}

/**
 * Install prompt-backed native agent config .toml files to ~/.codex/agents/
 * Returns the number of agent files written.
 */
export async function installNativeAgentConfigs(
  pkgRoot: string,
  options: {
    force?: boolean;
    dryRun?: boolean;
    verbose?: boolean;
    agentsDir?: string;
  } = {},
): Promise<number> {
  const {
    force = false,
    dryRun = false,
    verbose = false,
    agentsDir = codexAgentsDir(),
  } = options;
  const codexHomeOverride = join(agentsDir, "..");

  if (!dryRun) {
    await mkdir(agentsDir, { recursive: true });
  }

  let count = 0;