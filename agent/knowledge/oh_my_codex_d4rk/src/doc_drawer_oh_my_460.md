ound in this install (omx explore unavailable until packaged or OMX_EXPLORE_BIN is set)',
    };
  }

  const override = process.env[EXPLORE_BIN_ENV]?.trim();
  if (override) {
    const resolved = join(packageRoot, override);
    if (existsSync(override) || existsSync(resolved)) {
      return {
        name: 'Explore Harness',
        status: 'pass',
        message: `${EXPLORE_BIN_ENV} configured (${override})`,
      };
    }
    return {
      name: 'Explore Harness',
      status: 'warn',
      message: `OMX_EXPLORE_BIN is set but path was not found (${override})`,
    };
  }