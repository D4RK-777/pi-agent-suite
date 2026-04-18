scard\/reset parity/i);
    } finally {
      await rm(cwd, { recursive: true, force: true });
    }
  });

  it('routes autoresearch --help to command-local help', async () => {
    const cwd = await mkdtemp(join(tmpdir(), 'omx-autoresearch-local-help-'));
    try {
      const result = runOmx(cwd, ['autoresearch', '--help']);
      assert.equal(result.status, 0, result.stderr || result.stdout);
      assert.match(result.stdout, /Usage:[\s\S]*omx autoresearch run <mission-dir>/i);
      assert.match(result.stdout, /omx autoresearch init/i);
      assert.match(result.stdout, /--topic\/\.\.\./i);
      assert.match(result.stdout, /deep-interview/i);
      assert.match(result.stdout, /human entrypoint/i);