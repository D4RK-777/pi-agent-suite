`,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeTmuxPath], { stdio: 'ignore' });

      const result = runOmx(repo, ['autoresearch', 'run', missionDir], {
        PATH: `${fakeBin}:${process.env.PATH || ''}`,
        OMX_TEST_REPO_ROOT: repo,
        TMUX: '/tmp/fake-tmux,12345,0',
        TMUX_PANE: '%9',
      });
      assert.equal(result.status, 0, result.stderr || result.stdout);

      const logsRoot = join(repo, '.omx', 'logs', 'autoresearch');
      const [runId] = readdirSync(logsRoot, { withFileTypes: true })
        .filter(d => d.isDirectory())
        .map(d => d.name);
      assert.ok(runId);
    } finally {
      await rm(repo, { recursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });