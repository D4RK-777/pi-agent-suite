];
  if (!subcommand || HELP_TOKENS.has(subcommand)) {
    console.log(HELP.trim());
    return;
  }

  if (subcommand !== 'search') {
    throw new Error(`Unknown session subcommand: ${subcommand}\n${HELP}`);
  }

  if (args.slice(1).some((token) => HELP_TOKENS.has(token))) {
    console.log(HELP.trim());
    return;
  }

  const parsed = parseSessionSearchArgs(args.slice(1));
  const report = await searchSessionHistory(parsed.options);
  if (parsed.json) {
    console.log(JSON.stringify(report, null, 2));
    return;
  }
  console.log(formatReport(report));
}