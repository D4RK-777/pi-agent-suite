entry.state.completed_at = nowIso;
      entry.state.last_turn_at = nowIso;
      changed.add(mode);
      if (reportIfWasActive && wasActive) reported.add(mode);
    };

    const ralphLinksUltrawork = (state: Record<string, unknown>): boolean =>
      state.linked_ultrawork === true || state.linked_mode === "ultrawork";

    const ralph = states.get("ralph");
    const hadActiveRalph = !!(ralph && ralph.state.active === true);
    if (ralph && ralph.state.active === true) {
      cancelMode("ralph", "cancelled", true);
      if (ralphLinksUltrawork(ralph.state))
        cancelMode("ultrawork", "cancelled", true);
    }