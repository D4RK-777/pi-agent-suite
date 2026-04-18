throw new Error(`editor exited with status ${result.status ?? 'unknown'}`);
  }
  return path;
}

async function removeNativeAgent(
  name: string,
  options: { cwd?: string; scope?: AgentScope; force?: boolean } = {},
): Promise<string> {
  ensureInteractiveRemove(Boolean(options.force));
  const path = resolveExistingAgentPath(name, options);
  if (!options.force) {
    const confirmed = await confirmRemove(path);
    if (!confirmed) {
      throw new Error('remove aborted by user (pass --force to skip confirmation)');
    }
  }
  await rm(path, { force: true });
  return path;
}

function printAgentsTable(agents: NativeAgentInfo[]): void {
  if (agents.length === 0) {
    console.log('No native agents found.');
    return;
  }