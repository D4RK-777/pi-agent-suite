-warning-line\n');
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('resolves relative advisor override path from package root even on non-root cwd', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-ask-relative-'));
    try {
      const res = runOmx(wd, ['ask', 'gemini', 'relative-check'], {
        OMX_ASK_ADVISOR_SCRIPT: 'dist/scripts/fixtures/ask-advisor-stub.js',
        OMX_ASK_STUB_STDOUT: 'relative-override-ok\n',
        OMX_ASK_STUB_EXIT_CODE: '0',
      });
      if (shouldSkipForSpawnPermissions(res.error)) return;

      assert.equal(res.status, 0, res.stderr || res.stdout);
      assert.equal(res.stdout, 'relative-override-ok\n');
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });