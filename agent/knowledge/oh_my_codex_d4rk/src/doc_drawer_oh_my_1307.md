er" "- fallback harness recovered the lookup"\n',
      );
      await chmod(sparkshellStub, 0o755);
      await chmod(harnessStub, 0o755);

      const result = runOmx(wd, ['explore', '--prompt', 'git log --oneline'], {
        OMX_SPARKSHELL_BIN: sparkshellStub,
        OMX_EXPLORE_BIN: harnessStub,
      });
      if (shouldSkipForSpawnPermissions(result.error)) return;

      assert.equal(result.status, 0, result.stderr || result.stdout);
      assert.match(result.stderr, /GLIBC symbols/i);
      assert.match(result.stderr, /Falling back to the explore harness/);
      assert.match(result.stdout, /fallback harness recovered the lookup/);
      assert.doesNotMatch(result.stderr, /version `GLIBC_2\.39' not found/);
    } finally {
      await rm(wd, { recursive: true, force: true });