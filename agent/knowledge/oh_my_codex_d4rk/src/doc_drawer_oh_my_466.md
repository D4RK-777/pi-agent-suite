} catch {
    return { name: 'Config', status: 'fail', message: 'cannot read config.toml' };
  }
}


async function checkExploreRouting(configPath: string): Promise<Check> {
  const envValue = process.env[OMX_EXPLORE_CMD_ENV];
  if (typeof envValue === 'string' && !isExploreCommandRoutingEnabled(process.env)) {
    return {
      name: 'Explore routing',
      status: 'warn',
      message:
        'disabled by environment override; enable with USE_OMX_EXPLORE_CMD=1 (or remove the explicit opt-out)',
    };
  }

  if (!existsSync(configPath)) {
    return {
      name: 'Explore routing',
      status: 'pass',
      message: 'enabled by default (config.toml not found yet)',
    };
  }