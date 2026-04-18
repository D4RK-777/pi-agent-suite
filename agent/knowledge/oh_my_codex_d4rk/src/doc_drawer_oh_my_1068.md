gents, /`guide\.md`/);
      assert.equal(existsSync(join(wd, 'node_modules', 'AGENTS.md')), false);
      assert.equal(existsSync(join(wd, 'dist', 'AGENTS.md')), false);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('refreshes managed subtree files while preserving the manual notes block', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-init-'));
    try {
      await mkdir(join(wd, 'src', 'lib'), { recursive: true });
      await writeFile(join(wd, 'src', 'index.ts'), 'export const index = true;\n');

      await withCwd(wd, async () => {
        await agentsInit({ targetPath: 'src' });
      });