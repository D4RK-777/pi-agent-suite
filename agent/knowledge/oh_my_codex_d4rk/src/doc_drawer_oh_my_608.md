ldDetachedSessionBootstrapSteps(
        sessionName,
        cwd,
        codexCmd,
        hudCmd,
        workerLaunchArgs,
        codexHomeOverride,
        notifyTempContractRaw,
        nativeWindows,
        sessionId,
      );
      for (const step of bootstrapSteps) {
        const output = execFileSync("tmux", step.args, {
          stdio: "pipe",
          encoding: "utf-8",
        });
        if (step.name === "new-session") {
          createdDetachedSession = true;
          parsePaneIdFromTmuxOutput(output || "");
        }
        if (step.name === "split-and-capture-hud-pane") {
          const hudPaneId = parsePaneIdFromTmuxOutput(output || "");
          const hookWindowIndex = hudPaneId
            ? detectDetachedSessionWindowIndex(sessionName)
            : null;