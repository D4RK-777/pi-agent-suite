X_EXPLORE_BIN: harnessStub,
      });
      if (shouldSkipForSpawnPermissions(result.error)) return;

      assert.equal(result.status, 0, result.stderr || result.stdout);
      assert.match(result.stderr, /sparkshell backend unavailable/);
      assert.match(result.stderr, /Falling back to the explore harness/);
      assert.match(result.stdout, /fallback harness recovered the lookup/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });