',
      status: 'pass',
      message: 'enabled by default (config.toml not found yet)',
    };
  }

  try {
    const content = await readFile(configPath, 'utf-8');
    const parsed = parseToml(content) as { env?: Record<string, unknown> };
    const configuredValue = parsed?.env?.USE_OMX_EXPLORE_CMD;

    if (
      typeof configuredValue === 'string' &&
      !isExploreCommandRoutingEnabled({
        USE_OMX_EXPLORE_CMD: configuredValue,
      })
    ) {
      return {
        name: 'Explore routing',
        status: 'warn',
        message:
          'disabled in config.toml [env]; set USE_OMX_EXPLORE_CMD = "1" to restore default explore-first routing',
      };
    }