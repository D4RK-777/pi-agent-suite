; fi\necho "unexpected" 1>&2\nexit 3\n',
      );
      await chmod(join(fakeBin, 'claude'), 0o755);

      const res = runOmx(wd, ['ask', 'claude', 'non-root-default'], {
        PATH: `${fakeBin}:${process.env.PATH || ''}`,
      });
      if (shouldSkipForSpawnPermissions(res.error)) return;

      assert.equal(res.status, 0, res.stderr || res.stdout);
      const artifactPath = res.stdout.trim();
      assert.ok(artifactPath.startsWith(join(wd, '.omx', 'artifacts', 'claude-')));
      assert.equal(existsSync(artifactPath), true);
      const artifact = await readFile(artifactPath, 'utf-8');
      assert.match(artifact, /NONROOT_DEFAULT_OK/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });