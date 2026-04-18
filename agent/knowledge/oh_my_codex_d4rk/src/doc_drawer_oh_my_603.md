ionRequest(launchArgs)) {
    runCodexBlocking(cwd, launchArgs, codexEnvWithNotify);
    return;
  }

  if (launchPolicy === "inside-tmux") {
    // Already in tmux: launch codex in current pane, HUD in bottom split
    const currentPaneId = process.env.TMUX_PANE;
    const staleHudPaneIds = listHudWatchPaneIdsInCurrentWindow(currentPaneId);
    for (const paneId of staleHudPaneIds) {
      killTmuxPane(paneId);
    }

    let hudPaneId: string | null = null;
    try {
      hudPaneId = createHudWatchPane(cwd, hudCmd);
    } catch (err) {
      process.stderr.write(`[cli/index] operation failed: ${err}\n`);
      // HUD split failed, continue without it
    }