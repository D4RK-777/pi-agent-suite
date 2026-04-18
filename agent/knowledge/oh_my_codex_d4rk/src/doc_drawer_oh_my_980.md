).map((token) => token.toLowerCase());
      if (trailing.some((token) => HELP_TOKENS.has(token))) {
        console.log(buildTeamApiOperationHelp(operation));
        return;
      }
    }
    const wantsJson = teamArgs.includes('--json');
    const jsonBase = buildJsonBase();
    let parsedApi: ReturnType<typeof parseTeamApiArgs>;
    try {
      parsedApi = parseTeamApiArgs(teamArgs.slice(1));
    } catch (error) {
      if (wantsJson) {
        console.log(JSON.stringify({
          ...jsonBase,
          ok: false,
          command: 'omx team api',
          operation: 'unknown',
          error: {
            code: 'invalid_input',
            message: error instanceof Error ? error.message : String(error),
          },
        }));
        process.exitCode = 1;
        return;