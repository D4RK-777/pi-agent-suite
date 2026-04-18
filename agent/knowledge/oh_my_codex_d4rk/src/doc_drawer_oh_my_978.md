oop_hint: while ON, keep checking state (example: sleep 30 && omx team status ${sanitized})`,
  ];
}

export async function teamCommand(args: string[], _options: TeamCliOptions = {}): Promise<void> {
  const cwd = process.cwd();
  const parsedWorktree = parseWorktreeMode(args);
  const worktreeMode = resolveDefaultTeamWorktreeMode(parsedWorktree.mode);
  const teamArgs = parsedWorktree.remainingArgs;
  const [subcommandRaw] = teamArgs;
  const subcommand = (subcommandRaw || '').toLowerCase();

  if (HELP_TOKENS.has(subcommand)) {
    console.log(TEAM_HELP.trim());
    return;
  }