''}`, CODEX_HOME: codexHome },
      );
      if (shouldSkipForSpawnPermissions(res.error)) return;

      assert.equal(res.status, 0, res.stderr || res.stdout);
      const artifactPath = res.stdout.trim();
      const artifact = await readFile(artifactPath, 'utf-8');
      assert.match(artifact, /## Original task\n\nship feature/);
      assert.match(artifact, /## Final prompt[\s\S]*You are Executor\./);
      assert.match(artifact, /## Final prompt[\s\S]*Follow strict verification rules\./);
      assert.match(artifact, /## Final prompt[\s\S]*ship feature/);
      assert.match(artifact, /CLAUDE_FINAL_PROMPT:/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });