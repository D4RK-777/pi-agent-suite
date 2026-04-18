'utf-8');
      await writeFile(join(missionDir, 'sandbox.md'), 'No frontmatter here.\n', 'utf-8');

      const result = runOmx(repo, ['autoresearch', missionDir]);
      assert.notEqual(result.status, 0, result.stderr || result.stdout);
      assert.match(`${result.stderr}\n${result.stdout}`, /frontmatter|evaluator/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });