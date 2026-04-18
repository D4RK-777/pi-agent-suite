HUD_TMUX_HEIGHT_LINES,
      ),
    });
    steps.push({
      name: "reconcile-hud-resize",
      args: buildReconcileHudResizeArgs(hudPaneId, HUD_TMUX_HEIGHT_LINES),
    });
  }

  if (enableMouse) {
    steps.push({
      name: "set-mouse",
      args: ["set-option", "-t", sessionName, "mouse", "on"],
    });
  }
  steps.push({
    name: "attach-session",
    args: ["attach-session", "-t", sessionName],
  });
  return steps;
}