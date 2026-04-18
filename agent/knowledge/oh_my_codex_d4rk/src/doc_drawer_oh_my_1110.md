''}`, CODEX_HOME: codexHome },
      );
      if (shouldSkipForSpawnPermissions(res.error)) return;

      assert.equal(res.status, 1, res.stderr || res.stdout);
      assert.match(res.stderr, /--agent-prompt role "planner" not found/i);
      assert.doesNotMatch(res.stdout, /should-not-run/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });
});