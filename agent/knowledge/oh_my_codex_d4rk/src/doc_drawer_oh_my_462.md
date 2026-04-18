if (kind === 'missing') {
      return {
        name: 'Explore Harness',
        status: 'warn',
        message: `Rust harness sources are packaged, but no compatible packaged prebuilt or cargo was found (install Rust or set ${EXPLORE_BIN_ENV} for omx explore)`,
      };
    }
    return {
      name: 'Explore Harness',
      status: 'warn',
      message: `Rust harness sources are packaged, but cargo probe failed (${result.error.message})`,
    };
  }

  if (result.status === 0) {
    const version = (result.stdout || '').trim();
    return {
      name: 'Explore Harness',
      status: 'pass',
      message: `ready (${version || 'cargo available'})`,
    };
  }