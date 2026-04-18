erf.js',
        keepPolicy: 'pass_only',
        slug: 'db-perf',
        repoRoot: repo,
      });

      const sandboxContent = await readFile(join(result.missionDir, 'sandbox.md'), 'utf-8');
      assert.match(sandboxContent, /^---\n/);
      assert.match(sandboxContent, /evaluator:/);
      assert.match(sandboxContent, /command: node scripts\/eval-perf\.js/);
      assert.match(sandboxContent, /format: json/);
      assert.match(sandboxContent, /keep_policy: pass_only/);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });