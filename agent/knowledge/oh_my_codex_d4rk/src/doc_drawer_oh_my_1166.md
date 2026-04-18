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
    last=""
    for arg in "$@"; do
      last="$arg"
    done
    if printf '%s' "$last" | grep -q 'hud --watch'; then
      printf '%%3\n'
      exit 0
    fi
    printf '%%2\n'