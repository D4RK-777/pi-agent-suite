editResult.stdout);
      assert.match(await readFile(agentPath, 'utf-8'), /^model = "gpt-5\.4"$/m);

      const removeResult = runOmx(wd, ['agents', 'remove', 'editor-test', '--scope', 'project', '--force'], {
        HOME: home,
        CODEX_HOME: join(home, '.codex'),
      });
      if (shouldSkipForSpawnPermissions(removeResult.error)) return;

      assert.equal(removeResult.status, 0, removeResult.stderr || removeResult.stdout);
      assert.equal(existsSync(agentPath), false);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });