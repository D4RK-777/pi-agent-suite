EST_REPO_ROOT: repo,
      });
      assert.equal(result.status, 0, result.stderr || result.stdout);

      const missionContent = await readFile(join(repo, 'missions', 'test-launch', 'mission.md'), 'utf-8');
      const sandboxContent = await readFile(join(repo, 'missions', 'test-launch', 'sandbox.md'), 'utf-8');
      assert.match(missionContent, /Investigate flaky onboarding behavior/);
      assert.match(sandboxContent, /command: node scripts\/eval\.js/);
    } finally {
      await rm(repo, { recursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });