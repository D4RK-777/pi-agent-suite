eof result !== 'object') {
    return { enabled: false, reason: 'invalid_result', results: [] };
  }

  const obj = result as Record<string, unknown>;
  const results = Array.isArray(obj.results)
    ? obj.results.filter((item): item is Record<string, unknown> => !!item && typeof item === 'object')
    : [];

  return {
    enabled: obj.enabled !== false,
    reason: typeof obj.reason === 'string' ? obj.reason : 'ok',
    results,
  };
}

function pluginLabelFromResult(result: Record<string, unknown>): string {
  if (typeof result.plugin_id === 'string' && result.plugin_id) return result.plugin_id;
  if (typeof result.plugin === 'string' && result.plugin) return result.plugin;
  if (typeof result.file === 'string' && result.file) return result.file;
  return 'unknown-plugin';
}