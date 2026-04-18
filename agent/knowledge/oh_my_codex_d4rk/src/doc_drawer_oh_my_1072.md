GENTS.md'), 'utf-8'), original);
      assert.equal(existsSync(join(wd, 'src', 'AGENTS.md')), true);

      await withCwd(wd, async () => {
        await agentsInit({ force: true });
      });

      const adopted = await readFile(join(wd, 'AGENTS.md'), 'utf-8');
      assert.match(adopted, /OMX:AGENTS-INIT:MANAGED/);
      const backupRoot = join(wd, '.omx', 'backups', 'agents-init');
      assert.equal(existsSync(backupRoot), true);
      const timestamps = await readdir(backupRoot);
      assert.equal(timestamps.length > 0, true);
      const backupContent = await readFile(join(backupRoot, timestamps[0], 'AGENTS.md'), 'utf-8');
      assert.equal(backupContent, original);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });