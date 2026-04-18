cwd), { recursive: true });
  await writeFile(path, scaffoldAgentToml(normalized));
  return path;
}

function resolveExistingAgentPath(
  name: string,
  options: { cwd?: string; scope?: AgentScope } = {},
): string {
  const cwd = options.cwd ?? process.cwd();
  const normalized = normalizeAgentName(name);
  const candidateScopes: AgentScope[] = options.scope ? [options.scope] : ['project', 'user'];
  for (const scope of candidateScopes) {
    const path = getAgentFilePath(normalized, scope, cwd);
    if (existsSync(path)) return path;
  }
  throw new Error(`agent not found: ${normalized}`);
}