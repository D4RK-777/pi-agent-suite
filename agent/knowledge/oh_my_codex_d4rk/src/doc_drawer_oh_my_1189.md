,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });

      const result = runOmx(
        repo,
        ['autoresearch', missionDir, '--dangerously-bypass-approvals-and-sandbox'],
        { PATH: `${fakeBin}:${process.env.PATH || ''}`, OMX_TEST_REPO_ROOT: repo },
      );

      assert.equal(result.status, 0, result.stderr || result.stdout);

      const state = JSON.parse(await readFile(join(repo, '.omx', 'state', 'autoresearch-state.json'), 'utf-8')) as {
        active: boolean;
      };
      assert.equal(state.active, false);