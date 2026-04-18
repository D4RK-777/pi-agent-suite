ontent, original);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('protects project-root AGENTS.md during an active OMX session', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-init-'));
    try {
      const pidStartTicks = await readCurrentLinuxStartTicks();
      await mkdir(join(wd, '.omx', 'state'), { recursive: true });
      await mkdir(join(wd, 'src'), { recursive: true });
      await writeFile(join(wd, 'AGENTS.md'), '# unmanaged\n');
      await writeFile(join(wd, 'src', 'index.ts'), 'export const x = 1;\n');
      await writeFile(
        join(wd, '.omx', 'state', 'session.json'),
        JSON.stringify({
          session_id: 'session-1',
          started_at: new Date().toISOString(),
          cwd: wd,