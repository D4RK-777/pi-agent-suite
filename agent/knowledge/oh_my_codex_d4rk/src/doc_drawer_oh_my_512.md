},
    allowInTeamWorker: false,
  } as never);
  const result = normalizeDispatchResult(rawResult);

  console.log('hooks test dispatch complete');
  console.log(`plugins discovered: ${discovered.length}`);
  console.log(`plugins enabled: ${result.enabled ? 'yes' : 'no'}`);
  console.log(`dispatch reason: ${result.reason}`);

  for (const pluginResult of result.results) {
    const label = pluginLabelFromResult(pluginResult);
    const status = pluginStatusFromResult(pluginResult);
    const error = typeof pluginResult.error === 'string' ? pluginResult.error : '';
    console.log(error ? `${label}: ${status} (${error})` : `${label}: ${status}`);
  }