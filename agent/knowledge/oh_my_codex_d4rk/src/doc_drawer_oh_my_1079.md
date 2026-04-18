missions(err?: string): boolean {
  return typeof err === 'string' && /(EPERM|EACCES)/i.test(err);
}

describe('omx agents', () => {
  it('lists project and user native agents with name, description, and model', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-cli-'));
    const home = join(wd, 'home');
    try {
      const projectAgentsDir = join(wd, '.codex', 'agents');
      const userAgentsDir = join(home, '.codex', 'agents');
      await mkdir(projectAgentsDir, { recursive: true });
      await mkdir(userAgentsDir, { recursive: true });