.toml [env]; set USE_OMX_EXPLORE_CMD = "1" to restore default explore-first routing',
      };
    }

    return {
      name: 'Explore routing',
      status: 'pass',
      message: 'enabled by default',
    };
  } catch {
    return {
      name: 'Explore routing',
      status: 'fail',
      message: 'cannot read config.toml for explore routing check',
    };
  }
}

async function checkPrompts(dir: string): Promise<Check> {
  const expectations = getCatalogExpectations();
  if (!existsSync(dir)) {
    return { name: 'Prompts', status: 'warn', message: 'prompts directory not found' };
  }
  try {
    const files = await readdir(dir);
    const mdFiles = files.filter(f => f.endsWith('.md'));
    if (mdFiles.length >= expectations.promptMin) {