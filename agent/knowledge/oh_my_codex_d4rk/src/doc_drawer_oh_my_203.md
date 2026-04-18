assert.match(instructions, /Mission file:/i);
      assert.match(instructions, /Sandbox policy:/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('allows untracked .omx runtime files when checking reset safety', async () => {
    const repo = await initRepo();
    try {
      await mkdir(join(repo, '.omx', 'logs'), { recursive: true });
      await mkdir(join(repo, '.omx', 'state'), { recursive: true });
      await writeFile(join(repo, '.omx', 'logs', 'hooks-2026-03-15.jsonl'), '{}\n', 'utf-8');
      await writeFile(join(repo, '.omx', 'metrics.json'), '{}\n', 'utf-8');
      await writeFile(join(repo, '.omx', 'state', 'hud-state.json'), '{}\n', 'utf-8');