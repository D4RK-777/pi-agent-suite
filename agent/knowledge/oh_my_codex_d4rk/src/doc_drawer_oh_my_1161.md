intf '%s' "$last" | grep -q 'autoresearch '; then
      /bin/sh -lc "$last"
    fi
    exit 0
    ;;
  attach-session|set-option|set-hook|kill-session|kill-pane)
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

      const result = runOmx(repo, ['autoresearch', '--topic', 'Investigate flaky onboarding behavior', '--evaluator', 'node scripts/eval.js', '--slug', 'test-launch'], {
        PATH: `${fakeBin}:${process.env.PATH || ''}`,
        OMX_TEST_REPO_ROOT: repo,
        TMUX: '/tmp/fake-tmux,12345,0',
        TMUX_PANE: '%42',
      });
      assert.equal(result.status, 0, result.stderr || result.stdout);