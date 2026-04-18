sert.ok(!source.includes("completed_at: new Date().toISOString(),\n    }).catch(() => {});"));
  });

  it('uses warning logs for watcher lifecycle best-effort failures', async () => {
    const source = await readSource('src/cli/index.ts');

    assert.ok(!source.includes("await mkdir(join(cwd, '.omx', 'state'), { recursive: true }).catch(() => {});"));
    assert.ok(!source.includes('await unlink(pidPath).catch(() => {});'));