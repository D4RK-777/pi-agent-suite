cwd = process.cwd();
  const dir = hooksDir(cwd);
  const plugins = await discoverHookPlugins(cwd);

  console.log('hooks status');
  console.log('-----------');
  console.log(`Directory: ${dir}`);
  console.log(
    `Plugins enabled: ${isHookPluginsEnabled(process.env) ? 'yes' : 'no (disabled with OMX_HOOK_PLUGINS=0)'}`,
  );
  console.log(`Discovered plugins: ${plugins.length}`);
  for (const plugin of plugins) {
    console.log(`- ${plugin.fileName}`);
  }
}

async function validateHooks(): Promise<void> {
  const cwd = process.cwd();
  const plugins = await discoverHookPlugins(cwd);
  if (plugins.length === 0) {
    console.log('No plugins found. Run: omx hooks init');
    return;
  }