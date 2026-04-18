: parsed.log_level,
    skip_if_scrolling: parsed.skip_if_scrolling === false ? false : true,
  };
}

async function readValidatedConfig(cwd = process.cwd()): Promise<TmuxHookConfig> {
  const configPath = tmuxHookConfigPath(cwd);
  if (!existsSync(configPath)) {
    throw new Error('tmux-hook config missing. Run: omx tmux-hook init');
  }
  const content = await readFile(configPath, 'utf-8');
  return parseConfig(JSON.parse(content));
}

async function loadConfigForCommand(
  commandName: 'status' | 'validate' | 'test',
  cwd = process.cwd(),
): Promise<{ config: TmuxHookConfig; initResult: InitConfigResult | null }> {
  const configPath = tmuxHookConfigPath(cwd);
  let initResult: InitConfigResult | null = null;