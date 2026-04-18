essage: `found but could not be executed in this environment (${code || 'blocked'})`,
      };
    }
    return {
      name: 'Codex CLI',
      status: 'fail',
      message: `probe failed - ${result.error.message}`,
    };
  }
  if (result.status === 0) {
    const version = (result.stdout || '').trim();
    return { name: 'Codex CLI', status: 'pass', message: `installed (${version})` };
  }
  const stderr = (result.stderr || '').trim();
  return {
    name: 'Codex CLI',
    status: 'fail',
    message: stderr !== '' ? `probe failed - ${stderr}` : `probe failed with exit ${result.status}`,
  };
}