.stdout, /# Project Instructions/);
      assert.match(result.stdout, /<!-- OMX:RUNTIME:START -->/);

      const sessionRoot = join(wd, '.omx', 'state', 'sessions');
      const sessionEntries = await readdir(sessionRoot);
      assert.equal(sessionEntries.length, 1);
      const sessionFiles = await readdir(join(sessionRoot, sessionEntries[0]));
      assert.equal(sessionFiles.includes('AGENTS.md'), false, 'session-scoped AGENTS file should be cleaned up after exec exits');
      assert.equal(existsSync(join(wd, '.omx', 'state', 'session.json')), false);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });