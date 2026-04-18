,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });

      const fakeTmuxPath = join(fakeBin, 'tmux');
      await writeFile(
        fakeTmuxPath,
        `#!/bin/sh
case "$1" in
  -V)
    printf 'tmux 3.4\n'
    exit 0
    ;;
  display-message)
    case "$*" in
      *"#{pane_id}"*) printf '%%9\n' ;;
      *"#{pane_current_path}"*) printf '${repo}\n' ;;
      *"#S"*) printf 'devsess\n' ;;
      *) printf '0\n' ;;
    esac
    exit 0
    ;;
  list-panes)
    printf '%%9\tzsh\tomx autoresearch\n'
    exit 0
    ;;
  split-window)
    exit 1
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