config.cooldown_ms}ms`);
  console.log(`Max Injections/Pane: ${config.max_injections_per_session}`);
  console.log(`Dry Run: ${config.dry_run ? 'yes' : 'no'}`);
  console.log(`Skip If Scrolling: ${config.skip_if_scrolling ? 'yes' : 'no'}`);

  if (!existsSync(statePath)) {
    console.log(`State: missing (${statePath})`);
  } else {
    const state = JSON.parse(await readFile(statePath, 'utf-8')) as TmuxHookState;
    console.log(`State: ${statePath}`);
    console.log(`Total Injections: ${state.total_injections ?? 0}`);
    console.log(`Last Reason: ${state.last_reason ?? 'n/a'}`);
    console.log(`Last Event: ${state.last_event_at ?? 'n/a'}`);
    console.log(`Last Target: ${state.last_target ?? 'n/a'}`);
    const panes = state.pane_counts ? Object.keys(state.pane_counts).length : 0;