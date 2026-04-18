'--tail-lines='.length), 10);
      if (!Number.isFinite(parsed) || parsed < 100 || parsed > 1000) {
        throw new Error(`--tail-lines must be an integer between 100 and 1000.\n${SPARKSHELL_USAGE}`);
      }
      tailLines = parsed;
      sawTailLines = true;
      continue;
    }
    throw new Error(`tmux pane mode does not accept an additional command.\n${SPARKSHELL_USAGE}`);
  }

  if (!paneId) throw new Error(`--tmux-pane requires a pane id.\n${SPARKSHELL_USAGE}`);
  if (!paneId.trim()) throw new Error(`--tmux-pane requires a pane id.\n${SPARKSHELL_USAGE}`);

  return {
    kind: 'tmux-pane',
    argv: ['tmux', ...buildCapturePaneArgv(paneId, sawTailLines ? tailLines : 200)],
  };
}