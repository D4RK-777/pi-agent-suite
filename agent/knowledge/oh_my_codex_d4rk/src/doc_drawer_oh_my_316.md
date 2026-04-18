}

function askUsageError(reason: string): Error {
  return new Error(`${reason}\n${ASK_USAGE}`);
}

function resolveAskPromptsDir(cwd: string, env: NodeJS.ProcessEnv = process.env): string {
  const codexHomeOverride = env.CODEX_HOME?.trim();
  if (codexHomeOverride) {
    return join(codexHomeOverride, 'prompts');
  }

  try {
    const scopePath = join(cwd, '.omx', 'setup-scope.json');
    if (existsSync(scopePath)) {
      const parsed = JSON.parse(readFileSync(scopePath, 'utf-8')) as Partial<{ scope: string }>;
      if (parsed.scope === 'project' || parsed.scope === 'project-local') {
        return join(cwd, '.codex', 'prompts');
      }
    }
  } catch {
    // Ignore malformed persisted scope and fall back to user prompts.
  }

  return codexPromptsDir();
}