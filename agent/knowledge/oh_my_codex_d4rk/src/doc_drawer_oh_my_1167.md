s' "$last" | grep -q 'hud --watch'; then
      printf '%%3\n'
      exit 0
    fi
    printf '%%2\n'
    /bin/sh -lc "$last"
    exit 0
    ;;
  set-option|select-pane)
    exit 0
    ;;
  *)
    exit 0
    ;;
esac
`,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeTmuxPath], { stdio: 'ignore' });

      const result = runOmx(repo, ['autoresearch', 'run', missionDir, '--model', 'gpt-5'], {
        PATH: `${fakeBin}:${process.env.PATH || ''}`,
        OMX_TEST_REPO_ROOT: repo,
        TMUX: '/tmp/fake-tmux,12345,0',
        TMUX_PANE: '%9',
      });
      assert.equal(result.status, 0, result.stderr || result.stdout);