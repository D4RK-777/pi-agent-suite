laudeArtifactPath, 'utf-8');
      assert.match(claudeArtifact, /CLAUDE_PRINT_OK:claude-long-flag/);

      const geminiRes = runOmx(wd, ['ask', 'gemini', '--prompt', 'gemini-long-flag'], env);
      assert.equal(geminiRes.status, 0, geminiRes.stderr || geminiRes.stdout);
      const geminiArtifactPath = geminiRes.stdout.trim();
      const geminiArtifact = await readFile(geminiArtifactPath, 'utf-8');
      assert.match(geminiArtifact, /GEMINI_PROMPT_OK:gemini-long-flag/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });