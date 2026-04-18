d,
    };
  }

  const activePane = detectActivePaneFromList();
  if (activePane) return activePane;

  const sessions = runTmux(['list-sessions', '-F', '#{session_name}']);
  if (sessions.ok && sessions.stdout.trim() !== '') {
    const firstSession = sessions.stdout
      .split('\n')
      .map(line => line.trim())
      .find(Boolean);
    if (firstSession) {
      return {
        target: { type: 'session', value: firstSession },
        sessionName: firstSession,
      };
    }
  }

  return null;
}

async function initTmuxHookConfig(opts?: { silent?: boolean; cwd?: string }): Promise<InitConfigResult> {
  const cwd = opts?.cwd ?? process.cwd();
  const silent = opts?.silent ?? false;
  const configPath = tmuxHookConfigPath(cwd);
  await mkdir(omxDir(cwd), { recursive: true });