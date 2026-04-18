romptsDir: codexPromptsDir(),
    skillsDir: userSkillsDir(),
    stateDir: omxStateDir(cwd),
  };
}

export async function doctor(options: DoctorOptions = {}): Promise<void> {
  if (options.team) {
    await doctorTeam();
    return;
  }

  const cwd = process.cwd();
  const scopeResolution = await resolveDoctorScope(cwd);
  const paths = resolveDoctorPaths(cwd, scopeResolution.scope);
  const scopeSourceMessage = scopeResolution.source === 'persisted'
    ? ' (from .omx/setup-scope.json)'
    : '';

  console.log('oh-my-codex doctor');
  console.log('==================\n');
  console.log(`Resolved setup scope: ${scopeResolution.scope}${scopeSourceMessage}\n`);

  const checks: Check[] = [];

  // Check 1: Codex CLI installed
  checks.push(checkCodexCli());