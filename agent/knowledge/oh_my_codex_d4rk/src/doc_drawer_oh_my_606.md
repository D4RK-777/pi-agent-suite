, "-p", "-t", activePaneId, "#S"], {
          encoding: "utf-8",
        });
      } catch {}
    }

    try {
      runCodexBlocking(cwd, launchArgs, codexEnvWithNotify);
    } finally {
      const cleanupPaneIds = buildHudPaneCleanupTargets(
        listHudWatchPaneIdsInCurrentWindow(currentPaneId),
        hudPaneId,
        currentPaneId,
      );
      for (const paneId of cleanupPaneIds) {
        killTmuxPane(paneId);
      }
    }
  } else if (launchPolicy === "direct") {
    // Detached HUD sessions require tmux. Skip the bootstrap entirely when the
    // binary is unavailable so direct launches do not emit noisy ENOENT logs.
    runCodexBlocking(cwd, launchArgs, codexEnvWithNotify);
  } else {
    // Not in tmux: create a new tmux session with codex + HUD pane