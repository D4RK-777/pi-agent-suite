): Promise<void> {
  const cwd = process.cwd();
  const discovered = await discoverHookPlugins(cwd);

  const event = buildHookEvent('turn-complete', {
    source: 'native',
    context: {
      reason: 'omx-hooks-test',
    },
    session_id: 'omx-hooks-test',
    thread_id: `thread-${Date.now()}`,
    turn_id: `turn-${Date.now()}`,
  });

  const rawResult = await dispatchHookEvent(event, {
    cwd,
    event,
    env: {
      ...process.env,
      OMX_HOOK_PLUGINS: '1',
    },
    allowInTeamWorker: false,
  } as never);
  const result = normalizeDispatchResult(rawResult);