tmux target reachability
  omx tmux-hook test       Run a synthetic notify-hook turn (end-to-end)
`;

export async function tmuxHookCommand(args: string[]): Promise<void> {
  const subcommand = args[0] || 'status';
  switch (subcommand) {
    case 'init':
      await initTmuxHookConfig();
      return;
    case 'status':
      await showTmuxHookStatus();
      return;
    case 'validate':
      await validateTmuxHookConfig();
      return;
    case 'test':
      await testTmuxHook(args.slice(1));
      return;
    case 'help':
    case '--help':
    case '-h':
      console.log(HELP);
      return;
    default:
      throw new Error(`Unknown tmux-hook subcommand: ${subcommand}`);
  }
}

function omxDir(cwd = process.cwd()): string {
  return join(cwd, '.omx');
}