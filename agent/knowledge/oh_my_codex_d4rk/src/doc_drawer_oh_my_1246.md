{ recursive: true });
      await writeFile(join(canonicalHelp, 'SKILL.md'), '# canonical help\n');
      await writeFile(join(canonicalPlan, 'SKILL.md'), '# canonical plan\n');
      await writeFile(join(legacyHelp, 'SKILL.md'), '# legacy help\n');

      const res = runOmx(wd, ['doctor'], {
        HOME: home,
        CODEX_HOME: codexDir,
      });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 0, res.stderr || res.stdout);
      assert.match(
        res.stdout,
        /Legacy skill roots: 1 overlapping skill names between .*\.codex[\\/]+skills and .*\.agents[\\/]+skills; 1 differ in SKILL\.md content; Codex Enable\/Disable Skills may show duplicates until ~\/\.agents\/skills is cleaned up/,
      );
    } finally {