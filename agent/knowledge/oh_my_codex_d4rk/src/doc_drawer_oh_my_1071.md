ENTS.md')), true);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('skips unmanaged AGENTS.md files by default but can adopt them with --force and a backup', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-init-'));
    const original = '# custom root guidance\n';
    try {
      await mkdir(join(wd, 'src'), { recursive: true });
      await writeFile(join(wd, 'AGENTS.md'), original);
      await writeFile(join(wd, 'src', 'index.ts'), 'export const x = 1;\n');

      await withCwd(wd, async () => {
        await agentsInit();
      });
      assert.equal(await readFile(join(wd, 'AGENTS.md'), 'utf-8'), original);
      assert.equal(existsSync(join(wd, 'src', 'AGENTS.md')), true);