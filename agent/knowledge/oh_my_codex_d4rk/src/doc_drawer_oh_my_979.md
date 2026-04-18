owerCase();

  if (HELP_TOKENS.has(subcommand)) {
    console.log(TEAM_HELP.trim());
    return;
  }

  if (subcommand === 'api') {
    const apiSubcommand = (teamArgs[1] || '').toLowerCase();
    if (HELP_TOKENS.has(apiSubcommand)) {
      const operationFromHelpAlias = resolveTeamApiOperation((teamArgs[2] || '').toLowerCase());
      if (operationFromHelpAlias) {
        console.log(buildTeamApiOperationHelp(operationFromHelpAlias));
        return;
      }
      console.log(TEAM_API_HELP.trim());
      return;
    }
    const operation = resolveTeamApiOperation(apiSubcommand);
    if (operation) {
      const trailing = teamArgs.slice(2).map((token) => token.toLowerCase());
      if (trailing.some((token) => HELP_TOKENS.has(token))) {