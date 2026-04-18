);

      await withCwd(wd, async () => {
        await agentsInit({ targetPath: 'src' });
      });

      const refreshed = await readFile(agentsPath, 'utf-8');
      assert.match(refreshed, /Preserve this custom manual note\./);
      assert.match(refreshed, /`new-file\.ts`/);
      assert.equal(existsSync(join(wd, 'src', 'lib', 'AGENTS.md')), true);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });