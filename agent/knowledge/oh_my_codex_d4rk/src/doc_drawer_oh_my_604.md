rite(`[cli/index] operation failed: ${err}\n`);
      // HUD split failed, continue without it
    }

    // Enable mouse scrolling at session start so scroll works before team
    // expansion. Previously this was only called from createTeamSession().
    // Opt-out: set OMX_MOUSE=0. (closes #128)
    if (process.env.OMX_MOUSE !== "0") {
      try {
        const tmuxPaneTarget = process.env.TMUX_PANE;
        const displayArgs = tmuxPaneTarget
          ? ["display-message", "-p", "-t", tmuxPaneTarget, "#S"]
          : ["display-message", "-p", "#S"];
        const tmuxSession = execFileSync("tmux", displayArgs, {
          encoding: "utf-8",
        }).trim();
        if (tmuxSession) enableMouseScrolling(tmuxSession);
      } catch (err) {