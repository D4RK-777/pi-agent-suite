mdFiles = files.filter(f => f.endsWith('.md'));
    if (mdFiles.length >= expectations.promptMin) {
      return { name: 'Prompts', status: 'pass', message: `${mdFiles.length} agent prompts installed` };
    }
    return { name: 'Prompts', status: 'warn', message: `${mdFiles.length} prompts (expected >= ${expectations.promptMin})` };
  } catch {
    return { name: 'Prompts', status: 'fail', message: 'cannot read prompts directory' };
  }
}

async function checkLegacySkillRootOverlap(): Promise<Check> {
  const overlap = await detectLegacySkillRootOverlap();
  if (!overlap.legacyExists) {
    return {
      name: 'Legacy skill roots',
      status: 'pass',
      message: 'no ~/.agents/skills overlap detected',
    };
  }