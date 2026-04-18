or('remove requires an interactive terminal; rerun with --force in non-interactive environments');
}

async function editNativeAgent(
  name: string,
  options: { cwd?: string; scope?: AgentScope; editor?: string } = {},
): Promise<string> {
  const path = resolveExistingAgentPath(name, options);
  const editor = options.editor ?? process.env.EDITOR ?? process.env.VISUAL ?? 'vi';
  const result = spawnSync(editor, [path], {
    stdio: 'inherit',
    shell: true,
    env: process.env,
  });
  if (result.status !== 0) {
    throw new Error(`editor exited with status ${result.status ?? 'unknown'}`);
  }
  return path;
}