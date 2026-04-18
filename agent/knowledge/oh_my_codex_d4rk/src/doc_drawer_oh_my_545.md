ew Set(args.filter((a) => a.startsWith("--")));
  const options = {
    force: flags.has("--force"),
    dryRun: flags.has("--dry-run"),
    verbose: flags.has("--verbose"),
    team: flags.has("--team"),
  };

  if (flags.has("--help") && !commandOwnsLocalHelp(command)) {
    console.log(HELP);
    return;
  }

  try {
    switch (command) {
      case "launch":
        await launchWithHud(launchArgs);
        break;
      case "resume":
        await launchWithHud(["resume", ...launchArgs]);
        break;
      case "setup":
        await setup({
          force: options.force,
          dryRun: options.dryRun,
          verbose: options.verbose,
          scope: resolveSetupScopeArg(args.slice(1)),
        });
        break;
      case "agents":