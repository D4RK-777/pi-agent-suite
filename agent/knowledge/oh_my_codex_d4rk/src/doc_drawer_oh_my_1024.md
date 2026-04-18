(!config.enabled) {
    console.log('Note: config is currently disabled (`enabled: false`).');
  }
}

async function testTmuxHook(args: string[]): Promise<void> {
  const cwd = process.cwd();
  const { initResult } = await loadConfigForCommand('test', cwd);
  if (initResult?.usedPlaceholderTarget) {
    console.log('Proceeding with placeholder target; notify-hook may log `invalid_config` skips.');
  }
  const pkgRoot = getPackageRoot();
  const notifyHook = join(pkgRoot, 'dist', 'scripts', 'notify-hook.js');
  if (!existsSync(notifyHook)) {
    throw new Error(`notify-hook.js not found at ${notifyHook}`);
  }