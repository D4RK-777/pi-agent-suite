if (typeof result.file === 'string' && result.file) return result.file;
  return 'unknown-plugin';
}

function pluginStatusFromResult(result: Record<string, unknown>): string {
  if (typeof result.status === 'string' && result.status) return result.status;
  if (typeof result.reason === 'string' && result.reason) return result.reason;
  if (typeof result.ok === 'boolean') return result.ok ? 'ok' : 'error';
  return 'unknown';
}

async function testHooks(): Promise<void> {
  const cwd = process.cwd();
  const discovered = await discoverHookPlugins(cwd);