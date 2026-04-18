});
}
`;

function hooksDir(cwd = process.cwd()): string {
  return join(cwd, '.omx', 'hooks');
}

function samplePluginPath(cwd = process.cwd()): string {
  return join(hooksDir(cwd), 'sample-plugin.mjs');
}

interface HookPluginValidationResult {
  valid: boolean;
  reason?: string;
}

async function validateHookPluginExport(filePath: string): Promise<HookPluginValidationResult> {
  try {
    const moduleUrl = `${pathToFileURL(filePath).href}?t=${Date.now()}`;
    const mod = await import(moduleUrl) as { onHookEvent?: unknown };
    if (typeof mod.onHookEvent !== 'function') {
      return { valid: false, reason: 'missing export `onHookEvent(event, sdk)`' };
    }
    return { valid: true };
  } catch (error) {
    return {
      valid: false,