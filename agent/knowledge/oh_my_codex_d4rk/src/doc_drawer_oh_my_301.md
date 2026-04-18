user') return 'user';
    if (arg === '--scope=project') return 'project';
  }
  return undefined;
}

function inferMutationScope(cwd = process.cwd()): AgentScope {
  const persistedScopePath = join(cwd, '.omx', 'setup-scope.json');
  if (existsSync(persistedScopePath)) {
    try {
      const parsed = JSON.parse(readFileSync(persistedScopePath, 'utf8')) as { scope?: string };
      if (parsed.scope === 'project' || parsed.scope === 'project-local') return 'project';
      if (parsed.scope === 'user') return 'user';
    } catch {
      // fall through
    }
  }
  return existsSync(join(cwd, '.codex')) ? 'project' : 'user';
}

function getAgentFilePath(name: string, scope: AgentScope, cwd = process.cwd()): string {
  return join(resolveAgentsDir(scope, cwd), `${name}.toml`);
}