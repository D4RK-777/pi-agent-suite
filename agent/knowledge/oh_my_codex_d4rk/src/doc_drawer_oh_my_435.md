eDir: string;
  configPath: string;
  promptsDir: string;
  skillsDir: string;
  stateDir: string;
}

const LEGACY_SCOPE_MIGRATION: Record<string, DoctorSetupScope> = {
  'project-local': 'project',
};

async function resolveDoctorScope(cwd: string): Promise<DoctorScopeResolution> {
  const scopePath = join(cwd, '.omx', 'setup-scope.json');
  if (!existsSync(scopePath)) {
    return { scope: 'user', source: 'default' };
  }