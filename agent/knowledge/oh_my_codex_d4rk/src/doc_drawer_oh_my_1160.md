,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });

      const fakeTmuxPath = join(fakeBin, 'tmux');
      await writeFile(
        fakeTmuxPath,
        `#!/bin/sh
printf '%s\n' "$*" >>"${tmuxLog}"
case "$1" in
  -V)
    printf 'tmux 3.4\n'
    exit 0
    ;;
  display-message)
    case "$*" in
      *"#{pane_id}"*) printf '%%42\n' ;;
      *"#{pane_current_path}"*) printf '%s\n' "$OMX_TEST_REPO_ROOT" ;;
      *"#S"*) printf 'devsession\n' ;;
      *) printf 'devsession\n' ;;
    esac
    exit 0
    ;;
  list-panes)
    exit 0
    ;;
  split-window)
    last=""
    for arg in "$@"; do
      last="$arg"
    done
    printf '%%2\n'
    if printf '%s' "$last" | grep -q 'autoresearch '; then
      /bin/sh -lc "$last"
    fi
    exit 0
    ;;