ursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });

  it('rejects mission directories outside a git repo', async () => {
    const cwd = await mkdtemp(join(tmpdir(), 'omx-autoresearch-outside-git-'));
    try {
      await writeFile(join(cwd, 'mission.md'), '# Mission\n', 'utf-8');
      await writeFile(join(cwd, 'sandbox.md'), '---\nevaluator:\n  command: node eval.js\n---\n', 'utf-8');

      const result = runOmx(cwd, ['autoresearch', cwd]);
      assert.notEqual(result.status, 0, result.stderr || result.stdout);
      assert.match(`${result.stderr}\n${result.stdout}`, /git repo|git repository|inside a git repo/i);
    } finally {
      await rm(cwd, { recursive: true, force: true });
    }
  });