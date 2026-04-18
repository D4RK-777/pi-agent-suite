..args] };
  }

  let paneId: string | undefined;
  let tailLines = 200;
  let sawTailLines = false;

  for (let index = 0; index < args.length; index += 1) {
    const token = args[index];
    if (token === '--tmux-pane') {
      const next = args[index + 1];
      if (!next || next.startsWith('-')) throw new Error(`--tmux-pane requires a pane id.\n${SPARKSHELL_USAGE}`);
      paneId = next;
      index += 1;
      continue;
    }
    if (token.startsWith('--tmux-pane=')) {
      const value = token.slice('--tmux-pane='.length).trim();
      if (!value) throw new Error(`--tmux-pane requires a pane id.\n${SPARKSHELL_USAGE}`);
      paneId = value;
      continue;
    }
    if (token === '--tail-lines') {
      const next = args[index + 1];