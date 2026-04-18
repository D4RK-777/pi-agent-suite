ert.match(result.stdout, /deep-interview/i);
      assert.match(result.stdout, /human entrypoint/i);
      assert.doesNotMatch(result.stdout, /oh-my-codex \(omx\) - Multi-agent orchestration for Codex CLI/i);
    } finally {
      await rm(cwd, { recursive: true, force: true });
    }
  });

  it('documents --resume in command-local help', async () => {
    const cwd = await mkdtemp(join(tmpdir(), 'omx-autoresearch-resume-help-'));
    try {
      const result = runOmx(cwd, ['autoresearch', '--help']);
      assert.equal(result.status, 0, result.stderr || result.stdout);
      assert.match(result.stdout, /--resume <run-id>/i);
      assert.match(result.stdout, /run-tagged/i);
    } finally {
      await rm(cwd, { recursive: true, force: true });
    }
  });