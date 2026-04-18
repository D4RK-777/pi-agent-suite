ew Error('tmux is required for background autoresearch execution. Install tmux and try again.');
  }

  const sessionName = `omx-autoresearch-${slug}`;
  const hasSession = spawnSync('tmux', ['has-session', '-t', sessionName], { stdio: 'pipe',
      windowsHide: true,
    });
  if (hasSession.status === 0) {
    throw new Error(
      `tmux session "${sessionName}" already exists.\n`
      + `  Attach: tmux attach -t ${sessionName}\n`
      + `  Kill:   tmux kill-session -t ${sessionName}`,
    );
  }

  const omxPath = resolve(join(__dirname, '..', '..', 'bin', 'omx.js'));
  const cmd = `${shellQuote(process.execPath)} ${shellQuote(omxPath)} autoresearch ${shellQuote(missionDir)}`;