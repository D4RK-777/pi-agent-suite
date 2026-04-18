codexEnvWithNotify);
  } else {
    // Not in tmux: create a new tmux session with codex + HUD pane
    const codexCmd = buildTmuxPaneCommand("codex", launchArgs);
    const detachedWindowsCodexCmd = nativeWindows
      ? buildWindowsPromptCommand("codex", launchArgs)
      : null;
    const tmuxSessionId = `omx-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
    const sessionName = buildTmuxSessionName(cwd, tmuxSessionId);
    let createdDetachedSession = false;
    let registeredHookTarget: string | null = null;
    let registeredHookName: string | null = null;
    let registeredClientAttachedHookName: string | null = null;
    try {
      const bootstrapSteps = buildDetachedSessionBootstrapSteps(
        sessionName,
        cwd,
        codexCmd,
        hudCmd,