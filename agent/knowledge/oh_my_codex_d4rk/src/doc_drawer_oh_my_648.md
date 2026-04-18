ate,
      });
    }

    const changed = new Set<string>();
    const reported = new Set<string>();

    const cancelMode = (
      mode: string,
      phase: string = "cancelled",
      reportIfWasActive: boolean = true,
    ): void => {
      const entry = states.get(mode);
      if (!entry) return;
      const wasActive = entry.state.active === true;
      const needsChange =
        entry.state.active !== false ||
        entry.state.current_phase !== phase ||
        typeof entry.state.completed_at !== "string" ||
        String(entry.state.completed_at).trim() === "";
      if (!needsChange) return;
      entry.state.active = false;
      entry.state.current_phase = phase;
      entry.state.completed_at = nowIso;
      entry.state.last_turn_at = nowIso;
      changed.add(mode);