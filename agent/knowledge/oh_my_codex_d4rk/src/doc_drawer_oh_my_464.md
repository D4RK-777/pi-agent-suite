r instanceof Error) {
      return error.message;
    }
    return 'unknown TOML parse error';
  }
}

async function checkConfig(configPath: string): Promise<Check> {
  if (!existsSync(configPath)) {
    return { name: 'Config', status: 'warn', message: 'config.toml not found' };
  }

  try {
    const content = await readFile(configPath, 'utf-8');
    const tomlError = validateToml(content);

    if (tomlError) {
      const hint =
        tomlError.includes("Can't redefine existing key") ||
        tomlError.includes('duplicate') ||
        tomlError.includes('[tui]')
          ? 'possible duplicate TOML table such as [tui]'
          : 'invalid TOML syntax';

      return {
        name: 'Config',
        status: 'fail',
        message: `invalid config.toml (${hint})`,
      };
    }