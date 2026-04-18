ts, ...userAgents].sort((a, b) => a.name.localeCompare(b.name) || a.scope.localeCompare(b.scope));
}

async function addNativeAgent(
  name: string,
  options: { cwd?: string; scope?: AgentScope; force?: boolean } = {},
): Promise<string> {
  const cwd = options.cwd ?? process.cwd();
  const scope = options.scope ?? inferMutationScope(cwd);
  const normalized = normalizeAgentName(name);
  const path = getAgentFilePath(normalized, scope, cwd);
  if (existsSync(path) && !options.force) {
    throw new Error(`agent already exists: ${path}`);
  }
  await mkdir(resolveAgentsDir(scope, cwd), { recursive: true });
  await writeFile(path, scaffoldAgentToml(normalized));
  return path;
}