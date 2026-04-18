target ?? 'n/a'}`);
    const panes = state.pane_counts ? Object.keys(state.pane_counts).length : 0;
    const legacySessions = state.session_counts ? Object.keys(state.session_counts).length : 0;
    console.log(`Tracked Panes: ${panes}`);
    if (legacySessions > 0) {
      console.log(`Tracked Sessions (legacy): ${legacySessions}`);
    }
  }

  console.log(`Log (today): ${existsSync(logPath) ? logPath : 'none yet'}`);
}

async function validateTmuxHookConfig(): Promise<void> {
  const cwd = process.cwd();
  const { config, initResult } = await loadConfigForCommand('validate', cwd);
  if (initResult?.usedPlaceholderTarget) {
    return;
  }
  const resolved = resolveValidateTarget(config);