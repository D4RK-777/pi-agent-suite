muxPath, script);
  spawnSync('chmod', ['+x', tmuxPath], { encoding: 'utf-8' });
  return fakeBin;
}

describe('omx doctor --team', () => {
  it('exits non-zero and prints resume_blocker when team state references missing tmux session', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-team-'));
    try {
      const teamRoot = join(wd, '.omx', 'state', 'team', 'alpha');
      await mkdir(join(teamRoot, 'workers', 'worker-1'), { recursive: true });
      await writeFile(join(teamRoot, 'config.json'), JSON.stringify({
        name: 'alpha',
        tmux_session: 'omx-team-alpha',
      }));