, /run-tagged/i);
    } finally {
      await rm(cwd, { recursive: true, force: true });
    }
  });

  it('fails fast when mission dir is missing', async () => {
    const cwd = await mkdtemp(join(tmpdir(), 'omx-autoresearch-missing-arg-'));
    try {
      const result = runOmx(cwd, ['autoresearch']);
      assert.notEqual(result.status, 0, result.stderr || result.stdout);
      assert.match(`${result.stderr}\n${result.stdout}`, /mission-dir|Usage:\s*omx autoresearch <mission-dir>/i);
    } finally {
      await rm(cwd, { recursive: true, force: true });
    }
  });