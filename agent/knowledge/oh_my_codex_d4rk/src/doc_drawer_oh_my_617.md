eturn `powershell.exe -NoLogo -NoExit -EncodedCommand ${encodePowerShellCommand(wrappedCommand)}`;
}

/**
 * Wrap a command for tmux pane execution so the user's shell profile is
 * sourced.  Without this, tmux runs `default-shell -c "cmd"` which is
 * non-interactive/non-login and skips .zshrc / .bashrc.
 */
export function buildTmuxPaneCommand(
  command: string,
  args: string[],
  shellPath: string | undefined = process.env.SHELL,
): string {
  const bareCmd = buildTmuxShellCommand(command, args);
  let rcSource = "";
  if (shellPath && /\/zsh$/i.test(shellPath)) {
    rcSource = "if [ -f ~/.zshrc ]; then source ~/.zshrc; fi; ";
  } else if (shellPath && /\/bash$/i.test(shellPath)) {
    rcSource = "if [ -f ~/.bashrc ]; then source ~/.bashrc; fi; ";
  }
  const rawShell =