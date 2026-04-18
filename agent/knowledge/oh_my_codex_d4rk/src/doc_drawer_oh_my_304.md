catch {
    return {
      scope,
      path,
      file: basename(path),
      name: fallbackName,
      description: '<invalid TOML>',
    };
  }
}

async function readScopeAgents(scope: AgentScope, cwd = process.cwd()): Promise<NativeAgentInfo[]> {
  const dir = resolveAgentsDir(scope, cwd);
  if (!existsSync(dir)) return [];

  const entries = await readdir(dir, { withFileTypes: true });
  const agents: NativeAgentInfo[] = [];
  for (const entry of entries) {
    if (!entry.isFile() || !entry.name.endsWith('.toml')) continue;
    const path = join(dir, entry.name);
    const content = await readFile(path, 'utf8');
    agents.push(parseAgentInfo(content, path, scope));
  }
  return agents.sort((a, b) => a.name.localeCompare(b.name) || a.scope.localeCompare(b.scope));
}