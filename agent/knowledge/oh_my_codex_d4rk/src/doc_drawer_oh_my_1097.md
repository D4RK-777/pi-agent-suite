stub.md\n',
        OMX_ASK_STUB_STDERR: 'stub-warning-line\n',
        OMX_ASK_STUB_EXIT_CODE: '7',
      });
      if (shouldSkipForSpawnPermissions(res.error)) return;

      assert.equal(res.status, 7, res.stderr || res.stdout);
      assert.equal(res.stdout, 'artifact-path-from-stub.md\n');
      assert.equal(res.stderr, 'stub-warning-line\n');
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });