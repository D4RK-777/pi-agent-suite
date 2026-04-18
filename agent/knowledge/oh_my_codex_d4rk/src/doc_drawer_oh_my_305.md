}
  return agents.sort((a, b) => a.name.localeCompare(b.name) || a.scope.localeCompare(b.scope));
}

export async function listNativeAgents(
  cwd = process.cwd(),
  scope?: AgentScope,
): Promise<NativeAgentInfo[]> {
  if (scope) return readScopeAgents(scope, cwd);
  const [projectAgents, userAgents] = await Promise.all([
    readScopeAgents('project', cwd),
    readScopeAgents('user', cwd),
  ]);
  return [...projectAgents, ...userAgents].sort((a, b) => a.name.localeCompare(b.name) || a.scope.localeCompare(b.scope));
}