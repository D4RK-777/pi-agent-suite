'), '# Mission\nShip it\n', 'utf-8');
      await writeFile(
        join(missionDir, 'sandbox.md'),
        `---\nevaluator:\n  command: node scripts/eval.js\n  format: json\n---\nStay in bounds.\n`,
        'utf-8',
      );

      const contract = await loadAutoresearchMissionContract(missionDir);
      assert.equal(contract.repoRoot, repo);
      assert.equal(contract.missionRelativeDir.replace(/\\/g, '/'), 'missions/demo');
      assert.equal(contract.missionSlug, 'missions-demo');
      assert.equal(contract.sandbox.evaluator.command, 'node scripts/eval.js');
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});