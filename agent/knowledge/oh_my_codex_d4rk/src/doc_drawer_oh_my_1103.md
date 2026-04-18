emini'), 0o755);

      const env = {
        PATH: `${fakeBin}:${process.env.PATH || ''}`,
      };

      const claudeRes = runOmx(wd, ['ask', 'claude', '--print', 'claude-long-flag'], env);
      if (shouldSkipForSpawnPermissions(claudeRes.error)) return;
      assert.equal(claudeRes.status, 0, claudeRes.stderr || claudeRes.stdout);
      const claudeArtifactPath = claudeRes.stdout.trim();
      const claudeArtifact = await readFile(claudeArtifactPath, 'utf-8');
      assert.match(claudeArtifact, /CLAUDE_PRINT_OK:claude-long-flag/);