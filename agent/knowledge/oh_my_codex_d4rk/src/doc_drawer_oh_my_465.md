: 'Config',
        status: 'fail',
        message: `invalid config.toml (${hint})`,
      };
    }

    const hasOmx = content.includes('omx_') || content.includes('oh-my-codex');
    if (hasOmx) {
      return { name: 'Config', status: 'pass', message: 'config.toml has OMX entries' };
    }

    return {
      name: 'Config',
      status: 'warn',
      message: 'config.toml exists but no OMX entries yet (expected before first setup; run "omx setup --force" once)',
    };
  } catch {
    return { name: 'Config', status: 'fail', message: 'cannot read config.toml' };
  }
}