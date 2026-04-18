;
      return;
    default:
      throw new Error(`Unknown hooks subcommand: ${subcommand}`);
  }
}

async function initHooks(): Promise<void> {
  const cwd = process.cwd();
  const dir = hooksDir(cwd);
  const samplePath = samplePluginPath(cwd);
  await mkdir(dir, { recursive: true });

  if (existsSync(samplePath)) {
    console.log(`hooks scaffold already exists: ${samplePath}`);
    return;
  }

  await writeFile(samplePath, SAMPLE_PLUGIN);
  console.log(`Created ${samplePath}`);
  console.log('Plugins are enabled by default. Disable with OMX_HOOK_PLUGINS=0.');
}

async function statusHooks(): Promise<void> {
  const cwd = process.cwd();
  const dir = hooksDir(cwd);
  const plugins = await discoverHookPlugins(cwd);