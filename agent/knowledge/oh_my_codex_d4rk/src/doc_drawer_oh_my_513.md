t.error : '';
    console.log(error ? `${label}: ${status} (${error})` : `${label}: ${status}`);
  }

  const logPath = join(cwd, '.omx', 'logs', `hooks-${new Date().toISOString().split('T')[0]}.jsonl`);
  if (existsSync(logPath)) {
    const content = await readFile(logPath, 'utf-8').catch(() => '');
    if (content.trim()) {
      console.log(`log file: ${logPath}`);
    }
  }
}

export function formatHooksStatusLine(plugin: HookPluginDescriptor): string {
  return plugin.fileName;
}