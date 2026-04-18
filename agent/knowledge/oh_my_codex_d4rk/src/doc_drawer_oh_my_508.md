f (plugins.length === 0) {
    console.log('No plugins found. Run: omx hooks init');
    return;
  }

  let failed = 0;
  for (const plugin of plugins) {
    const result = await validateHookPluginExport(plugin.filePath);
    if (result.valid) {
      console.log(`✓ ${plugin.fileName}`);
    } else {
      failed += 1;
      console.log(`✗ ${plugin.fileName}: ${result.reason || 'invalid export'}`);
    }
  }

  if (failed > 0) {
    throw new Error(`hooks validation failed (${failed} plugin${failed === 1 ? '' : 's'})`);
  }
}

function normalizeDispatchResult(result: unknown): {
  enabled: boolean;
  reason: string;
  results: Record<string, unknown>[];
} {
  if (!result || typeof result !== 'object') {
    return { enabled: false, reason: 'invalid_result', results: [] };
  }