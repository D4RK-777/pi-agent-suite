'No running tmux target detected. Update `target.value` when ready.');
    }
  }

  return result;
}

export async function ensureTmuxHookInitialized(cwd = process.cwd()): Promise<void> {
  try {
    await initTmuxHookConfig({ silent: true, cwd });
  } catch {
    // Best-effort only: state tools must remain available even without tmux.
  }
}

async function showTmuxHookStatus(): Promise<void> {
  const cwd = process.cwd();
  const statePath = tmuxHookStatePath(cwd);
  const logPath = tmuxHookLogPath(cwd);