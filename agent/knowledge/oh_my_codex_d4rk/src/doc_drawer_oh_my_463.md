Harness',
      status: 'pass',
      message: `ready (${version || 'cargo available'})`,
    };
  }

  return {
    name: 'Explore Harness',
    status: 'warn',
    message: `Rust harness sources are packaged, but cargo probe failed with exit ${result.status} (install Rust or set ${EXPLORE_BIN_ENV})`,
  };
}

function checkDirectory(name: string, path: string): Check {
  if (existsSync(path)) {
    return { name, status: 'pass', message: path };
  }
  return { name, status: 'warn', message: `${path} (not created yet)` };
}

function validateToml(content: string): string | null {
  try {
    parseToml(content);
    return null;
  } catch (error) {
    if (error instanceof Error) {
      return error.message;
    }
    return 'unknown TOML parse error';
  }
}