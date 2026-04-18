(
      "launch",
      sessionName,
      hookWindowIndex,
      hudPaneId,
    );
    steps.push({
      name: "register-resize-hook",
      args: buildRegisterResizeHookArgs(
        hookTarget,
        hookName,
        hudPaneId,
        HUD_TMUX_HEIGHT_LINES,
      ),
    });
    steps.push({
      name: "register-client-attached-reconcile",
      args: buildRegisterClientAttachedReconcileArgs(
        hookTarget,
        clientAttachedHookName,
        hudPaneId,
        HUD_TMUX_HEIGHT_LINES,
      ),
    });
    steps.push({
      name: "schedule-delayed-resize",
      args: buildScheduleDelayedHudResizeArgs(
        hudPaneId,
        undefined,
        HUD_TMUX_HEIGHT_LINES,
      ),
    });
    steps.push({
      name: "reconcile-hud-resize",