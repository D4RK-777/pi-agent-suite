${subcommand}`);
  }
}

function omxDir(cwd = process.cwd()): string {
  return join(cwd, '.omx');
}

function tmuxHookConfigPath(cwd = process.cwd()): string {
  return join(omxDir(cwd), 'tmux-hook.json');
}

function tmuxHookStatePath(cwd = process.cwd()): string {
  return join(omxDir(cwd), 'state', 'tmux-hook-state.json');
}

function tmuxHookLogPath(cwd = process.cwd()): string {
  return join(omxDir(cwd), 'logs', `tmux-hook-${new Date().toISOString().split('T')[0]}.jsonl`);
}