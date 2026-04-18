ess.cwd()): string {
  return scope === 'project' ? projectCodexAgentsDir(cwd) : codexAgentsDir();
}

function parseScopeArg(args: string[]): AgentScope | undefined {
  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];
    if (arg === '--scope') {
      const value = args[i + 1];
      if (value === 'user' || value === 'project') return value;
      throw new Error('Expected --scope user|project');
    }
    if (arg === '--scope=user') return 'user';
    if (arg === '--scope=project') return 'project';
  }
  return undefined;
}