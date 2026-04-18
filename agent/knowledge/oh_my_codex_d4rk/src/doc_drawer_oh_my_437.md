valid persisted scope and fall back to default
  }

  return { scope: 'user', source: 'default' };
}

function resolveDoctorPaths(cwd: string, scope: DoctorSetupScope): DoctorPaths {
  if (scope === 'project') {
    const codexHomeDir = join(cwd, '.codex');
    return {
      codexHomeDir,
      configPath: join(codexHomeDir, 'config.toml'),
      promptsDir: join(codexHomeDir, 'prompts'),
      skillsDir: projectSkillsDir(cwd),
      stateDir: omxStateDir(cwd),
    };
  }

  return {
    codexHomeDir: codexHome(),
    configPath: codexConfigPath(),
    promptsDir: codexPromptsDir(),
    skillsDir: userSkillsDir(),
    stateDir: omxStateDir(cwd),
  };
}