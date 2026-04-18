'warn', message: `${skillDirs.length} skills (expected >= ${expectations.skillMin})` };
  } catch {
    return { name: 'Skills', status: 'fail', message: 'cannot read skills directory' };
  }
}

function checkAgentsMd(scope: DoctorSetupScope, codexHomeDir: string): Check {
  if (scope === 'user') {
    const userAgentsMd = join(codexHomeDir, 'AGENTS.md');
    if (existsSync(userAgentsMd)) {
      return { name: 'AGENTS.md', status: 'pass', message: `found in ${userAgentsMd}` };
    }
    return {
      name: 'AGENTS.md',
      status: 'warn',
      message: `not found in ${userAgentsMd} (run omx setup --scope user)`,
    };
  }