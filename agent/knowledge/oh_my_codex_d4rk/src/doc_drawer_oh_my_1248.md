(canonicalHelp, { recursive: true });
      await mkdir(join(home, '.agents'), { recursive: true });
      await writeFile(join(canonicalHelp, 'SKILL.md'), '# canonical help\n');
      await symlink(
        canonicalSkillsRoot,
        legacyRoot,
        process.platform === 'win32' ? 'junction' : 'dir',
      );

      const res = runOmx(wd, ['doctor'], {
        HOME: home,
        CODEX_HOME: codexDir,
      });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 0, res.stderr || res.stdout);
      assert.match(
        res.stdout,
        /Legacy skill roots: ~\/\.agents\/skills links to canonical .*\.codex[\\/]+skills; treating both paths as one shared skill root/,
      );
      assert.doesNotMatch(res.stdout, /\[!!\] Legacy skill roots:/);